#!python.exe
import cgi, subjects, os
import db, session

import cgitb
cgitb.enable(display=0, logdir="")

session_id = session.get_session_id()

if session_id is not None:
    _, data = db.get_session(session_id) 

if session_id is None:
    print('Location: login.py\n\n')

uloga=db.get_uloga(data['user_id'])

if (uloga!='admin'): #zaminit da bude admin
    print('\nNEMATE PRAVO PRISTUPA\n')

params=cgi.FieldStorage()

print ("Content-type:text/html\r\n")
print('''<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <link rel="stylesheet" type="text/css" href="/stil.css">
        <title>Forma</title>
    </head>
    <body><form method="get" action="/user_id">''') #nesto ovako 

studenti=db.get_all_students()


if not os.path.isdir('mapa/'):
    os.mkdir('mapa/')
for i in studenti:
    print('<a href="mapa/'+str(i[0]) +'.py">'+i[1]+'</a>') #???
    filename=""+str(i[0])+'.py'
    print(filename)
    file_path=os.path.join('mapa/', filename)
    with open(file_path, 'w') as file:
        file.write('#!python.exe')

    print('<br>')

print(params)


#nedovrseno (dodati upisne listove)



print('''</form><br><a href="zd1.py"><input type="button" value="Povratak"><br>
                    <a href="odjava.py"><input type="button" value="Odjava"></body>
    </html>''')