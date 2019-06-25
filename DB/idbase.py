import rethinkdb as r
import os
import binascii
import random


class IdBase(object):
    def __init__(self):
        self.connection = r.connect(host='10.0.0.4', port=28015)

    def create_new_instance(self, st):
        """Assigns an ID and ID password to an account that logged in with the additional IP given

        ARGS:
            st(string) - IP of the account's computer
        """
        data = r.db("screenshare").table("idbase").run(self.connection)
        for cust in data:
            if st == cust["id"]:
                r.db("screenshare").table("idbase").filter(r.row["id"] == st).delete().run(self.connection)

        id_user = str(binascii.hexlify(os.urandom(8)))
        id_user = id_user[2:len(id_user) - 2]
        id_psw = str(random.randint(1001, 4999))
        r.db("screenshare").table("idbase").insert({"id_user": id_user,
                                                    "id_psw": id_psw,
                                                    "id": st}).run(self.connection)
        return id_user, id_psw

    def get_id(self, idu, idp):
        """Filters the database in search of the IP of the user using the ID and ID password

        ARGS:
            idu(string) - ID of the user
            idp(string) - ID password of the user
        """
        data = r.db("screenshare").table("idbase").run(self.connection)
        for cust in data:
            if idu == cust["id_user"] and idp == cust["id_psw"]:
                return True, cust["id"]

        return False, ''

    def close(self):
        """Closes connection with database"""
        self.connection.close()


