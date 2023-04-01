"""
Module for work with archive file.
"""

import json


def readjsonarchive() -> list:
    """Read json-archive and return it"""
    with open('./archive/archive.json', 'r') as jstreamr:
        return json.load(jstreamr)


def addtoarchive(add: dict) -> None:
    """Read json-archive; add new dict to the end; rewrite json-archive"""
    jsadd = readjsonarchive()
    jsadd.append(add)
    with open('./archive/archive.json', 'w') as jstreamw:
        json.dump(jsadd, jstreamw, ensure_ascii=False)
