import streamlit as st
import os

def run():
    st.markdown(
    """
    <div style="
        background-color: teal;
        padding: 0.75em;
        border-radius: 8px;
        border: 2px solid #006666;
        text-align: center;
    ">
        <h2 style="color: white; font-weight: bold; margin: 0;">
            File Consistency Checker
        </h2>
    </div>
    """,
    unsafe_allow_html=True
    )
    
    st.markdown("""---""")

    if st.button("🔄 Refresh & Update"):
        st.rerun()


    log_path = "modified_log.txt"
    edit_log_path = "edited_files.txt"
    edited_root = st.session_state.get("edited_folder", "edited_data")

    # Load edited file log (actual saved names like file_1_MAG.csv)
    if not os.path.exists(log_path):
        st.error("❌ modified_log.txt not found.")
        return

    if not os.path.exists(edit_log_path):
        st.warning("⚠️ edited_files.txt not found. Only checking basic log.")
        edited_saved_files = set()
    else:
        with open(edit_log_path, "r") as f:
            all_logged = set(line.strip() for line in f.readlines())

        # Cross-check with actual files in edited_data
        actual_files = set()
        for root, dirs, files in os.walk(edited_root):
            for file in files:
                if file.endswith(".csv"):
                    actual_files.add(file)

        # Keep only those logged files that still exist
        edited_saved_files = {f for f in all_logged if f in actual_files}


    with open(log_path, "r") as f:
        logged_files = [line.strip() for line in f.readlines()]

    # Scan edited_data folders (actual saved files)
    file_counts = {}
    for root, dirs, files in os.walk(edited_root):
        for file in files:
            if file.endswith(".csv"):
                file_counts[file] = file_counts.get(file, 0) + 1

    # Check for missing files based on logged base names
    missing_files = []
    for base_file in logged_files:
        root_name = os.path.splitext(base_file)[0]
        
        # Consider it found if:
        # - Any saved file starts with root_name + "_"
        # - OR exact base file exists in edited_files.txt
        # - OR exact file exists in edited_data folders
        found = any([
            any(f.startswith(root_name + "_") for f in edited_saved_files),
            base_file in edited_saved_files,
            base_file in file_counts
        ])
        
        if not found:
            missing_files.append(base_file)


    # Check for duplicate base names saved in multiple forms
    base_name_counts = {}
    for f in edited_saved_files:
        base = f.split("_")[0] + ".csv" if "_" in f else f
        base_name_counts[base] = base_name_counts.get(base, 0) + 1

    duplicate_files = [f for f, count in base_name_counts.items() if count > 1 and f in logged_files]

    # Files in edited_data not recorded in either log
    logged_set = set(logged_files)
    edited_base_set = {f.split("_")[0] + ".csv" if "_" in f else f for f in edited_saved_files}
    untracked_files = []
    for f in file_counts:
        if f not in edited_saved_files:
            untracked_files.append(f)

    # Output results
    st.subheader("📁 Files in LOG but NOT Found in Edited Folder:")
    if missing_files:
        st.error(f"{len(missing_files)} missing file(s):")
        for f in missing_files:
            st.text(f"• {f}")
    else:
        st.success("✅ No missing files!")

    st.subheader("⚠️ Files in LOG Appearing MULTIPLE Times:")
    if duplicate_files:
        for f in duplicate_files:
            st.warning(f"{f} found {base_name_counts[f]} times.")
    else:
        st.success("✅ No duplicates found!")

    st.subheader("📌 Files in Edited Folder NOT recorded in LOG:")
    if untracked_files:
        for f in untracked_files:
            st.info(f"{f} (x{file_counts[f]})")
    else:
        st.success("✅ All files in edited_data are logged.")
