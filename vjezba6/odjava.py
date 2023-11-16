#!python.exe

import cgitb
import db, session
from http import cookies

cgitb.enable(display=0, logdir="")

session_id=session.get_or_create_session_id()
cookie = cookies.SimpleCookie()
cookie["session_id"]=""
cookie["session_id"]["expires"]=0
print(cookie.output()) 

query = "DELETE FROM sessions WHERE session_id = %s"
values = (session_id,)
mydb = db.get_DB_connection()
cursor = mydb.cursor()
cursor.execute(query, values)
mydb.commit()

print('Location: login.py\n\n')