import streamlit as st
import os
from collections import defaultdict
from datetime import datetime

def run():
    st.markdown(
    """
    <div style="
        background-color: #e0c000;
        padding: 0.75em;
        border-radius: 8px;
        border: 2px solid #006666;
        text-align: center;
    ">
        <h2 style="color: white; font-weight: bold; margin: 0;">
            CSV Editor Statistics
        </h2>
    </div>
    """,
    unsafe_allow_html=True
    )

    st.markdown("""---""")

    if st.button("🔄 Refresh & Update"):
        st.rerun()

    log_dir = os.path.join("logs", "csv_editor")
    data_folder = st.session_state.get("data_folder", "data")

    # 1️⃣ Count total .csv files in "data/"
    total_csv_files = 0
    for root, _, files in os.walk(data_folder):
        for file in files:
            if file.endswith(".csv"):
                total_csv_files += 1

    # 2️⃣ Parse log files in logs/csv_editor/
    edits_per_day = defaultdict(int)
    all_edited_files = set()

    if os.path.exists(log_dir):
        for log_file in os.listdir(log_dir):
            if log_file.endswith(".txt"):
                log_path = os.path.join(log_dir, log_file)
                with open(log_path, "r") as f:
                    for line in f:
                        if "Edited:" in line:
                            filename = line.strip().split("Edited:")[-1].strip()
                            all_edited_files.add(filename)
                            date = log_file.replace("log_", "").replace(".txt", "")
                            edits_per_day[date] += 1

    # 3️⃣ Show summary
    st.metric("📂 Total CSV Files", total_csv_files)
    st.metric("🛠️ Files Edited", len(all_edited_files))
    
    # Avoid div by zero
    percent = (len(all_edited_files) / total_csv_files) * 100 if total_csv_files else 0
    st.metric("✅ Completion Progress", f"{percent:.2f}%")

    # 4️⃣ Show daily edit counts
    st.write("### 🗓️ Edits Per Day")
    if edits_per_day:
        sorted_days = sorted(edits_per_day.items())
        for date, count in sorted_days:
            st.write(f"• {date}: {count} file(s)")
    else:
        st.info("No edits logged yet.")
