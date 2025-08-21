from collections import Counter
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

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
            not_exist = True
            for word in text_list:
                if word in weapons_text:
                    weapons_exist.append(word)
                    not_exist = False
                    break
            if not_exist:
                weapons_exist.append('')

        return weapons_exist







    def sentiment_of_text(self, df):
        nltk.download('vader_lexicon')
        sia = SentimentIntensityAnalyzer()
        sentiment_list = []

        for row_idx in range(len(df)):
            text = df.iloc[row_idx]["Text"]
            score = sia.polarity_scores(text)

            if score['compound'] >= 0.05:
                sentiment_list.append("positive")
            elif score['compound'] <= -0.05:
                sentiment_list.append("negative")
            else:
                sentiment_list.append("neutral")

        return sentiment_list

    # def sentiment_of_text(self, df):
    #     sentiment_list = []
    #     for row_idx in range(len(df)):
    #         text = df.iloc[row_idx]["Text"]
    #         score = SentimentIntensityAnalyzer().polarity_scores(text)
    #         if score['compound'] >= 0.5:
    #             sentiment_list.append('positive')
    #         elif score['compound'] >= -0.49:
    #             sentiment_list.append("neutral")
    #         else:
    #             sentiment_list.append("negative")
    #     return sentiment_list











