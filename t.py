import pandas as pd

raw_data = pd.read_csv('小学英语大纲词汇.txt', header=None, names=['单词'])
raw_data.to_excel('words.xlsx', index=None)