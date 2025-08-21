from app.manager import Manager
from collections import Counter

class TextProcessing:
    def __init__(self):
        pass


    def rarest_words(self,df):
        rarest_words_per_row = []
        for row_idx in range(len(df)):
            text = df.iloc[row_idx]["Text"]
            rarest_words = text.split()
            counts_words = Counter(rarest_words)
            rarest_word = min(counts_words)
            rarest_words_per_row.append(rarest_word)

        return rarest_words_per_row








