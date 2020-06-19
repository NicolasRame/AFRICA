import sqlite3
from zipfile import ZipFile
import json
import re
import wptools

conn = sqlite3.connect('pays.sqlite')


def init_db(continent):
    with ZipFile('{}.zip'.format(continent), 'r') as z:
        files = z.namelist()
        for f in files:
            country = f.split('.')[0]
            print(country)
            info = json.loads(z.read(f))
            save_country(conn, country, info)
