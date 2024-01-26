from flask import Flask, request, render_template, send_from_directory,session,flash
import pandas as pd
import string
import os
import random
import mysql.connector
import numpy as np
from datetime import timedelta
import sys
from PIL import Image
import base64
import io
import re
import random
# from random import *
import secrets
from flask_mail import *
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


app = Flask(__name__)
app.config['SECRET_KEY'] = 'the random string'
mail = Mail(app)

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/doctor")
def doctor():
    a=random.randrange(10000, 999999)
    return render_template("doctor.html",a=a)

@app.route('/dlog',methods=['POST', 'GET'])
def dlog():
    if request.method == "POST":

        email = request.form['email']
        capt = request.form['capt']
        c1 = request.form['capt1']
        password1 = request.form['pwd']
        print('p')
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="healthcare_sector")
        cursor = mydb.cursor()

        sql = "select * from doctor where email='%s' and pwd='%s' " % (email, password1)
        print('q')
        x = cursor.execute(sql)
        print(x)
        results = cursor.fetchall()
        print(results)
        global name
        name = results[0][1]
        print(name)
        session['fname'] = results[0][1]
        session['email'] = email
        # session['r']=r
        if(capt==c1):
            if len(results) > 0:
                print('r')
                # session['user'] = username
                # session['id'] = results[0][0]
                # print(id)
                # print(session['id'])
                flash("Sucessfully Login to the Page", "primary")
                return render_template('dhome.html', m="Login Success", msg=results[0][1])

            else:
                return render_template('doctor.html', msg="Login Failure!!!")
        else:
            return render_template('doctor.html', msg="invalid value")

    return render_template('doctor.html')


@app.route("/dreg")
def dreg():
    return render_template("dreg.html")

@app.route('/dregback',methods=['POST','GET'])
def dregback():
    print("gekjhiuth")
    if request.method=='POST':
        print("gekjhiuth")
        fname=request.form['fname']
        lname=request.form['lname']
        email=request.form['email']
        pwd=request.form['pwd']
        addr=request.form['addr']
        cpwd=request.form['cpwd']
        ph=request.form['pno']
        area=request.form['area']
        print(ph)
        print(addr)

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="healthcare_sector"
        )
        mycursor = mydb.cursor()

        sql="select * from doctor"
        result=pd.read_sql_query(sql,mydb)
        email1=result['email'].values
        print(email1)
        if email in email1:
            flash("email already existed","success")
            return render_template('dreg.html', msg="email existed")
        if(pwd==cpwd):
            sql = "INSERT INTO doctor (fname,lname,email,pwd,area,addr,pno) VALUES (%s,%s,%s,%s,%s,%s,%s)"
            val = (fname,lname,email,pwd,area,addr,ph)
            mycursor.execute(sql, val)
            mydb.commit()
            print("Successfully Registered")
            return render_template('dreg.html', msg="registered successfully")
        else:
            flash("Password and Confirm Password not same")
    return render_template('dreg.html',msg="somthing wrong")

@app.route("/dhome")
def dhome():
    return render_template("dhome.html")
@app.route("/feature")
def feature():
    print("lakshmi")
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="healthcare_sector",
        charset='utf8')
    mycursor = mydb.cursor()
    sql = "select * from features"
    print(sql)
    x = pd.read_sql_query(sql, mydb)
    print(x)
    x = x.drop(['email'], axis=1)

    return render_template("feature.html", col_name=x.columns.values, row_val=x.values.tolist())

@app.route('/featureadd',methods=['POST','GET'])
def featureadd():
    print("gekjhiuth")
    if request.method=='POST':
        print("gekjhiuth")
        fname=request.form['fname']
        disp=request.form['disp']
        email = session.get('email')
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="healthcare_sector"
        )
        mycursor = mydb.cursor()

        sql = "INSERT INTO features (email,fname,disp) VALUES (%s,%s,%s)"
        val = (email,fname,disp)
        mycursor.execute(sql, val)
        mydb.commit()
        return render_template('feature.html')

@app.route("/update/<s1>/<s2>/<s3>")
def update(s1=0,s2='',s3=''):
    #sql = "select * from  sreg where id='%s'" % (s)
    #cursor.execute(sql)
    #cursor.fetchall()
    #result1 = pd.read_sql_query(sql, db)
    #db.commit()
    global n
    n = s1
    print(n)
    return render_template("update.html", n=n, s2=s2, s3=s3)
@app.route("/upback",methods=["POST","GET"])
def upback():
    if request.method=="POST":
        n = request.form['id']
        fname = request.form['fname']
        disp = request.form['disp']

        print("b")

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="healthcare_sector",
            charset='utf8'
        )
        print("c")
        mycursor = mydb.cursor()
        print("d")

    sql="update features set fname='%s' , disp='%s' where id='%s' " % (fname,disp,n)
    print(sql)
    mycursor.execute(sql)
    print("11111111111111111111")
    mydb.commit()
    print("11111111111111111111")
    sql = "SELECT * from features where id='%s' " % (n)
    print(sql)
    result1 = pd.read_sql_query(sql, mydb)
    print("11111111111111111111")
    return render_template("feature.html")

@app.route("/delete/<s1>")
def delete(s1=0):
    print("delete items here")
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="healthcare_sector",
        charset='utf8'
    )
    mycursor = mydb.cursor()

    sql = "delete from features where id='"+s1+"' "
    '''mycursor.execute(sql)
    x=mycursor.fetchall()'''
    mycursor.execute(sql)
    mydb.commit()
    print("^^^^^^^^^^^^^")
    '''print(type(x))
    print(x)
    x = x.drop(['photo'], axis=1)
    x["Delete"] = " "'''
    # x["Order"] = " "
    return render_template('delete.html', msg='item deleted successfully')

@app.route("/patient")
def patient():
    a=random.randrange(10000, 999999)
    return render_template("patient.html",a=a)

@app.route('/plog',methods=['POST', 'GET'])
def plog():
    global name, name1
    global r
    if request.method == "POST":
        capt = request.form['capt']
        c1 = request.form['capt1']
        email = request.form['email']
        password1 = request.form['pwd']

        print('p')
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="healthcare_sector")
        cursor = mydb.cursor()


        sql = "select * from patient where email='%s' and pwd='%s' "%(email,password1)
        print('q')
        x = cursor.execute(sql)
        print(x)
        results = cursor.fetchall()
        print(results)
        global name
        name=results[0][1]
        print(name)
        session['fname']=results[0][1]
        session['email'] = email
        #session['r']=r
        if(capt==c1):
            if len(results) > 0:
                print('r')
                # session['user'] = username
                # session['id'] = results[0][0]
                # print(id)
                # print(session['id'])
                flash("Sucessfully Login to the Page", "primary")
                return render_template('phome.html', m="Login Success", msg=results[0][1])

            else:
                return render_template('patient.html', msg="Login Failure!!!")
        else:
            return render_template('patient.html', msg="invalid value")

    return render_template('patient.html')

@app.route("/preg")
def preg():
    return render_template("preg.html")

@app.route('/pregback',methods=['POST','GET'])
def pregback():
    print("gekjhiuth")
    if request.method=='POST':
        print("gekjhiuth")
        fname=request.form['fname']
        lname=request.form['lname']
        email=request.form['email']
        pwd=request.form['pwd']
        addr=request.form['addr']
        cpwd=request.form['cpwd']
        ph=request.form['pno']
        print(ph)
        print(addr)

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="healthcare_sector"
        )
        mycursor = mydb.cursor()

        sql="select * from patient"
        result=pd.read_sql_query(sql,mydb)
        email1=result['email'].values
        print(email1)
        if email in email1:
            flash("email already existed","success")
            return render_template('preg.html', msg="email existed")
        if(pwd==cpwd):
            sql = "INSERT INTO patient(fname,lname,email,pwd,addr,pno) VALUES (%s,%s,%s,%s,%s,%s)"
            val = (fname,lname,email,pwd,addr,ph)
            mycursor.execute(sql, val)
            mydb.commit()
            print("Successfully Registered")
            return render_template('preg.html', msg="registered successfully")
        else:
            flash("Password and Confirm Password not same")
    return render_template('preg.html',msg="somthing wrong")

@app.route("/vd")
def vd():
    print("Reading BLOB data from python_employee table")
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="healthcare_sector",
        charset='utf8'
    )
    mycursor = mydb.cursor()

    sql = "select * from doctor "
    '''mycursor.execute(sql)
    x=mycursor.fetchall()'''
    #mycursor.execute(sql, (id,))
    #record = mycursor.fetchall()
    x = pd.read_sql_query(sql, mydb)
    print("^^^^^^^^^^^^^")
    print(type(x))
    print(x)
    x = x.drop(['pwd'], axis=1)
    x = x.drop(['id'], axis=1)
    x = x.drop(['lname'], axis=1)

    return render_template("vd.html", col_name=x.columns.values, row_val=x.values.tolist())

@app.route("/vd1/<s1>/<s2>")
def vd1(s1='',s2=''):
    global s
    s=s1
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="healthcare_sector",
        charset='utf8'
    )
    mycursor = mydb.cursor()
    sql = "select * from  features where email='%s'" % (s)
    #cursor.execute(sql)
    #cursor.fetchall()
    x = pd.read_sql_query(sql, mydb)
    #db.commit()
    global n
    n = s2
    print(n)
    x = x.drop(['id'], axis=1)
    x = x.drop(['email'], axis=1)

    return render_template("vd1.html",n=n, col_name=x.columns.values, row_val=x.values.tolist())

@app.route("/vd2/<s1>/<s2>")
def vd2(s1='',s2=''):
    email = session.get('email')
    fname = session.get('fname')
    return render_template("vd2.html", s1=s1, s2=s2,e=email,n=fname)

@app.route('/vd2back',methods=['POST','GET'])
def vd2back():
    print("gekjhiuth")
    if request.method=='POST':
        print("gekjhiuth")
        dname=request.form['dname']
        pname=request.form['pname']
        demail=request.form['demail']
        pemail=request.form['pemail']
        sym=request.form['sym']
        date=request.form['date']


        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="healthcare_sector"
        )
        mycursor = mydb.cursor()

        sql = "INSERT INTO book_slot(dname,demail,pname,pemail,sym,date) VALUES (%s,%s,%s,%s,%s,%s)"
        val = (dname,demail,pname,pemail,sym,date)
        mycursor.execute(sql, val)
        mydb.commit()

        return render_template('vd.html', msg="slot booking")

    return render_template('vd2.html',msg="somthing wrong")

@app.route("/appoint")
def appoint():
    print("Reading BLOB data from python_employee table")
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="healthcare_sector",
        charset='utf8'
    )
    mycursor = mydb.cursor()
    email = session.get('email')

    sql = "select * from book_slot where demail='%s' "%(email)
    #mycursor.execute(sql, (id,))
    #record = mycursor.fetchall()
    x = pd.read_sql_query(sql, mydb)
    print("^^^^^^^^^^^^^")
    print(type(x))
    print(x)
    x = x.drop(['dname'], axis=1)
    x = x.drop(['demail'], axis=1)

    return render_template("appoint.html", col_name=x.columns.values, row_val=x.values.tolist())

@app.route("/sendreport/<s1>/<s2>/<s3>/<s4>/<s5>")
def sendreport(s1=0,s2='',s3='',s4='',s5=''):
    global s
    s=s1
    email = session.get('email')
    fname = session.get('fname')

    return render_template("sendreport.html",s=s,s2=s2,s3=s3,s4=s4,s5=s5,e=email,f=fname)

@app.route("/sendback",methods=["POST","GET"])
def sendback():
    if request.method=="POST":
        n = request.form['id']
        print(n)
        report = request.form['report']
        disp = request.form['disp']
        pname = request.form['pname']
        pemail = request.form['pemail']
        sym = request.form['sym']
        date = request.form['date']
        demail = request.form['demail']
        dname = request.form['dname']
        otp = random.randint(000000, 999999)
        skey = secrets.token_hex(4)
        k1=str(skey)
        print(type(k1))



        print("b")
        dd = "D:/A Categorization of Cloud-Based Services and their Security Analysis in the Healthcare Sector/text file/" + report
        f = open(dd, "r")
        data = f.read()
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="healthcare_sector",
            charset='utf8'
        )
        print("c")
        mycursor = mydb.cursor()
        print("d")
        status="Completed"
        action="Close"
        sql1="update book_slot set status='Completed' where id='%s'"%(n)
        mycursor.execute(sql1)
        print("11111111111111111111")
        mydb.commit()
        sql="INSERT INTO report(rid,pname,pemail,dname,demail,sym,disp,report,date,status,action,pkey) VALUES (%s,%s,%s,%s,%s,%s,%s,AES_ENCRYPT(%s,'lakshmi'),%s,%s,%s,%s)"
        val = (n,pname,pemail, dname,demail,sym,disp, data, date,status,action,k1)
        mycursor.execute(sql, val)
        mydb.commit()
        m = "Your secret key is:"
        mail_content = m + ' ' + k1
        sender_address = 'cse.takeoff@gmail.com'
        sender_pass = 'Takeoff$321'
        receiver_address = pemail
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = receiver_address
        message['Subject'] = 'A Categorization of Cloud-Based Services and their Security Analysis in the Healthcare Sector'

        message.attach(MIMEText(mail_content, 'plain'))
        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.starttls()
        session.login(sender_address, sender_pass)
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()

        return render_template("appoint.html", msg="sended report")

@app.route("/report")
def report():
    print("Reading BLOB data from python_employee table")
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="healthcare_sector",
        charset='utf8'
    )
    mycursor = mydb.cursor()
    email = session.get('email')

    sql = "select * from report where demail='%s' "%(email)
    #mycursor.execute(sql, (id,))
    #record = mycursor.fetchall()
    x = pd.read_sql_query(sql, mydb)
    print("^^^^^^^^^^^^^")
    print(type(x))
    print(x)
    x = x.drop(['dname'], axis=1)
    x = x.drop(['demail'], axis=1)
    x = x.drop(['rid'], axis=1)
    x = x.drop(['report'], axis=1)
    x = x.drop(['pkey'], axis=1)

    return render_template("report.html", col_name=x.columns.values, row_val=x.values.tolist())

@app.route("/download/<s1>")
def download(s1=0):
    global p
    p=s1
    mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="healthcare_sector",
            charset='utf8'
    )
    mycursor = mydb.cursor()


    sql = "select count(*),AES_DECRYPT(report,'lakshmi') from report where id='"+p+"'"
    x = pd.read_sql_query(sql, mydb)
    count=x.values[0][0]
    print(count)
    asss=x.values[0][1]
    print(asss)

    print("^^^^^^^^^^^^^")

    if count==1:
        return render_template("hdfs.html", msg=asss)

    return render_template("report.html")

@app.route("/schedule")
def schedule():
    print("Reading BLOB data from python_employee table")
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="healthcare_sector",
        charset='utf8'
    )
    mycursor = mydb.cursor()
    email = session.get('email')

    sql = "select * from book_slot where pemail='%s' "%(email)
    #mycursor.execute(sql, (id,))
    #record = mycursor.fetchall()
    x = pd.read_sql_query(sql, mydb)
    print("^^^^^^^^^^^^^")
    print(type(x))
    print(x)
    x = x.drop(['pname'], axis=1)
    x = x.drop(['pemail'], axis=1)
    x = x.drop(['id'], axis=1)

    return render_template("schedule.html", col_name=x.columns.values, row_val=x.values.tolist())

@app.route("/re")
def re():
    print("Reading BLOB data from python_employee table")
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="healthcare_sector",
        charset='utf8'
    )
    mycursor = mydb.cursor()
    email = session.get('email')

    sql = "select * from report where pemail='%s' "%(email)
    #mycursor.execute(sql, (id,))
    #record = mycursor.fetchall()
    x = pd.read_sql_query(sql, mydb)
    print("^^^^^^^^^^^^^")
    print(type(x))
    print(x)
    x = x.drop(['pname'], axis=1)
    x = x.drop(['pemail'], axis=1)
    x = x.drop(['rid'], axis=1)
    x = x.drop(['report'], axis=1)
    x = x.drop(['pkey'], axis=1)

    return render_template("re.html", col_name=x.columns.values, row_val=x.values.tolist())

@app.route("/filedown/<s1>")
def filedown(s1=0):
    global s
    s=s1


    return render_template("filedown.html",s=s)

@app.route("/filedownload",methods=["POST","GET"])
def filedownload():
    if request.method == "POST":
        n = request.form['id']
        print(n)
        pkey = request.form['pkey']

    mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="healthcare_sector",
            charset='utf8'
    )
    mycursor = mydb.cursor()

    sql = "select count(*),aes_decrypt(report,'lakshmi') from report where id='" + n + "' and pkey='" + pkey + "'"
    x = pd.read_sql_query(sql, mydb)
    count = x.values[0][0]
    print(count)
    asss = x.values[0][1]

    print("^^^^^^^^^^^^^")
    if count == 0:
        msg = "Enter valid key"
        return render_template("filedown.html", msg="invalid")
    if count == 1:
        return render_template("h1.html", msg=asss)

    return render_template("filedown.html")



if __name__ == "__main__":
    app.run(debug=True)