import pandas as pd

reddit_df = pd.read_csv('./Dataset/cleanedRedditSuicide.csv')
twitter_df = pd.read_csv('./Dataset/cleanedTwitterSuicide.csv')
genral_df = pd.read_csv('./Dataset/cleanedRedditNonSuicide.csv')

suicide_text = []
suicide_label = []
for text in reddit_df['cleaned']:
    suicide_text.append(text)
    suicide_label.append(1)

for text in twitter_df['cleaned']:
    suicide_text.append('text')
    suicide_label.append(1)

non_suicide_text = []
non_suicide_label = []
for text in genral_df['cleaned']:
    non_suicide_text.append(text)
    non_suicide_label.append(0)

suicide_df = pd.DataFrame(data={"text": suicide_text, "label": suicide_label})
non_suicide_df = pd.DataFrame(
    data={"text": non_suicide_text, "label": non_suicide_label})

df = pd.concat([suicide_df, non_suicide_df], axis=0)
df.to_csv('./mergedData.csv', index=False)
