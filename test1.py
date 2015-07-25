#!/usr/bin/env python

import sqlite3

cx = sqlite3.connect("test1.db")
cu = cx.cursor()

cu.execute("create table bom1 (id integer primary key, \
        pid integer, nmae varchar(10) UNIQUE, nickname text NULL)")
for t in [(0,10,'abc','Yu'),(1,20,'cba','Xu')]:
    cx.execute("insert into bom1 values (?,?,?,?)",t)
cx.commit()

cu.execute("select * from bom1")
a = cu.fetchall()
print a

