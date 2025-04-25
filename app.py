import streamlit as st
from apps import csv_editor, min_max_extractor, file_consistency_checker, statistics

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
