def make_album (artist_name, album_name, number_track = ''):
    album = {
        'artist_name' : artist_name.title(),
        'album_name' : album_name.title(),
    }

    if number_track:
        album['number_track'] = number_track

    return album

while True:
    art_name = input('\nEnter an artist name: ')
    alb_name = input('Enter on of the album of this artist: ')
    ask_number = input('Do you know the number of track  of the album? (yes/no) ')

    if ask_number == 'yes':
        nbr_track = input('Please enter the number of track: ')
    else:
        nbr_track = ''

    album = make_album(art_name, alb_name, nbr_track)
    print('\n')
    print(album)

    adding_more = input('\nDo you want to makean other album? (yes/no) ')
    if adding_more == 'no':
        break

