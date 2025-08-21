from fetcher import Connection
import pandas as pd
class TextProcessing:
    def __init__(self):
        self.df = self.load_df_from_db()
        print(self.df.head())

    def load_df_from_db(self):
        db_connection = Connection()
        return pd.DataFrame(db_connection.get_collection_as_list())



t = TextProcessing()