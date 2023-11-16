import mysql.connector # "C:\ProgramData\Anaconda3\python.exe" -m pip install mysql-connector 
import json
import password_utils

db_conf = {
    "host":"localhost",
    "db_name": "predmeti",
    "user":"root",
    "passwd":""
}

def get_DB_connection():
    mydb = mysql.connector.connect(
        host=db_conf["host"],
        user=db_conf["user"],
        passwd=db_conf["passwd"],
        database=db_conf["db_name"]
    )
    return mydb

def create_session():
    query = "INSERT INTO sessions (data) VALUES (%s)"
    values = (json.dumps({}),)
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute(query, values)
    mydb.commit()
    return cursor.lastrowid 

def get_session(session_id):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM sessions WHERE session_id=" + str(session_id))
    myresult = cursor.fetchone()
    return myresult[0], json.loads(myresult[1])

def replace_session(session_id, data):#replace-prvo izbrisi, a onda ubaci (delete/insert)
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("""
    REPLACE INTO sessions(session_id,data) 
    VALUES (%s,%s)""",
    (session_id, json.dumps(data)))
    mydb.commit()


def create_user(username, email, password):
    query = "INSERT INTO users (ime, email, password) VALUES (%s, %s, %s)" 
    hashed_password = password_utils.hash_password(password)
    values = (username, email, hashed_password) 
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute(query, values)
    mydb.commit()
    return cursor.lastrowid 

def existing_user(name, email):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM users WHERE ime='" + name + "'OR email='"
                   + email + "'")
    myresult = cursor.fetchall() #treba biti prazan ako user ne postoji
    
    if (myresult): 
        return True
    return False

def get_user(username): 
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM users WHERE ime='" + username + "'")
    myresult = cursor.fetchone()

    return myresult

def change_user_password(username, password):
    query = "UPDATE users SET password=%s WHERE ime=%s"
    password = password_utils.hash_password(password)
    values = (password, username)
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute(query, values)
    mydb.commit()


def add_user_to_session(session_id, user):
    data={"user_id": user[0]}
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("""
    REPLACE INTO sessions(session_id,data) 
    VALUES (%s,%s)""",
    (session_id, json.dumps(data)))
    mydb.commit()

def get_username(user_id):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT ime FROM users WHERE id="+str(user_id))
    myresult = cursor.fetchone()

    return myresult[0]

def get_predmet_id(predmet):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT id FROM subjects WHERE kod='"+str(predmet)+"'")
    myresult = cursor.fetchone()
    return myresult[0]

def update_upisni_list(user_id, predmet): #pomocna funkcija koja provjerava postoji li predmet u upisnom listu za studenta
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM upisni_list WHERE id_studenta='" + str(user_id) + "'AND id_predmeta='"
                   + str(predmet) + "'")
    myresult = cursor.fetchall() #treba biti prazan ako ne postoji
    if (myresult): 
        return True
    return False


def add_to_upisni_list(user_id, params): #UPDATEA STATUSE ZA POSTOJECE PREDMETE, DODAJE STATUSE ZA NOVE
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    for k in range(len(params.keys())):
        if (params.keys()[k]!='year'):
            predmet=get_predmet_id(str(params.keys()[k]))
            status=params.getvalue(params.keys()[k])
            query1="INSERT INTO upisni_list (id_studenta, id_predmeta, status) VALUES (%s, %s, %s)"
            query2="UPDATE upisni_list SET status=%s WHERE id_predmeta=%s AND id_studenta=%s"
            values1=(user_id, predmet, status)
            values2=(status, predmet, user_id)
            if (update_upisni_list(user_id, predmet)==True):
                cursor.execute(query2, values2)
            else:
                cursor.execute(query1, values1)
                
            mydb.commit()

def get_status(user_id, predmet):
    mydb = get_DB_connection()
    cursor = mydb.cursor()

    cursor.execute("SELECT status FROM upisni_list WHERE id_studenta='"+str(user_id) + "'AND id_predmeta='"+str(get_predmet_id(predmet)) +"'" )
    myresult = cursor.fetchone() #treba biti prazan ako user ne postoji
    if (myresult): 
        return myresult[0]
    return False


def get_uloga(user_id):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT uloga FROM users WHERE id="+str(user_id))
    myresult = cursor.fetchone()
    return myresult[0]


def get_all_students():
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT id, ime FROM users WHERE uloga <> 'admin'")
    myresult = cursor.fetchall()
    return myresult