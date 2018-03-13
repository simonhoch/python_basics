def make_album (artist_name, albums_tracks):
    make_albums = {
        'artist_name' : artist_name.title(),
        'albums_tracks' : albums_tracks
    }

    return make_albums

while True:
    art_name = input("\nEnter an artist name('q' to stop): ")
    albums = []
    if art_name == 'q':
        break
    else:
        while True:
            alb_name = input("Enter one or more album of this artist ('q' to stop): ")
            album = {}

            if alb_name == 'q':
                break
            else:
                nbr_tracks = input('What is the number of track of this album? ')
                album['alb_name'] = alb_name
                album['nbr_tracks'] = nbr_tracks
        
            albums.append(album)

    make_albums = make_album(art_name, albums)
    
    print('\n')
    print(make_albums)
    print('\n' + make_albums['artist_name'] + ' did:')
    for make_album in make_albums['albums_tracks']:
        print('\t-' + make_album['alb_name'] + ' with ' + str(make_album['nbr_tracks']) + ' tracks')
            
