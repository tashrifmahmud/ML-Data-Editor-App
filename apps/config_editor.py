import streamlit as st
import os
import json

CONFIG_DIR = "config"
os.makedirs(CONFIG_DIR, exist_ok=True)

FOLDER_CONFIG_PATH = os.path.join(CONFIG_DIR, "config.json")
COLUMNS_CONFIG_PATH = os.path.join(CONFIG_DIR, "columns.json")

DEFAULT_FOLDERS = {
    "data_folder": "data",
    "edited_folder": "edited_data"
}

DEFAULT_COLUMNS = [
    "Coord_X", "Coord_Y", "resistivity", "conductivity",
    "K_corr", "TH_corr", "U_corr", "mag_res", "mag_dev", "altitude"
]

def folder_config_ui():
    st.subheader("📁 Folder Path Configuration")

    # Load existing config or use defaults
    if os.path.exists(FOLDER_CONFIG_PATH):
        with open(FOLDER_CONFIG_PATH, "r") as f:
            folder_config = json.load(f)
    else:
        folder_config = DEFAULT_FOLDERS.copy()

    data_path = st.text_input("Input Folder (raw CSVs)", value=folder_config.get("data_folder", "data"))
    edited_path = st.text_input("Output Folder (for edits)", value=folder_config.get("edited_folder", "edited_data"))

    col1, col2 = st.columns(2)

    with col1:
        if st.button("💾 Save Folder Config"):
            folder_config["data_folder"] = data_path
            folder_config["edited_folder"] = edited_path
            with open(FOLDER_CONFIG_PATH, "w") as f:
                json.dump(folder_config, f, indent=2)
            st.success("✅ Folder paths saved!")

    with col2:
        if st.button("♻️ Reset to Default Paths"):
            with open(FOLDER_CONFIG_PATH, "w") as f:
                json.dump(DEFAULT_FOLDERS, f, indent=2)
            st.success("🔁 Paths reset to default.")
            st.rerun()


def column_config_ui():
    st.subheader("🧱 Standard Column Names")

    # Load existing or fallback to default
    if os.path.exists(COLUMNS_CONFIG_PATH):
        with open(COLUMNS_CONFIG_PATH, "r") as f:
            columns = json.load(f)
    else:
        columns = DEFAULT_COLUMNS.copy()

    # Editable column inputs
    new_columns = []
    for i, col in enumerate(columns):
        new_value = st.text_input(f"Column {i+1}", value=col, key=f"col_input_{i}")
        if new_value.strip():
            new_columns.append(new_value.strip())

    col1, col2 = st.columns(2)

    with col1:
        if st.button("💾 Save Column Names"):
            with open(COLUMNS_CONFIG_PATH, "w") as f:
                json.dump(new_columns, f, indent=2)
            st.success("✅ Column names saved!")

    with col2:
        if st.button("♻️ Reset to Default Columns"):
            with open(COLUMNS_CONFIG_PATH, "w") as f:
                json.dump(DEFAULT_COLUMNS, f, indent=2)
            st.success("🔁 Columns reset to default.")
            st.rerun()


def run():
    st.markdown(
        "<h2 style='text-align: center; font-size: 24px;'>⚙️ Config Manager</h2>",
        unsafe_allow_html=True
    )

    st.markdown("---")

    tab1, tab2 = st.tabs(["📁 Folder Paths", "🧱 Column Names"])

    with tab1:
        folder_config_ui()

    with tab2:
        column_config_ui()
