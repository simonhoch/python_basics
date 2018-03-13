def make_album (artist_name, album_name, number_track = ''):
    """
    Storing information in a dictionnary about artist (name, album, nb of
    tracks optionnaly)
    """
    album = {
        'artist_name' : artist_name.title(),
        'album_name' : album_name.title(),
    }

    if number_track:
        album['number_track'] = number_track

    print(album)
