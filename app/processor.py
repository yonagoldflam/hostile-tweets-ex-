from fetcher import Connection
import pandas as pd
from collections import Counter

class TextProcessing:
    def __init__(self):
        self.df = self.load_df_from_db()
        self.add_field_rarest_word()

    def load_df_from_db(self):
        db_connection = Connection()
        return pd.DataFrame(db_connection.get_collection_as_list())

    def add_field_rarest_word(self):
        rarest_words_per_row = []
        for row_idx in range(len(self.df)):
            text = self.df.iloc[row_idx]["Text"]
            rarest_words = text.split()
            counts_words = Counter(rarest_words)
            rarest_word = min(counts_words)
            rarest_words_per_row.append(rarest_word)

        self.df["rarest_word"] = rarest_words_per_row








t = TextProcessing()