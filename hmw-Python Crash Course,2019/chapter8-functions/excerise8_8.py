# Start with your program from Exercise 8-7. Write a while loop that allows users to enter an album’s artist and title.
#  Once you have that information, call make_album() with the user’s input and print the dictionary that’s created.
#  Be sure to include a quit value in the while loop

def make_album(artist, title, songs=None):
    album = {'artist': artist, 'title': title, 'songs': songs}
    return album

while True:
    print("\nEnter 'q' at anytime to quit")
    print("-----------------------------")

    artist = input("Enter an artist: ")
    if artist == 'q':
        break

    title = input("Enter an album title: ")
    if title == 'q':
        break

    album = make_album(artist, title)
    print(album)