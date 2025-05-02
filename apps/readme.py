import streamlit as st

def run():
    st.title("App Guide: User Manual")

    st.markdown(""" 
This guide explains what each tool and button does.

---
                
### 🔄 Refresh & Update
Accessible in all Apps:
- Resets column selections and refreshes the app state + interface to update paths and files.
                
---                
### 📝 CSV Editor
- **Show Only Unedited Files**: Only show files that haven't been edited or logged yet.
- **Select CSV**: Choose a file from your input folder.
- **Preview of CSV file**: Displays the first 50 rows of the selected `.csv` file.
- **Select All Columns for Deletion**: Toggles all columns to be deleted.
- **Log Only**: Logs a file as processed without editing it.
- **Delete 'column'**: Marks the column for deletion when saving. Only unchecked columns are retained.
- **Rename Dropdowns**: Map inconsistent column names to standard ones.
- **Apply Changes & Save**: Saves edited file with `_MAG`, `_EM`, etc. suffixes.
- **Save in Extra Data**: Saves to a special folder without categorization.
- **Data Region Dropdown**: Classify where the data is from and determine the folder where it's saved.
- **Data Type Dropdown**: Geophysical category of the data. Appends to name and organizes into subfolders.


---

### 📐 Min-Max Extractor
- **Path to Data Folder**: Folder containing processed `.csv` files.
- **Path to Location folder**: Specifies where the summary `.csv` file will be saved.
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
                
### 📄 Log Files Explained
- **edited_files.txt**: Stores the actual filenames saved (e.g., `file_1_MAG.csv`). Used for audit and duplicate detection.

- **modified_log.txt**: Tracks original base filenames (e.g., `file_1.csv`). Used for progress tracking and unedited file filtering.

- **logs\csv_editor**: Daily logs of saved or logged files from the CSV Editor. Filenames are grouped by timestamped `.txt` files.

- **logs\min_max_extractor**: Stores timestamped error logs for files that couldn’t be read during coordinate extraction.

- **locations**: Output folder where coordinate summary files (`Locations_YYYY-MM-DD.csv`) are saved.

- **edited_data\logged_only_files**: Contains dummy `.csv` files for datasets that were marked as “log only” but not edited.
                
---

""")

    st.info("For more information please check out the detailed GITHUB repo of this project.")
