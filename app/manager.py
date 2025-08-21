from app.fetcher import Connection
from app.processor import TextProcessing
import pandas as pd

class Manager:
    def __init__(self):
        self.processor = TextProcessing()
        self.df = self.load_df_from_db()
        self.add_column_to_df('rarest_word',self.processor.rarest_words(self.df))

    def load_df_from_db(self):
        db_connection = Connection()
        return pd.DataFrame(db_connection.get_collection_as_list())

    def read_txt_file(self):
        with open('data/weapons.txt') as f:
            weapons = f.readlines()
        print(weapons)

    def add_column_to_df(self, column_name, values_list):
        self.df[column_name] = values_list
