from numpy.core.numeric import NaN
import pandas as pd
from googletrans import Translator

last_week_df = pd.read_csv("last week.csv")
last_week_df["daily_imp"] = last_week_df["Site Impressions"]/7
last_week_df = last_week_df.round(0)
print(last_week_df)

previous_week_df = pd.read_csv("previous week.csv")
previous_week_df["daily_imp"] = previous_week_df["Site Impressions"]/7
previous_week_df = previous_week_df.round(0)
print(previous_week_df)

compare_df = last_week_df.merge(previous_week_df, how="left", on="Query")

print(compare_df[["Query","daily_imp_x","daily_imp_y"]])

compare_df = compare_df[["Query","daily_imp_x","daily_imp_y"]]

compare_df["diff"] = (compare_df["daily_imp_x"]-compare_df["daily_imp_y"])/compare_df["daily_imp_y"]
compare_df["daily_imp_y"] = compare_df["daily_imp_y"].fillna(0)
compare_df["diff"] = compare_df["diff"].fillna("New")

compare_df.to_excel("result_non_translate.xlsx")

translator = Translator()

compare_df['English'] = compare_df['Query'].apply(lambda x: translator.translate(x, src='th', dest='en').text )
print(compare_df)

compare_df.to_excel("result.xlsx")

# compare_df_new = compare_df[compare_df.daily_imp_y == 0]

# print(compare_df_new)

