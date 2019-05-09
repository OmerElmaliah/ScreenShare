import rethinkdb as r


class UserBase(object):
    def __init__(self):
        self.connection = r.connect(host='127.0.0.1', port=28015)
        # create database 'screenshare' and table 'userbase'

    def create_account(self, user, psw):
        data = r.db("screenshare").table("userbase").filter(r.row["user"] == user).run(self.connection)
        if user in str(data):
            return False

        r.db("screenshare").table("userbase").insert({"user": user, "psw": psw}).run(self.connection)
        return True

    def verification(self, user, psw):
        if len(user) and len(psw) > 0:
            data_user = r.db("screenshare").table("userbase").filter(r.row["user"] == user).run(self.connection)
            data_psw = r.db("screenshare").table("userbase").filter(r.row["psw"] == psw).run(self.connection)

            if user in str(data_user) and psw in str(data_psw):
                return True
        return False

    def close(self):
        self.connection.close()
