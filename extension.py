from extension_helpers import make_javascript_cell, make_html_cell, add_player

def load_ipython_extension(ipython):
    ipython.run_cell("from IPython.display import display, Javascript, HTML", silent=True)
    ipython.enable_matplotlib(gui='inline')
    ipython.run_cell("players = {}", silent=True)
    ipython.run_cell("from extension_helpers import add_player, delete_player", silent=True)
    ipython.run_cell(make_html_cell("_player_input.html"), silent=True)
    ipython.run_cell(make_javascript_cell('googleSuggest.js'), silent=True)
    ipython.run_cell(make_javascript_cell('eventHandlers.js'), silent=True)
  