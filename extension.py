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

# def javascript_setup():
#     "%%javascript

#     $.fn.googleSuggest = function(opts){
#       opts = $.extend({service: 'web', secure: false}, opts);

#       var services = {
#         web: { client: 'psy', ds: '' },
#       }, service = services[opts.service];

#       opts.source = function(request, response){
#         $.ajax({
#           url: 'http'+(opts.secure?'s':'')+'://clients1.google.com/complete/search',
#           dataType: 'jsonp',
#           data: {
#             q: 'basketball reference player ' + request.term,
#             nolabels: 't',
#             client: service.client,
#             ds: service.ds
#           },
#           success: function(data) {
#             response($.map(data[1], function(item){
#               return { value: $("<span>").html(item[0]).text().split("basketball reference player ")[1] };
#             }));
#           }
#         });  
#       };
      
#       return this.each(function(){
#         $(this).autocomplete(opts);
#       });
#     }

#     var input = $("#input input");
#     input.googleSuggest({ service : 'web' });

#     $("#player").on('submit', function() {
#         var inPlayer = $("#player #input input").val();
#         var executionString = "players.append(get_player_data('" + inPlayer + "'))";
#         IPython.notebook.kernel.execute(executionString);
#         event.preventDefault();
#     });"