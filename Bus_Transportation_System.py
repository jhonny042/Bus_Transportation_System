from tkinter import messagebox
from tkinter import *
import numbers
import sqlite3
conn=sqlite3.connect('login.db')
c=conn.cursor()
class Main():
    def __init__(self,parent):
        self.parent=parent
        self.parent.title("COLLEGE TRANSPORTATION SYSTEM")
        #self.parent.config(bg="blue")
        self.parent.minsize(400,300)
        self.page=StringVar()
        self.page2=StringVar()
        self.loginName=StringVar()
        self.loginPass=StringVar()
        self.signinName=StringVar()
        self.signinPass=StringVar()
        self.busnumbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33]
        self.sts=StringVar()
        self.exe=StringVar()
        self.rname=StringVar()
        self.dis=StringVar()
        self.buses=StringVar()
        self.time=StringVar()
        self.createwidgets()
        self.showLogin()
                    
    def createwidgets(self):
        Label(self.parent,bg='orange',textvariable=self.page,font=("",20)).pack()
        Label(self.parent,textvariable=self.page2,font=("",15)).pack()
        frame1=Frame(self.parent)
        Label(frame1,text='Name',fg='blue').grid(sticky=W)
        Entry(frame1,textvariable=self.loginName).grid(row=0,column=1,pady=10,padx=10)
        Label(frame1,text='Password',fg='blue').grid(sticky=W)
        Entry(frame1,textvariable=self.loginPass,show='*').grid(row=1,column=1)
        Button(frame1,text='Login',command=self.login,fg='black',bg='yellow',height=1,width=7,font='Bold 10').grid(pady=10)
        Button(frame1,text='signup',command=self.signin,fg='black',bg='yellow',height=1,width=7,font='Bold 10').grid(row=2,column=1,pady=10)
        frame2=Frame(self.parent)
        Label(frame2,text='Name',fg='blue').grid(sticky=W)
        Entry(frame2,textvariable=self.signinName).grid(row=0,column=1,pady=10,padx=10)
        Label(frame2,text='Password',fg='blue').grid(sticky=W)
        Entry(frame2,textvariable=self.signinPass,show='*').grid(row=1,column=1)
        Button(frame2,text='Create',command=self.create,fg='brown',bg='yellow',height=1,width=7,font='Bold 10').grid(pady=10)
        Button(frame2,text='Back',command=self.showLogin,fg='brown',bg='yellow',height=1,width=7,font='Bold 10').grid(row=2,column=1,pady=10)
        frame3=Frame(self.parent)
        #Label(frame3,text='',font=("",30)).pack(padx=10,pady=10)
        Button(frame3,text='8:00',command=self.time800,fg="red",bg="powder blue",height=2,width=15,font='Bold 15').grid(row=0,column=1,pady=10,padx=10)
        Button(frame3,text='11:00',command=self.time1100,fg="red",bg="powder blue",height=2,width=15,font='Bold 15').grid(row=1,column=1,pady=10,padx=10)
        Button(frame3,text='1:15',command=self.time1315,fg="red",bg="powder blue",height=2,width=15,font='Bold 15').grid(row=2,column=1,pady=10,padx=10)
        Button(frame3,text='3:20',command=self.time1520,fg="red",bg="powder blue",height=2,width=15,font='Bold 15').grid(row=3,column=1,pady=10,padx=10)
        Button(frame3,text='LOGOUT',command=self.logout,fg="white",bg='red',font='Bold 10').grid(row=4,column=1,pady=20,padx=10,sticky=W)
        Label(frame3,textvariable=self.exe).grid(row=0,column=0,sticky=W)
        frame4=Frame(self.parent)
        Button(frame4,text='back',command=self.backtohome,fg="white",bg="red",height=1,width=7,font='Bold 10').grid(row=100,column=1,pady=50,sticky=S)
        frame5=Frame(self.parent)
        Button(frame5,text='back',command=self.backtohome,fg="white",bg="red",height=1,width=7,font='Bold 10').grid(row=100,column=1,pady=50,sticky=S)
        frame6=Frame(self.parent)
        Button(frame6,text='back',command=self.backtohome,fg="white",bg="red",height=1,width=7,font='Bold 10').grid(row=100,column=1,pady=50,sticky=S)
        frame7=Frame(self.parent)
        Button(frame7,text='back',command=self.backtohome,fg="white",bg="red",height=1,width=7,font='Bold 10').grid(row=100,column=1,pady=50,sticky=S)
        frame8=Frame(self.parent)
        Button(frame8,text='Add Route',command=self.addRoute,fg="red",bg="powder blue",height=2,width=15,font='Bold 15').grid(row=2,column=1,pady=10)
        Button(frame8,text='Update Route',command=self.update,fg="red",bg="powder blue",height=2,width=15,font='Bold 15').grid(row=3,column=1,pady=10)
        Button(frame8,text='Delete Route',command=self.deleteRoute,fg="red",bg="powder blue",height=2,width=15,font='Bold 15').grid(row=4,column=1,pady=10)
        Button(frame8,text='LOGOUT',command=self.logout,fg="white",bg='red',font='Bold 10').grid(row=5,column=1,pady=10,sticky=W)
        frame9=Frame(self.parent)
        Label(frame9,text='Route',fg='blue').grid(sticky=W)
        Entry(frame9,textvariable=self.rname).grid(row=0,column=1,pady=10,padx=10)
        Label(frame9,text='Distance',fg='blue').grid(sticky=W)
        Entry(frame9,textvariable=self.dis).grid(row=1,column=1)
        Label(frame9,text='Bus Numbers',fg='blue').grid(sticky=W)
        Entry(frame9,textvariable=self.buses).grid(row=2,column=1)
        Label(frame9,text='Time',fg='blue').grid(sticky=W)
        Entry(frame9,textvariable=self.time).grid(row=3,column=1)
        Button(frame9,text='back',command=self.backtoAdmin,fg="white",bg="red",height=1,width=7,font='Bold 10').grid(pady=10,sticky=S)
        Button(frame9,text='Add',command=self.add,fg='black',bg='yellow',height=1,width=7,font='Bold 10').grid(row=4,column=1,pady=10)
        frame11=Frame(self.parent)
        self.loginFrame=frame1
        self.signinFrame=frame2
        self.loggedFrame=frame3
        self.homeFrame=frame4
        self.homeFrame2=frame5
        self.homeFrame3=frame6
        self.homeFrame4=frame7
        self.adminFrame=frame8
        self.addFrame=frame9
        #self.updateFrame=frame10
        self.updateFrame2=frame11
        Label(self.parent,textvariable=self.sts).pack()

    def login(self):
        name=self.loginName.get()
        password=self.loginPass.get()
        c.execute("select * from loginDetails")
        if(name,password)==('mukul','kumar'):
            self.showadmin()
        elif (name,password) in c.fetchall():
            self.showLogged()
        else:
            self.sts.set("Wrong Name or Password")
        '''try:
            f=open("data","r")
            cname,cpass=f.read().split(',')
            if name==cname and password==cpass:
                self.showLogged()
            else:
                self.sts.set("Wrong Name or Password")
        except:
            self.sts.set("Wrong Name or Password")'''

    def signin(self):
        #createTable()
        self.page.set("Sign Up")
        self.page2.set('')
        self.loginFrame.pack_forget()
        self.signinFrame.pack()
        self.signinName.set('')
        self.signinPass.set('')
    def showLogin(self):
        self.page.set('Login')
        self.page2.set('')
        self.signinFrame.pack_forget()
        self.loginPass.set("")
        self.loginName.set("")
        self.loginFrame.pack()
    def showLogged(self):
        #name=str(self.loginName)
        name=self.loginName.get()
        self.page.set('College Transportation Service')
        self.page2.set('Welcome '+name)
        self.loginFrame.pack_forget()
        self.sts.set("")
        #self.exe.set('Bus Timings:')
        self.loggedFrame.pack()
        #self.exe.set('Bus Timings:')

    def showadmin(self):
        self.page.set('College Transportation Service')
        self.page2.set('Welcome Admin')
        self.loginFrame.pack_forget()
        self.sts.set("")
        self.adminFrame.pack()


        
    def create(self):
        name=self.signinName.get()
        password=self.signinPass.get()
        '''f=open("data","w")
        f.write("{0},{1}".format(name,password))
        f.close()'''
        c.execute("select * from loginDetails")
        if (name,password) in c.fetchall():
            self.sts.set("User already exists")
            self.showLogin()
        elif name=='mukul':
            self.sts.set("This username is for the ADMIN")
            self.showLogin()
        elif name=="" or password=="":
            messagebox.showerror("ERROR4","Name and Password must not be left EMPTY")
        elif len(password)<5:
            messagebox.showerror("ERROR4","Password length should be greater than or equal to 5")
        else:
            c.execute("insert into loginDetails values (?,?)",(name,password))
            conn.commit()
            self.showLogin()

    '''def dataEntry(self,name,password):
        c.execute("insert into loginDetails(user_name,password) values (?,?)",
                  (name,password))
        conn.commit'''

    def backtohome(self):
        self.homeFrame.pack_forget()
        self.homeFrame2.pack_forget()
        self.homeFrame3.pack_forget()
        self.homeFrame4.pack_forget()
        self.loggedFrame.pack()

    def backtoadmin(self,r):
        self.addFrame.pack_forget()
        r.pack_forget()
        self.adminFrame.pack()
        self.rname.set("")
        self.dis.set("")
        self.buses.set("")
        self.time.set("")

    def backtoAdmin(self):
        self.addFrame.pack_forget()
        #r.pack_forget()
        self.adminFrame.pack()
        self.rname.set("")
        self.dis.set("")
        self.buses.set("")
        self.time.set("")
        
    
    def time800(self):
        c.execute("select route,busNumbers from busSchedule where time='8:00'")
        result = c.fetchall()
        self.loggedFrame.pack_forget()
        self.homeFrame.pack()
        l1=Label(self.homeFrame,text='Route',font=("",15)).grid(row=4,column=0,sticky=S)
        l1=Label(self.homeFrame,text='BusNumber',font=("",15)).grid(row=4,column=1,sticky=S)
        i=5
        for route,bus in result:
            l1=Label(self.homeFrame,text=route,font=("",10)).grid(row=i,column=0)
            l2=Label(self.homeFrame,text=bus,font=("",10)).grid(row=i,column=1)
            i+=1
        #self.exe.set(result)
    def time1100(self):
        c.execute("select route,busNumbers from busSchedule where time='11:00'")
        result = c.fetchall()
        self.loggedFrame.pack_forget()
        self.homeFrame2.pack()
        l1=Label(self.homeFrame2,text='Route',font=("",15)).grid(row=4,column=0,sticky=S)
        l1=Label(self.homeFrame2,text='BusNumber',font=("",15)).grid(row=4,column=1,sticky=S)
        i=5
        for route,bus in result:
            l1=Label(self.homeFrame2,text=route,font=("",10)).grid(row=i,column=0)
            l1=Label(self.homeFrame2,text=bus,font=("",10)).grid(row=i,column=1)
            i+=1
    def time1315(self):
        c.execute("select route,busNumbers from busSchedule where time='1:15'")
        result = c.fetchall()
        self.loggedFrame.pack_forget()
        self.homeFrame3.pack()
        l1=Label(self.homeFrame3,text='Route',font=("",15)).grid(row=4,column=0,sticky=S)
        l1=Label(self.homeFrame3,text='BusNumber',font=("",15)).grid(row=4,column=1,sticky=S)
        i=5
        for route,bus in result:
            l1=Label(self.homeFrame3,text=route,font=("",10)).grid(row=i,column=0)
            l1=Label(self.homeFrame3,text=bus,font=("",10)).grid(row=i,column=1)
            i+=1
    def time1520(self):
        c.execute("select route,busNumbers from busSchedule where time='3:20'")
        result = c.fetchall()
        self.loggedFrame.pack_forget()
        self.homeFrame4.pack()
        l1=Label(self.homeFrame4,text='Route',font=("",15)).grid(row=4,column=0,sticky=S)
        l2=Label(self.homeFrame4,text='BusNumber',font=("",15)).grid(row=4,column=1,sticky=S)
        i=5
        for route,bus in result:
            l1=Label(self.homeFrame4,text=route,font=("",10)).grid(row=i,column=0)
            l1=Label(self.homeFrame4,text=bus,font=("",10)).grid(row=i,column=1)
            i+=1
    def logout(self):
        self.page.set('Login')
        self.page2.set('')
        self.loggedFrame.pack_forget()
        self.adminFrame.pack_forget()
        #self.homeFrame.pack_forget()
        self.loginPass.set("")
        self.loginName.set("")
        self.loginFrame.pack()

    def add(self):
        x=0
        s=[]
        s=self.buses.get().split(',')
        #print(s)
        if self.rname.get()=="" or self.dis.get()=="" or self.buses.get()=="" or self.time.get()=="":
            x=1
            messagebox.showerror("ERROR1","Each Field is Mandatory")
        else:
                #if isinstance(self.dis.get(),numbers.Integral)==False or self.dis.get()>50:
                    #messagebox.showerror("ERROR2","Distance should be an Integer and less than equal to 50")
                if not(self.time.get()=='8:00' or self.time.get()=='11:00' or self.time.get()=='1:15' or self.time.get()=='3:20'):
                    messagebox.showerror("ERROR3","wrong time value entered. Time value can be 8:00,11:00,1:15 or 3:20")
                    x=1
                else:
                    for i in s:
                        #print(i,self.busnumbers)
                        if int(i) not in self.busnumbers:
                            x=1
                            messagebox.showerror("ERROR4","wrong bus number, valid bus numbers are integers from 1 to 33")
                            break

        if x==0:
            c.execute('insert into busSchedule values(?,?,?,?)',(self.rname.get(),self.dis.get(),self.buses.get(),self.time.get()))
            conn.commit()
            messagebox.showinfo("SUCCESS","Record successfully added")
            self.rname.set("")
            self.dis.set("")
            self.buses.set("")
            self.time.set("")
            self.addFrame.pack_forget()
            self.adminFrame.pack()
            

    def backtoupdate(self,r,b):
        r.pack_forget()
        b.pack()

    def query(self,bnum,route,dis,bus,time,frame,r):
        x=0
        s=[]
        s=self.buses.get().split(',')
        if self.rname.get()=="" or self.dis.get()=="" or self.buses.get()=="" or self.time.get()=="":
                x=1
                messagebox.showerror("ERROR1","Each Field is Mandatory")
        else:
                #if isinstance(self.dis.get(),numbers.Integral)==False or self.dis.get()>50:
                    #messagebox.showerror("ERROR2","Distance should be an Integer and less than equal to 50")
                    #x=1
                if not(self.time.get()=='8:00' or self.time.get()=='11:00' or self.time.get()=='1:15' or self.time.get()=='3:20'):
                    messagebox.showerror("ERROR3","wrong time value entered. Time value can be 8:00,11:00,1:15 or 3:20")
                    x=1
                else:
                    for i in s:
                        #print(i,self.busnumbers)
                        if int(i) not in self.busnumbers:
                            x=1
                            messagebox.showerror("ERROR4","wrong bus number, valid bus numbers are integers from 1 to 33")
                            break
        if x==0:
            c.execute('update busSchedule set route=?,distance=?,busNumbers=?,time=? where busNumbers=?',(route,dis,bus,time,bnum,))
            conn.commit()
            messagebox.showinfo("Record updated")
            frame.pack_forget()
            self.update()
        
    def updatedata(self,a,r):
        #a=str(a)
        #print(a)
        x=0
        s=[]
        s=self.buses.get().split(',')
        r.pack_forget()
        if a!='L':
            frame10=Frame(self.parent)
            Label(frame10,text='Route',fg='blue').grid(sticky=W)
            Entry(frame10,textvariable=self.rname).grid(row=0,column=1,pady=10,padx=10)
            Label(frame10,text='Distance',fg='blue').grid(sticky=W)
            Entry(frame10,textvariable=self.dis).grid(row=1,column=1)
            Label(frame10,text='Bus Numbers',fg='blue').grid(sticky=W)
            Entry(frame10,textvariable=self.buses).grid(row=2,column=1)
            Label(frame10,text='Time',fg='blue').grid(sticky=W)
            Entry(frame10,textvariable=self.time).grid(row=3,column=1)
            Button(frame10,text='Back',command=lambda : self.backtoupdate(frame10,r),fg="black",bg="yellow").grid(pady=10,sticky=S)
            Button(frame10,text='Update',command=lambda : self.query(a,self.rname.get(),self.dis.get(),self.buses.get(),self.time.get(),frame10,r),fg='black',bg='yellow').grid(row=4,column=1,pady=10)
            c.execute('select * from busSchedule where busNumbers=?',(a,))
            res=c.fetchall()
            for rname,dis,buses,time in res:
                self.rname.set(rname)
                self.dis.set(dis)
                self.buses.set(buses)
                self.time.set(time)
            frame10.pack()
            
        else:
            r.pack()
            messagebox.showerror('Error 1','No Schedule Selected')

    count=0      
    def update(self):
        self.adminFrame.pack_forget()
        frame11=Frame(self.parent)
        a=StringVar()
        a.set("L")
        lt1=Label(frame11,fg="brown",bg="powder blue",font="Helvetica 20 bold",text="Route").grid(row=1,column=1)
        lt2=Label(frame11,fg="brown",bg="powder blue",font="Helvetica 20 bold",text="Distance").grid(row=1,column=3)
        lt3=Label(frame11,fg="brown",bg="powder blue",font="Helvetica 20 bold",text="Bus No.").grid(row=1,column=5)
        lt4=Label(frame11,fg="brown",bg="powder blue",font="Helvetica 20 bold",text="Time").grid(row=1,column=7)
        i=2
        c.execute('select * from busSchedule')
        res=c.fetchall()
        for route,dis,bnum,time in res:
            Radiobutton(frame11,variable=a,value=bnum).grid(row=i,column=0)	    
            l1=Label(frame11,font="Bold 15",fg="black",text=route).grid(row=i,column=1)
            l2=Label(frame11,font="Bold 15",fg="black",text=dis).grid(row=i,column=3)
            l3=Label(frame11,font="Bold 15",fg="black",text=bnum).grid(row=i,column=5)
            l4=Label(frame11,font="Bold 15",fg="black",text=time).grid(row=i,column=7)
            i+=1
        Button(frame11,text='Back',command=lambda : self.backtoadmin(frame11),fg="white",bg="red",height=1,width=7,font='Bold 10').grid(row=i,column=0,pady=10)
        Button(frame11,text='Update',command=lambda: self.updatedata(a.get(),frame11),fg='black',bg='yellow',height=1,width=7,font='Bold 10').grid(row=i,column=1,pady=10)
        frame11.pack()
        
    def addRoute(self):
        self.adminFrame.pack_forget()
        self.addFrame.pack()
        
    def deleteRoute(self):
        self.adminFrame.pack_forget()
        frame12=Frame(self.parent)
        a=StringVar()
        a.set("L")
        lt1=Label(frame12,fg="brown",bg="powder blue",font="Helvetica 20 bold",text="Route").grid(row=1,column=1)
        lt2=Label(frame12,fg="brown",bg="powder blue",font="Helvetica 20 bold",text="Distance").grid(row=1,column=2)
        lt3=Label(frame12,fg="brown",bg="powder blue",font="Helvetica 20 bold",text="Bus No.").grid(row=1,column=3)
        lt4=Label(frame12,fg="brown",bg="powder blue",font="Helvetica 20 bold",text="Time").grid(row=1,column=4)
        i=2
        c.execute('select * from busSchedule')
        res=c.fetchall()
        for route,dis,bnum,time in res:
            Radiobutton(frame12,variable=a,value=bnum).grid(row=i,column=0)		
            l1=Label(frame12,font="Bold 15",fg="black",text=route).grid(row=i,column=1)
            l2=Label(frame12,font="Bold 15",fg="black",text=dis).grid(row=i,column=2)
            l3=Label(frame12,font="Bold 15",fg="black",text=bnum).grid(row=i,column=3)
            l4=Label(frame12,font="Bold 15",fg="black",text=time).grid(row=i,column=4)
            i+=1
        Button(frame12,text='Back',command=lambda: self.back(frame12),fg="black",bg="yellow",height=1,width=7,font='Bold 10').grid(row=i,column=0,pady=10)
        Button(frame12,text='Delete',command=lambda: self.deletedata(a.get(),frame12),fg='white',bg='red',height=1,width=7,font='Bold 10').grid(row=i,column=1,pady=10)
        frame12.pack()

    def back(self,r):
        r.pack_forget()
        self.adminFrame.pack()
        
    def deletedata(self,a,r):
        a=str(a)
        #print(a)
        if a!='L':
            c.execute('delete from busSchedule where busNumbers=?',(a,))
            conn.commit()
            r.pack_forget()
            self.deleteRoute()
        else:
            r.pack()
            messagebox.showerror('Error 1','No Schedule Selected')
    
def createTable():
        c.execute("create table if not exists loginDetails(user_name TEXT not null,password TEXT not null)")
        c.execute("CREATE TABLE if not exists busSchedule(route	TEXT NOT NULL,distance INTEGER NOT NULL,busNumbers TEXT NOT NULL,time TEXT NOT NULL)")
        

#if __name__=="__main__":
createTable()
root=Tk()
Main(root)
root.mainloop()


        
c.close()
conn.close()
