# Adwiro 2022
# Get billboard source data

class GetAttractionDailyDataQuery:

    @staticmethod
    def query_attraction_daily_data():
        attraction_daily = f'''
                select *
                from attraction_detail;
                 ;'''
        return attraction_daily
