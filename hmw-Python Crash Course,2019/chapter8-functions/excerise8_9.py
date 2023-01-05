# Make a list containing a series of short text messages. Pass the list to a function called show_messages(),
# which prints each text message.

def show_messages(messages):
    for message in messages:
        print(message)

messages = ["Happy New Year", "Merry Christmas", "Happy Halloween"]
show_messages(messages)