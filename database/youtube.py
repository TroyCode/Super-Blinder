import _my

# def channel_insert(data):
#   _mysql.cur.execute("INSERT INTO youtube_channels (youtube_id, username, title, description, country_id, published_at,"
#           	                                       "created_at, updated_at)"
#           	         "VALUES('{data.youtubeId}', '{data.username}', '{data.title}', '{data.description}',"
#           	                "'1', "2010-11-19T09:07:52.000Z", NOW(), NOW());"

def test():
  _mysql.cur.execute("CREATE TABLE `SuperBlinder`.`new_table` ("
                     ");")