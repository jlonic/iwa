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

params=cgi.FieldStorage()
if (os.environ["REQUEST_METHOD"].upper() == "POST"):
    session.add_to_session(params) #dodaje user_id u sesiju
    db.add_to_upisni_list(data['user_id'], params)

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
predmeti=subjects.get_all_subject_data()
godine=subjects.get_year()
print('<form action="" method="post">')
for i in range(len(godine)): #za odabir godine
    print('<input type="submit" name="year" value="'+str(godine[i][0])+'">')
print('<input type="submit" name="year" value="All">')
if ((params.getfirst('year')=="All")): #ispis svih predmeta
    print('''<br><br><table>
                    <tr>
                        <th>All</th>
    <th>Ects</th><th>Status</th>''')
    for i in range(len(predmeti)):
            print('''<tr><td>''')
            print(predmeti[i][2])
            print('''</td><td>''')
            print(predmeti[i][3])
            print('''</td><td>''')

            st=db.get_status(data['user_id'], predmeti[i][1])            
            if (st=='pass'):
                print('<input type="radio" name="'+str(predmeti[i][1])+'" value="pass" checked>')
                print('Passed')
                print('<input type="radio" name="'+str(predmeti[i][1])+'" value="enr">')
                print('Enrolled')
            elif (st=='enr'):
                print('<input type="radio" name="'+str(predmeti[i][1])+'" value="pass">')
                print('Passed')
                print('<input type="radio" name="'+str(predmeti[i][1])+'" value="enr" checked>')
                print('Enrolled')
            else:
                print('<input type="radio" name="'+str(predmeti[i][1])+'" value="pass">')
                print('Passed')
                print('<input type="radio" name="'+str(predmeti[i][1])+'" value="enr">')
                print('Enrolled')
    print('''</td></tr>''')
    print('''</table>''')    

for b in range(len(godine)):  #ispis po godini
    if ((params.getfirst('year')==str(godine[b][0]))): #B=BROJ GODINE
        print('''<br><br><table>
                        <tr>
                            <th>''')
        print('Year: ')
        print(b+1) #+1 jer pocinje od 0
        print('''</th>
        <th>Ects</th><th>Status</th>''' )

        for i in range(len(predmeti)):
            if ((predmeti[i][4])==(godine[b][0])):
                print('''<tr><td>''')
                print(predmeti[i][2])
                print('''</td><td>''')
                print(predmeti[i][3])
                print('''</td><td>''')
                st=db.get_status(data['user_id'], predmeti[i][1])            
                if (st=='pass'):
                    print('<input type="radio" name="'+str(predmeti[i][1])+'" value="pass" checked>')
                    print('Passed')
                    print('<input type="radio" name="'+str(predmeti[i][1])+'" value="enr">')
                    print('Enrolled')
                elif (st=='enr'):
                    print('<input type="radio" name="'+str(predmeti[i][1])+'" value="pass">')
                    print('Passed')
                    print('<input type="radio" name="'+str(predmeti[i][1])+'" value="enr" checked>')
                    print('Enrolled')
                else:
                    print('<input type="radio" name="'+str(predmeti[i][1])+'" value="pass">')
                    print('Passed')
                    print('<input type="radio" name="'+str(predmeti[i][1])+'" value="enr">')
                    print('Enrolled')
        print('''</table>''')        

print('''</form><br><a href="popis_studenata.py"><input type="button" value="Popis studenata"><br>
                    <a href="odjava.py"><input type="button" value="Odjava"></body>
    </html>''')