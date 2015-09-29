#!/usr/bin/python
import MySQLdb

DB = MySQLdb.connect(host='localhost', # your host, usually localhost
                     user='troy', # your username
                     passwd='810748a', # your password
                     db='SuperBlinder') # name of the data base

# you must create a Cursor object. It will let
# you execute all the queries you need
CUR = DB.cursor() 

def channel_insert(data):
  CUR.execute("")

  CUR.execute("INSERT INTO youtube_channels (youtube_id, username, title, description, country_id, published_at,"
	                                        "created_at, updated_at)"
	          "VALUES('{data.youtubeId}', '{data.username}', '{data.title}', '{data.description}',"
	            "'1', "2010-11-19T09:07:52.000Z", NOW(), NOW());"