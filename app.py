from flask import Flask, url_for, request, render_template
from br_player_finder import *

app = Flask(__name__) 





@app.route("/")
def get_index():
    index = open("static/index.html")
    index_string = index.read()
    index.close
    return index_string


@app.route("/player_search/")
def player_search():
    player = request.args.get('player')
    if player[0] == " ":
        player = player[1:]

    page = get_player_page(player)
    return page

if __name__ == "__main__":
    app.debug = True
    app.run()

url_for("static", filename="index.html")
url_for("static", filename="googleSuggest.js")