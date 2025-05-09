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
