#!python.exe
import cgi
import cgitb
cgitb.enable(display=0, logdir="")

print ("Content-type:text/html\r\n")
print('''<!DOCTYPE html>
<html>
    <head> 
        <meta charset="UTF-8">
        <link rel="stylesheet" type="text/css" href="/stil.css">
        <title>Forma</title>
    </head>
    <body>
        <form action="zd2.py" method="post">
            <table>
                <tr>
                    <th>Ime:</th>
                    <th><input type="text" name="firstname" value=""></th>
                </tr>
                <tr>
                    <th>Lozinka</th>
                    <th><input type="password" name="p1"></th>
                </tr>
                <tr>
                    <th>Ponovi lozinku:</th>
                    <th><input type="password" name="p2"></th>
                </tr>
                <tr>
                    <th><input type="submit" value="Next"></a></th>
                </tr>
            </table>
        </form>
    </body>
</html>''')