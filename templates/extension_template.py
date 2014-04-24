from player_data import get_player_data

def load_ipython_extension(ipython):
    ipython.enable_matplotlib(gui='inline')
    player = get_player_data("{{player_name}}")
    ipython.push('player')