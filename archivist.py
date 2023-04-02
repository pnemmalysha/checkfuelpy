"""
Module for work with archive file.
"""

import json
import sqlite3


archivejsonfile = './archive/archive.json'
archivedbfile = './archive/archive.db'


def readjsonarchive() -> list:
    """Read json-archive and return it"""
    with open(archivejsonfile, 'r') as jstreamr:
        return json.load(jstreamr)


def addtoarchive(add: dict) -> None:
    """Read json-archive; add new dict to the end; rewrite json-archive"""
    jsadd = readjsonarchive()
    jsadd.append(add)
    with open(archivejsonfile, 'w') as jstreamw:
        json.dump(jsadd, jstreamw, ensure_ascii=False, indent=4)


def dosqlcode(sqlcode: str) -> list:
    with sqlite3.connect(archivedbfile) as con:
        cur = con.cursor()
        cur.execute(sqlcode)
        contents = cur.fetchall()
        return contents
