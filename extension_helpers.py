from player_data import get_player_data

def make_html_cell(html_filename):
    html_file = open(html_filename)
    html = ''.join(html_file.readlines())
    html_file.close()
    html_cell = "display(HTML(\"%s\"))" % html.replace("\n", "")
    return html_cell

def make_javascript_cell(js_filename):
    js_file = open(js_filename)
    js = ''.join(js_file.readlines())
    js_file.close()
    js_cell = "%%javascript\n\n  " + js
    return js_cell

def add_player(player_hash, player_name, player_id):
    data = get_player_data(player_name)
    player_hash[player_id] = player_name
    return player_hash

def delete_player(player_hash, player_id):
    player_hash.pop(player_id)
    return player_hash
