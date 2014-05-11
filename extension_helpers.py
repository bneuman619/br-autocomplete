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