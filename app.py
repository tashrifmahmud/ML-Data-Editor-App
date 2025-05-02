import streamlit as st
from apps import csv_editor, min_max_extractor, file_consistency_checker, statistics, readme
import os

# Sidebar navigation

st.sidebar.markdown(
    "<h2 style='text-align: center; font-size: 24px;'>App Navigation</h2>",
    unsafe_allow_html=True
)


button_style = """
<style>
div.stButton > button {
    width: 100%;
    border-radius: 8px;
    margin-bottom: 8px;
    padding: 0.5em 1em;
    background-color: #262730;
    color: white;
    border: 1px solid #444;
    transition: 0.2s;
}
div.stButton > button:hover {
    background-color: #393B4B;
}
</style>
"""
st.markdown(button_style, unsafe_allow_html=True)

# Manual buttons instead of radio
if st.sidebar.button("CSV Editor"):
    st.session_state["page"] = "CSV Editor"

if st.sidebar.button("Min-Max Extractor"):
    st.session_state["page"] = "Min-Max Extractor"

if st.sidebar.button("File Consistency Checker"):
    st.session_state["page"] = "File Consistency Checker"

if st.sidebar.button("Statistics"):
    st.session_state["page"] = "Statistics"


# App logic

page = st.session_state.get("page", "CSV Editor")

if page == "CSV Editor":
    csv_editor.run()
elif page == "Min-Max Extractor":
    min_max_extractor.run()
elif page == "File Consistency Checker":
    file_consistency_checker.run()
elif page == "Statistics":
    statistics.run()
elif page == "README":
    readme.run()


# Sidebar input/output folder selection
st.sidebar.write("### 📁 Folder Settings")
st.sidebar.caption("Paste full path to your input folder.")

data_folder = st.sidebar.text_input("Input Folder (raw CSVs)", value="data")
edited_folder = st.sidebar.text_input("Output Folder (for edits)", value="edited_data")


# #### Debugging: Show all files in the input folder ####
# st.write("Searching in:", data_folder)

# for root, dirs, files in os.walk(data_folder):
#     st.write("Found folder:", root)
#     for file in files:
#         st.write("  •", file)
# ########################################################

# Ensure folders exist
if not os.path.exists(data_folder):
    st.sidebar.error(f"❌ Input folder not found: {data_folder}")

os.makedirs(edited_folder, exist_ok=True)

# Save folders in session state to access in other modules
st.session_state["data_folder"] = data_folder
st.session_state["edited_folder"] = edited_folder

# Readme

if st.sidebar.button("ℹ️ App Guide"):
    st.session_state["page"] = "README"