import socket
import sqlite3
import pickle


IP = '192.168.1.174'
PORT = 8888
CONN = sqlite3.connect('screenshare.db')
C = CONN.cursor()
C.execute('CREATE TABLE IF NOT EXISTS userbase(Username TEXT, Password TEXT)')


def main():
    socket_db = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_db.bind((IP, PORT))
    while True:
        socket_db.listen(1)
        (client_socket, client_address) = socket_db.accept()
        cmd = client_socket.recv(1024).decode('utf-8')
        user = client_socket.recv(1024).decode('utf-8')
        psw = client_socket.recv(1024).decode('utf-8')
        ans = handle_request(cmd, user, psw)
        client_socket.send(pickle.dumps(ans))


def handle_request(cmd, user, psw):
    if cmd is "ub-ca":
        C.execute('SELECT * FROM userbase')
        data = C.fetchall()
        for row in data:
            if row[0] == user:
                return False

        C.execute('INSERT INTO userbase (Username, Password) VALUES(?, ?)', (user, psw))
        CONN.commit()
        return True

    elif cmd is 'ub-ver':
        C.execute('SELECT * FROM userbase WHERE Username == ? and Password == ?', (user, psw))
        data = C.fetchall()
        if data:
            return True
        return False


if __name__ == '__main__':
    main()
