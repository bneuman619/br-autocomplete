def load_ipython_extension(ipython):
    ipython.enable_matplotlib(gui='inline')
    ipython.run_cell("from IPython.display import display, Javascript, HTML", silent=True)
    ipython.run_cell("players = []", silent=True)
    ipython.run_cell("from player_data import get_player_data", silent=True)
    ipython.run_cell(make_html_cell("_player_input.html"), silent=True)
    ipython.run_cell(make_html_cell("_current_players.html"), silent=True)
    ipython.run_cell(make_html_cell("_angular.html"), silent=True)
    ipython.run_cell(make_javascript_cell('googleSuggest.js'), silent=True)
    ipython.run_cell(make_javascript_cell('eventHandlers.js'), silent=True)


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