# ML-Data-Editor-App

A Streamlit-based interactive application for previewing, cleaning, renaming, and organizing large CSV files. Built originally for geophysical survey data but designed to be flexible enough for any machine learning (ML) preprocessing pipeline.

---

## What It Does

- Preview large CSV files without opening them in Excel
- Select and keep only relevant columns
- Rename messy columns using predefined standard names
- Save cleaned files in a consistent folder structure
- Log every modification with timestamps
- Track editing progress with a visual dashboard
- Supports alternate save locations like:
  - `extra_data/`
  - `logged_only_files/`
- Handles large CSVs efficiently (tested with multi-GB files)
- File consistency checker app to detect duplicates, missing files or other errors
- Min-Max extractor app to find the minimum and maximum values from data

---

## Folder Structure

```
ML-Data-Editor-App/
├── apps/                  # All streamlit app python scripts
├── data/                  # Input CSV files (messy, raw)
├── edited_data/           # Organized outputs
│   ├── Region/Type/       # Cleaned CSVs by region and category
│   ├── extra_data/        # Alternate save path
│   └── logged_only_files/ # Files marked without editing
├── locations/             # Min-Max extractor data output folder
├── logs/
│   ├── csv_editor/        # Daily logs & statistics
│   └── min_max_extractor/ # Min-Max extractor log files
├── config/                # External config for columns, regions
├── scripts/               # Min-Max extractor script
├── file_handler.py        # File management logic
├── app.py                 # Main streamlit app file
├── modified_logs.txt      # All edited files will be logged here
├── requirements.txt       # Install dependencies before running
├── run.bat                # Quickrun the app by running this
├── .gitignore
└── README.md
```

---

## How to Run

1️. Clone the Repository:
```bash
git clone https://github.com/tashrifmahmud/ML-Data-Editor-App.git
cd ML-Data-Editor-App
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the app:
```bash
streamlit run app.py
```

5. **Quickrun: Simply double-click `run.bat` to start the app.**
---


## Use Cases

This app is ideal for:
- ML Engineers and Researchers working with messy field data
- Teams managing diverse CSV formats from multiple sources
- Anyone needing a lightweight UI to standardize tabular data

---

## Features In Development

- Region & Type dropdowns powered by CSV config files
- Visual charts of progress by region/type
- Multi-user logging support
- Data type in output file names

---



[MIT License](LICENSE)

---



Built by [Tashrif Mahmud](https://www.linkedin.com/in/tashrifmahmud/) | Part of a geophysical ML pipeline project @ Healthcare Systems R&A Inc.
