"""
David Vayman
IS211_Assignment10"""


import sqlite3 as lite
import sys

conn = lite.connect('pets.db')

pers_id = raw_input("Person ID: ")
if pers_id == "-1":
    sys.exit()

try:
    cur = conn.cursor()
    cur.execute("SELECT first_name,last_name,per.age,name,pet.age,breed,dead "\
                "FROM person per "\
                "INNER JOIN person_pet pp ON per.id = pp.person_id "\
                "INNER JOIN pet pet ON pet.id = pp.pet_id "\
                "WHERE per.id = ?",pers_id)

    rows = cur.fetchall()
    for row in rows:
        if row[6]:
            tense1 = 'had'
            tense2 = 'was'
        else:
            tense1 = 'has'
            tense2 = 'is'
        print "{} {},Age {}".format(row[0],row[1],row[2])
        print "{} {} a {} named {} that {} {} years old".format(
            row[0],tense1,row[5],row[3],tense2,row[4])
        
#except lite.Error:
#    print "Invalid User ID"
#    pers_id = raw_input("Person ID: ")

except lite.Error as e:
    raise lite.Error(e)