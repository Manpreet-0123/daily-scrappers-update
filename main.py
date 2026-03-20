from src.components.data_extraction import DataExtraction
from datetime import datetime

if __name__ == "__main__":
    print(f"[{datetime.now()}] Running scraper...")
    data_extraction = DataExtraction()
    data_extraction.save_dataframe_to_csv()
    print(f"[{datetime.now()}] Scraper completed!")