import sqlite3 as lite

con = None  # db connection


class ScrapingPipeline(object):

    def __init__(self):
        self.setupDBCon()
    #    self.dropTable()
    #    self.createTable()

    def process_item(self, item, spider):
        self.storeInDb(item)
        return item

    def setupDBCon(self):
        self.con = lite.connect('/home/ugur/PycharmProjects/author/db.sqlite3')
        self.cur = self.con.cursor()

    def storeInDb(self, item):
        self.cur.execute("INSERT INTO myQuotes_author(author, text, tags, owner_id) VALUES (?, ?, ?, 0)",
                         (
                             item['author'],
                             item['text'],
                             item['tags']
                         ))
        self.con.commit()

    def __del__(self):
        self.closeDB()

    def closeDB(self):
        self.con.close()

    def createTable(self):
        self.cur.execute("CREATE TABLE IF NOT EXISTS myQuotes_author(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, \
    		author TEXT, \
    		text TEXT, \
            tags TEXT, \
            owner_id INTEGER AUTOINCREMENT \
    		)")

    def dropTable(self):
        self.cur.execute("DROP TABLE IF EXISTS myQuotes_author")


