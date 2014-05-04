var input = $("#input input");
input.googleSuggest({ service : 'web' });

$("#player").on('submit', function() {
    var inPlayer = $("#player #input input").val();
    var executionString = "players.append(get_player_data('" + inPlayer + "'))";
    IPython.notebook.kernel.execute(executionString);
    event.preventDefault();
});