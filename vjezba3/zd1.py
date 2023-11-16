#!python.exe
import cgi, subjects, os
from http import cookies

import cgitb
cgitb.enable(display=0, logdir="")

cookies_str=os.environ.get('HTTP_COOKIE', '')
cookie=cookies.SimpleCookie(cookies_str)

cookie['year']="1st Year" #default year
params=cgi.FieldStorage()
for k in params: 
    cookie[str(k)]=params.getvalue(k)
print(cookie)

print ("Content-type:text/html\r\n")
print('''<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <link rel="stylesheet" type="text/css" href="/stil.css">
        <title>Forma</title>
    </head>
    <body>''')

print('<form action="" method="post">')

for k,v in subjects.year_ids.items(): #za odabir godine
    print('<input type="submit" name="year" value="'+k+'">')

if (params.getvalue("all")): #ispis svih predmeta
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
            if (cookie.get(str(k))):
                if (cookie.get(str(k)).value==x):
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
    cookie['year']=0 #da se petlja ispod ne izvrsi 

for a,b in subjects.year_ids.items():  #ispis po godini
    if (a==cookie.get('year').value):
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
                    if (cookie.get(str(k))):
                        if (cookie.get(str(k)).value==x):
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


print('<br><input type="submit" name="all" value="All">')
print('''</form></body>
    </html>''')