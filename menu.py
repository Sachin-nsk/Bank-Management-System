import datetime as dt
import  mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='root',database='sachi')
cur = conn.cursor()
conn.autocommit = True
while True:
                         print('1.CREATE BANK ACCOUNT')
                         print('2.TRANSACTION')
                         print('3.CUSTOMER DETAILS')
                         print('4.TRANSACTION DETAILS')
                         print('5.DELETE ACCOUNT')
                         print('6.QUIT')
                         n=int(input('Enter your CHOICE='))
                         if n == 1:
                                    acc_no=int(input('Enter your ACCOUNT NUMBER='))
                                    acc_name=input('Enter your ACCOUNT NAME=')
                                    ph_no=int(input('Enter your PHONE NUMBER='))
                                    add=(input('Enter your place='))
                                    cr_amt=int(input('Enter your credit amount='))
                                    V_SQLInsert="INSERT  INTO customer_details values ({},'{}',{},'{}',{})".format(acc_no,acc_name,ph_no,add,cr_amt)
                                    cur.execute(V_SQLInsert)
                                    print('Account Created Succesfully!!!!!')
                                    conn.commit()
                         elif n == 2:
                              acct_no=int(input('Enter Your Account Number='))
                              cur.execute('select * from customer_details where acct_no={}'.format(acct_no))
                              data=cur.fetchall()
                              count=cur.rowcount
                              conn.commit()
                              if count == 0:
                                   print('Account Number Invalid Sorry Try Again Later')
                              else:
                                   print('1.WITHDRAW AMOUNT')
                                   print('2.ADD AMOUNT')
                                   x=int(input('Enter your CHOICE='))
                                   if x == 1:
                                        amt=int(input('Enter withdrawl amount='))
                                        cr_amt=0
                                        cur.execute('update customer_details set   cr_amt=cr_amt-{}  where acct_no={}'.format(amt,acct_no ))
                                        V_SQLInsert="INSERT  INTO transactions values ({} , '{}' , {} , {}) ".format(acct_no,dt.datetime.today(),amt,cr_amt) 
                                        cur.execute(  V_SQLInsert)
                                        conn.commit()
                                        print('Account Updated Succesfully!!!!!')
                                   elif x== 2:
                                         amt=int(input('Enter amount to be added='))
                                         cr_amt=0
                                         cur.execute('update customer_details set  cr_amt=cr_amt+{}  where acct_no={} '.format(amt,acct_no))
                                         V_SQLInsert="INSERT  INTO transactions values ({} , '{}' , {} , {}) ".format(acct_no,dt.datetime.today(),cr_amt,amt)
                                         cur.execute(  V_SQLInsert)
                                         conn.commit()
                                         print('Account Updated Succesfully!!!!!')
                         elif n == 3:
                              acct_no=int(input('Enter your account number='))
                              print()
                              cur.execute('select * from customer_details where acct_no={}'.format(acct_no))
                              if cur.fetchone() is  None:
                                   print('Invalid Account number')
                              else:
                                   cur.execute('select * from customer_details where acct_no={}'.format(acct_no))
                                   data=cur.fetchall()
                                   for row in data:
                                        print('ACCOUNT NO=',acct_no)
                                        print('ACCOUNT NAME=',row[1])
                                        print('PHONE NUMBER=',row[2])
                                        print('ADDRESS=',row[3])
                                        print('cr_amt=',row[4])
                         elif n == 4:
                               acct_no=int(input('Enter your account number='))
                               cur.execute('select * from customer_details where acct_no={}'.format(acct_no))
                               if cur.fetchone() is  None:
                                   print('Invalid Account number')
                               else:
                                   cur.execute('select * from transactions where acct_no={}'.format(acct_no))
                                   data=cur.fetchall()
                                   count=cur.rowcount
                                   if count==0:
                                       print("No Transactions Done Yet")
                                   else:
                                   
                                        for row in data:
                                            print('ACCOUNT NO=',row[0])
                                            print('DATE=',row[1])
                                            print(' WITHDRAWAL AMOUNT=',row[2])
                                            print('AMOUNT ADDED=',row[3])
                         elif n == 5:
                              print('DELETE YOUR ACCOUNT')
                              acct_no=int(input('Enter your account number='))
                              cur.execute('delete from customer_details where acct_no={}'.format(acct_no))
                              print('ACCOUNT DELETED SUCCESFULLY')
                         elif n == 6:
                             break
else:
     print('THANK YOU PLEASE VISIT AGAIN')
     quit()
