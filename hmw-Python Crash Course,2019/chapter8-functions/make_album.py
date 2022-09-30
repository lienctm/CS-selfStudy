# function returing values
def build_album(artist_name, album_title, number_of_songs = " "):
    album = f"{artist_name.title()}, album {album_title.title()} has {number_of_songs} songs"
    return album

album = build_album('adele', '21','11' )
print(album)

print()

# passing a list to a function
def greeter_user(names):
    for name in names:
        msg = f"Hello, {name.title()} !"
        print(msg)

usernames = ['An', 'Nam', 'My', 'Phuong']
greeter_user(usernames)