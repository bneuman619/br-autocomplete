var input = $("#input input");
input.googleSuggest({ service : 'web' });

$("#player").on('submit', function() {
    var inPlayer = $("#player #input input").val();
    var inPlayerID = "p" + getNextPlayerID();
    var executionString = "players = add_player(players, '" + inPlayer + "','" + inPlayerID + "')";
    IPython.notebook.kernel.execute(executionString);
    addPlayer(inPlayer, inPlayerID);
    event.preventDefault();
});

$("#current_players").on('submit', function() {
  var playerID = $("#current_players :selected").attr('value');
  var executionString = "players = delete_player(players, '" + playerID + "')";
  IPython.notebook.kernel.execute(executionString);
  $("#current_players :selected").remove();
  event.preventDefault();
})

function addPlayer(playerName, playerID) {
  var $playerList = getPlayerList();
  var element = generatePlayerEntry(playerName, playerID);
  $playerList.append(element);
}

function getPlayerList() {
  return $("#current_players select");
}

function generatePlayerEntry(playerName, playerID) {
  return "<option value=" + playerID + ">" + playerID + ": " + playerName + "</option>";
}

function getNextPlayerID() {
  var $playerList = $("#current_players select option");

  if ($playerList.length == 0) {
    return 1;
  }

  var lastPlayer = $playerList.get(-1);
  var lastPlayerID = $(lastPlayer).attr('value');
  var nextPlayerID = Number($(lastPlayerID.split('p')).get(-1)) + 1;
  return nextPlayerID;
}