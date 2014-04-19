from flask import Flask, url_for, request, render_template
from random import randint

app = Flask(__name__) 

@app.route("/")
def get_index():
    index = open("static/index.html")
    index_string = index.read()
    index.close
    return index_string


@app.route("/player_search/")
def player_search():
    player = request.args.get('player').strip()
    notebook = render_template('player_notebook_template.ipynb', player=player)
    notebook_filename = "br_viewer/%d.ipynb" % randint(1, 1000)
    notebook_file = open(notebook_filename, 'w')
    notebook_file.write(notebook)
    notebook_file.close
    return notebook_filename

if __name__ == "__main__":
    app.debug = True
    app.run()

url_for("static", filename="index.html")
url_for("static", filename="googleSuggest.js")