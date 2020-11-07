from tkinter import *
import pandas as pd
import array
import numpy as np
from matplotlib import pyplot as plt
from tkinter import messagebox
from tkinter import scrolledtext
import socket
import bs4
import requests


root = Tk()
root.title("SMS")
root.resizable(True,True)
root.geometry("2000x1000+0+0")

photo = PhotoImage(file="sms.png")
label = Label(root, image=photo)
label.image = photo
label.place(x=0, y=0)


#filename = PhotoImage(file = "sms.png")
#background_label = Label(root, image=filename)
#background_label.place(x=10, y=10, relwidth=1, relheight=1)

############################################Temperature##########################################################################
try:
	city = "Mumbai"
	socket.create_connection( ("www.google.com", 80)  )
	a1 = "http://api.openweathermap.org/data/2.5/weather?units=metric"
	a2 = "&q=" + city
	a3 = "&appid=c6e315d09197cec231495138183954bd"
	api_address = a1 +a2 +a3
	res1 = requests.get(api_address)
	
	j1 = res1.json()
	
	d1 = j1['main']

	temp = d1['temp']
	lblTemp = Label(root,text = "Temperature Today is: " + str(temp) + " degree" ,font=('ariel',18,'bold')).place(x = 420, y = 550)

except OSError:
	print("Check internet connection ")

######################################################Quote########################################################################
res = requests.get("https://www.brainyquote.com/quotes_of_the_day.html")
soup = bs4.BeautifulSoup(res.text,'lxml')
quote =  soup.find('img',{"class" :"p-qotd"})
texts = quote['alt']
lblQuote = Label(root, text = texts ,font=('ariel',18,'bold')).place(x = 100, y =500)

#############################################################FRAME2###################################################################
Frame2 = Toplevel(root)
Frame2.title("CRUD FRAME")
Frame2.geometry("2000x1000+0+0")
Frame2.resizable(True,True)
p1 = PhotoImage(file="crudim.png")
label = Label(Frame2, image=p1)
label.image = p1
label.place(x=0, y=0)
Frame2.withdraw()

def frame2():
	Frame2.deiconify()
	root.withdraw()
btnProceed = Button(root,text = "NEXT",font=('ariel',18,'bold'),bg = 'yellow', command = frame2).place(x=500,y=600)

def f13():
	root.deiconify()
	Frame2.withdraw()

def f16():
	Frame2.deiconify()
	GraphStud.withdraw()

	
Frame2 = Toplevel(root)
Frame2.title("CRUD FRAME")
Frame2.geometry("2000x1000+0+0")
Frame2.resizable(True,True)
p1 = PhotoImage(file="crudim.png")
label = Label(Frame2, image=p1)
label.image = p1
label.place(x=0, y=0)

#fname = PhotoImage(file = "crudim.png")
#background_label = Label(Frame2, image=fname)
#background_label.place(x=0, y=0, relwidth=1, relheight=1)

Frame2.withdraw()


def f1():
	addStud.deiconify()
	Frame2.withdraw()

def f9():
	UpdateStud.deiconify()
	Frame2.withdraw()

def f12():
	DeleteStud.deiconify()
	Frame2.withdraw()

def f15():
	GraphStud.deiconify()
	Frame2.withdraw()


def f3():
	viewStud.deiconify()
	Frame2.withdraw()
	#wap to perfrom fetching of records

	import cx_Oracle
	con = None
	cursor = None
	try:
		con = cx_Oracle.connect("system/abc123")
		print("CONNECTED")
		cursor = con.cursor()
		sql = "select id , name ,marks from Stud"
		cursor.execute(sql)
		data = cursor.fetchall()
		mdata = " "
		for d in data:
			mdata = mdata + "Id:" + str(d[0]) + " Name:" + d[1] + " Marks:" + str(d[2]) + "\n"
		st.insert(INSERT,mdata)
	except cx_Oracle.DatabaseError as e:
		print("isssueeeeee",e)
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()
			print("DISCONNECTED")	
		
btnAdd = Button(Frame2, text="ADD" ,font=('ariel',12,'bold'),width =20 , command = f1)
btnview = Button(Frame2, text="VIEW",font=('ariel',12,'bold') ,width =20 , command = f3)
btnUpdate = Button(Frame2, text="UPDATE" ,font=('ariel',12,'bold'),width =20 , command = f9)      
btnDelete = Button(Frame2, text="DELETE" ,font=('ariel',12,'bold'),width =20 , command = f12)  
btnGraph = Button(Frame2, text = "GRAPH",font=('ariel',12,'bold'),width =20 , command = f15)
btnGOBACK = Button(Frame2, text="PREVIOUS" ,font=('ariel',18,'bold'),bg = 'yellow', command = f13)
btnAdd.pack(pady = 20)
btnview.pack(pady = 20)
btnUpdate.pack(pady = 20)
btnDelete.pack(pady = 20)
btnGraph.pack(pady=20)
btnGOBACK.pack(pady = 20)


#################################################################GRAPH##############################################
GraphStud = Toplevel(Frame2)
GraphStud.title("Graph Student")
GraphStud.geometry("2000x1000+0+0")
p11 = PhotoImage(file="graphim.png")
label = Label(GraphStud, image=p11)
label.image = p11
label.place(x=0, y=0)
GraphStud.withdraw()

def f20():

	import cx_Oracle
	con = None
	cursor = None
	try:
		con = cx_Oracle.connect("system/abc123")
		print("CONNECTED")
		cursor = con.cursor()
		sql = "select * from Stud"
		cursor.execute(sql)
		data = cursor.fetchall()
		nm = []
		mk = []
		for g in data:
			nm.append(g[1]) 
			mk.append(g[2])
		nm = np.array(nm)
		mk = np.array(mk)

		plt.plot(nm,mk)
		plt.title("Exam Score")
		plt.xlabel("Name of Students")
		plt.ylabel("Marks in %")
		plt.grid()
		plt.show() 

		
	except cx_Oracle.DatabaseError as e:
		print("isssueeeeee",e)
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()
			print("DISCONNECTED")	

def f21():

	import cx_Oracle
	con = None
	cursor = None
	try:
		con = cx_Oracle.connect("system/abc123")
		print("CONNECTED")
		cursor = con.cursor()
		sql = "select * from Stud"
		cursor.execute(sql)
		data = cursor.fetchall()
		n = []
		m = []
		for g in data:
			n.append(g[1]) 
			m.append(g[2])
		n = np.array(n)
		m = np.array(m)

		plt.bar(n,m)
		plt.title("Exam Score")
		plt.xlabel("Name of Students")
		plt.ylabel("Marks in %")
		
		plt.show() 

		
	except cx_Oracle.DatabaseError as e:
		print("isssueeeeee",e)
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()
			print("DISCONNECTED")	


def f17():
	Frame2.deiconify()
	GraphStud.withdraw()

btnLine = Button(GraphStud, text="Line Graph" ,font=('ariel',12,'bold'),width =20 , command = f20)
btnBar = Button(GraphStud, text="Bar Graph" ,font=('ariel',12,'bold'),width =20 , command = f21)
btnGraphBack = Button(GraphStud , text = "BACK" ,font=('ariel',12,'bold'), command = f17)
btnLine.pack(pady = 20)
btnBar.pack(pady = 20)
btnGraphBack.pack(pady=20)

#################################################################DELETE################################################3

DeleteStud = Toplevel(Frame2)
DeleteStud.title("Delete Student")
DeleteStud.geometry("2000x1000+0+0")
p2 = PhotoImage(file="deleteim.png")
label = Label(DeleteStud, image=p2)
label.image = p2
label.place(x=0, y=0)

DeleteStud.withdraw()
lblDeleteEid = Label(DeleteStud, text = "ID",font=('ariel',12,'bold'))
entDeleteEid= Entry(DeleteStud,bd = 10)
def f10():
	import cx_Oracle
	con = None
	cursor = None
	try:
		con = cx_Oracle.connect("system/abc123")
		print("CONNECTED")
		cursor = con.cursor()	
		sql = "delete from Stud where id = '%d' "
		try:
			id = int(entDeleteEid.get())
			if(id <= 0):
				messagebox.showerror("ID Error \n", "Please enter valid id")
				entDeleteEid.focus_set()
				entDeleteEid.delete(0, END)
				con.rollback()
				con.close()			
				return
			

			
		except ValueError:
			messagebox.showerror("ID Error \n", "Please enter an integer")
			entDeleteEid.focus_set()
			entDeleteEid.delete(0, END)
			return			
				
		
		args = (id)
		cursor.execute(sql % args)
		con.commit()
		if(cursor.rowcount == 0):
			msg = "  Record Does not exists "
			messagebox.showinfo(" Failure \n" ,msg)
			entDeleteEid.focus_set()
			entDeleteEid.delete(0, END)	
		
		else:
			msg = str(cursor.rowcount) + "  Record Deleted"	
			messagebox.showinfo(" SUCCESS \n" ,msg)
			entDeleteEid.focus_set()
			entDeleteEid.delete(0, END)			
			
		

	except cx_Oracle.DatabaseError as e:
		con.rollback()
		print("issueeeee   ",e)
		messagebox.showerror(" Error \n" , "Some Database Error")
		return

	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()
			print("DISCONNECTED")

btnDeleteSave = Button(DeleteStud, text = "Delete" ,font=('ariel',12,'bold'), command = f10)
def f11():
	entDeleteEid.delete('0',END)
	Frame2.deiconify()
	DeleteStud.withdraw()
btnDeleteBack = Button(DeleteStud , text = "BACK" ,font=('ariel',12,'bold'), command = f11)
lblDeleteEid.pack(pady = 20)
entDeleteEid.pack(pady = 20)
btnDeleteSave.pack(pady = 20)
btnDeleteBack.pack(pady = 20)

###############################################################UPDATE###############################################################

UpdateStud = Toplevel(Frame2)
UpdateStud.title("Update Student")
UpdateStud.geometry("2000x1000+0+0")
p3 = PhotoImage(file="updateim.png")
label = Label(UpdateStud, image=p3)
label.image = p3
label.place(x=0, y=0)

UpdateStud.withdraw()
lblUpdateEid = Label(UpdateStud, text = "ID",font=('ariel',12,'bold'))
entUpdateEid= Entry(UpdateStud,bd = 10)
lblUpdateEname = Label(UpdateStud , text = "Name",font=('ariel',12,'bold'))
entUpdateEname = Entry(UpdateStud ,bd = 10)
lblUpdateMarks = Label(UpdateStud, text = "Marks %",font=('ariel',12,'bold'))
entUpdateMarks = Entry(UpdateStud, bd=10)
def f7():
	import cx_Oracle
	con = None
	cursor = None
	try:
		con = cx_Oracle.connect("system/abc123")
		print("CONNECTED")
		cursor = con.cursor()	
		sql = "update Stud set name = '%s' , marks = '%f' where id = '%d' "
		try:
			id = int(entUpdateEid.get())
			if(id <= 0):
				messagebox.showerror("ID Error \n", "Please enter valid id")
				entUpdateEid.focus_set()
				entUpdateEid.delete(0, END)
				entUpdateEname.delete(0, END)
				entUpdateMarks.delete(0, END)
				con.rollback()
				con.close()			
				return

			
		except ValueError:
			messagebox.showerror("ID Error \n", "Please enter an integer")
			entUpdateEid.focus_set()
			entUpdateEid.delete(0, END)
			entUpdateEname.delete(0, END)
			entUpdateMarks.delete(0, END)			
			return
		
		try:
			name = entUpdateEname.get()
			
			if name.isdigit():
				messagebox.showerror("Name Error \n", "Please enter a string")
				entUpdateEname.focus_set()
				entUpdateEname.delete(0, END)
				con.rollback()
				con.close()
				return
			elif (len(name) < 2 ):
				messagebox.showerror("Name Error \n", "Please enter a proper name")
				entUpdateEname.focus_set()
				entUpdateEname.delete(0, END)
				return
			else:
				lc, dc , oc = 0, 0, 0
				for s in name:
					if(s>='A' and s<='Z') or (s>='a' and s<='z') :
						lc =lc + 1
					elif(s>='0' and s<='9'):
						dc = dc + 1
					else:
						oc = oc+ 1
				if(oc != 0):
					messagebox.showerror("Name Error \n", "Please enter a proper name")
					entUpdateEname.focus_set()
					entUpdateEname.delete(0, END)	
					con.rollback()
					con.close()
					return
			
			
			
		except ValueError:
				messagebox.showerror("Name Error \n", "Please enter a string")
				return
		try:
			marks = float(entUpdateMarks.get())
			if(marks < 0.0 or marks >= 100.0):
				messagebox.showerror("Marks Error \n", "Please enter valid marks")
				entMarks.focus_set()
				entMarks.delete(0, END)
				con.rollback()
				con.close()
				return			
			
			
		except ValueError:
			messagebox.showerror("Marks Error \n", "Please enter integer or decimal value")
			entUpdateMarks.focus_set()
			entUpdateMarks.delete(0, END)
			return			
						

		args = (name,marks,id)
		cursor.execute(sql % args)
		con.commit()
		msg = str(cursor.rowcount) + "  Record Updated"
		if(cursor.rowcount == 0 ):
			messagebox.showinfo(" ERROR \n" ,"ID does not exists")
			entUpdateEid.focus_set()
			entUpdateEid.delete(0, END)			
			return
		
		else:
			messagebox.showinfo(" SUCCESS \n" ,msg)
		entUpdateEid.focus_set()
		entUpdateEid.delete(0, END)
		entUpdateEname.focus_set()
		entUpdateEname.delete(0, END)			
		entUpdateMarks.focus_set()
		entUpdateMarks.delete(0, END)			
							
			

	except cx_Oracle.DatabaseError as e:
		con.rollback()
		print("issueeeee   ",e)
		messagebox.showerror("Error \n" , "Some Database Error")
		return
		

	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()
			print("DISCONNECTED")

btnUpdateSave = Button(UpdateStud, text = "SAVE" ,font=('ariel',12,'bold'), command = f7)
def f8():
	entUpdateEid.delete('0',END)
	entUpdateEname.delete('0',END)
	entUpdateMarks.delete('0',END)
	Frame2.deiconify()
	UpdateStud.withdraw()
btnUpdateBack = Button(UpdateStud , text = "BACK" ,font=('ariel',12,'bold'), command = f8)
lblUpdateEid.pack(pady = 20)
entUpdateEid.pack(pady = 20)
lblUpdateEname.pack(pady = 20)
entUpdateEname.pack(pady = 20)
lblUpdateMarks.pack(pady = 20)
entUpdateMarks.pack(pady = 20)
btnUpdateSave.pack(pady = 20)
btnUpdateBack.pack(pady = 20)

###############################################################ADD#################################################

addStud = Toplevel(Frame2)
addStud.title("Add Student")
addStud.geometry("2000x1000+0+0")
p4 = PhotoImage(file="addim.png")
label = Label(addStud, image=p4)
label.image = p4
label.place(x=0, y=0)

addStud.withdraw()
lblEid = Label(addStud, text = "ID",font=('ariel',12,'bold'))
entEid= Entry(addStud,bd = 10)
lblEname = Label(addStud , text = "Name",font=('ariel',12,'bold'))
entEname = Entry(addStud ,bd = 10)
lblMarks = Label(addStud, text = "Marks %",font=('ariel',12,'bold'))
entMarks = Entry(addStud, bd=10)
def f5():
	import cx_Oracle
	con = None
	cursor = None
	try:
		con = cx_Oracle.connect("system/abc123")
		print("CONNECTED")
		cursor = con.cursor()	
		sql = "insert into Stud values('%d'  ,'%s' , '%f')"
		try:
			eid = int(entEid.get())
			if(eid <= 0):
				messagebox.showerror("ID Error \n", "Please enter valid id")
				entEid.focus_set()
				entEid.delete(0, END)
				entEname.delete(0, END)
				entMarks.delete(0, END)
				con.rollback()
				con.close()			
				return

		except ValueError:
			messagebox.showerror("ID Error \n", "Please enter an integer")
			entEid.focus_set()
			entEid.delete(0, END)
			entEname.delete(0, END)
			entMarks.delete(0, END)	
			return		
				
		
		try:
			ename = entEname.get()
			if ename.isdigit():
				messagebox.showerror("Name Error \n", "Please enter a string")
				entEname.focus_set()
				entEname.delete(0, END)
				con.rollback()
				con.close()
				return
			elif (len(ename) < 2 ):
				messagebox.showerror("Name Error \n", "Name too short")
				entEname.focus_set()
				entEname.delete(0, END)	
				con.rollback()
				con.close()
				return
			else:
				lc, dc , oc = 0, 0, 0
				for s in ename:
					if(s>='A' and s<='Z') or (s>='a' and s<='z') :
						lc =lc + 1
					elif(s>='0' and s<='9'):
						dc = dc + 1
					else:
						oc = oc+ 1
				if(oc != 0):
					messagebox.showerror("Name Error \n", "Please enter a proper name")
					entEname.focus_set()
					entEname.delete(0, END)	
					con.rollback()
					con.close()
					return
			


			
		except ValueError:
				messagebox.showerror("Name Error \n", "Please enter a string")
				return

		try:
			emarks = float(entMarks.get())
			if(emarks < 0.0 or emarks > 100.0):
				messagebox.showerror("Marks Error \n", "Please enter valid marks")
				entMarks.focus_set()
				entMarks.delete(0, END)
				con.rollback()
				con.close()			
				return

				
		except ValueError:
			messagebox.showerror("Marks Error \n", "Please enter integer or decimal value")
			entMarks.focus_set()
			entMarks.delete(0, END)			
			return


		args = (eid,ename,emarks)
		cursor.execute(sql % args)
		con.commit()
		msg = str(cursor.rowcount) + "  Record Inserted"
		messagebox.showinfo(" SUCCESS \n" ,msg)
		entEid.focus_set()
		entEid.delete(0, END)
		entEname.focus_set()
		entEname.delete(0, END)						
		entMarks.focus_set()
		entMarks.delete(0, END)			
			



	except cx_Oracle.DatabaseError as e:
		con.rollback()
		print("issueeeee   ",e)
		messagebox.showerror("Id Error \n" , "ID already exists")
		entEid.focus_set()
		entEid.delete(0, END)	
		return

	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()
			print("DISCONNECTED")

btnAddSave = Button(addStud, text = "SAVE" ,font=('ariel',12,'bold'), command = f5)
def f2():
	entEid.delete('0',END)
	entEname.delete('0',END)
	entMarks.delete('0',END)
	Frame2.deiconify()
	addStud.withdraw()
btnAddBack = Button(addStud , text = "BACK" ,font=('ariel',12,'bold'), command = f2)
lblEid.pack(pady = 20)
entEid.pack(pady = 20)
lblEname.pack(pady = 20)
entEname.pack(pady = 20)
lblMarks.pack(pady = 20)
entMarks.pack(pady = 20)
btnAddSave.pack(pady = 20)
btnAddBack.pack(pady = 20)

#########################################################VIEW###################################################################

viewStud = Toplevel(Frame2)
viewStud.title("View Student")
viewStud.geometry("2000x1000+0+0")
p5 = PhotoImage(file="viewim.png")
label = Label(viewStud, image=p5)
label.image = p5
label.place(x=0, y=0)

viewStud.withdraw()
def f4():
	st.delete('1.0',END)
	Frame2.deiconify()
	viewStud.withdraw()
st = scrolledtext.ScrolledText(viewStud , width = 40, height = 30)
btnViewBack = Button(viewStud , text = "BACK",font=('ariel',12,'bold'), command = f4)
st.pack(pady = 10)
btnViewBack.pack(pady = 10)
	

root.mainloop()