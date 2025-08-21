from fetcher import Connection
from processor import TextProcessing
import pandas as pd

class Manager:
    def __init__(self):
        self.processor = TextProcessing()
        self.df = self.load_df_from_db()
        self.add_column_to_df('rarest_word',self.processor.rarest_words(self.df))
        self.add_column_to_df('weapon_exist',self.processor.weapon_exist(self.df,self.read_txt_file()))
        print(self.df['weapon_exist'].head())

    def load_df_from_db(self):
        db_connection = Connection()
        return pd.DataFrame(db_connection.get_collection_as_list())

    def read_txt_file(self):
        with open('C:/db_progects/hostile-tweets-ex/data/weapons.txt') as f:
            return f.read()


    def add_column_to_df(self, column_name, values_list):
        self.df[column_name] = values_list

if __name__ == '__main__':
    manager = Manager()