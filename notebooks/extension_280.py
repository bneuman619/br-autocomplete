from player_data import get_player_data

def load_ipython_extension(ipython):
    ipython.enable_matplotlib()
    player = get_player_data("ron harper")
    ipython.push('player')