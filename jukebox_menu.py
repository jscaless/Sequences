from nested_data import albums
# print(albums[0][3])
# print(albums[1][3])
# print(albums[2][3])
# print(albums[3][3])

SONGS_LIST_INDEX = 3 # Values in all CAPS are constants and should not be changed.
SONGS_CHOICE_INDEX = 1

while True:
    print("Please choose your album (invalid choice exits): ")
    for index, (title, artist, year, songs) in enumerate(albums):
        # Have to include () around title, artist, year, songs,
        # Because within albums it within a tuple
        print("{}: {}".format(index + 1, title))
    choice = int(input())
    if 1 <= choice <= len(albums):
        song_list = albums[choice - 1][SONGS_LIST_INDEX] # CONSTANT Variable
    else:
        break

    print("Please choose your song: ")
    for index, (track_number, song) in enumerate(song_list):
        print("{}: {}".format(index + 1, song))
    song_choice = int(input())
    if 1 <= song_choice <= len(song_list):
        song_selection = song_list[song_choice - 1][SONGS_CHOICE_INDEX]
    else:
        continue # Starts Over the While Loop
    print("Playing: {}".format(song_selection))
    print("="*40)



    # for index, values in enumerate(albums):
    # # Values represents the (title, artist, year, songs) other an error will appear
    # # However we need to unpack values unlike above where we unpacked it at the top:
    #     title, artist, year, songs = values
    #     print("{}: {}, {}, {}, {}"
    #           .format(index + 1, title, artist, year, songs))
    # break