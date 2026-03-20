from dataclasses import dataclass
import pandas as pd
import os
from datetime import datetime, timedelta
from src.bastion_connection import open_bastion_connection, close_bastion_connection, execute_query_to_dataframe
from src.query_required import scrappers_query
from openpyxl import load_workbook


@dataclass
class DataExtractionPath:
    data_extraction_path = os.path.join(os.getcwd(), "data")

class DataExtraction:
    def save_dataframe_to_csv(self):
            # end_date = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
            # start_date = end_date - timedelta(days=1)
            end_date = '2026-03-20 00:00:00.00'
            start_date = '2026-03-01 00:00:00.00'

            # start_date_str = start_date.strftime('%Y-%m-%d %H:%M:%S.00')
            # end_date_str = end_date.strftime('%Y-%m-%d %H:%M:%S.00')

            open_bastion_connection()
            os.makedirs(DataExtractionPath.data_extraction_path, exist_ok=True)

            excel_file_path = os.path.join(DataExtractionPath.data_extraction_path, "Scrappers_Info.xlsx")
            channels = ["Blinkit","Zepto","Instamart"]
            
            try:
                # Create or load existing Excel file
                if os.path.exists(excel_file_path):
                    excel_file = pd.ExcelFile(excel_file_path)
                    existing_sheets = excel_file.sheet_names
                else:
                    existing_sheets = []
                
                with pd.ExcelWriter(excel_file_path, engine='openpyxl', mode='a' if os.path.exists(excel_file_path) else 'w') as writer:
                    for channel in channels:
                        sql_query = scrappers_query(start_date, end_date, channel)
                        success, df, message = execute_query_to_dataframe(sql_query)

                        if success:
                            print(f"✅ Query successful for {channel}:\n{df}\n")
                        else:
                            print(f"❌ Query failed for {channel}: {message}\n")

                        # Append data if sheet exists, otherwise create new sheet
                        if channel in existing_sheets:
                            existing_df = pd.read_excel(excel_file_path, sheet_name=channel)
                            df = pd.concat([existing_df, df], ignore_index=True)
                        
                        df.to_excel(writer, sheet_name=channel, index=False)
            finally:
                close_bastion_connection()