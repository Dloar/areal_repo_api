import datetime
import logging

import pandas as pd

from src.services.create_db_connection import DbConnectorModel


class UpdateReceivedDataStatusHandler:
    def __init__(self, income_data, status, calculation_id):
        data = {
            "calculation_id": calculation_id,
            "status": status,
            "income_input": str(income_data),
            "load_time": datetime.datetime.now()
        }

        self.status_data_df = pd.DataFrame(data=data, index=[0])
        self.update_status_data()

    def update_status_data(self):
        logging.info(f"Logging status data.")
        engine = DbConnectorModel().create_upload_db_connection()

        self.status_data_df.to_sql(name="servis_income_status_table",
                                   con=engine,
                                   if_exists='append',
                                   index=False)

        logging.info("Status data loaded")
