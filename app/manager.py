from app.fetcher import Connection
from app.processor import TextProcessing
import pandas as pd

class Manager:
    def __init__(self):
        self.processor = TextProcessing()
        self.df = None

    def load_and_process(self):
        self.df = self.load_df_from_db()
        self.add_column_to_df('rarest_word', self.processor.rarest_words(self.df))
        self.add_column_to_df('sentiment', self.processor.sentiment_of_text(self.df))
        self.add_column_to_df('weapons_detected', self.processor.weapon_exist(self.df,self.read_txt_file()))
        return self.df.to_dict(orient='records')

    def load_df_from_db(self):
        db_connection = Connection()
        return pd.DataFrame(db_connection.get_collection_as_list())

    def read_txt_file(self):
        with open('data/weapons.txt') as f:
            return f.read()


    def add_column_to_df(self, column_name, values_list):
        self.df[column_name] = values_list

