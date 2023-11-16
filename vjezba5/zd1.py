#!python.exe
import cgi, subjects, os
import db, session

import cgitb
cgitb.enable(display=0, logdir="")

params=cgi.FieldStorage()
if (os.environ["REQUEST_METHOD"].upper() == "POST"):
    session.add_to_session(params)


session_id = session.get_session_id()

if session_id is not None:
    _, data = db.get_session(session_id) 

if session_id is None:
    print('Location: login.py\n\n')


def get_data(data, key, value): #key=enr/not/pass, value=id predmeta
    for k in data:
        if (k==key and data[k]==value): 
            return True
    return False

def get_year(data, key):
    for k in data:
        if (k=='year' and data[k]==key):
            return True
    return False

print ("Content-type:text/html\r\n")
print('''<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <link rel="stylesheet" type="text/css" href="/stil.css">
        <title>Forma</title>
    </head>
    <body>''')
username=db.get_username(data['user_id'])
print('<p>Hej '+username+'!</p>')
print('<form action="" method="post">')

for k,v in subjects.year_ids.items(): #za odabir godine
    print('<input type="submit" name="year" value="'+k+'">')
print('<input type="submit" name="year" value="All">')
if (get_year(data, "All")): #ispis svih predmeta
    print('''<br><br><table>
                    <tr>
                        <th>All</th>
    <th>Ects</th><th>Status</th>''')
    for k, v in subjects.subjects.items():
        print('''<tr><td>''')
        print(v['name'])
        print('''</td><td>''')
        print(v['ects'])
        print('''</td><td>''')
        for x, y in subjects.status_names.items():
            if (get_data(data, k, x)):
                if (get_data(data, k, x)==True):
                    print('<input type="radio" name="'+k+'" value="'+x+'" checked>')
                    print(y)
                else: #ISPISUJE 2 PREOSTALA KOJI NISU ODABRANI
                    print('<input type="radio" name="'+k+'" value="'+x+'">')
                    print(y)
            else: #ISPISUJE AKO NISTA NIJE ODABRANO 
                print('<input type="radio" name="'+k+'" value="'+x+'">')
                print(y)
    print('''</td></tr>''')
    print('''</table>''')    

for a,b in subjects.year_ids.items():  #ispis po godini
    if (get_year(data, a)):
        print('''<br><br><table>
                        <tr>
                            <th>''')
        for k,v in subjects.year_names.items():
            if k==b:
                print(v)
        print('''</th>
        <th>Ects</th><th>Status</th>''' )

        for k, v in subjects.subjects.items():
            if v['year']==b:
                print('''<tr><td>''')
                print(v['name'])
                print('''</td><td>''')
                print(v['ects'])
                print('''</td><td>''')
                for x, y in subjects.status_names.items():
                    if (get_data(data, k, x)):
                        if (get_data(data, k, x)==True):
                            print('<input type="radio" name="'+k+'" value="'+x+'" checked>')
                            print(y)
                        else: #ISPISUJE 2 PREOSTALA KOJI NISU ODABRANI
                            print('<input type="radio" name="'+k+'" value="'+x+'">')
                            print(y)
                    else: #ISPISUJE AKO NISTA NIJE ODABRANO 
                        print('<input type="radio" name="'+k+'" value="'+x+'">')
                        print(y)
                print('''</td></tr>''')
        print('''</table>''')        
print('''</form><br><a href="odjava.py"><input type="button" value="Odjava"></body>
    </html>''')