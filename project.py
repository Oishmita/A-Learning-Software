from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import mysql.connector
root = Tk()
root.title("Cryptography Hub")
root.iconbitmap("E:\Python_Project_tkinter\page_icon.ico")
root.geometry("2000x800")


#function for getting the inputs
def getinput():
    global user
    global userid
    user=username_entry.get()
    userid=id_entry.get()
    checkdb(user,userid)

#Creating a new popup window
def popup_window():
    top2=Toplevel()
    top2.title("Cryptography Hub")
    top2.geometry("600x200")
    top2.iconbitmap("E:\Python_Project_tkinter\page_icon.ico")

    #show user id function
    def showid():
        global idLabel
        idLabel=Label(top2, text=newid, font=("Helvetica",16,"bold"))
        idLabel.pack()

    #reregister function
    def reregister():
        top2.destroy()
        signup_window()

    #frame7 for holding popup buttons
    frame7=LabelFrame(top2)
    frame7.pack()
    
    #Displaying the new user id button
    b5=Button(frame7, text="SHOW USER ID", padx=20, pady=5, fg="burlywood1", bg="DodgerBlue3", command=showid)
    b5.grid(row=0, column=0, padx=10, pady=10)

    #register again
    b6=Button(frame7, text="REGISTER AGAIN", padx=20, pady=5, fg="burlywood1", bg="DodgerBlue3", command=reregister)
    b6.grid(row=0, column=1, padx=10, pady=10)
    

#Creating new window for new user credentials
def signup_window():
    top1=Toplevel()
    top1.title("Cryptography Hub")
    top1.geometry("800x300")
    top1.iconbitmap("E:\Python_Project_tkinter\page_icon.ico")

    
    
    #function for new user sign up
    def signup():
        global newUser, newid
        #global dob
        newUser=newUser_entry.get()
        #dob=dob_entry.get()
        newid=enterdb(newUser)

        if(
            messagebox.showinfo("Registered", "Your data has been successfully saved. You can now login from the main page.\nClick on 'SHOW USER ID' button to get your ID.\nClick on 'REGISTER AGAIN' for another registration")
        ):
            top1.destroy()
            popup_window()



    #function to access database for newUser
    def enterdb(newUser):
        mydb=mysql.connector.connect(host="localhost",user="Oishmita",passwd="skcusevol!", database="usercredentials")
        myCursor=mydb.cursor()
        myCursor.execute("select UserID from details")
        for i in myCursor:
            newid = i[0]
        newid=newid+1
        myCursor.execute("""
        insert into details (UserID, UserName) values (%s,%s)
        """,(newid,newUser))
        mydb.commit()
        mydb.close()
        return newid




    #signup frame
    signup_frame=Label(top1, bg="DarkSeaGreen2")
    signup_frame.pack(padx=20, pady=40)

    #entry boxes for signup
    newUser_label=Label(signup_frame, text="Username", padx=0, pady=0, fg="Black", font=("Helvetica",10,"bold"), bg="DarkSeaGreen2")
    newUser_entry=Entry(signup_frame, width=50, borderwidth=3)
    newUser_entry.insert(0,"Full Name")
    #dob_label=Label(signup_frame, text="User ID", padx=0, pady=0, fg="Black", font=("Helvetica",10,"bold"), bg="SlateGray3")
    #dob_entry=Entry(signup_frame, width=50, borderwidth=3)
    #dob_entry.insert(0,"DD-MM-YYYY")

    #placing the entry boxes in grid
    newUser_label.grid(row=1, column=0)
    newUser_entry.grid(row=1, column=1, padx=10, pady=10, columnspan=2)
    #dob_label.grid(row=2, column=0)
    #dob_entry.grid(row=2, column=1, padx=10, pady=10, columnspan=2)

    #frame to hold the confirm button
    frame6=LabelFrame(top1)
    frame6.pack(padx=20, pady=40)

    #confirm button
    b4=Button(frame6, text="CONFIRM", padx=20, pady=5, fg="burlywood1", bg="DodgerBlue3", command=signup)
    b4.pack()


#connecting with the existing database
def checkdb(un,unid):
    f=0
    mydb=mysql.connector.connect(host="localhost",user="Oishmita",passwd="skcusevol!", database="usercredentials")
    myCursor=mydb.cursor()
    myCursor.execute("select * from details")
    for i in myCursor:
        if(i[0]==int(unid)):
            f=1
            NewWindow()
            break
    if(f!=1):
        AccessDenied()

#Creating new window- info1
def NewWindow():
    top=Toplevel()
    top.title("Cryptography Hub")
    top.geometry("2000x800")
    top.iconbitmap("E:\Python_Project_tkinter\page_icon.ico")

    #introduction
    intro_frame=Label(top, text="Welcome "+str(user)+"!", font=("times",20,"italic","bold"))
    intro_frame.pack(padx=20, pady=10)


    #1st text
    info_frame = Label(top, text="""
    Cryptography refers almost exclusively to encryption, the process of converting ordinary information (plaintext) into unintelligible gibberish (i.e., ciphertext).\nDecryption is the reverse, moving from unintelligible ciphertext to plaintext.

    A cipher (or cypher) is a pair of algorithms which creates the encryption and the reversing decryption.\nThe detailed operation of a cipher is controlled both by the algorithm and in each instance, by a key.\nThis is a secret parameter (ideally, known only to the communicants) for a specific message exchange context.

    This site aims to provide a practical approach to cryptography.\nWe attempt to provide javascript examples and detailed diagrams where possible, in order to make the learning process much smoother.
    What is there to know?""",
    padx=1000,bg="black", fg="snow", relief=RAISED,borderwidth=3, font=("Times",13,"bold"))
    info_frame.pack(pady=5)

    #2nd text
    info_frame2 = Label(top, text="""
    Ciphers

    Understand the fine details of a wide range of cryptographic ciphers.\nFind information on block ciphers, symmetric ciphers, public key encryption and many more.
    Cryptanalysis

    Discover how often under public scrutiny, holes are poked and cracks begin to form, in algorithms which were once considered secure.""",
    padx=1000,bg="chocolate3", fg="snow", relief=SUNKEN,borderwidth=3, font=("Times",15,"bold"))
    info_frame2.pack(pady=5)
    
#function for access denial
def AccessDenied():
    messagebox.showerror("Access Denied", "Your access has been denied since this UserID is not registered. Please check again to continue.\nOr click 'sign up' to get a new ID")


#frame to hold the main page heading
frame0=LabelFrame(root)
frame0.pack()

#top label
myLabel = Label(frame0,text="WELCOME TO CRYPTOGRAPHY HUB!",padx=120,pady=20,bg="black",fg="white",relief="raised",borderwidth=3, font=("Times",20,"bold"))
myLabel.pack()

#my_img=ImageTk.PhotoImage(Image.open("cover.jpg"))
#myLabel=Label(root,image=my_img, text="CRYPTOGRAPHY HUB", compound="bottom", font=("Times",26,"bold"), padx=1000, pady=50)
#myLabel.pack()

#frame to hold the introduction
frame2=LabelFrame(root, padx=5)
frame2.pack()

#Frame to hold the login and sign up boxes
frame1=LabelFrame(root, padx=10, pady=10, bg="SlateGray3")
frame1.pack(pady=50)

#frame to hold the login button
frame3=LabelFrame(root, padx=10, pady=10, bg="SlateGray3")
frame3.pack()

#frame to hold the exit button
frame4=LabelFrame(root)
frame4.pack(side=RIGHT)

#frame to hold the new user sign up box
frame5=LabelFrame(root)
frame5.pack(side=LEFT)

#Introduction
intro=Label(frame2, text="""
Meet Cryptography....
\nA branch of both mathematics and computer science, cryptography is the study and practice of obscuring information.
\nIllustration of simple encryption.""",font=("Helvetica",16,"bold"))
intro2=Label(frame2, text="plaintext=SECRET \nencrypted=ESRCTE""",font=("Times", 20, "bold"),fg="coral3")

intro.pack()
intro2.pack()


#Entry boxes for credentials
username_label=Label(frame1, text="Username", padx=0, pady=0, fg="Black", font=("Helvetica",10,"bold"), bg="SlateGray3")
username_entry=Entry(frame1, width=50, borderwidth=3)
id_label=Label(frame1, text="User ID", padx=0, pady=0, fg="Black", font=("Helvetica",10,"bold"), bg="SlateGray3")
id_entry=Entry(frame1, width=50, borderwidth=3)


#Placing the Credential Labels in grid
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, padx=10, pady=10, columnspan=2)
id_label.grid(row=2, column=0)
id_entry.grid(row=2, column=1, padx=10, pady=10, columnspan=2)

#Login Button
photo=PhotoImage(file="E:\Python_Project_tkinter\key.png")
img=photo.subsample(10,10)
b=Button(frame3, image=img, command=getinput)
button_label=Label(frame3, text="Click below to login", fg="Black", font=("Helvetica",10,"bold"), bg="SlateGray3")
button_label.pack()
b.pack()

#Exit button
b2=Button(frame4, text="EXIT", padx=10,pady=5, fg="snow", bg="firebrick3", font=(20), command=root.destroy)
b2.pack(side=RIGHT)

#New user Sign up
b3=Button(frame5, text="SIGN UP", padx=50, pady=5, fg="burlywood1", bg="DodgerBlue3", command=signup_window)
b3.pack(side=LEFT)

root.mainloop()