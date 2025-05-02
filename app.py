import streamlit as st
from apps import csv_editor, min_max_extractor, file_consistency_checker, statistics
import os

# Sidebar navigation
st.sidebar.title("App Navigation")
app_choice = st.sidebar.radio("Go to:", 
                              ["CSV Editor", 
                               "Min-Max Extractor",
                               "File Consistency Checker",
                               "Statistics"
                               ])

# App logic
if app_choice == "CSV Editor":
    csv_editor.run()
elif app_choice == "Min-Max Extractor":
    min_max_extractor.run()
elif app_choice == "File Consistency Checker":
    file_consistency_checker.run()
elif app_choice == "Statistics":
    statistics.run()

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
