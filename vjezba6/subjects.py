#!python.exe
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

def get_year(): 
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT DISTINCT godina FROM subjects")
    myresult = cursor.fetchall() 
    return myresult

def get_subject_names(): #puno ime predmeta
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT ime FROM subjects")
    myresult = cursor.fetchall() 
    return myresult

def get_subject_kod(): #kod predmeta
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT kod FROM subjects")
    myresult = cursor.fetchall() 
    return myresult

def get_ects():
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT bodovi FROM subjects")
    myresult = cursor.fetchall() 
    return myresult


def get_all_subject_data():
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM subjects")
    myresult = cursor.fetchall() 
    return myresult
