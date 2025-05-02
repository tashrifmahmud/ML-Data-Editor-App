# Changelog

All notable changes to this project will be documented here.

---

## [Unreleased]
- Planned: Desktop `.exe` packaging
- Planned: Multi-file processing support
- Planned: Collapsible README sections
- Planned: Save/export statistics view

---

## [v1.1.1] - 2025-05-01
### Added
- Sidebar README navigation with detailed usage breakdown
- Styled section headers with color-coded banners
- Custom favicon and tab title `⚡ ML Data Editor App`
- Modern sidebar buttons with icons and rounded edges

---
## [v1.1.0] - 2025-04-30
### Added
- Selectable input/output folders via text input
- Integrated refresh button in Min-Max extractor
- Auto-generated logs include timestamped edited filenames

---

## [v1.0.9] - 2025-04-27
### Fixed
- File consistency checker now compares modified logs against saved outputs (`edited_files.txt`)
- Dummy files from “Log Only” are now tracked in both logs

### Added
- `edited_files.txt` for audit history
- Duplicate detection by base name
- Detection of untracked files in `edited_data`

---

## [v1.0.8] - 2025-04-24
### Improved
- Saved file names now include data type suffix (`_MAG.csv`, `_EM.csv`, etc.)
- Allowed saving the same file under multiple types without overwriting

---

## [v1.0.7] - 2025-04-23
### Added
- Logging for “Log Only” button
- Dummy `.csv` creation for logged-only files
- Log system creates daily timestamped logs in `logs/csv_editor/`

---

## [v1.0.6] - 2025-04-21
### Added
- New “Save in Extra Data” button
- Saved files into `extra_data/` folder for miscellaneous categorization
- Separated logging for base names vs. actual saved files

---

## [v1.0.5] - 2025-04-19
### Improved
- Introduced file consistency checker UI
- Tracked missing, duplicate, and unlogged files

---

## [v1.0.4] - 2025-04-16
### Added
- Min-Max Coordinate Extractor tool
- Saves summary `Locations_YYYY-MM-DD.csv`
- Logs errors per run in `logs/min_max_extractor/`

---

## [v1.0.3] - 2025-04-13
### Added
- Sidebar app switching across CSV Editor, Min-Max Extractor, Stats, and Checker
- Centralized app layout and modular routing

---

## [v1.0.2] - 2025-04-09
### Added
- Data region and data type dropdowns for saving
- Files saved into region/type-specific folders

---

## [v1.0.1] - 2025-04-07
### Added
- Column renaming dropdowns
- Select All Columns for Deletion toggle
- Auto-uncheck if column is renamed
- “Show only unedited CSVs” toggle

---

## [v1.0.0] - 2025-04-05
### Added
- Basic CSV loader and preview
- Select and delete columns
- Save processed files to `formatted_data/` folder