from collections import Counter

class TextProcessing:

    def rarest_words(self,df):
        rarest_words_per_row = []
        for row_idx in range(len(df)):
            text = df.iloc[row_idx]["Text"]
            rarest_words = text.split()
            counts_words = Counter(rarest_words)
            rarest_word = min(counts_words)
            rarest_words_per_row.append(rarest_word)

        return rarest_words_per_row

    def weapon_exist(self,df, weapons_text):
        weapons_exist = []
        weapons_text = weapons_text.split('\n')
        for row_idx in range(len(df)):

            text_list = df.iloc[row_idx]["Text"].split()
            if row_idx == 0:
                text_list.append('bat')
            not_exist = True
            for word in text_list:
                if word in weapons_text:
                    weapons_exist.append(word)
                    not_exist = False
                    break
            if not_exist:
                weapons_exist.append(None)

        return weapons_exist










