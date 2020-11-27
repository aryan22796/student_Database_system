from tkinter import*
from tkinter import ttk
import tkinter.messagebox
import pymysql #pip install pymysql

#if you enter own dbms MY SQL  LOCALHOST PASSWORD 


#first Basic frame design for our project by using Tkinter Gui.
class School:
    
    def __init__(self,root):
        self.root=root
        self.root.title("School management system")
        self.root.geometry("1350x800+0+0")
        self.root.configure(background='gainsboro')

        #=====================================Frame=================================
        MainFrame=Frame(self.root,bd=10,width=1350,height=700,relief=RIDGE)
        MainFrame.grid()
        
        OuterFrame=Frame(MainFrame,bd=10,width=1340,height=650,relief=RIDGE)
        OuterFrame.grid(row=0,column=0)
        
        InnerMostFrame=Frame(OuterFrame,bd=5,width=600,height=500,bg='cadet blue',relief=RIDGE)
        InnerMostFrame.grid(row=0,column=0)
        
        InnerFrame=Frame(OuterFrame,bd=5,width=800,height=500,bg='cadet blue',relief=RIDGE)
        InnerFrame.grid(row=0,column=1)
        
        BottomInnerFrame=Frame(MainFrame,bd=7,width=1340,height=300,relief=RIDGE)
        BottomInnerFrame.grid(row=2,column=0)


        Record_Frame=Frame(InnerFrame,bd=4,width=500,height=300,relief=RIDGE)
        Record_Frame.grid()

        Display_Frame=Frame(InnerMostFrame,bd=4,width=500,height=300,relief=RIDGE)
        Display_Frame.grid()
        
        Subject_Frame_Left=Frame(BottomInnerFrame,bd=5,width=600,height=250,bg='blue',padx=0,relief=RIDGE)
        Subject_Frame_Left.grid(row=0,column=0)

        Subject_Frame_Right=Frame(BottomInnerFrame,bd=5,width=600,height=250,bg='cadet blue',padx=0,relief=RIDGE)
        Subject_Frame_Right.grid(row=0,column=1)

        SubjectFrame1=Frame(Subject_Frame_Left,bd=5,width=300,height=250,bg='gainsboro',padx=2,relief=RIDGE)
        SubjectFrame1.grid(row=0,column=0)

        SubjectFrame2=Frame(Subject_Frame_Left,bd=5,width=400,height=250,bg='gainsboro',padx=2,relief=RIDGE)
        SubjectFrame2.grid(row=0,column=1)

        infoFrame=Frame(Subject_Frame_Right,bd=5,width=400,height=250,bg='gainsboro',padx=4,pady=4,relief=RIDGE)
        infoFrame.grid(row=0,column=0)

        ButtonsFrame=Frame(Subject_Frame_Right,bd=5,width=300,height=250,bg='gainsboro',padx=4,pady=4,relief=RIDGE)
        ButtonsFrame.grid(row=0,column=1)

        #==============================================Frame==================================================End=============


        #================================================Variable Decalretion================================================
        self.StudentID=StringVar()
        self.Firstname=StringVar()
        self.Lastname=StringVar()
        self.Phone=StringVar()
        self.Address=StringVar()
        self.Gender=StringVar()
        self.DOB=StringVar()
        self.Email=StringVar()
        self.English=StringVar()
        self.Physics=StringVar()
        self.Chemistry=StringVar()
        self.Mathematics=StringVar()
        self.Computer=StringVar()
        self.Biology=StringVar()
        self.Hindi=StringVar()
        self.Bussiness=StringVar()
        self.Accounts=StringVar()
        self.Economics=StringVar()
        self.PhE=StringVar()
        self.ParentGuidence=StringVar()
        self.pgfirstname=StringVar()
        self.pglastname=StringVar()
        self.pgPhone=StringVar()
        self.pgAddress=StringVar()
        self.pgEmail=StringVar()
       

        #===============================================Label==================================================================


        self.lblStudentId=Label(Display_Frame,font=('arial',12,'bold'),text="Student ID",bd=7)
        self.lblStudentId.grid(row=0,column=0,sticky=W,padx=5,pady=5)

        self.txtlStudentId=Entry(Display_Frame,font=('arial',12,'bold'),text="Student ID",bd=7,width=29,textvariable=self.StudentID)
        self.txtlStudentId.grid(row=0,column=1)


        self.lblFirstName=Label(Display_Frame,font=('arial',12,'bold'),text="First Name",bd=7)
        self.lblFirstName.grid(row=1,column=0,sticky=W,padx=5,pady=5)
        self.txtFirstName=Entry(Display_Frame,font=('arial',12,'bold'),text="First Name",bd=7,width=29,textvariable=self.Firstname)
        self.txtFirstName.grid(row=1,column=1)

        self.lblLastName=Label(Display_Frame,font=('arial',12,'bold'),text="Last Name",bd=7)
        self.lblLastName.grid(row=2,column=0,sticky=W,padx=5,pady=5)
        self.txtLastName=Entry(Display_Frame,font=('arial',12,'bold'),text="Last Name",bd=7,width=29,textvariable=self.Lastname)
        self.txtLastName.grid(row=2,column=1)

        
        self.lblPhone=Label(Display_Frame,font=('arial',12,'bold'),text="Mobile Number",bd=7)
        self.lblPhone.grid(row=3,column=0,sticky=W,padx=5,pady=5)
        self.txtPhone=Entry(Display_Frame,font=('arial',12,'bold'),text="Mobile Number",bd=7,width=29,textvariable=self.Phone)
        self.txtPhone.grid(row=3,column=1)

        self.lblAddress=Label(Display_Frame,font=('arial',12,'bold'),text="Address",bd=7)
        self.lblAddress.grid(row=4,column=0,sticky=W,padx=5,pady=5)
        self.txtAddress=Entry(Display_Frame,font=('arial',12,'bold'),text="Address",bd=7,width=29,textvariable=self.Address)
        self.txtAddress.grid(row=4,column=1)


        
        self.lblGender=Label(Display_Frame,font=('arial',12,'bold'),text="Gender",bd=3)
        self.lblGender.grid(row=5,column=0,sticky=W,padx=5,pady=5)
        self.cboGender=ttk.Combobox(Display_Frame,width=26,font=('arial',12,'bold'),state='readonly',textvariable=self.Gender)
        self.cboGender['values']=['','Female','Male']
        self.cboGender.current(0)
        self.cboGender.grid(row=5,column=1)


        self.lblDOB=Label(Display_Frame,font=('arial',12,'bold'),text="Date of Birth",bd=7)
        self.lblDOB.grid(row=6,column=0,sticky=W,padx=5,pady=5)
        self.txtDOB=Entry(Display_Frame,font=('arial',12,'bold'),text="Date of Birth",bd=7,width=29,textvariable=self.DOB)
        self.txtDOB.grid(row=6,column=1)



        self.lblEmail=Label(Display_Frame,font=('arial',12,'bold'),text="Email",bd=7)
        self.lblEmail.grid(row=7,column=0,sticky=W,padx=5,pady=5)
        self.txtEmail=Entry(Display_Frame,font=('arial',12,'bold'),text="Email",bd=7,width=29,textvariable=self.Email)
        self.txtEmail.grid(row=7,column=1)

        #======================================Student Record ====================================================
        scroll_x=Scrollbar(Record_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Record_Frame,orient=VERTICAL)
        self.studnet_records=ttk.Treeview(Record_Frame,height=13,columns=('stdid','firstname','lastname','phonenumber',
        'address','gender','dob','email'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)


        self.studnet_records.heading("stdid",text="Student ID")
        self.studnet_records.heading("firstname",text="First Name")
        self.studnet_records.heading("lastname",text="Last Name")
        self.studnet_records.heading("phonenumber",text="Mobile Number")
        self.studnet_records.heading("address",text="Address")
        self.studnet_records.heading("gender",text="Gender")
        self.studnet_records.heading("dob",text="DOB")
        self.studnet_records.heading("email",text="Email")
        
        self.studnet_records['show']='headings'

        self.studnet_records.column("stdid",width=70)
        self.studnet_records.column("firstname",width=100)
        self.studnet_records.column("lastname",width=100)
        self.studnet_records.column("phonenumber",width=70)
        self.studnet_records.column("address",width=150)
        self.studnet_records.column("gender",width=70)
        self.studnet_records.column("dob",width=100)
        self.studnet_records.column("email",width=100)

        self.studnet_records.pack(fill=BOTH,expand=1)
        self.studnet_records.bind("<ButtonRelease-1>",self.LearnInfo)
        self.view_data()

        #====================================== End Student Record ===============================================

        #===============================Lable of Display Frame Endend==============================



        #=============================== Subject  of student in Subject Frame=================================

        #================================== Subject Frame One  for Science Stream==========================
        self.lblEnglish=Label(SubjectFrame1,font=('arial',12,'bold'),text="English",bd=7 ,bg="gainsboro")
        self.lblEnglish.grid(row=0,column=0,sticky=W,padx=5,pady=5)

        self.cboEnglish=ttk.Combobox(SubjectFrame1,width=15,font=('arial',12,'bold'),state='readonly',textvariable=self.English)
        self.cboEnglish['values']=['Core','Yes','No', 'Completed']
        self.cboEnglish.current(0)
        self.cboEnglish.grid(row=0,column=1)


        self.lblPhysics=Label(SubjectFrame1,font=('arial',12,'bold'),text="Physics",bd=7,bg="gainsboro")
        self.lblPhysics.grid(row=1,column=0,sticky=W,padx=5,pady=5)

        self.cboPhysics=ttk.Combobox(SubjectFrame1,width=15,font=('arial',12,'bold'),state='readonly',textvariable=self.Physics)
        self.cboPhysics['values']=['Core','Yes','No', 'Completed']
        self.cboPhysics.current(0)
        self.cboPhysics.grid(row=1,column=1)


        self.lblChemistry=Label(SubjectFrame1,font=('arial',12,'bold'),text="Chemistry",bd=7,bg="gainsboro")
        self.lblChemistry.grid(row=2,column=0,sticky=W,padx=5,pady=5)

        self.cboChemistry=ttk.Combobox(SubjectFrame1,width=15,font=('arial',12,'bold'),state='readonly',textvariable=self.Chemistry)
        self.cboChemistry['values']=['Core','Yes','No', 'Completed']
        self.cboChemistry.current(0)
        self.cboChemistry.grid(row=2,column=1)



        self.lblMathematics=Label(SubjectFrame1,font=('arial',12,'bold'),text="Mathematics",bd=7,bg="gainsboro")
        self.lblMathematics.grid(row=3,column=0,sticky=W,padx=5,pady=5)

        self.cboMathematics=ttk.Combobox(SubjectFrame1,width=15,font=('arial',12,'bold'),state='readonly',textvariable=self.Mathematics)
        self.cboMathematics['values']=['Core','Yes','No', 'Completed']
        self.cboMathematics.current(0)
        self.cboMathematics.grid(row=3,column=1)


        self.lblComputer=Label(SubjectFrame1,font=('arial',12,'bold'),text="Computer Science",bd=7,bg="gainsboro")
        self.lblComputer.grid(row=4,column=0,sticky=W,padx=5,pady=5)

        self.cboComputer=ttk.Combobox(SubjectFrame1,width=15,font=('arial',12,'bold'),state='readonly',textvariable=self.Computer)
        self.cboComputer['values']=['Core','Yes','No', 'Completed']
        self.cboComputer.current(0)
        self.cboComputer.grid(row=4,column=1)


        


        self.lblHindi=Label(SubjectFrame1,font=('arial',12,'bold'),text="Hindi",bd=7,bg="gainsboro")
        self.lblHindi.grid(row=5,column=0,sticky=W,padx=5,pady=5)

        self.cboHindi=ttk.Combobox(SubjectFrame1,width=15,font=('arial',12,'bold'),state='readonly',textvariable=self.Hindi)
        self.cboHindi['values']=['Core','Yes','No', 'Completed']
        self.cboHindi.current(2)
        self.cboHindi.grid(row=5,column=1)

        self.lblBio=Label(SubjectFrame1,font=('arial',12,'bold'),text="Biology",bd=7,bg="gainsboro")
        self.lblBio.grid(row=6,column=0,sticky=W,padx=5,pady=5)

        self.cboBio=ttk.Combobox(SubjectFrame1,width=15,font=('arial',12,'bold'),state='readonly',textvariable=self.Biology)
        self.cboBio['values']=['Core','Yes','No', 'Completed']
        self.cboBio.current(2)
        self.cboBio.grid(row=6,column=1)



        #=================================================Subject Frame One ================================



        #       ================================================subject Frame TWO For commerce=====================
        #Bussines studies ,Finacail Accounting, Economics

       

        self.lblBussines=Label(SubjectFrame2,font=('arial',12,'bold'),text="Bussines Studies",bd=7,bg="gainsboro")
        self.lblBussines.grid(row=1,column=0,sticky=W,padx=5,pady=5)

        self.cbolBussines=ttk.Combobox(SubjectFrame2,width=15,font=('arial',12,'bold'),state='readonly',textvariable=self.Bussiness)
        self.cbolBussines['values']=['Core','Yes','No', 'Completed']
        self.cbolBussines.current(2)
        self.cbolBussines.grid(row=1,column=1)

        self.lblAccounting=Label(SubjectFrame2,font=('arial',12,'bold'),text="Finacial Accounting",bd=7,bg="gainsboro")
        self.lblAccounting.grid(row=2,column=0,sticky=W,padx=5,pady=5)

        self.cbolAccounts=ttk.Combobox(SubjectFrame2,width=15,font=('arial',12,'bold'),state='readonly',textvariable=self.Accounts)
        self.cbolAccounts['values']=['Core','Yes','No', 'Completed']
        self.cbolAccounts.current(2)
        self.cbolAccounts.grid(row=2,column=1)

        
        self.lblEconomics=Label(SubjectFrame2,font=('arial',12,'bold'),text="Economics",bd=7,bg="gainsboro")
        self.lblEconomics.grid(row=3,column=0,sticky=W,padx=5,pady=5)

        self.cbolEconomics=ttk.Combobox(SubjectFrame2,width=15,font=('arial',12,'bold'),state='readonly',textvariable=self.Economics)
        self.cbolEconomics['values']=['Core','Yes','No', 'Completed']
        self.cbolEconomics.current(2)
        self.cbolEconomics.grid(row=3,column=1)



       

        self.lblPhE=Label(SubjectFrame2,font=('arial',12,'bold'),text="Physical Education",bd=7,bg="gainsboro")
        self.lblHindi.grid(row=5,column=0,sticky=W,padx=5,pady=5)

        self.cboPhE=ttk.Combobox(SubjectFrame2,width=15,font=('arial',12,'bold'),state='readonly',textvariable=self.PhE)
        self.cboPhE['values']=['Core','Yes','No', 'Completed']
        self.cboPhE.current(2)
        self.cboPhE.grid(row=5,column=1)

        #============================ Comerce Frame End =================================
        #==============================================End of Subject Frame  ====================================




        #=================================================Parent Frame  ===================================

        self.lblParentGuidence=Label(infoFrame,font=('arial',12,'bold'),text="Gurdians's details Of : - ",bd=7)
        self.lblParentGuidence.grid(row=0,column=0,sticky=W,padx=5,pady=5)
        self.cboParentGuidence=ttk.Combobox(infoFrame,width=26,font=('arial',12,'bold'),state='readonly',textvariable=self.ParentGuidence)
        self.cboParentGuidence['values']=['Mother','Father','Brother','Sister']
        self.cboParentGuidence.current()
        self.cboParentGuidence.grid(row=0,column=1)

        
        self.lblFirstName=Label(infoFrame,font=('arial',12,'bold'),text="First Name",bd=7)
        self.lblFirstName.grid(row=1,column=0,sticky=W,padx=5,pady=5)
        self.txtFirstName=Entry(infoFrame,font=('arial',12,'bold'),text="First Name",bd=7,width=29,textvariable=self.pgfirstname)
        self.txtFirstName.grid(row=1,column=1)

        self.lblLastName=Label(infoFrame,font=('arial',12,'bold'),text="Last Name",bd=7)
        self.lblLastName.grid(row=2,column=0,sticky=W,padx=5,pady=5)
        self.txtLastName=Entry(infoFrame,font=('arial',12,'bold'),text="Last Name",bd=7,width=29,textvariable=self.pglastname)
        self.txtLastName.grid(row=2,column=1)

        
        self.lblPhone=Label(infoFrame,font=('arial',12,'bold'),text="Phone Number",bd=7)
        self.lblPhone.grid(row=3,column=0,sticky=W,padx=5,pady=5)
        self.txtPhone=Entry(infoFrame,font=('arial',12,'bold'),text="Phone Number",bd=7,width=29,textvariable=self.pgPhone)
        self.txtPhone.grid(row=3,column=1)

        self.lblAddress=Label(infoFrame,font=('arial',12,'bold'),text="Address",bd=7)
        self.lblAddress.grid(row=4,column=0,sticky=W,padx=5,pady=5)
        self.txtAddress=Entry(infoFrame,font=('arial',12,'bold'),text="Address",bd=7,width=29,textvariable=self.pgAddress)
        self.txtAddress.grid(row=4,column=1)

        self.lblEmail=Label(infoFrame,font=('arial',12,'bold'),text="Email",bd=7)
        self.lblEmail.grid(row=5,column=0,sticky=W,padx=5,pady=5)
        self.txtEmail=Entry(infoFrame,font=('arial',12,'bold'),text="Email",bd=7,width=29,textvariable=self.pgEmail)
        self.txtEmail.grid(row=5,column=1)



        #==============================================End OF Parent Frame ============================



        #========================================== Button for Add  ===================================


        self.btnAddNew=Button(ButtonsFrame,pady=5,padx=15,font=('arial',12,'bold'),width=5,text="Add New",command=self.add_student)
        self.btnAddNew.grid(row=0,column=0)

        self.btnDelete=Button(ButtonsFrame,pady=1,padx=15,font=('arial',12,'bold'),width=5,text="Delete",command=self.Delete)
        self.btnDelete.grid(row=1,column=0)

        self.btnUpdate=Button(ButtonsFrame,pady=0.5,padx=15,font=('arial',12,'bold'),width=5,text="Update",command=self.Update)
        self.btnUpdate.grid(row=2,column=0)

        self.btnReset=Button(ButtonsFrame,pady=0.5,padx=15,font=('arial',12,'bold'),width=5,text="Reset",command=self.Resets)
        self.btnReset.grid(row=3,column=0)
 
        self.btnExit=Button(ButtonsFrame,pady=0.5,padx=15,font=('arial',12,'bold'),width=5,text="Exit",command=self.iExit)
        self.btnExit.grid(row=4,column=0)

        self.btnSearch=Button(ButtonsFrame,pady=0.5,padx=15,font=('arial',12,'bold'),width=5,text="Search")
        self.btnSearch.grid(row=5,column=0)




          # ============================================== End Buttton frame==================


        #===============================================================Function =================================================
   
    def add_student(self):
        if self.StudentID.get()=="" or self.Firstname.get()=="" or self.Lastname.get()=="":
                tkinter.messagebox.askyesno("Enter the studnet Details")
        else:
                sqlCon=pymysql.connect(host="localhost",user="root",password="admin",database="schooldb")
                cur=sqlCon.cursor()
                cur.execute("insert into schooldb values(%s,%s,%s,%s,%s,%s,%s,%s)",(self.StudentID.get(),
                                                                                        self.Firstname.get(),
                                                                                        self.Lastname.get(),
                                                                                        self.Phone.get(),
                                                                                        self.Address.get(),
                                                                                        self.Gender.get(),
                                                                                        self.DOB.get(),
                                                                                        self.Email.get()))
                sqlCon.commit()
                sqlCon.close()
                self.view_data()
                tkinter.messagebox.askyesno("Success","Entered successfully")
    def view_data(self):
        sqlCon=pymysql.connect(host="localhost",user="root",password="admin",database="schooldb")
        cur=sqlCon.cursor()
        cur.execute("select * from schooldb")
        rows=cur.fetchall()
        if len(rows)!=0:
                self.studnet_records.delete(*self.studnet_records.get_children())
                for row in rows:
                        self.studnet_records.insert('',END,values=row)
                sqlCon.commit()
        sqlCon.close()
    def LearnInfo(self,ev):
        viewInfo=self.studnet_records.focus()
        learnData=self.studnet_records.item(viewInfo)
        row=learnData['values']
        self.StudentID.set(row[0])
        self.Firstname.set(row[1])
        self.Lastname.set(row[2])
        self.Phone.set(row[3])
        self.Address.set(row[4])
        self.Gender.set(row[5])
        self.DOB.set(row[6])
        self.Email.set(row[7])



    def Update(self):
        sqlCon=pymysql.connect(host="localhost",user="root",password="admin",database="schooldb")
        cur=sqlCon.cursor()
        cur.execute("update schooldb set firstname=%s,lastname=%s,phonenumber=%s,address=%s,gender=%s,dob=%s,email=%s where stdid=%s",(
                self.Firstname.get(),
                self.Lastname.get(),
                self.Phone.get(),
                self.Address.get(),
                self.Gender.get(),
                self.DOB.get(),
                self.Email.get(),
                self.StudentID.get()))

        sqlCon.commit()
        self.view_data()
        #self.Resets()
        sqlCon.close()
        tkinter.messagebox.askyesno("Success","Updated Successfully")

    def Delete(self):
        sqlCon=pymysql.connect(host="localhost",user="root",password="admin",database="schooldb")
        cur=sqlCon.cursor()
        cur.execute("delete from schooldb where stdid=%s",self.StudentID.get())

        sqlCon.commit()
        self.view_data()
        #self.Resets()
        sqlCon.close()
        tkinter.messagebox.showinfo("Delete Successfully")
        



    def Resets(self):
        self.StudentID.set("")
        self.Firstname.set("")
        self.Lastname.set("")
        self.Phone.set("")
        self.Address.set("")
        self.Gender.set("")
        self.DOB.set("")
        self.Email.set("")
        self.English.set("Core")
        self.Physics.set("Core")
        self.Chemistry.set("Core")
        self.Mathematics.set("Core")
        self.Computer.set("Core")
        self.Biology.set("No")
        self.Hindi.set("No")
        self.Bussiness.set("")
        self.Accounts.set("")
        self.Economics.set("")
        self.PhE.set("")
        self.ParentGuidence.set("Mother")
        self.pgfirstname.set("")
        self.pglastname.set("")
        self.pgPhone.set("")
        self.pgAddress.set("")
        self.pgEmail.set("")
             
                
    def iExit(self):
        iExit=tkinter.messagebox.askyesno("School Management DataBase System","Confirm if you want to exit")
        if iExit >0:
                root.destroy()
        return    



        
        
        
        

if __name__== '__main__':
    root =Tk()
    application=School(root)
    root.mainloop()
                           
                           
                           
