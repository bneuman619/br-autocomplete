/**@license
This file uses Google Suggest for jQuery plugin (licensed under GPLv3) by Haochi Chen ( http://ihaochi.com )
 */
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
