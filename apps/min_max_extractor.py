import streamlit as st
import pandas as pd
import os
from datetime import datetime

def run():
    st.title("Min-Max Coordinate Extractor")

    data_folder_path = st.text_input("Path to data folder", "edited_data")
    location_file_path = st.text_input("Path to location file", "locations")

    errors = []  # List to collect all error messages

    if st.button("Extract Coordinates"):
        results = []

        for root, dirs, files in os.walk(data_folder_path):
            for file in files:
                if file.endswith('.csv'):
                    file_path = os.path.join(root, file)
                    try:
                        df = pd.read_csv(file_path)

                        x_min = df['Coord_X'].min()
                        x_max = df['Coord_X'].max()
                        y_min = df['Coord_Y'].min()
                        y_max = df['Coord_Y'].max()

                        results.append({
                            'file_name': file,
                            'file_path': file_path,
                            'x_min': x_min,
                            'x_max': x_max,
                            'y_min': y_min,
                            'y_max': y_max
                        })
                    except Exception as e:
                        # errors.append(f"Error reading {file}: {e}") # This will show only file name
                        errors.append(f"Error reading {file_path}: {e}") # This will show full path

        if results:
            output_df = pd.DataFrame(results)
            st.write("### Extracted Min-Max Coordinates")
            st.dataframe(output_df)

            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
            csv_path = os.path.join(location_file_path, f"Locations_{timestamp}.csv")

            output_df.to_csv(csv_path, index=False)
            st.success(f"Summary CSV file saved to: {csv_path}")

        # Show all errors at the bottom
        if errors:
            st.write("---")
            st.subheader("⚠️ Files with Errors")
            for err in errors:
                st.error(err)

            # Prepare logs directory
            log_dir = os.path.join("logs", "min_max_extractor")
            os.makedirs(log_dir, exist_ok=True)

            # Timestamped log file
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
            log_file_path = os.path.join(log_dir, f"log_{timestamp}.txt")

            # Write errors to log file
            with open(log_file_path, "w") as f:
                for err in errors:
                    f.write(err + "\n")

            st.info(f"Error log saved to: {log_file_path}")
