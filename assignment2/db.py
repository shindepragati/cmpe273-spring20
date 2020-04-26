import sqlite3
import time
from flask import Flask, escape, request,jsonify
import json

app = Flask(__name__)

sqlite_file = '/Users/karthikkathirvel/Desktop/GitHub_273/scantron.sqlite'

table_scantron = 'pratests'
new_field = 'actual_data'
col_1 = 'subject'
col_2 ='answer_keys'
id_col='test_id'
field_type =  'TEXT'
conn=sqlite3.connect(sqlite_file)
c=conn.cursor()

def altertable(col_val,col_type):
    conn=sqlite3.connect(sqlite_file)
    c=conn.cursor()
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=table_scantron, cn=col_val, ct=col_type))
    conn.commit()
    conn.close()

def insertInDB(subject,anskeys,jsonval):
    conn=sqlite3.connect(sqlite_file)
    c=conn.cursor()
    c.execute("insert into pratests values (?,?,?)",[subject,anskeys, json.dumps(jsonval)])       
    conn.commit()
    conn.close()

def insertInSubmissionDB(idval,url,name,subject,anskeys,score):
    conn=sqlite3.connect(sqlite_file)
    c=conn.cursor()
    c.execute("insert into praSubmissions values (?,?,?,?,?,?)",[idval,url,name,subject,anskeys,score])       
    conn.commit()
    conn.close()

def querDBWithConditionTESTS(tname,colname,cvalue):
    conn=sqlite3.connect(sqlite_file)
    c=conn.cursor()
    c.execute('SELECT rowid,subject,answer_keys,submissions FROM {tn} Where {col}="{colval}"'.format(tn=tname,col=colname,colval=cvalue))
    all_rows = c.fetchall()
    conn.close()
    return all_rows
    
def querDBWithCondition(ecolval,tname,colname,cvalue):
    conn=sqlite3.connect(sqlite_file)
    c=conn.cursor()
    c.execute('SELECT {expctedcol} FROM {tn} Where {col}="{colval}"'.format(expctedcol=ecolval,tn=tname,col=colname,colval=cvalue))
    all_rows = c.fetchall()
    conn.close()
    return all_rows

def querySubmissionTable(table_scantron):
    conn=sqlite3.connect(sqlite_file)
    c=conn.cursor()
    c.execute('SELECT * FROM {tn}'.format(tn=table_scantron))
    all_rows = c.fetchall()
    conn.close()
    return all_rows

def queryTestsTable(table_scantron):
    conn=sqlite3.connect(sqlite_file)
    c=conn.cursor()
    c.execute('SELECT rowid,subject,answer_keys,submissions FROM {tn}'.format(tn=table_scantron))
    all_rows = c.fetchall()
    conn.close()
    return all_rows

def showtable(tablename):
    conn=sqlite3.connect(sqlite_file)
    c=conn.cursor()
    c.execute('PRAGMA TABLE_INFO({})'.format(tablename))
    names = [tup[1] for tup in c.fetchall()]
    print(names)
    conn.close()

def createTestsTable():
    conn=sqlite3.connect(sqlite_file)
    c=conn.cursor()
    sql ='''CREATE TABLE IF NOT EXISTS praTESTS(
        subject TEXT,
        answer_keys TEXT,
        submissions json
        )'''
    c.execute(sql)
    conn.commit()
    conn.close()

def createScantronAnswersTable():
    conn=sqlite3.connect(sqlite_file)
    c=conn.cursor()
    sql ='''CREATE TABLE IF NOT EXISTS praSubmissions(
        scantron_id INTEGER,
        scantron_url TEXT,
        name TEXT,
        subject TEXT,
        actualans_keys TEXT,
        score INTEGER
        )'''
    c.execute(sql)
    conn.commit()
    conn.close()

def droptable(tablename):
    conn=sqlite3.connect(sqlite_file)
    c=conn.cursor()
    c.execute('DROP TABLE {tname}'.format(tname=tablename))
    conn.commit()
    conn.close()

#droptable('submissions')
#createCompleteTable()
# altertable('submission1','json')

# insertInDB('science','12344','fff')

#createScantronAnswersTable()
#showtable('Submissions')
#querDBWithCondition('answer_keys','TESTS','subject','Math')
#querDBWithCondition('answer_keys','TESTS','rowid',1)

#querySubmissionTable('Submissions')

