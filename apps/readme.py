import streamlit as st

def run():
    st.title("📘 App README & Guide")

    st.markdown("""
Welcome to the **GeoData Combined App**!  
This guide explains what each tool and button does.

---

### 📝 CSV Editor
- **Select CSV**: Choose a file from your input folder.
- **Select All Columns for Deletion**: Toggles all columns to be deleted.
- **Rename Dropdowns**: Map inconsistent column names to standard ones.
- **Apply Changes & Save**: Saves edited file with `_MAG`, `_EM`, etc. suffixes.
- **Save in Extra Data**: Saves to a special folder without categorization.
- **📄 Log Only**: Logs a file as processed without editing it.

---

### 📐 Min-Max Extractor
- **Path to Data Folder**: Folder containing processed `.csv` files.
- **Extract Coordinates**: Scans all CSVs and records min/max `Coord_X` and `Coord_Y`.
- **Summary CSV**: Automatically saved with a timestamp in your location folder.
- **Error Log**: Lists files that couldn’t be processed and saves a log.

---

### ✅ File Consistency Checker
- Checks if every file logged in `modified_log.txt` was actually saved.
- Warns about missing files, duplicate saves, and untracked files.

---

### 📊 Statistics
- **Total CSV Files**: Based on your selected input folder.
- **Files Edited**: Based on log entries.
- **Completion %**: Helps track overall progress day by day.

---

### 📂 Folder Settings
Accessible from the sidebar:
- Lets you select custom input (`data/`) and output (`edited_data/`) folders.

---

""")

    st.info("This README is automatically shown when you click 📘 README in the sidebar.")
