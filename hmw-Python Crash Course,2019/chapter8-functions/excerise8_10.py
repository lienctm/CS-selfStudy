# Start with a copy of your program from Exercise 8-9. Write a function called send_messages()
# that prints each text message and moves each message to a new list called sent_messages as it’s printed.
# After calling the function, print both of your lists to make sure the messages were moved correctly.

new_messages = ["Happy New Year", "Merry Christmas", "Happy Halloween"]
sent_messages = []

def send_message (new_messages, sent_messages):
    print("New messages:")
    while new_messages:
        unsent_message = new_messages.pop()
        print(unsent_message)
        sent_messages.append(unsent_message)
    print("\nThese messages are sent:")
    for sent_message in sent_messages:
        print(sent_message)

send_message(new_messages, sent_messages)

  