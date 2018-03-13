def make_album (artist_name, album_name, number_track = ''):
    """
    Storing information about artist (name, album, nb of
    tracks optionnaly)
    """
    album = {
        'artist_name' : artist_name.title(),
        'album_name' : album_name.title(),
    }

    if number_track:
        album['number_track'] = number_track

    return album

album = make_album('bob marley', 'kaya', 10)
print(album)
album = make_album('dub inc', 'paradise')
print(album)
