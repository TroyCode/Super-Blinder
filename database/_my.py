import MySQLdb

db = MySQLdb.connect(host='localhost',
                     user='troy', 
                     passwd='810748a', 
                     db='SuperBlinder')

cur = db.cursor("CREATE TABLE `SuperBlinder`.`new_table` ("
                ");") 