import rethinkdb as r


class UserBase(object):
    def __init__(self):
        self.connection = r.connect(host='10.0.0.4', port=28015)

    def create_account(self, user, psw):
        """Gets username and password and checks if they already exist in the table, if not adds them

        ARGS:
            user(string) - The username of the user's account
            psw(string) - The password of the user's account
        """
        data = r.db("screenshare").table("userbase").filter(r.row["user"] == user).run(self.connection)
        if user in str(data):
            return False

        r.db("screenshare").table("userbase").insert({"user": user, "psw": psw}).run(self.connection)
        return True

    def verification(self, user, psw):
        """Verifies if the given user and password do exist in the table of the database, if so connects to the main
        window

        ARGS:
            user(string) - The username of the user's account
            psw(string) - The password of the user's account
        """
        if len(user) and len(psw) > 0:
            data_user = r.db("screenshare").table("userbase").filter(r.row["user"] == user).run(self.connection)
            data_psw = r.db("screenshare").table("userbase").filter(r.row["psw"] == psw).run(self.connection)

            if user in str(data_user) and psw in str(data_psw):
                return True
        return False

    def close(self):
        """Closes connection with database"""
        self.connection.close()
