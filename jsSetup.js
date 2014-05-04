%%javascript

$.fn.googleSuggest = function(opts){
  opts = $.extend({service: 'web', secure: false}, opts);

  var services = {
    web: { client: 'psy', ds: '' },
  }, service = services[opts.service];

  opts.source = function(request, response){
    $.ajax({
      url: 'http'+(opts.secure?'s':'')+'://clients1.google.com/complete/search',
      dataType: 'jsonp',
      data: {
        q: 'basketball reference player ' + request.term,
        nolabels: 't',
        client: service.client,
        ds: service.ds
      },
      success: function(data) {
        response($.map(data[1], function(item){
          return { value: $("<span>").html(item[0]).text().split("basketball reference player ")[1] };
        }));
      }
    });  
  };
  
  return this.each(function(){
    $(this).autocomplete(opts);
  });
}

var input = $("#input input");
input.googleSuggest({ service : 'web' });

$("#player").on('submit', function() {
    var inPlayer = $("#player #input input").val();
    var executionString = "players.append(get_player_data('" + inPlayer + "'))";
    IPython.notebook.kernel.execute(executionString);
    event.preventDefault();
});