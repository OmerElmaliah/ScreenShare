import sqlite3


class UserBase(object):
    def __init__(self):
        self.conn = sqlite3.connect('screenshare.db')
        self.c = self.conn.cursor()
        self.c.execute('CREATE TABLE IF NOT EXISTS userbase(Username TEXT, Password TEXT)')

    def create_account(self, user, psw):
        self.c.execute('SELECT * FROM userbase')
        data = self.c.fetchall()
        for row in data:
            if row[0] == user and row[1] == psw:
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
