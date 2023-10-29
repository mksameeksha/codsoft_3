from tkinter import *
from random import randint

root=Tk()
root.title("Password Generator")
root.geometry("500x300")

def new_rand():
    pw_entry.delete(0,END)
    pw_length=int(my_entry.get())
    my_password=''
    for x in range(pw_length):
        my_password += chr(randint(33,126))
    pw_entry.insert(0, my_password)



def clipper():
    root.clipboard_clear()
    root.clipboard_append(pw_entry.get())

lf=LabelFrame(root, text="Enter the desired password length")
lf.pack(pady=20)

my_entry= Entry(lf,font=("Helvetica",20),relief="flat",bg="#DADDB1")
my_entry.pack(pady=20,padx=20)

pw_entry=Entry(root,text="",font=("Helvica",20), bd=0,relief="flat",bg="#DADDB1")
pw_entry.pack(pady=20)

my_frame=Frame(root)
my_frame.pack(pady=20)
my_button=Button(my_frame,text="Generate Password",command=new_rand,bg="#B3A492")
my_button.grid(row=0,column=0,padx=10)

clip_button=Button(my_frame,text="Copy to Clipboard",command=clipper,bg="#B3A492")
clip_button.grid(row=0,column=5,padx=10)

root.mainloop()
