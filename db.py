import os
import sys
import sqlite3 as sql

def connect(db_file):
        global con 
        con = sql.connect(db_file)

def execute(to_execute):
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS users (name TEXT, password TEXT)")
