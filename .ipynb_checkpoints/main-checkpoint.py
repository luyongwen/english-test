from flask import Flask
from en_test import get_word
from prettytable import PrettyTable
import numpy as np

app = Flask(__name__)

@app.route('/<name>')
def test(name):
    words = get_word()
    table = PrettyTable()
    table.add_rows(np.array(words.keys()).reshape(10, 10))
    return table.get_html_string()


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)