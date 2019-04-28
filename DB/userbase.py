import socket


class UserBase(object):
    # TODO: Reorganize accordingly to dataserver
    def __init__(self):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client_socket.connect(('192.168.1.174', 8880))

    def create_account(self, user, psw):
        self.c.execute('SELECT * FROM userbase')
        data = self.c.fetchall()
        for row in data:
            if row[0] == user:
                return False

        self.c.execute('INSERT INTO userbase (Username, Password) VALUES(?, ?)', (user, psw))
        self.conn.commit()
        return True

    def verification(self, user, psw):
        self.c.execute('SELECT * FROM userbase WHERE Username == ? and Password == ?', (user, psw))
        data = self.c.fetchall()
        if data:
            return True
        return False

    def close(self):
        self.c.close()
        self.conn.close()
