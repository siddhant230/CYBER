import socket

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)


def socket_create():
    try:
        global host
        global port
        global s
        global IPAddr
        host = IPAddr
        port = 9999
        s = socket.socket()
    except:
        print('socket creation error')


def socket_bind():
    try:
        global host
        global s
        global port
        print('binding socket to port : ', str(port))
        s.bind((host, port))
        s.listen(5)
    except:
        print('unable to make a connection')
        print('retrying...')
        socket_bind()


def socket_accept():
    conn, address = s.accept()
    print('connection has been made')
    print('IP : ', address[0], 'with port : ', address[1])
    send_commands(conn)
    s.close()


def send_commands(conn):
    while True:
        text = input('YOU : ')
        if len(str.encode(text)) > 0:
            conn.send(str.encode(text))
            response = str(conn.recv(1024), 'utf-8')
            print('SENDER : ' + response)


if __name__ == '__main__':
    socket_create()
    socket_bind()
    socket_accept()
