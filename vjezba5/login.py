#!python.exe
import cgi, os
import db, session
import cgitb
import password_utils

cgitb.enable(display=0, logdir="")

params=cgi.FieldStorage()

if (os.environ["REQUEST_METHOD"].upper() == "POST"):
    username=params.getvalue("username")
    password=params.getvalue("password")

    if(password_utils.autentikacija(username, password)==True):
        user=db.get_user(username)
        session_id=session.get_or_create_session_id()
        db.add_user_to_session(session_id, user)
        print('Location:zd1.py')
    else:        
        print('\n\nGRESKA U USERNAME/PASSWORD')

print ("Content-type:text/html\r\n")
print('''<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <link rel="stylesheet" type="text/css" href="/stil.css">
        <title>Forma</title>
    </head>
    <body>''')
print('<form method="post">')
print('''<p>LOGIN</p>
        <div class="login">
            <br>Korisnicko ime:<input type="text" name="username" placeholder="User"><br>
            <br>Lozinka:<input type="password" name="password"><br>
            <br><input type="submit" value="Login">
        </form>
            <a href="promjenalozinke.py"><input type="button" value="Promjena lozinke">
            <a href="registracija.py"><input type="button" value="Povratak na registraciju"></div>
    </body>
</html>''')