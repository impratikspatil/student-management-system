

############   insert_into_db  #################


def cennect_to_database():
    if host_entry.get() != "127.0.0.1" or user_entry.get()!="root" or  pass_entry.get()!="PSP1234@psp":
        dbroot.destroy()
        show_n=messagebox.showerror("ERROR","enter valid credentials")

    import mysql.connector
    mydb = mysql.connector.connect(
        host=host_entry.get(),
        user=user_entry.get(),
        password=pass_entry.get(),
        database="mydatabase"
    )
    dbroot.destroy()
    show_notification = messagebox.showinfo("information","DATABASE CONNECTED SUCCESSFULLY")





    ###################  create table in database  ############
    #mycursor #= mydb.cursor()

    #mycursor.execute("CREATE TABLE `student_management_system`(`id` INT ZEROFILL NOT NULL AUTO_INCREMENT,`name` VARCHAR(45) NOT NULL,`email` VARCHAR(45) NOT NULL,`adress` VARCHAR(45) NULL,`gender` VARCHAR(45) NOT NULL,`birth date` VARCHAR(45) NOT NULL,`mobile` VARCHAR(45) NOT NULL,`date` VARCHAR(45) NOT NULL,PRIMARY KEY (`id`))")

    mydb.commit()
    add_std_btn['state'] = 'normal'
    search_std_btn['state'] = 'normal'
    delete_std_btn['state'] = 'normal'
    update_std_btn['state'] = 'normal'
    showall_std_btn['state'] = 'normal'
    export_data_std_btn['state'] = 'normal'



    ###########   ADD FUNCTION (TOPLEVEL) #########
def add():
    def insert_into_db():

        import pymysql
        mydb = pymysql.connect(
            host="127.0.0.1",
            user="root",
            password="PSP1234@psp",
            database="mydatabase"
        )
        global time
        global date
        id = id_entry_for_add.get()
        name = name_entry_for_add.get()
        email = email_entry_for_add.get()
        adress = adress_entry_for_add.get()
        gender = gender_entry_for_add.get()
        dob = dob_entry_for_add.get()
        mobile = mobile_entry_for_add.get()
        date = time.strftime("%d/%m/%Y")
        times= time.strftime("%H:%M:%S")

        mycursor = mydb.cursor()

        try:
            sql = 'INSERT  INTO student_management_system values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(sql, (id, name, email, adress, gender, dob, mobile, date, times))
            mydb.commit()
            res = messagebox.showinfo("notification", "ID {} NAME {} added successfully".format(id, name),
                                      parent=add_screen)
            add_screen.destroy()

        except:
            show_no = messagebox.showerror("error", "error occoured ID already exist")
            add_screen.destroy()

        strr = 'select * from student_management_system'
        mycursor.execute(strr)

        all_data = mycursor.fetchall()
        student_table.delete(*student_table.get_children())
        for i in all_data:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
            student_table.insert('', END, values=vv)


    global add_screen
    add_screen=Toplevel()
    add_screen.geometry('550x600+200+450')
    add_screen.config(bg='gold4')
    add_screen.resizable(False, False)
    add_screen.title("ADD STUDENT")
    add_screen.grab_set()


    ######### add credentials labels  #########
    id_lbl=Label(add_screen,text="ENTER ID:",font=('arial',15,'bold'),width=15,relief=RIDGE,borderwidth=4,anchor='w')
    id_lbl.place(x=20,y=30)

    name_lbl = Label(add_screen, text="ENTER NAME:", font=('arial', 15, 'bold'), width=15, relief=RIDGE, borderwidth=4,  anchor='w')
    name_lbl.place(x=20, y=90)

    email_lbl = Label(add_screen, text="ENTER EMAIL:", font=('arial', 15, 'bold'), width=15, relief=RIDGE, borderwidth=4,anchor='w')
    email_lbl.place(x=20, y=150)

    adress_lbl = Label(add_screen, text="ENTER ADRESS:", font=('arial', 15, 'bold'), width=15, relief=RIDGE, borderwidth=4,anchor='w')
    adress_lbl.place(x=20, y=210)

    gender_lbl = Label(add_screen, text="ENTER GENDER:", font=('arial', 15, 'bold'), width=15, relief=RIDGE, borderwidth=4, anchor='w')
    gender_lbl.place(x=20, y=270)

    dob_lbl = Label(add_screen, text="ENTER DOB:", font=('arial', 15, 'bold'), width=15, relief=RIDGE,borderwidth=4, anchor='w')
    dob_lbl.place(x=20, y=330)

    mobile_lbl = Label(add_screen, text="ENTER MOBILE:", font=('arial', 15, 'bold'), width=15, relief=RIDGE, borderwidth=4,anchor='w')
    mobile_lbl.place(x=20, y=390)



    ######### add credentials entry  #########
    global id_entry_for_add
    global name_entry_for_add
    global email_entry_for_add
    global adress_entry_for_add
    global gender_entry_for_add
    global dob_entry_for_add
    global mobile_entry_for_add


    id_entry_for_add = Entry(add_screen,  width=40, relief=RIDGE, borderwidth=4)
    id_entry_for_add.place(x=250, y=30,height=30)


    name_entry_for_add = Entry(add_screen,  width=40, relief=RIDGE, borderwidth=4)
    name_entry_for_add.place(x=250, y=90,height=30)

    email_entry_for_add = Entry(add_screen,  width=40, relief=RIDGE,  borderwidth=4)
    email_entry_for_add.place(x=250, y=150,height=30)

    adress_entry_for_add = Entry(add_screen,   width=40, relief=RIDGE, borderwidth=4)
    adress_entry_for_add.place(x=250, y=210,height=30)

    gender_entry_for_add = Entry(add_screen,   width=40, relief=RIDGE, borderwidth=4)
    gender_entry_for_add.place(x=250, y=270,height=30)

    dob_entry_for_add= Entry(add_screen,   width=40, relief=RIDGE, borderwidth=4)
    dob_entry_for_add.place(x=250, y=330,height=30)

    mobile_entry_for_add = Entry(add_screen, width=40, relief=RIDGE, borderwidth=4)
    mobile_entry_for_add.place(x=250, y=390, height=30)



    ###### SUBMIT BTN FOR ADD STUDENT ########
    submit_for_add=Button(add_screen,text="ADD",font=('arial',17,'bold'),width=10, relief=GROOVE, borderwidth=4,bg='black',fg='white',
                                    activebackground= 'gold2', activeforeground = 'black',command=insert_into_db)
    submit_for_add.place(x=200,y=500)

    add_screen.mainloop()


###########   SEARCH FUNCTION (TOPLEVEL) #########
def search():
    def search_into_db():
        import pymysql
        mydb = pymysql.connect(
            host="127.0.0.1",
            user="root",
            password="PSP1234@psp",
            database="mydatabase"
        )
        mycursor=mydb.cursor()

        id= id_entry_for_search.get()
        name= name_entry_for_search.get()
        email= email_entry_for_search.get()
        adress= adress_entry_for_search.get()
        gender= gender_entry_for_search.get()
        dob= dob_entry_for_search.get()
        mobile = mobile_entry_for_search.get()
        if (id !=''):
            strr='select * from student_management_system where id=%s'
            mycursor.execute(strr,(id))
            all_data=mycursor.fetchall()
            student_table.delete(*student_table.get_children())
            for i in all_data:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                student_table.insert('', END, values=vv)

        elif (name !=''):
            strr = 'select * from student_management_system where name=%s'
            mycursor.execute(strr, (name))
            all_data=mycursor.fetchall()
            student_table.delete(*student_table.get_children())
            for i in all_data:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                student_table.insert('', END, values=vv)
        elif (email !=''):
            strr = 'select * from student_management_system where email=%s'
            mycursor.execute(strr, (email))
            all_data=mycursor.fetchall()
            student_table.delete(*student_table.get_children())
            for i in all_data:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                student_table.insert('', END, values=vv)

        elif (adress !=''):
            strr = 'select * from student_management_system where adress=%s'
            mycursor.execute(strr, (adress))
            all_data=mycursor.fetchall()
            student_table.delete(*student_table.get_children())
            for i in all_data:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                student_table.insert('', END, values=vv)


        elif (gender !=''):
            strr = 'select * from student_management_system where gender=%s'
            mycursor.execute(strr, (gender))
            all_data=mycursor.fetchall()
            student_table.delete(*student_table.get_children())
            for i in all_data:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                student_table.insert('', END, values=vv)






        elif (dob !=''):
            strr = 'select * from student_management_system where dob=%s'
            mycursor.execute(strr, (dob))
            all_data=mycursor.fetchall()
            student_table.delete(*student_table.get_children())
            for i in all_data:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                student_table.insert('', END, values=vv)


        elif (mobile !=''):
            strr = 'select * from student_management_system where mobile=%s'
            mycursor.execute(strr, (mobile))
            all_data=mycursor.fetchall()
            student_table.delete(*student_table.get_children())
            for i in all_data:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                student_table.insert('', END, values=vv)
        search_screen.destroy()


    global search_screen
    search_screen = Toplevel()
    search_screen.geometry('550x600+200+520')
    search_screen.config(bg='gold4')
    search_screen.resizable(False, False)
    search_screen.title("SEARCH STUDENT")


    ######### search credentials labels  #########
    id_lbl = Label(search_screen, text="ENTER ID:", font=('arial', 15, 'bold'), width=15, relief=RIDGE, borderwidth=4,
                   anchor='w')
    id_lbl.place(x=20, y=30)

    name_lbl = Label(search_screen, text="ENTER NAME:", font=('arial', 15, 'bold'), width=15, relief=RIDGE, borderwidth=4, anchor='w')
    name_lbl.place(x=20, y=90)

    email_lbl = Label(search_screen, text="ENTER EMAIL:", font=('arial', 15, 'bold'), width=15, relief=RIDGE,
                      borderwidth=4, anchor='w')
    email_lbl.place(x=20, y=150)

    adress_lbl = Label(search_screen, text="ENTER ADRESS:", font=('arial', 15, 'bold'), width=15, relief=RIDGE,
                       borderwidth=4, anchor='w')
    adress_lbl.place(x=20, y=210)

    gender_lbl = Label(search_screen, text="ENTER GENDER:", font=('arial', 15, 'bold'), width=15, relief=RIDGE,
                       borderwidth=4, anchor='w')
    gender_lbl.place(x=20, y=270)

    dob_lbl = Label(search_screen, text="ENTER DOB:", font=('arial', 15, 'bold'), width=15, relief=RIDGE, borderwidth=4,
                    anchor='w')
    dob_lbl.place(x=20, y=330)

    mobile_lbl = Label(search_screen, text="ENTER MOBILE:", font=('arial', 15, 'bold'), width=15, relief=RIDGE, borderwidth=4,
                       anchor='w')
    mobile_lbl.place(x=20, y=390)


    ######### search credentials entry  #########
    idval = StringVar()
    nameval=StringVar()
    emailval = StringVar()
    adressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    mobileval = StringVar()


    global id_entry_for_search
    id_entry_for_search = Entry(search_screen, width=40, relief=RIDGE, borderwidth=4,textvariable=idval)
    id_entry_for_search.place(x=250, y=30, height=30)

    global name_entry_for_search
    name_entry_for_search = Entry(search_screen, width=40, relief=RIDGE, borderwidth=4, textvariable=nameval)
    name_entry_for_search.place(x=250, y=90, height=30)

    global email_entry_for_search
    email_entry_for_search = Entry(search_screen, width=40, relief=RIDGE, borderwidth=4,textvariable=emailval)
    email_entry_for_search.place(x=250, y=150, height=30)

    global adress_entry_for_search
    adress_entry_for_search = Entry(search_screen, width=40, relief=RIDGE, borderwidth=4,textvariable=adressval)
    adress_entry_for_search.place(x=250, y=210, height=30)

    global  gender_entry_for_search
    gender_entry_for_search= Entry(search_screen, width=40, relief=RIDGE, borderwidth=4,textvariable=genderval)
    gender_entry_for_search.place(x=250, y=270, height=30)

    global dob_entry_for_search
    dob_entry_for_search = Entry(search_screen, width=40, relief=RIDGE, borderwidth=4,textvariable=dobval)
    dob_entry_for_search.place(x=250, y=330, height=30)
    global mobile_entry_for_search
    mobile_entry_for_search = Entry(search_screen, width=40, relief=RIDGE, borderwidth=4,textvariable=mobileval)
    mobile_entry_for_search.place(x=250, y=390, height=30)

    ###### SUBMIT BTN FOR ADD STUDENT ########
    submit_for_add = Button(search_screen, text="SEARCH", font=('arial', 17, 'bold'), width=10, relief=GROOVE,
                            borderwidth=4, bg='black', fg='white',
                            activebackground='gold2', activeforeground='black',command=search_into_db)
    submit_for_add.place(x=200, y=450)

    search_screen.mainloop()


###########   DELETE FUNCTION (TOPLEVEL) #########
def delete():
    import pymysql
    mydb = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="PSP1234@psp",
        database="mydatabase"
    )
    mycursor = mydb.cursor()

    cc=student_table.focus()

    content=student_table.item(cc)
    pp=content['values'][0]
    strr='delete from student_management_system where id=%s'
    mycursor.execute(strr,(pp))
    mydb.commit()
    messagebox.showinfo('Notification','ID {} deleted successfully'.format(pp))

    strr='select * from student_management_system'
    mycursor.execute(strr)
    all_data =mycursor.fetchall()
    student_table.delete(*student_table.get_children())
    for i in all_data:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        student_table.insert('', END, values=vv)


###########   UPDATE FUNCTION (TOPLEVEL) #########
def update():
    global time
    global date
    def update_into_db():
        import pymysql
        mydb = pymysql.connect(
            host="127.0.0.1",
            user="root",
            password="PSP1234@psp",
            database="mydatabase"
        )
        mycursor = mydb.cursor()
        global date
        global tm
        id = id_entry_for_update.get()
        name = name_entry_for_update.get()
        email = email_entry_for_update.get()
        adress = adress_entry_for_update.get()
        gender = gender_entry_for_update.get()
        dob = dob_entry_for_update.get()
        mobile = mobile_entry_for_update.get()
        date = time.strftime("%d/%m/%Y")
        tm = time.strftime("%H:%M:%S")

        strr='update student_management_system set name=%s,email=%s,adress=%s,gender=%s,mobile=%s,date=%s,time=%s where id =%s'
        mycursor.execute(strr,(name, email ,adress,gender,mobile,date,tm,id))
        mydb.commit()
        messagebox.showinfo('Notification','id {} updated successfully'.format(id))
        update_screen.destroy()
        strr = 'select * from student_management_system'
        mycursor.execute(strr)
        all_data = mycursor.fetchall()
        student_table.delete(*student_table.get_children())
        for i in all_data:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
            student_table.insert('', END, values=vv)


    global update_screen
    update_screen = Toplevel()
    update_screen.geometry('550x550+200+660')
    update_screen.config(bg='gold4')
    update_screen.resizable(False, False)
    update_screen.title("UPDATE STUDENT")
    update_screen.grab_set()

    #####---------------labels for update  -------------########33
    id_lbl = Label(update_screen, text="UPDATE ID:", font=('arial', 15, 'bold'), width=15, relief=RIDGE, borderwidth=4,
                   anchor='w')
    id_lbl.place(x=20, y=30)

    name_lbl = Label(update_screen, text="UPDATE NAME:", font=('arial', 15, 'bold'), width=15, relief=RIDGE,
                     borderwidth=4, anchor='w')
    name_lbl.place(x=20, y=90)

    email_lbl = Label(update_screen, text="UPDATE EMAIL:", font=('arial', 15, 'bold'), width=15, relief=RIDGE,
                      borderwidth=4, anchor='w')
    email_lbl.place(x=20, y=150)

    adress_lbl = Label(update_screen, text="UPDATE ADRESS:", font=('arial', 15, 'bold'), width=15, relief=RIDGE,
                       borderwidth=4, anchor='w')
    adress_lbl.place(x=20, y=210)

    gender_lbl = Label(update_screen, text="UPDATE GENDER:", font=('arial', 15, 'bold'), width=15, relief=RIDGE,
                       borderwidth=4, anchor='w')
    gender_lbl.place(x=20, y=270)

    dob_lbl = Label(update_screen, text="UPDATE DOB:", font=('arial', 15, 'bold'), width=15, relief=RIDGE, borderwidth=4,
                    anchor='w')
    dob_lbl.place(x=20, y=330)

    mobile_lbl = Label(update_screen, text="UPDATE MOBILE:", font=('arial', 15, 'bold'), width=15, relief=RIDGE,
                       borderwidth=4,
                       anchor='w')
    mobile_lbl.place(x=20, y=390)



    ######### update credentials entry  #########
    id_update = StringVar()
    name_update = StringVar()
    email_update = StringVar()
    adress_update = StringVar()
    gender_update = StringVar()
    dob_update = StringVar()
    mobile_update = StringVar()







    global id_entry_for_update
    id_entry_for_update = Entry(update_screen, width=40, relief=RIDGE, borderwidth=4,textvariable=id_update)
    id_entry_for_update.place(x=250, y=30, height=30)

    global name_entry_for_update
    name_entry_for_update = Entry(update_screen, width=40, relief=RIDGE, borderwidth=4,textvariable=name_update)
    name_entry_for_update.place(x=250, y=90, height=30)

    global email_entry_for_update
    email_entry_for_update = Entry(update_screen, width=40, relief=RIDGE, borderwidth=4,textvariable=email_update)
    email_entry_for_update.place(x=250, y=150, height=30)

    global adress_entry_for_update
    adress_entry_for_update = Entry(update_screen, width=40, relief=RIDGE, borderwidth=4,textvariable=adress_update)
    adress_entry_for_update.place(x=250, y=210, height=30)

    global  gender_entry_for_update
    gender_entry_for_update= Entry(update_screen, width=40, relief=RIDGE, borderwidth=4,textvariable=gender_update)
    gender_entry_for_update.place(x=250, y=270, height=30)

    global dob_entry_for_update
    dob_entry_for_update = Entry(update_screen, width=40, relief=RIDGE, borderwidth=4,textvariable=dob_update)
    dob_entry_for_update.place(x=250, y=330, height=30)
    global mobile_entry_for_update
    mobile_entry_for_update = Entry(update_screen, width=40, relief=RIDGE, borderwidth=4,textvariable=mobile_update)
    mobile_entry_for_update.place(x=250, y=390, height=30)

    ###### update BTN FOR STUDENT ########
    submit_for_update = Button(update_screen, text="UPDATE", font=('arial', 17, 'bold'), width=10, relief=GROOVE, borderwidth=4, bg='black',
                               fg='white', activebackground='gold2', activeforeground='black',command=update_into_db)
    submit_for_update.place(x=200, y=450)


    cc=student_table.focus()
    content=student_table.item(cc)
    pp=content['values']
    if(len(pp))!=0:
       id_update.set(pp[0])
       name_update.set(pp[1])
       email_update.set(pp[2])
       adress_update.set(pp[3])
       gender_update.set(pp[4])
       dob_update.set(pp[5])
       mobile_update.set(pp[6])




    update_screen.mainloop()
###########  SHOW_ALL FUNCTION (TOPLEVEL) #########
def show():
    import pymysql
    mydb = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="PSP1234@psp",
        database="mydatabase"
    )
    mycursor = mydb.cursor()

    strr='select * from student_management_system'
    mycursor.execute(strr)

    all_data=mycursor.fetchall()
    student_table.delete(*student_table.get_children())
    for i in all_data:
        vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
        student_table.insert('',END,values=vv)



 ###########   EXPORT FUNCTION (TOPLEVEL) #########
def export():
    import mysql.connector
    mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="PSP1234@psp",
        database="mydatabase"
    )
    mycursor = mydb.cursor()
    ff=filedialog.asksaveasfilename()
    gg = student_table.get_children()
    id, name, email, adress, gender, dob, mobile, date, time = [], [], [], [], [], [], [], [], []
    for i in gg:
        content = student_table.item(i)
        pp = content['values']
        id.append(pp[0]), name.append(pp[1]), email.append(pp[2]), adress.append(pp[3]), gender.append(
            pp[4]), dob.append(pp[5]), mobile.append(pp[6]), date.append(pp[7]), time.append(pp[8])

    dd = ['id', 'name', 'email', 'adress', 'gender', 'birth', 'mobile', 'date', 'time']
    df = pandas.DataFrame(list(zip(id, name, email, adress, gender, dob, mobile, date, time)), columns=dd)
    path = r'{}.csv'.format(ff)
    df.to_csv(path, index=False)
    if bool(ff)==True:
        messagebox.showinfo('Notification', 'DATA exported successfully')
    elif bool(ff)==False:
        messagebox.showinfo('Notification', 'DATA  not exported ')

def exit():
    show_notification=messagebox.askyesno('notification','Do you Want To Exit?')
    if (show_notification==True):
        root.destroy()

#####################  CREATE A DATABASE  ###########################


#############   DATABSE FUNCTION ################
def connectdb():

    ############   TOP LEVEL WINDOW ##########
    global dbroot
    dbroot=Toplevel()
    dbroot.geometry('550x300+700+400')
    dbroot.resizable(False,False)
    dbroot.title("database connectivity")
    dbroot.grab_set()
    dbroot.config(bg='medium purple')


    ######### DATABASE LABELS  #####
    host_label=Label(dbroot ,text="Enter host:",font=('arial',17,'bold'),width=14,relief=RIDGE,borderwidth=4,anchor='w')
    host_label.place(x=10 ,y=10)

    user_label = Label(dbroot, text="Enter root:", font=('arial', 17, 'bold'), width=14, relief=RIDGE, borderwidth=4,anchor='w')
    user_label.place(x=10, y=70)

    pass_label = Label(dbroot, text="Enter password:", font=('arial', 17, 'bold'), width=14, relief=RIDGE, borderwidth=4,anchor='w')
    pass_label.place(x=10, y=130)



    ######################  DATABASE ENTRY LABLES  ###################
    global host_entry
    host_entry = Entry(dbroot,bd=5)
    host_entry.place(x=260,y=9,width=250,height=35)
   

    global user_entry
    user_entry = Entry(dbroot, bd=5)
    user_entry.place(x=260, y=69, width=250, height=35)

    global pass_entry
    pass_entry = Entry(dbroot, bd=5,show = '*')
    pass_entry.place(x=260, y=129, width=250, height=35)


    ################## SUBMIT BUTTON ########################


    submit_btn=Button(dbroot,text="SUBMIT",font=('arial',17,'bold'),width=10, relief=RIDGE, borderwidth=4,bg='black',fg='white',
                                    activebackground= 'gold2', activeforeground = 'black',command=cennect_to_database)
    submit_btn.place(x=180,y=200)

    dbroot.mainloop()


###############################  SLIDER ANIMATION ################
import random
colors=['red','orange','yellow','green','blue','white','violet']
def animation_with_color():
    fg=random.choice(colors)
    slider_label.config(fg=fg)
    slider_label.after(10,animation_with_color)

def animation_intro():
    global text,count
    if(count>=len(a)):
        text=''
        count=-1
        slider_label.config(text=text)
    else:
        text=text+a[count]
        slider_label.config(text=text)
    count+=1
    slider_label.after(70,animation_intro)


#################################   DATE AND TIME FUNCTION  ##########
def clock():
    time_str=time.strftime("%H:%M:%S")
    date_str=time.strftime("%d/%m/%Y")
    time_and_date.config(text="DATE:"+time_str+"\n"+"TIME:"+date_str)
    time_and_date.after(250,clock)


########################  MAIN WINDOW ###########################
from tkinter import *
import time
from tkinter import Toplevel
from tkinter.ttk import Treeview
from tkinter import messagebox,filedialog
from tkinter import ttk
import pandas
import pymysql
root = Tk()
root.title('students management system')
root.config(bg='aquamarine2')
root.geometry('1500x850+200+160')

root.resizable(False,False)


###################   BUTTON FOR DATABASE CONNECTIVITY ######################333
btn_for_database_connectivity=Button(root,text="Connect with database",font=('airel',15,'bold'),
                                     fg='white',bg='dimgrey',relief=RIDGE,borderwidth=4,
                                     activebackground='black',activeforeground='white',command=connectdb)
btn_for_database_connectivity.place(x=1200 ,y=0,width=250,height=60)


##############################         FRAMES 1     #########################
DataEntryFrame=Frame(root,bg='gold2',relief=GROOVE,borderwidth=5)
DataEntryFrame.place(x=40,y=150,height=600 ,width=500)

#######################   FRAME 1 BUTTONS  ###############

#####  ADD BUTTON #####

add_std_btn=Button(DataEntryFrame,text="1. ADD STUDENT",font=('arial',10,'bold'),width=20, relief=GROOVE, borderwidth=4, bg='black',fg='white',
                                    activebackground='red', activeforeground='black',height=2,command=add)
add_std_btn.place(x=150,y=50)
add_std_btn['state']='disabled'

#####   SEARCH BUTTON #####
search_std_btn=Button(DataEntryFrame,text="2. SEARCH STUDENT",font=('arial',10,'bold'),width=20, relief=GROOVE, borderwidth=4, bg='black',fg='white',
                                    activebackground='red', activeforeground='black',height=2,command=search)
search_std_btn.place(x=150,y=120)
search_std_btn['state']='disabled'




#####    DELETEBUTTON #####
delete_std_btn=Button(DataEntryFrame,text="3. DELETE STUDENT",font=('arial',10,'bold'),width=20, relief=GROOVE, borderwidth=4, bg='black',fg='white',
                                    activebackground='red', activeforeground='black',height=2,command=delete)
delete_std_btn.place(x=150,y=190)
delete_std_btn['state']='disabled'


#####   UPDATE BUTTON #####
update_std_btn=Button(DataEntryFrame,text="4. UPDATE STUDENT",font=('arial',10,'bold'),width=20, relief=GROOVE, borderwidth=4, bg='black',fg='white',
                                    activebackground='red', activeforeground='black',height=2,command=update)
update_std_btn.place(x=150,y=260)
update_std_btn['state']='disabled'




#####  SHOW  ALL BUTTON #####
showall_std_btn=Button(DataEntryFrame,text="5. SHOW  ALL",font=('arial',10,'bold'),width=20, relief=GROOVE, borderwidth=4, bg='black',fg='white',
                                    activebackground='red', activeforeground='black',height=2,command=show)
showall_std_btn.place(x=150,y=330)
showall_std_btn['state']='disabled'




#####    EXPORT BUTTON #####
export_data_std_btn=Button(DataEntryFrame,text="6. EXPORT DATA",font=('arial',10,'bold'),width=20, relief=GROOVE, borderwidth=4, bg='black',fg='white',
                                    activebackground='red', activeforeground='black',height=2,command=export)
export_data_std_btn.place(x=150,y=400)
export_data_std_btn['state']='disabled'




#####  EXIT  BUTTON #####
exit_std_btn=Button(DataEntryFrame,text="7. EXIT",font=('arial',10,'bold'),width=20, relief=GROOVE, borderwidth=4, bg='black',fg='white',
                                    activebackground='red', activeforeground='black',height=2,command=exit)
exit_std_btn.place(x=150,y=470)






########################  FRAME 2  #####################33

DataShowFrame=Frame(root,bg='white',relief=GROOVE,borderwidth=5)

DataShowFrame.place(x=660,y=150,height=600 ,width=800)


#######--------------treeview--------------##########
style=ttk.Style()
style.configure('Treeview.Heading',font=('',13,'bold'))

style.configure('Treeview',font=('arial',10,'bold'),foreground='black',background='cyan')

scroll_x=Scrollbar(DataShowFrame,orient=HORIZONTAL)
scroll_y=Scrollbar(DataShowFrame,orient=VERTICAL)


student_table=Treeview(DataShowFrame,columns=('ID','NAME','EMAIL','ADDRESS','GENDER','DOB','MOBILE','DATE','TIME',),yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=student_table.xview)
scroll_y.config(command=student_table.yview)
student_table.pack(fill=BOTH,expand=1)

student_table.heading('ID',text='ID')
student_table.heading('NAME',text='NAME')
student_table.heading('EMAIL',text='EMAIL')
student_table.heading('ADDRESS',text='ADDRESS')
student_table.heading('GENDER',text='GENDER')
student_table.heading('DOB',text='DOB')
student_table.heading('MOBILE',text='MOBILE')
student_table.heading('DATE',text='DATE')
student_table.heading('TIME',text='TIME')
student_table['show']='headings'

student_table.column('ID',width=200)
student_table.column('NAME',width=200)
student_table.column('EMAIL',width=200)
student_table.column('ADDRESS',width=200)
student_table.column('GENDER',width=200)
student_table.column('DOB',width=200)
student_table.column('MOBILE',width=200)
student_table.column('DATE',width=200)
student_table.column('TIME',width=200)


#######################   SLIDER ###################
a='Welcome to students management system'
slider_label=Label(root, text=a,font=('chiller',30,'italic bold'),bg='black',relief=GROOVE,borderwidth=4)
slider_label.place(x=400,y=0,width=650)
count=0
text=''
animation_intro()
animation_with_color()


############### TIME AND DATE LABEL    ####################
time_and_date=Label(root ,font=('times',14,'bold'),relief=RIDGE ,borderwidth=4, bg='lightslateblue')
time_and_date.place(x=0 ,y=0,width=200,height=60)
clock()

root.mainloop()


