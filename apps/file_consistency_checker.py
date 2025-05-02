import streamlit as st
import os

def run():
    st.title("File Consistency Checker")

    log_path = "modified_log.txt"
    edited_root = "edited_data"

    # Load edited file log
    if not os.path.exists(log_path):
        st.error("modified_log.txt not found.")
        return

    with open(log_path, "r") as f:
        logged_files = [line.strip() for line in f.readlines()]

    # Scan edited_data folders
    file_counts = {}
    for root, dirs, files in os.walk(edited_root):
        for file in files:
            if file.endswith(".csv"):
                file_counts[file] = file_counts.get(file, 0) + 1

    # Analysis
    missing_files = [f for f in logged_files if file_counts.get(f, 0) == 0]
    duplicate_files = [f for f, count in file_counts.items() if count > 1 and f in logged_files]

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
            st.warning(f"{f} found {file_counts[f]} times.")
    else:
        st.success("✅ No duplicates found!")

    # Optional: Files in edited_data not in log
    untracked_files = [f for f in file_counts if f not in logged_files]
    st.subheader("📌 Files in Edited Folder NOT recorded in LOG:")
    if untracked_files:
        for f in untracked_files:
            st.info(f"{f} (x{file_counts[f]})")
    else:
        st.success("✅ All files in edited_data are logged.")
