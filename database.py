class Database:
    db = open("source.txt", "r")

    def read_entry(self):
        return self.db.readline()

    def close(self):
        self.db.close()


def connect():
    return Database()
