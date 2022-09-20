def are_you_playing_banjo(name):
    return "{} plays banjo".format(name) if name.startswith('r') or name.startswith('R') else "{} does not play banjo".format(name)
