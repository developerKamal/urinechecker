from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    color_class = ""
    if request.method == 'POST':
        color = request.form['color']
        frequency = int(request.form['frequency'])

        if color == 'Helder' and frequency >= 6:
            result = 'Top gehydrateerd!'
            color_class = 'helder'
        elif color == 'Donker' or frequency < 4:
            result = 'Drink wat meer water.'
            color_class = 'donker'
        else:
            result = 'Redelijk, maar let op je vochtinname.'
            color_class = 'troebel'
    return render_template('index.html', result=result, color_class=color_class)

import os

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))


