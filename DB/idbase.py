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

        id_user = str(binascii.hexlify(os.urandom(8)))
        id_user = id_user[2:len(id_user) - 2]
        r.db("screenshare").table("idbase").insert({"id_user": id_user,
                                                    "id": st}).run(self.connection)
        return id_user

    def get_id(self, idu):
        data = r.db("screenshare").table("idbase").filter(r.row["id_user"] == idu).run(self.connection)
        if idu in data:
            print(data)
            # return id

    def close(self):
        self.connection.close()

