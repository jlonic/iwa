#!python.exe
import cgi, os
import db, password_utils, cgitb

cgitb.enable(display=0, logdir="")

params=cgi.FieldStorage()

if (os.environ["REQUEST_METHOD"].upper() == "POST"):
    username=params.getvalue("username")
    oldpassword=params.getvalue("password")
    new_password=params.getvalue("newpassword")
    rep_password=params.getvalue("newpassword2")

    if (password_utils.autentikacija(username, oldpassword)==True): 
        if ((params.getvalue("newpassword"))==(params.getvalue("newpassword2"))):
            db.change_user_password(username, new_password)
            print('Location:login.py')
        else:
            print('\n\nnova lozinka i ponovljena nova lozinka se ne podudaraju')
    else:
        print('\n\nkorisnicko ime i stara lozinka se ne podudaraju')

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
print('''<p>PROMJENA LOZINKE</p>
        <div class="promjenalozinke"><br>Korisnicko ime:<input type="text" name="username" placeholder="User"><br>
            <br>Stara lozinka:<input type="password" name="password"><br>
            <br>Nova lozinka:<input type="password" name="newpassword"><br>
            <br>Ponovljena nova lozinka:<input type="password" name="newpassword2"><br>
            <br><input type="submit" value="Submit">
            <a href="login.py"><input type="button" value="Login">
            <a href="registracija.py"><input type="button" value="Povratak na registraciju">
        </div>
        </form>
    </body>
</html>''')