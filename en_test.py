import numpy as np
import pandas as pd
from HTMLTable import HTMLTable
from bs4 import BeautifulSoup

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

def beautify(words):
    table = HTMLTable(caption='100单词表')
    table.caption.set_style({
        'font-size': '15px',
    })
    # 表格样式，即<table>标签样式
    table.set_style({
        'border-collapse': 'collapse',
        'word-break': 'keep-all',
        'white-space': 'nowrap',
        'font-size': '14px',
    })
    # 统一设置所有单元格样式，<td>或<th>
    table.set_cell_style({
        'border-color': '#000',
        'border-width': '1px',
        'border-style': 'solid',
        'padding': '5px',
    })
    table.append_data_rows(np.array(words).reshape(10, -1))
    soup = BeautifulSoup(table.to_html())
    return soup.prettify()

if __name__ == '__main__':
    word, chinese = get_word()
    print(word, chinese)