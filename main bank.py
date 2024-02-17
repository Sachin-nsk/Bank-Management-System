import  mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='root',database='sachi')
cur = conn.cursor()
print('=========================WELCOME TO STARK BANK============================================================')
import datetime as dt
while True:
     print(dt.datetime.now())
     print('1.REGISTER')
     print('2.LOGIN')
     print('3.EXIT')
     n=int(input('enter your choice='))
     if n== 1:
          name=input('Enter a Username=')
          pas=int(input('Enter a 4 DIGIT Password='))
          inQ="INSERT  INTO user_table (username,passwrd) values('{}',{})".format(name,pas)
          cur.execute(inQ)
          conn.commit()
          print('USER created succesfully')
          
     elif  n==2 :
          name=input('Enter your Username=')
          passwd=int(input('Enter your 4 DIGIT Password='))
          V_Sql_Sel="select * from user_table where passwrd={} and username='{}'".format(passwd,name) 
          cur.execute(V_Sql_Sel)
          if cur.fetchone() is  None:
               print('Invalid username or password')
          else:
               import menu
     elif n==3:
          break
     else:
          print('Enter Valid Choice (1-3)')
