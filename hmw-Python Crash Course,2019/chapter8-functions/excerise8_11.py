# Start with your work from Exercise 8-10. Call the function send_messages() with a copy of the list of messages. 
# After calling the function, print both of your lists to show that the original list has retained its messages.

new_messages = ["Happy New Year", "Merry Christmas", "Happy Halloween"]
sent_messages = []

def show_messages(new_messages, sent_messages):
    print("New messages:")
    while new_messages:
        unsent_message = new_messages.pop()
        print(unsent_message)
        sent_messages.append(unsent_message)

def send_messages(sent_messages):
    print("\nThese messages are sent:")
    for sent_message in sent_messages:
        print(sent_message)

show_messages(new_messages, sent_messages)
send_messages(sent_messages)
  