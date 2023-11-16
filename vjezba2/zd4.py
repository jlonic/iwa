#!python.exe
import cgi
import cgitb
cgitb.enable(display=0, logdir="")

params = cgi.FieldStorage() 

print ("Content-type:text/html\r\n")
print('''<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <link rel="stylesheet" type="text/css" href="/stil.css">
        <title>Ispis</title>
    </head>
    <body>
        <form method="post">
            <table>
                    <caption><b>Uneseni podaci</b></caption>
                <tr>
                    <th>Ime:</th>
                    <th>''')
print (params.getvalue("firstname")) 
print('''           </th>
                </tr>
                <tr>
                    <th>E-mail:</th>
                    <th>''')
print (params.getvalue("email"))
print('''           </th>
                </tr>
                <tr>
                    <th>Status:</th>
                    <th>''')
print (params.getvalue("status"))
print('''           </th>          
                </tr>
                <tr>
                    <th>Smjer:</th>
                    <th>''')
print (params.getvalue("smjer"))                    
print('''            </th>
                </tr>
                <tr>
                    <th>Zavrsni:</th>
                    <th>''')
if  params.getvalue("zavrsni"):
    print (params.getvalue("zavrsni"))
else:
    print("ne")
print('''           </th>
                </tr>
                <tr>
                    <th>Napomene:</th>
                    <th>''')
print (params.getvalue("napomene"))
print('''           </th>
                </tr>
            </table>''')
# print ('<input type="hidden" name="firstname" value="' + params.getvalue("firstname") + '">')
# print ('<input type="hidden" name="status" value="' + params.getvalue("status") + '">')
# print ('<input type="hidden" name="email" value="' + params.getvalue("email") + '">')
# print ('<input type="hidden" name="smjer" value="' + params.getvalue("smjer") + '">')
# print ('<input type="hidden" name="zavrsni" value="' + params.getvalue("zavrsni") + '">')
# print ('<input type="hidden" name="napomene" value="' + params.getvalue("napomene") + '">')
print('''            
        </form>
        <br><a href="zd1.py"><button>Na pocetak:</button></a>
    </body>
</html>''')