# ML-Data-Editor-App

A Streamlit-based interactive application for previewing, cleaning, renaming, and organizing large CSV files — built originally for geophysical survey data but designed to be flexible enough for any machine learning (ML) preprocessing pipeline.

---

## 🧠 What It Does

- ✅ Preview large CSV files without opening them in Excel
- ✅ Select and keep only relevant columns
- ✅ Rename messy columns using predefined standard names
- ✅ Save cleaned files in a consistent folder structure
- ✅ Log every modification with timestamps
- ✅ Track editing progress with a visual dashboard
- ✅ Supports alternate save locations like:
  - `extra_data/`
  - `logged_only_files/`
- ✅ Handles large CSVs efficiently (tested with multi-GB files)

---

## 📁 Folder Structure

```
ML-Data-Editor-App/
├── data/                   # Input CSV files (messy, raw)
├── edited_data/           # Organized outputs
│   ├── Region/Type/       # Cleaned CSVs by region and category
│   ├── extra_data/        # Alternate save path
│   └── logged_only_files/ # Files marked without editing
├── logs/
│   └── csv_editor/        # Daily logs & statistics
├── config/                # [Optional] External config for columns, regions
├── file_handler.py
├── app.py
├── requirements.txt
└── README.md
```

---

## 🛠 Features Coming Soon

- Region & Type dropdowns powered by CSV config files
- Visual charts of progress by region/type
- Multi-user logging support

---

## 🚀 How to Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the app:
   ```bash
   streamlit run app.py
   ```

---

## 🧩 Tech Stack

- **Python**
- **Pandas**
- **Streamlit**
- **File-based logging** (no database required)

---

## ✨ Showcase Potential

This app is ideal for:
- ML Engineers and Researchers working with messy field data
- Teams managing diverse CSV formats from multiple sources
- Anyone needing a lightweight UI to standardize tabular data

---

## 📄 License

[MIT License](LICENSE)

---

## 🙌 Author

Built by Tashrif Mahmud  
Part of a geophysical ML pipeline project.
