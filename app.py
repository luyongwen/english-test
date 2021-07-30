from flask import Flask, render_template
from en_test import get_jms_word, beautify
from prettytable import PrettyTable
import numpy as np

app = Flask(__name__)

# words = {}

@app.route('/jms/')
def test(name):
    # global words
    words = get_jms_word()
    en = np.array(list(words.keys())).reshape(-1, 5)
    en_ch = []
    word_keys = list(words.keys())
    word_values = list(words.values())
    for i in range(10):
        en_ch.append(word_keys[10*i:10*(i+1)])
        en_ch.append(word_values[10*i:10*(i+1)])
    # bea_table = beautify(en)
    # return render_template('temp.html', bea_table=bea_table)
    return render_template('temp.html', en=en, en_ch=en_ch)

@app.route('/ps/')
def result():
    all_words = []
    word_keys = list(words.keys())
    word_values = list(words.values())
    for i in range(10):
        all_words.append(word_keys[10*i:10*(i+1)])
        all_words.append(word_values[10*i:10*(i+1)])
    # bea_table = beautify(all_words)
    return render_template('result.html', en=all_words)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)