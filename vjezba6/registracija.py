#!python.exe
import cgi, os
import db
import cgitb

cgitb.enable(display=0, logdir="")

params=cgi.FieldStorage()

if (os.environ["REQUEST_METHOD"].upper() == "POST"):
    username=params.getvalue("username")
    email=params.getvalue("email")
    password=params.getvalue("password")
    
    if ((db.existing_user(username, email))==True): #ako user vec postoji
        print('\n\nGRESKA, POSTOJECI USER')
    elif ((password)!=(params.getvalue("password2"))):
        print('\n\nUNESENE LOZINKE NISU JEDNAKE')
    else:
        db.create_user(username, email, password)
        print('Location: login.py')

print ("Content-type:text/html\r\n")
print('''\r\n<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <link rel="stylesheet" type="text/css" href="/stil.css">
        <title>Forma</title>
    </head>
    <body>''')
print("""<form method="POST">
    <p>REGISTRACIJA</p>
    <div class="registracija">
       Username: <input type="text" name="username" placeholder="User"><br><br>
       Email: <input type="email" name="email" placeholder="email@email.com"><br><br>
       Password: <input type="password" name="password"><br><br>
       Repeat password: <input type="password" name="password2"><br><br>
       <input type="submit" value="Register">
        </form>
        <a href="login.py"><input type="button" value="Login">
    </div>""")
print('''</body>
    </html>''')