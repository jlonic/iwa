#!python.exe
import cgi
import cgitb
cgitb.enable(display=0, logdir="")

params = cgi.FieldStorage() 

print ("Content-type:text/html")
if ((params.getvalue("p1"))!=(params.getvalue("p2"))):
    # print("UNESENE LOZINKE NISU ISTE")    
    # print('''<br><a href="zd1.py"><button>Na pocetak:</button></a>''')
    print("Location: zd1.py")
    print()
else:
    print()   
    print('''<!DOCTYPE html>
    <html>
        <head> 
            <meta charset="UTF-8">
            <link rel="stylesheet" type="text/css" href="/stil.css">
            <title>Forma</title>
        </head>
        <body>
            <form action="zd3.py" method="post">
                <table>
                    <tr>
                        <th>Status:</th>
                        <th>Redovan: <input name="status" value="Redovan" type="radio"> Izvanredan: <input name="status" value="Izvanredan" type="radio"></th>
                    </tr>
                    <tr>
                        <th>E-mail:</th>
                        <th><input type="email" name="email" placeholder="abc@oss.unist.hr"></th>
                    </tr>
                    <tr>
                        <th>Smjer:</th>
                        <th>
                            <select name="smjer">
                                <option value="Baze podataka">Baza podataka</option>
                                <option value="Programiranje">Programiranje</option>
                                <option value="Mreze">Mreze</option>
                                <option value="Informacijski sustavi">Informacijski sustavi</option>
                            </select>
                        </th>
                    </tr>
                    <tr>
                        <th>Zavrsni:</th>
                        <th>
                            <input type="checkbox" name="zavrsni" value="da">
                        </th>
                    </tr>
                    <tr>
                        <th><input type="submit" value="Next"></a></th>
                    </tr>
                </table>''')
    print ('<input type="hidden" name="firstname" value="' + params.getvalue("firstname") + '">')
    print('''        
            </form>
        </body>
    </html>''')