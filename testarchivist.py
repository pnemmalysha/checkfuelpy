"""
Module with class for work with archive file.

Same as archivist.
Needs attention.
"""

import json
import sqlite3


class Archivist:
    archivepath = './archive/'


class JSONArchivist(Archivist):
    def __init__(self) -> None:
        self.jsonfile = 'archive.json'

    def readjsonarchive(self) -> list:
        """Read json-archive and return it"""
        with open(self.archivepath + self.jsonfile, 'r') as jstreamr:
            return json.load(jstreamr)

    def addtoarchive(self, add: dict) -> None:
        """Read json-archive; add new dict to the end; rewrite json-archive"""
        jsadd = self.readjsonarchive(self)
        jsadd.append(add)
        with open(self.archivepath + self.jsonfile, 'w') as jstreamw:
            json.dump(jsadd, jstreamw, ensure_ascii=False, indent=4)


class SQLArchivist(Archivist):
    def __init__(self) -> None:
        self.dbfile = 'archive.db'

    def dosqlcode(self, sqlcode: str) -> list:
        """Connect to SQLite DB, execute code, return fetch as list"""
        with sqlite3.connect(self.archivepath + self.dbfile) as con:
            cur = con.cursor()
            cur.execute(sqlcode)
            contents = cur.fetchall()
            return contents

    def dosqlcodefetchone(self, sqlcode: str) -> tuple:
        """Connect to SQLite DB, execute code, return one fetch as tuple"""
        with sqlite3.connect(self.archivepath + self.dbfile) as con:
            cur = con.cursor()
            cur.execute(sqlcode)
            contents = cur.fetchone()
            return contents
