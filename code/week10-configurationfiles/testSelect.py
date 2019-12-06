import mysql.connector
import dbconfig as cfg

db = mysql.connector.connect(
  host=cfg.mysql['host'],
  user=cfg.mysql['username'],
  password=cfg.mysql['password'],
  #user="datarep",  # this is the user name on my mac
  #passwd="password" # for my mac
  database=cfg.mysql['database']
)

cursor = db.cursor()
sql="select * from student"


cursor.execute(sql)
result = cursor.fetchall()
for x in result:
  print(x)

