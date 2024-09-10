
try:
    import sqlite3
    con=sqlite3.connect(database='banking.sqlite')
    cur=con.cursor()
    cur.execute("create table accounts(acn integer primary key autoincrement,name text,password text,email text,mob text,bal float,type text, opendate text)")
    cur.execute("create table txn_history (acn int, txn_amt float, txn_type text, txn_date text, update_bal float)")
    con.commit()
    print("tables created")
except:
    print("something went wrong,might be tables already exist")
con.close()


from tkinter import *
from tkinter.ttk import Combobox
from datetime import datetime
import time
from tkinter import messagebox,filedialog
import random
from tkinter.ttk import Style,Treeview,Scrollbar
from PIL import Image, ImageTk 
import shutil
import os



#1.window banaya gya
win=Tk()
win.state("zoomed")
win.resizable(width=False,height=True)
win.configure(bg="pink")

#2.label banaya gya
lbl_title=Label(win,text="Banking Automation",bg="pink",fg='blue',font=('arial',50,'bold',"underline"))
lbl_title.pack()

#main screen per date dikhane ke liye
lbl_date=Label(win,text=f"{datetime.now().date()}",bg="pink",font=('arial',14,'bold'))
lbl_date.place(relx=.93,rely=.1)

#3.screen ke upper 1 fram ko lagana----aur fram me label,entry,button
def main_screen():
    frm=Frame(win)
    frm.configure(bg='Powder blue')
    frm.place(relx=0,rely=.13,relwidth=1,relheight=.87)
    #----------------------------------------------------------------
    
    #command=forgot_password ko as a nested function
    def forgot_pass():
        frm.destroy()
        forgotpass_screen()
        
    #command=open_account ko as a nested function
    def open_account():
        frm.destroy()
        openaccount_screen()
        
    #command=login_account ko as a nested function
    def login_account():
        global name,acn           #global variable
        #validation-----------ydi acn/Pass shi hai tabhi aage badne diya jayega otherwise nhi.
        acn=entry_acn.get()
        pwd=entry_pass.get()
        #yha entry ko check krege ki user ne kuch likha hai ya nhi.
        if(acn=="" or pwd==""):
            messagebox.showerror("Login","ACN/PASS cna't be empty")
            return                                                                          #return function lagane se wo dubara se usi jagah pe le aata hai.
        #ydi humne kuch bhi likh kr login kr le to use rokne ke liye connectivity krege.
        con=sqlite3.connect(database='banking.sqlite')
        cur=con.cursor()
        cur.execute("select name from accounts where acn=? and password=?",(acn,pwd))  #select query se humesha ek hi row aur columns ke ke record hume milte hai.
        row=cur.fetchone()
        con.close()
        if(row==None):
            messagebox.showerror("Login","Invalid ACN/PASS")
            
        else:
            #welcome ke aage user ka name aana chaiye;
            name=row[0]                      #global variable            #name variable ko global variable banana padega because iska use hum dusre fram me kr rhe hai isliye.
            frm.destroy()
            loginaccount_screen()
        
    #reset ke liye function banayege
    def reset():
        entry_acn.delete(0,'end')
        entry_pass.delete(0,"end")
        entry_acn.focus()
        
            
    lbl_acn=Label(frm,text="ACN",bg="powder blue",font=('arial',20,'bold'))
    lbl_acn.place(relx=.36,rely=.1)
    
    entry_acn=Entry(frm,font=('arial',20,'bold'),bd=5)
    entry_acn.place(relx=.43,rely=.1)
    entry_acn.focus()
    
    lbl_pass=Label(frm,text="PASS",bg="powder blue",font=('arial',20,'bold'))
    lbl_pass.place(relx=.36,rely=.2)
    
    entry_pass=Entry(frm,font=('arial',20,'bold'),bd=5,show='*')
    entry_pass.place(relx=.43,rely=.2)
    
    btn_login=Button(frm,text="login",command=login_account,font=('arial',17,'bold'),bd=7,bg="pink")                                       #command
    btn_login.place(relx=.46,rely=.3)
    
    btn_reset=Button(frm,text="reset",command=reset,font=('arial',17,'bold'),bd=7,bg="pink")                                               #command
    btn_reset.place(relx=.55,rely=.3)
    
    btn_open=Button(frm,text="open account",command=open_account,width=17,font=('arial',17,'bold'),bd=7,bg="pink",fg='green')              #command
    btn_open.place(relx=.45,rely=.42)
    
    btn_forgotpass=Button(frm,text="forgot password",command=forgot_pass,width=21,font=('arial',17,'bold'),bd=7,bg="pink",fg='red') #4.command=forgot_password use karege (for new fram screen)
    btn_forgotpass.place(relx=.43,rely=.52)

#ye ek new fram hai----------for forgot pass
def forgotpass_screen():
    frm=Frame(win)
    frm.configure(bg='powder blue')
    frm.place(relx=0,rely=.13,relwidth=1,relheight=.87)
    
    def back():
        main_screen()
        frm.destroy()
        
    #send otp ke liye hum uspe command=send_otp banayege.
    #DATA KO GET KIYA GAYA;------------------------------button---send otp===========================================>
    def send_otp():
        acn=entry_acn.get()
        email=entry_email.get()
    
        con=sqlite3.connect(database='banking.sqlite')
        cur=con.cursor()
        cur.execute("select email,password from accounts where acn=?",(acn,))
        row=cur.fetchone()
        if(row==None):
            messagebox.showerror("Password Recovery","ACN does not exist")
        else:
            if(row[0]==email):
                #live mail krne ke liye code
                otp=random.randint(1000,9999)
                print(otp)
                try:
                    con=gmail.GMail("kumardas2041996@gmail.com","khmpjhqlrodkrkmh")
                    msg=gmail.Message(to=mail,subject="OTP verification",text=f"Your OTP is :{[otp]}")
                    con.send(msg)
                    messagebox.showinfo("Password Recovery","OTP send")
                except:
                    messagebox.showerror("Password Recovery","Something went wrong,check your email")
                
                
                lbl_otp=Label(frm,text="otp",bg="powder blue",font=('arial',15,'bold'))
                lbl_otp.place(relx=.43,rely=.42)

                entry_otp=Entry(frm,font=('arial',20,'bold'),bd=5)
                entry_otp.place(relx=.43,rely=.5)
                entry_otp.focus()
                
                def getpass():
                    verify_otp=int(entry_otp.get())
                    if(otp==verify_otp):
                        messagebox.showinfo("Password Recovery",f"Your pass:{row[1]}")
                    else:
                        messagebox.showerror("Password Recovery","Incorrect OTP")
                        
                btn_verify=Button(frm,text="verify",command=getpass,font=('arial',17,'bold'),bd=7,bg="pink")                                                   #command
                btn_verify.place(relx=.57,rely=.6)
                
            else:
                messagebox.showerror("Password Recovery","Email is not correct")
        con.close()
    #===========================================================================================
    btn_back=Button(frm,text="Back",command=back,font=('arial',17,'bold'),bd=7,bg="pink")                                                   #command
    btn_back.place(relx=0,rely=.0)
    
    lbl_frmtitle=Label(frm,text="This is Forgot Password Screen",fg='green',bg="powder blue",font=('arial',20,'bold'))
    lbl_frmtitle.place(relx=.36,rely=.01)
    
    lbl_acn=Label(frm,text="ACN",bg="powder blue",font=('arial',20,'bold'))
    lbl_acn.place(relx=.36,rely=.1)
    
    entry_acn=Entry(frm,font=('arial',20,'bold'),bd=5)
    entry_acn.place(relx=.43,rely=.1)
    entry_acn.focus()
    
    lbl_email=Label(frm,text="Email",bg="powder blue",font=('arial',20,'bold'))
    lbl_email.place(relx=.36,rely=.2)
    
    entry_email=Entry(frm,font=('arial',20,'bold'),bd=5)
    entry_email.place(relx=.43,rely=.2)
    
    btn_otp=Button(frm,text="Send OTP",command=send_otp,font=('arial',17,'bold'),bd=7,bg="pink")                             #command=send_otp
    btn_otp.place(relx=.54,rely=.3)
    
#ye ek new fram hai------------for open account 
def openaccount_screen():
    frm=Frame(win)
    frm.configure(bg='powder blue')
    frm.place(relx=0,rely=.13,relwidth=1,relheight=.87)
    
    def back():
        main_screen()
        frm.destroy()
        
    #open account screen pe 'open' button ko click krne per jo activity hongi.----ek open_acn function  bananyege
    #DATA KO GET KRNE KA CODE HAI YE
    def open_acn():
        name=entry_name.get()
        pwd=entry_pass.get()
        email=entry_email.get()
        mob=entry_mob.get()
        acn_type=combo_type.get()
        opendate=time.ctime()
        bal=1000
        
        #database connectivity banayege taki ye jo upper get krege hume unhe open se connect kr paye
        #DATABASE ME INSERT KRNE KE LIYE
        con=sqlite3.connect(database='banking.sqlite')
        cur=con.cursor()
        cur.execute("insert into accounts(name,password,email,mob,bal,type,opendate) values(?,?,?,?,?,?,?)",(name,pwd,email,mob,bal,acn_type,opendate))
        con.commit()
        con.close()
        
        #acn no ke liye ye connectivity banayi ja rhi hai,
        #MAXIMUM ACN KO KO LANE KE LIYE-----BECAUSE HUME YAHA PE ACN NO BHI FETCH KRNA HAI.
        con=sqlite3.connect(database='banking.sqlite')
        cur=con.cursor()
        cur.execute("select max(acn) from accounts")        #yha humne max(acn) liya hai because acn field me primary key lagi huyi hai.
        row=cur.fetchone()
        
        #acn no fetch krne ke bad hume ek label banana hai for the massagebox
        lbl_acn_open=Label(frm,text=f"Account opened with ACN:{row[0]}",bg="powder blue",font=('arial',20,'bold'),fg="green")
        lbl_acn_open.place(relx=.42,rely=.8)       
        con.close()
        
    #reset button ke, taki hum pure entry_fields ko reset kr sake.--------------pending for reset button
    
    def reset_open_acn():

        entry_name.delete(0,'end')
        entry_pass.delete(0,"end")
        entry_email.delete(0,"end")
        entry_mob.delete(0,"end")
        entry_name.focus()
        
        #----------------------------------------------------------------------------------------------------------------------------------------------
        
        
    btn_back=Button(frm,text="Back",command=back,font=('arial',17,'bold'),bd=7,bg="pink")                                               #command
    btn_back.place(relx=0,rely=.0)
    
    lbl_frmtitle=Label(frm,text="This is Open Account Screen",fg='green',bg="powder blue",font=('arial',20,'bold'))
    lbl_frmtitle.place(relx=.36,rely=.01)
    
    lbl_name=Label(frm,text="Name",bg="powder blue",font=('arial',20,'bold'))
    lbl_name.place(relx=.32,rely=.2)
    
    entry_name=Entry(frm,font=('arial',20,'bold'),bd=5)
    entry_name.place(relx=.43,rely=.2)
    entry_name.focus()
    
    lbl_password=Label(frm,text="Password",bg="powder blue",font=('arial',20,'bold'))
    lbl_password.place(relx=.32,rely=.3)
    
    entry_pass=Entry(frm,font=('arial',20,'bold'),bd=5,show='*')
    entry_pass.place(relx=.43,rely=.3)
    
    lbl_email=Label(frm,text="Email",bg="powder blue",font=('arial',20,'bold'))
    lbl_email.place(relx=.32,rely=.4)
    
    entry_email=Entry(frm,font=('arial',20,'bold'),bd=5)
    entry_email.place(relx=.43,rely=.4)
    
    lbl_mob=Label(frm,text="Mobile",bg="powder blue",font=('arial',20,'bold'))
    lbl_mob.place(relx=.32,rely=.5)
    
    entry_mob=Entry(frm,font=('arial',20,'bold'),bd=5)
    entry_mob.place(relx=.43,rely=.5)
    
    #combobox banana (drop down list)--------combobox ko import krna padta hai.
    lbl_type=Label(frm,text="Type",bg="powder blue",font=('arial',20,'bold'))
    lbl_type.place(relx=.32,rely=.6)
    
    combo_type=Combobox(frm,font=('arial',20,'bold'),values=['Saving','Current'])
    combo_type.current(0)
    combo_type.place(relx=.43,rely=.6)
    #-------------------------------------------------------------------------
    btn_open=Button(frm,text="open",command=open_acn,font=('arial',17,'bold'),bd=7,bg="pink")                        #command=open_acn
    btn_open.place(relx=.46,rely=.7)
    
    btn_reset=Button(frm,text="reset",command=reset_open_acn,font=('arial',17,'bold'),bd=7,bg="pink")                         #command=reset_open_acn
    btn_reset.place(relx=.55,rely=.7)
    
    
#ye ek new fram hai-------------for login account 
def loginaccount_screen():
    frm=Frame(win)
    frm.configure(bg='Powder blue')
    frm.place(relx=0,rely=.13,relwidth=1,relheight=.87)
    
    def logout():
        main_screen()
        frm.destroy()
        
    #fram ke upper fram banane ke liye ek new function bana rhe hai.
    def details():
        ifrm=Frame(frm)
        ifrm.configure(bg='white',highlightthickness=1,highlightcolor='black',highlightbackground='black')
        ifrm.place(relx=.25,rely=.15,relwidth=.5,relheight=.7)
        
        
        #kisi label ka title,text,color change krna ho to.                                                         
        lbl_frmtitle.configure(text='This is Check Details Screen')
        lbl_frmtitle.place(relx=.38,rely=.01)
        
        #ifram pe user ka data fetch krna jisme us user ka account details honge;------connectivity               
        con=sqlite3.connect(database='banking.sqlite')
        cur=con.cursor()
        cur.execute("select acn,bal,opendate,type from accounts where acn=?",(acn,))     #acn is global variable
        row=cur.fetchone()
        con.close()
        
        #ifram pe label banana hai;-----aur jo label is bari hum banayege use hum innonemous Label khte hai.
        Label(ifrm,text=f"Account No.\t{row[0]}",bg="white",font=("",15,'bold')).place(relx=.3,rely=.2)
        Label(ifrm,text=f"Account Bal.\t{row[1]}",bg="white",font=("",15,'bold')).place(relx=.3,rely=.3)
        Label(ifrm,text=f"Account Open Date\t{row[2]}",bg="white",font=("",15,'bold')).place(relx=.21,rely=.4)
        Label(ifrm,text=f"Account Type.\t{row[3]}",bg="white",font=("",15,'bold')).place(relx=.28,rely=.5)
        
        
        
    def update_profile():
        ifrm=Frame(frm)
        ifrm.configure(bg='white',highlightthickness=1,highlightcolor='black',highlightbackground='black')
        ifrm.place(relx=.25,rely=.15,relwidth=.5,relheight=.7)
        
        #kisi label ka title,text,color change krna ho to.
        lbl_frmtitle.configure(text='This is Update Profile Screen')
        lbl_frmtitle.place(relx=.38,rely=.01)
        
        #---------------------------------------------------------------------------->
        def update_profile_afterlogin():
            name=entry_name.get()
            pwd=entry_pass.get()
            email=entry_email.get()
            mob=entry_mob.get()
            
            con=sqlite3.connect(database="banking.sqlite")
            cur=con.cursor()
            cur.execute("update accounts set name=?,password=?,email=?,mob=? where acn=?",(name,pwd,email,mob,acn))
            con.commit()
            con.close()
            
            messagebox.showinfo("Update Profile","Profile Updated")
            
            lbl_wel.configure(text=f"Welcome,{name}")                             #global variabl---------->after updating, name welcom ke aage aana chaiye
        
        
        
        lbl_name=Label(ifrm,text="Name",bg='white',font=('arial',13,"bold"))                                    
        lbl_name.place(relx=.19,rely=.14)
        
        entry_name=Entry(ifrm,font=('arial',15,),bd=5)
        entry_name.place(relx=.19,rely=.2)
        
        lbl_pass=Label(ifrm,text="Password",bg='white',font=('arial',13,"bold"))                                    
        lbl_pass.place(relx=.52,rely=.14)
        
        entry_pass=Entry(ifrm,font=('arial',15,),bd=5)
        entry_pass.place(relx=.52,rely=.2)
        
        
        lbl_email=Label(ifrm,text="Email",bg='white',font=('arial',13,"bold"))                                    
        lbl_email.place(relx=.19,rely=.35)
        
        entry_email=Entry(ifrm,font=('arial',15,),bd=5)
        entry_email.place(relx=.19,rely=.41)
        
        lbl_mob=Label(ifrm,text="Mobile",bg='white',font=('arial',13,"bold"))                                    
        lbl_mob.place(relx=.52,rely=.35)
        
        entry_mob=Entry(ifrm,font=('arial',15,),bd=5)
        entry_mob.place(relx=.52,rely=.41)

        btn_update=Button(frm,text="Update",command=update_profile_afterlogin,width=11,font=('arial',14,'bold'),bd=7,bg="pink")           #command=update_profile_afterlogin                                       
        btn_update.place(relx=.45,rely=.52)
        
        #yha ek connection banayege , jo ki jo humne entry(name,pass,emai,mob) banai hai usme uski phle se jo name hai wo aa jeye.
        con=sqlite3.connect(database="banking.sqlite")
        cur=con.cursor()
        cur.execute("select name,password,email,mob from accounts where acn=?",(acn,))
        row=cur.fetchone()
        con.close()
        
        #jo humari entry hai usme hum insert krege--
        entry_name.insert(0,row[0])               #is name ko hume welcom,.. ke aage lagana hai.
        entry_pass.insert(0,row[1])
        entry_email.insert(0,row[2])
        entry_mob.insert(0,row[3])
        
        
        
        #=============================================================================>
    def deposit():
        ifrm=Frame(frm)
        ifrm.configure(bg='white',highlightthickness=1,highlightcolor='black',highlightbackground='black')
        ifrm.place(relx=.25,rely=.15,relwidth=.5,relheight=.7)
        
        #kisi label ka title,text,color change krna ho to.
        lbl_frmtitle.configure(text='This is Deposit Screen')
        lbl_frmtitle.place(relx=.40,rely=.01)
        
        #ifram pe deposit ka code lagayege
        def deposit_acn():
            amt=float(entry_amt.get())
            
            con=sqlite3.connect(database='banking.sqlite')
            cur=con.cursor()
            cur.execute("select bal from accounts where acn=?",(acn,))
            bal=cur.fetchone()[0]
            cur.close()
            
            cur=con.cursor()
            cur.execute("update accounts set bal=bal+? where acn=?",(amt,acn))
            cur.execute("insert into txn_history values(?,?,?,?,?)",(acn,amt,"Cr",time.ctime(),bal+amt))
            con.commit()
            con.close()
            
            messagebox.showinfo("Deposit",f"Amount{amt} credited to ACN:{acn} \n Your Balance:{bal+amt}")
            
            entry_amt.delete(0,"end")
            entry_amt.focus()
            
        lbl_amt=Label(ifrm,text="Amount",bg='white',font=('arial',19,'bold'))                                    
        lbl_amt.place(relx=.2,rely=.3)
        
        entry_amt=Entry(ifrm,font=('arial',20,'bold'),bd=5)
        entry_amt.place(relx=.34,rely=.3)
        entry_amt.focus()
        
        btn_dept=Button(ifrm,text="Deposit",command=deposit_acn,font=('arial',17,'bold'),bd=7,bg="pink")                           #command=deposit_acn
        btn_dept.place(relx=.46,rely=.4)
        #===========================================================================
        
    def withdraw():
        ifrm=Frame(frm)
        ifrm.configure(bg='white',highlightthickness=1,highlightcolor='black',highlightbackground='black')
        ifrm.place(relx=.25,rely=.15,relwidth=.5,relheight=.7)
        
        #kisi label ka title,text,color change krna ho to.
        lbl_frmtitle.configure(text='This is Withdraw Screen')
        lbl_frmtitle.place(relx=.40,rely=.01)
        
        #ifram pe withdraw ka code lagayege
        def withdraw_acn():
            amt=float(entry_amt.get())
            
            con=sqlite3.connect(database='banking.sqlite')
            cur=con.cursor()
            cur.execute("select bal from accounts where acn=?",(acn,))
            bal=cur.fetchone()[0]
            cur.close()
            
            if(bal>amt):
                cur=con.cursor()
                cur.execute("update accounts set bal=bal-? where acn=?",(amt,acn))
                cur.execute("insert into txn_history values(?,?,?,?,?)",(acn,amt,"Dr",time.ctime(),bal-amt))
                con.commit()
                con.close()

                messagebox.showinfo("Withdraw",f"Amount{amt} debited from ACN:{acn} \n Your Balance:{bal-amt}")
            else:
                messagebox.showerror("Withdraw",f"Insufficient Bal:{bal}")
                   
            entry_amt.delete(0,"end")
            entry_amt.focus()
        
        lbl_amt=Label(ifrm,text="Amount",bg='white',font=('arial',19,'bold'))                                    
        lbl_amt.place(relx=.2,rely=.3)
        
        entry_amt=Entry(ifrm,font=('arial',20,'bold'),bd=5)
        entry_amt.place(relx=.34,rely=.3)
        entry_amt.focus()
        
        btn_dept=Button(ifrm,text="Withdraw",command=withdraw_acn,font=('arial',17,'bold'),bd=7,bg="pink")                         #command=withdraw_acn   
        btn_dept.place(relx=.46,rely=.4)
        #===========================================================================
        
    def transfer():
        ifrm=Frame(frm)
        ifrm.configure(bg='white',highlightthickness=1,highlightcolor='black',highlightbackground='black')
        ifrm.place(relx=.25,rely=.15,relwidth=.5,relheight=.7)
        
        #kisi label ka title,text,color change krna ho to.
        lbl_frmtitle.configure(text='This is Transfer Screen')
        lbl_frmtitle.place(relx=.40,rely=.01)
        #<----------------------------------------------------------------------->
        def transfer_acn():
            to_acn=entry_to.get()
            from_amt=float(entry_amt.get())
            
            con=sqlite3.connect(database='banking.sqlite')
            cur=con.cursor()
            cur.execute("select acn,bal from accounts where acn=?",(to_acn,))
            to_row=cur.fetchone()
            cur.close()
            
            if(to_row==None):
                messagebox.showerror("Transfer","To Account does not exist")
                
            else:
                cur=con.cursor()
                cur.execute("select bal from accounts where acn=?",(acn,))
                bal=cur.fetchone()[0]
                cur.close()
                if(bal>from_amt):
                    cur=con.cursor()
                    cur.execute("update accounts set bal=bal+? where acn=?",(from_amt,to_acn))
                    cur.execute("update accounts set bal=bal-? where acn=?",(from_amt,acn))
                    cur.execute("insert into txn_history values(?,?,?,?,?)",(acn,from_amt,"Dr",time.ctime(),bal-from_amt))
                    cur.execute("insert into txn_history values(?,?,?,?,?)",(to_acn,from_amt,"Cr",time.ctime(),to_row[1]+from_amt))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Transfer","Txn. Done")
                    
                    entry_to.delete(0,"end")
                    entry_amt.delete(0,"end")
                    entry_amt.focus()
                    
                else: 
                    messagebox.showerror("Transfer",f"Insufficient Bal:{bal}")
                    
                    
                
                
                
                
        #ifram pe transfer krne ka code
        lbl_to=Label(ifrm,text="To",bg='white',font=('arial',19,'bold'))                                    
        lbl_to.place(relx=.2,rely=.3)
        
        entry_to=Entry(ifrm,font=('arial',20,'bold'),bd=5)
        entry_to.place(relx=.34,rely=.3)
        entry_to.focus()
        
        lbl_amt=Label(ifrm,text="Amount",bg='white',font=('arial',19,'bold'))                                    
        lbl_amt.place(relx=.2,rely=.4)
        
        entry_amt=Entry(ifrm,font=('arial',20,'bold'),bd=5)
        entry_amt.place(relx=.34,rely=.4)
        
        btn_trans=Button(ifrm,text="Transfer",command=transfer_acn,font=('arial',17,'bold'),bd=7,bg="pink")                         #command=transfer_acn   
        btn_trans.place(relx=.46,rely=.5)
        
    def txn():
        ifrm=Frame(frm)
        ifrm.configure(bg='white',highlightthickness=1,highlightcolor='black',highlightbackground='black')
        ifrm.place(relx=.25,rely=.15,relwidth=.5,relheight=.7)
        
        #--------------------------------------------------------->
        #kisi label ka title,text,color change krna ho to.
        lbl_frmtitle.configure(text='This is Txn. History Screen')
        lbl_frmtitle.place(relx=.39,rely=.01)
        
        #txn_history banane ke liye hume treeview banana padta hai.
        tv=Treeview(ifrm)
        tv.place(x=8,y=10,height=250,width=750)
        
        #treeview ko stylist banane ke liye
        style=Style()
        style.configure("Treeview.Heading",font=('Arial',10,'bold'),foreground="red")
        
        #ye sb=Scrollbar hai.
        sb=Scrollbar(ifrm,orient="vertical",command=tv.yview)
        sb.place(x=735,y=11,height=248,)             #(anchor="c")TclError: bad anchor ==> must be n, ne, e, se, s, sw, w, nw, or center
        tv.configure(yscrollcommand=sb.set)

        #column ke head banane ke liye
        tv['columns']=('col1','col2','col3','col4')

        #columns ke head ko columns,width and anchor
        tv.column('col1',width=150,anchor="c")
        tv.column('col2',width=100,anchor="c")
        tv.column('col3',width=80,anchor="c")
        tv.column('col4',width=100,anchor="c")
        
        #column ke head ke Name
        tv.heading('col1',text="Date")
        tv.heading('col2',text="Amount")
        tv.heading('col3',text="Type")
        tv.heading('col4',text="Update Bal")

        #jo heading humne banaya hai use show krne ke liye
        tv['show']="headings"
        
        #ek connectivity banayege kyoki humne jo columns banage hai uske liye rows bhi chaiye--------------to wo hum database se connect kr ke ek table se layege.
        
        con=sqlite3.connect(database="banking.sqlite")
        cur=con.cursor()
        cur.execute("select * from txn_history where acn=?",(acn,))

        #ek loop banayege jo ki jitni bhi cursor me rows aai hai use hum loop ke jariye insert krege ---- treeview me
        for row in cur:
            tv.insert("","end",values=(row[3],row[1],row[2],row[4]))
        
        
    btn_logout=Button(frm,text="logout",command=logout,font=('arial',17,'bold'),bd=7,bg="pink")                                      #command
    btn_logout.place(relx=.93,rely=.0)
    
    lbl_frmtitle=Label(frm,text="This is Login Account Screen",fg='green',bg="powder blue",font=('arial',20,'bold'))
    lbl_frmtitle.place(relx=.36,rely=.01)
    
    #------------------------------------------------------------------------------------>
    def open_file():
        img=filedialog.askopenfilename()                #user ne jo path bataya wo humne read kr li
        shutil.copy(img,f"{acn}.jpeg")                  #current directry me past kr li humne
        #imgname=img[img.rindex('/'+1):]                #kisi image ka name nikalne ke liye
        #print(imgname)
        img=Image.open(f"{acn}.jpeg").resize((120,140)) #read wali image ko open kr liya
        imgtk=ImageTk.PhotoImage(img,master=win)        #tkinter competable bana diya
        lbl_img.image=imgtk                             #lable pe jo phle default image lagi thi--------uspe humne new image laga di
        lbl_img['image']=imgtk                          ##lable pe jo phle default image lagi thi--------uspe humne new image laga di
        
        
    global lbl_wel
    lbl_wel=Label(frm,text=f"Welcome,{name}",bg='powder blue',font=('arial',19,'bold'))                                    #name is global variable
    lbl_wel.place(relx=0,rely=0)
    
    #image ko lagana----from PIL import Image
    global img,imgtk,lbl_img
    if(os.path.exists(f"{acn}.jpeg")):        
        img=Image.open(f"{acn}.jpeg").resize((120,140))
        imgtk=ImageTk.PhotoImage(img,master=win)        #tk inter competable ho gai hai.
    else:
        img=Image.open("default.jpeg").resize((120,140))
        imgtk=ImageTk.PhotoImage(img,master=win)        #tk inter competable ho gai hai.
    
    lbl_img=Label(frm,image=imgtk)
    lbl_img.place(relx=.01,rely=.06)
    
    
    btn_update_img=Button(frm,text="Upadate Image",command=open_file,width=10,font=('arial',7,'bold'),bd=3,bg="pink")                    #command=open_file
    btn_update_img.place(relx=.1,rely=.25)
    #====================================================================================>
    
    btn_details=Button(frm,text="Check Details",command=details,width=15,font=('arial',17,'bold'),bd=7,bg="pink")                    #command
    btn_details.place(relx=0,rely=.3)
    
    btn_update_profile=Button(frm,text="Update Profile",command=update_profile,width=15,font=('arial',17,'bold'),bd=7,bg="pink")     #command
    btn_update_profile.place(relx=0,rely=.4)
    
    btn_deposit=Button(frm,text="Deposit",command=deposit,width=15,font=('arial',17,'bold'),bd=7,bg="pink")                                          #command
    btn_deposit.place(relx=0,rely=.5)
    
    btn_withdraw=Button(frm,text="Withdraw",command=withdraw,width=15,font=('arial',17,'bold'),bd=7,bg="pink")                                        #command
    btn_withdraw.place(relx=0,rely=.6)
    
    btn_transfer=Button(frm,text="Transfer",command=transfer,width=15,font=('arial',17,'bold'),bd=7,bg="pink")                                        #command
    btn_transfer.place(relx=0,rely=.7)
    
    btn_txn=Button(frm,text="Txn. History",command=txn,width=15,font=('arial',17,'bold'),bd=7,bg="pink")                                         #command
    btn_txn.place(relx=0,rely=.8)
    
main_screen()    
win.mainloop()





