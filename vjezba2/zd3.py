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
        <title>Forma</title>
    </head>
    <body>
        <form action="zd4.py" method="post">
            <table>
                <tr>
                    <th>Napomene:</th>
                    <th><textarea name="napomene" placeholder="Prelazak na izvanredni studij..."></textarea></th>
                </tr>
                
                <tr>
                    <th><input type="submit" value="Next"></th>
                </tr>
            </table>''')
print ('<input type="hidden" name="firstname" value="' + params.getvalue("firstname") + '">')
print ('<input type="hidden" name="status" value="' + params.getvalue("status") + '">')
print ('<input type="hidden" name="email" value="' + params.getvalue("email") + '">')
print ('<input type="hidden" name="smjer" value="' + params.getvalue("smjer") + '">')
if  params.getvalue("zavrsni"):
    print ('<input type="hidden" name="zavrsni" value="' + params.getvalue("zavrsni") + '">')


print('''        
        </form>
    </body>
</html>''')