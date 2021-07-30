import numpy as np
import pandas as pd

def get_word():
    df = pd.read_csv('./中考英语词汇表.txt', sep='\t', names=['单词', '发音', '中文'])
    df['单词'] = df['单词'].str.strip()
    df['发音'] = df['发音'].str.strip()
    df['中文'] = df['中文'].str.strip()
    rand_num = np.random.choice(df.shape[0], 100, replace=False)
    words = {}
    for i in rand_num:
        word, chinese = df.iloc[i]['单词'], df.iloc[i]['中文']
        words[word] = chinese
    return words

if __name__ == '__main__':
    word, chinese = get_word()
    print(word, chinese)