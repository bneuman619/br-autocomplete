def load_ipython_extension(ipython):
    ipython.enable_matplotlib(gui='inline')
    ipython.run_cell("from IPython.display import display, Javascript, HTML", silent=True)
    ipython.run_cell("players = []", silent=True)
    ipython.run_cell("from player_data import get_player_data", silent=True)
    html = get_html()
    ipython.run_cell(html, silent=True)
    js = get_js()
    ipython.run_cell(js, silent=True)

def get_js():
    js_file = open('jsSetup.js')
    js = ''.join(js_file.readlines())
    js_file.close()
    return js

def get_html():
  html1 = "<form id='player' action='/player_search' method='get'>"
  html2 = "<div id='input'><input type='text' name='player'></input></div><input type='submit' /></form>"
  html = '"%s%s"' % (html1, html2)
  html_cell = "display(HTML(%s))" % html
  return html_cell