import rethinkdb as r
import os
import binascii
import random


class IdBase(object):
    # TODO: Reorganize accordingly to dataserver
    def __init__(self):
        self.connection = r.connect(host='192.168.1.174', port=28015)

    def create_new_instance(self, st):
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
        data = r.db("screenshare").table("idbase").run(self.connection)
        for cust in data:
            if idu == cust["id_user"] and idp == cust["id_psw"]:
                return True, cust["id"]

        return False, ''

    def close(self):
        self.connection.close()


