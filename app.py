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
    player_name = request.args.get('player').strip()
    extension = render_template('extension_template.py', player_name=player_name)

    extension_filename = "extension.py"
    extension_file = open(extension_filename, 'w')
    extension_file.write(extension)
    extension_file.close

    notebook = render_template('player_notebook_template.ipynb', extension = extension_filename.split('.')[0])
    notebook_filename = 'notebook-%d.ipynb' % randint(1, 1000)
    notebook_file = open(notebook_filename, 'w')
    notebook_file.write(notebook)
    notebook_file.close
    notebook_url = "http://localhost:8888/notebooks/%s" % notebook_filename

    return render_template('_player_view.html', notebook_url=notebook_url)

if __name__ == "__main__":
    app.debug = True
    app.run()

url_for("static", filename="index.html")
url_for("static", filename="googleSuggest.js")