import streamlit as st
import pandas as pd
import os
from file_handler import list_csv_files, preview_csv


def run():
    # Predefined column names
    STANDARD_COLUMNS = ["Coord_X", "Coord_Y", "resistivity", "conductivity", "K_corr", "TH_corr", "U_corr", "mag_res", "mag_dev", "altitude"]


    # Streamlit App
    st.title("CSV Editor & Formatter")


    # Select project folder
    data_folder = "data"  # We can change data directory if needed


    # Read log of modified files
    log_path = "modified_log.txt"
    if os.path.exists(log_path):
        with open(log_path, "r") as log_file:
            modified_files = set(log_file.read().splitlines())
    else:
        modified_files = set()


    # Toggle to filter edited files
    col1, col2 = st.columns([3, 2])  # Width ratio can be adjusted

    with col1:
        show_only_unedited = st.checkbox("Show only unedited CSV files", value=False)

    with col2:
        if st.button("🔄 Reset Column Selections"):
            # Clear all session state keys related to rename/delete/select_all
            keys_to_clear = [k for k in st.session_state.keys() if k.startswith("rename_") or k.startswith("delete_")]
            for k in keys_to_clear:
                del st.session_state[k]
            st.session_state.select_all = False
            st.rerun()


    # List all CSV files
    all_csv_files = list_csv_files(data_folder)


    # Initialize select_all in session state
    if "select_all" not in st.session_state:
        st.session_state.select_all = False


    # Filter files based on toggle
    if show_only_unedited:
        csv_files = [
            f for f in all_csv_files
            if os.path.basename(f) not in modified_files
        ]
    else:
        csv_files = all_csv_files



    if csv_files:
        # User selects a CSV file
        selected_file = st.selectbox("Select a CSV file:", csv_files)

        # Load selected CSV
        file_path = os.path.join(data_folder, selected_file)
        df = pd.read_csv(file_path, nrows=100)  # Load a small sample to save memory (newly added)

        st.write(f"### Preview of {selected_file}")
        st.dataframe(df.head(50), height=300)  # Show sample data (we can adjust the number of rows)

        ## Select All Columns for Deletion and Log Only
        col_sel, col_log = st.columns([2, 1])

        with col_sel:
            st.checkbox("Select All Columns for Deletion", key="select_all")

        with col_log:
            if st.button("📄 Log Only"):
                if selected_file:
                    file_name = os.path.basename(selected_file)

                    # Log to modified_log.txt if not already present
                    log_path = "modified_log.txt"
                    if os.path.exists(log_path):
                        with open(log_path, "r") as log_file:
                            logged_files = log_file.read().splitlines()
                    else:
                        logged_files = []

                    if file_name not in logged_files:
                        with open(log_path, "a") as log_file:
                            log_file.write(f"{file_name}\n")

                    # Save dummy file
                    dummy_dir = os.path.join("edited_data", "logged_only_files")
                    os.makedirs(dummy_dir, exist_ok=True)
                    dummy_path = os.path.join(dummy_dir, file_name)

                    if not os.path.exists(dummy_path):
                        pd.DataFrame(columns=["Dummy"]).to_csv(dummy_path, index=False)

                    # Daily log
                    from datetime import datetime
                    log_dir = os.path.join("logs", "csv_editor")
                    os.makedirs(log_dir, exist_ok=True)
                    today_str = datetime.now().strftime("%Y-%m-%d")
                    log_file_path = os.path.join(log_dir, f"log_{today_str}.txt")

                    with open(log_file_path, "a") as log_file:
                        timestamp = datetime.now().strftime("%H:%M:%S")
                        log_file.write(f"{timestamp} - Logged only: {file_name}\n")

                    st.success(f"✅ Logged only (no edit): {file_name}")
                else:
                    st.warning("⚠️ Please select a CSV file first.")

        select_all = st.session_state.select_all


        # Column selection and renaming
        st.write("### Select and Rename Columns")
        new_columns = {}
        delete_columns = []

        for col in df.columns:
            col1, col2 = st.columns([2, 1])

            # Dropdown for renaming
            new_name = col1.selectbox(
                f"Rename '{col}'",
                ["(Keep Original)"] + STANDARD_COLUMNS,
                key=f"rename_{col}"
            )

            # Logic: if user renamed the column, override deletion (uncheck)
            is_renamed = new_name != "(Keep Original)"

            # If renamed, we won't mark it for deletion even if 'select all' is on
            default_delete = select_all and not is_renamed

            # Checkbox for deletion
            delete = col2.checkbox(f"Delete '{col}'", value=default_delete, key=f"delete_{col}")

            # Save results
            if is_renamed:
                new_columns[col] = new_name
            if delete:
                delete_columns.append(col)


        # New optional categorization for saving in edited_data
        st.write("### Save Destination")

        region = st.selectbox("Select the data region:", ["ON, Canada", "QC, Canada", "USA", "Australia"])
        data_type = st.selectbox(
            "Select the data type:",
            ["Magnetic (MAG)", "Electromagnetic (EM)", "Radiometric (SPEC)", "Gravimetric (GRAV)"]
        )



        # Apply Changes and Save Button (Dual save buttons in a row)
        col_save1, col_save2 = st.columns(2)
        with col_save1:
            save_main = st.button("Apply Changes & Save")

        with col_save2:
            save_extra = st.button("Save in Extra Data")

            if save_main or save_extra:
                # Reload the full CSV file
                full_df = pd.read_csv(file_path)
                full_df = full_df.drop(columns=delete_columns, errors="ignore")
                full_df = full_df.rename(columns=new_columns)

                if save_extra:
                    base_folder = os.path.join("edited_data", "extra_data")
                else:
                    category_folder_map = {
                        "Magnetic (MAG)": "MAG",
                        "Electromagnetic (EM)": "EM",
                        "Radiometric (SPEC)": "SPEC",
                        "Gravimetric (GRAV)": "GRAV"
                    }
                    base_folder = os.path.join("edited_data", region, category_folder_map[data_type])

                file_name = os.path.basename(selected_file)
                save_path = os.path.join(base_folder, file_name)
                os.makedirs(os.path.dirname(save_path), exist_ok=True)
                full_df.to_csv(save_path, index=False)

                # === LOG MODIFIED FILE ===
                log_path = "modified_log.txt"
                relative_path = file_name  # just the file name
                if os.path.exists(log_path):
                    with open(log_path, "r") as log_file:
                        logged_files = log_file.read().splitlines()
                else:
                    logged_files = []

                if relative_path not in logged_files:
                    with open(log_path, "a") as log_file:
                        log_file.write(f"{relative_path}\n")

                st.success(f"File saved successfully: {save_path}")

                # === Append to daily log ===
                from datetime import datetime
                log_dir = os.path.join("logs", "csv_editor")
                os.makedirs(log_dir, exist_ok=True)
                today_str = datetime.now().strftime("%Y-%m-%d")
                log_file_path = os.path.join(log_dir, f"log_{today_str}.txt")

                with open(log_file_path, "a") as log_file:
                    timestamp = datetime.now().strftime("%H:%M:%S")
                    log_file.write(f"{timestamp} - Edited: {file_name}\n")

    else:
        st.warning("No CSV files found in the data folder.")
