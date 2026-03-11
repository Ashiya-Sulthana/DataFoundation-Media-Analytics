import os
import subprocess

def run_script(script_path):
    print(f"\n🚀 Running {script_path} ...")
    result = subprocess.run(["python", script_path], capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print("⚠️ Errors/Warnings:\n", result.stderr)

def main():
    print("=== DataFoundation: Media Content Analytics Platform ===")

    # Step 1: YouTube ingestion
    run_script("youtube_ingest.py")

    # Step 2: Kaggle news preprocessing
    run_script("preprocess_news.py")

    # Step 3: Load into BigQuery
    run_script("warehouse/load_to_bigquery.py")

    # Step 4: Launch Streamlit dashboard
    print("\n📊 Launching Streamlit dashboard...")
    os.system("streamlit run dashboard.py")

if __name__ == "__main__":
    main()
