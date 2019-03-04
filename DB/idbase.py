import rethinkdb as r
import os
import binascii
import random


class IdBase(object):
    def __init__(self):
        self.connection = r.connect(host='192.168.1.174', port=28015)

    def create_new_instance(self, st):
        data = r.db("screenshare").table("idbase").filter(r.row["id"] == st).run(self.connection)
        if st in data:
            r.db("screenshare").table("idbase").filter(r.row["id"] == st).delete(self.connection)

        id_user = binascii.hexlify(os.urandom(16))
        id_psw = random.randint(1001, 4999)
        r.db("screenshare").table("idbase").insert({"id_user": id_user,
                                                    "id_psw": id_psw,
                                                    "id": st}).run(self.connection)
        return id_user, id_psw

    def get_id(self, idu, idp):
        data = r.db("screenshare").table("idbase").filter(r.row["id_user"] == idu,
                                                            r.row["id_psw"] == idp).run(self.connection)
        if (idu in data) and (idp in data):
            print(data)
            # return id

    def close(self):
        self.connection.close()
