import tkinter as tk
from tkinter import PhotoImage
from tkinter import *
import time
import random
import json

root = Tk()
root.iconbitmap("wwm.ico")
root.geometry("1600x800")
root.title("Wer wird Millionär Quiz")
modus_auswahl_image = PhotoImage(file="modusauswahl.png")
game_bg = PhotoImage(file="gamebg.png")
default_bg = PhotoImage(file="backgroundimage.png")
gewonnen_bg = PhotoImage(file="gewonnen.png")
verloren_bg = PhotoImage(file="verloren.png")
verloren_safe_bg = PhotoImage(file="verlorensafe.png")

konto = 0
frage = 1
joker1 = False
joker2 = False
saveMoney = False
verloren = False
konto_array = [100, 200, 300, 500, 1000]
antwort1_btn = Button()
antwort2_btn = Button()
antwort3_btn = Button()
antwort4_btn = Button()
joker1_btn = Button()
joker2_btn = Button()
questions = []

def load_frage():
    global questions
    fri = random.randint(1, 6)
    file_path = 'questions' + str(fri) + '.txt'

    with open(file_path, 'r', encoding='utf-8') as file:
        
        file_content = file.read()

    questions = json.loads(file_content)


def build_modus():
    
    load_frage()
    
    for widget in root.grid_slaves():
        widget.grid_forget()
    
    tk.Label(root, image=modus_auswahl_image).place(relwidth=1, relheight=1) 
    btn1 = Button(root, text="Zocker", width=15, height= 2, command=lambda: Click("Zocker"), bg="#3f0961", fg="white", bd=2, relief=tk.SOLID, font=("Helvetica", 16, "bold"))
    btn2 = Button(root, text="Sicherheit", width=15, height= 2, command=lambda: Click("Sicherheit"), bg="#3f0961", fg="white", bd=2, relief=tk.SOLID, font=("Helvetica", 16, "bold"))
    btn1.grid(row=1, column=0, padx=290, pady=320)
    btn2.grid(row=1, column=1, padx=320, pady=320)        

def Click(modus):
    global joker1
    global joker2
    global saveMoney 
    global konto
    global frage
    global verloren
     
    if modus == "Zocker":
        joker1 = True
        joker2 = True
        saveMoney = False
        
    if modus == "Sicherheit":
        joker1 = True
        joker2 = False
        saveMoney = True

    konto = 0
    frage = 1
    verloren = False
    widget_clear()
    root.update_idletasks()
    root.after(800, build_game)

def widget_clear():
    global frage
    global verloren
    global saveMoney
    restart_btn = Button(root, text="Neustarten", width=60, height=3, command=lambda: (restart_btn.configure(state="disable"),  root.after(800, build_modus)), bg="#3f0961", fg="white", bd=2, relief=tk.SOLID, font=("Helvetica", 12, "bold"))

    for widget in root.winfo_children():
        widget.destroy()

    if verloren == True:
        if (saveMoney == True) and (frage > 3):
            tk.Label(root, image=verloren_safe_bg).place(relwidth=1, relheight=1)
            restart_btn = Button(root, text="Neustarten", width=60, height=3, command=lambda: (restart_btn.configure(state="disable"),  root.after(800, build_modus)), bg="#3f0961", fg="white", bd=2, relief=tk.SOLID, font=("Helvetica", 12, "bold"))
            restart_btn.grid(row=1, column=0,sticky="s", pady=450, padx=470)
        else:
            tk.Label(root, image=verloren_bg).place(relwidth=1, relheight=1)
            restart_btn = Button(root, text="Neustarten", width=60, height=3, command=lambda: (restart_btn.configure(state="disable"),  root.after(800, build_modus)), bg="#3f0961", fg="white", bd=2, relief=tk.SOLID, font=("Helvetica", 12, "bold"))
            restart_btn.grid(row=1, column=0, sticky="s", pady=450, padx=470)

    elif frage == 5:
        tk.Label(root, image=gewonnen_bg).place(relwidth=1, relheight=1)
        restart_btn = Button(root, text="Neustarten", width=60, height=3, command=lambda: (restart_btn.configure(state="disable"),  root.after(800, build_modus)), bg="#3f0961", fg="white", bd=2, relief=tk.SOLID, font=("Helvetica", 12, "bold"))
        restart_btn.grid(row=1, column=0, sticky="s", pady=450, padx=470)

    else:
        tk.Label(root, image=default_bg).place(relwidth=1, relheight=1)

def build_game():
    tk.Label(root, image=game_bg).place(relwidth=1, relheight=1)
    
    root.update_idletasks()
    time.sleep(0.5)

    kontostand = "Kontostand: " + str(konto) + " €"
    konto_lb = Label(root, text=kontostand, width=15, height=3, bg="#3f0961", fg="white", bd=2, relief=tk.SOLID, font=("Helvetica", 12, "bold"), padx=3)
    konto_lb.grid(row=0, column=0, pady=(42,0), sticky="w", padx=(60,9))

    joker1_btn = Button(root, text="Joker 1 einsetzen", width=15, height=3, bg="#3f0961", fg="white", bd=2, relief=tk.SOLID, font=("Helvetica", 12, "bold"), command=lambda: (Joker(1), joker1_btn.config(state="disabled"), joker2_btn.config(state="disabled")))
    joker1_btn.grid(row=2, column=0, sticky="w", padx=(60, 0))
    if joker1 == False:
        joker1_btn.configure(state="disabled")

    joker2_btn = Button(root, text="Joker 2 einsetzen", width=15, height=3, bg="#3f0961", fg="white", bd=2, relief=tk.SOLID, font=("Helvetica", 12, "bold"), command=lambda: (Joker(2), joker1_btn.config(state="disabled"), joker2_btn.config(state="disabled")))
    joker2_btn.grid(row=2, column=0, sticky="w", padx=(225, 0))
    if joker2 == False:
        joker2_btn.configure(state="disabled")


    frage1 = "100 €"
    frage1_lb = Label(root, text=frage1, width=23, height=3, fg="white", bd=2, relief=tk.SOLID, font=("Helvetica", 12, "bold"))
    frage1_lb.grid(row=4, column=4, sticky="e", pady=5)
    if frage == 1:
        frage1_lb.configure(bg="orange")
    else:
        frage1_lb.configure(bg="green", fg="black")

    frage2 = "200 €"
    frage2_lb = Label(root, text=frage2, width=23, height=3, fg="black", bd=2, relief=tk.SOLID, font=("Helvetica", 12, "bold"))
    frage2_lb.grid(row=3, column=4, sticky="e", pady=5)
    if frage == 2:
        frage2_lb.configure(bg="orange")
    elif frage > 2:
        frage2_lb.configure(bg="green")
    else:
        frage2_lb.configure(bg="#3f0961", fg="white")

    frage3 = "300 €"
    frage3_lb = Label(root, text=frage3, width=23, height=3, fg="black", bd=2, relief=tk.SOLID, font=("Helvetica", 12, "bold"))
    frage3_lb.grid(row=2, column=4, sticky="e", pady=5)
    if frage == 3:
        frage3_lb.configure(bg="orange")
    elif frage > 3:
        frage3_lb.configure(bg="green")
    else:
        frage3_lb.configure(bg="#3f0961", fg="white")

    frage4 = "500 €"
    frage4_lb = Label(root, text=frage4, width=23, height=3, fg="black", bd=2, relief=tk.SOLID, font=("Helvetica", 12, "bold"))
    frage4_lb.grid(row=1, column=4, sticky="e", pady=(0,4))
    if frage == 4:
        frage4_lb.configure(bg="orange")
    elif frage > 4:
        frage4_lb.configure(bg="green")
    else:
        frage4_lb.configure(bg="#3f0961", fg="white")

    frage5 = "1000 €"
    frage5_lb = Label(root, text=frage5, width=23, height=3, fg="black", bd=2, relief=tk.SOLID, font=("Helvetica", 12, "bold"))
    frage5_lb.grid(row=0, column=4, sticky="e", pady=(40,9))
    if frage == 5:
        frage5_lb.configure(bg="orange")
    else:
        frage5_lb.configure(bg="#3f0961", fg="white")

    build_frage(frage)

def build_frage(frage):
    global antwort1_btn
    global antwort2_btn
    global antwort3_btn
    global antwort4_btn
    global questions

    question_data = questions[frage-1]
    options = question_data["options"]
    original_array = [0, 1, 2, 3]
    shuffled_array = random.sample(original_array, len(original_array))

    fragestellung = question_data["question"]
    fragestellung_lb = Label(root, text=fragestellung, width=140, height=3, bg="#3f0961", fg="white", bd=2, relief=tk.SOLID, font=("Helvetica", 12, "bold"))
    fragestellung_lb.grid(row=5, column=0, columnspan=5, padx=(90, 0), pady=(130, 10))
    
    antwort1 = "A: " + options[shuffled_array[0]]
    antwort1_btn = Button(root, text=antwort1, width=60, height=3, command=lambda: check_antwort(options[shuffled_array[0]],question_data["correct_answer"], antwort1_btn), bg="#3f0961", fg="white", bd=2, relief=tk.SOLID, font=("Helvetica", 12, "bold"))
    antwort1_btn.grid(row=6, column=0, columnspan=2,padx=(90, 0), sticky="w", pady=3)

    antwort2 = "B: " + options[shuffled_array[1]]
    antwort2_btn = Button(root, text=antwort2, width=60, height=3, command=lambda: check_antwort(options[shuffled_array[1]],question_data["correct_answer"], antwort2_btn), bg="#3f0961", fg="white", bd=2, relief=tk.SOLID, font=("Helvetica", 12, "bold"))
    antwort2_btn.grid(row=6, column=2, columnspan=4, sticky="e", pady=3)

    antwort3= "C: " + options[shuffled_array[2]]
    antwort3_btn = Button(root, text=antwort3, width=60, height=3, command=lambda: check_antwort(options[shuffled_array[2]],question_data["correct_answer"], antwort3_btn), bg="#3f0961", fg="white", bd=2, relief=tk.SOLID, font=("Helvetica", 12, "bold"))
    antwort3_btn.grid(row=7, column=0, columnspan=2,padx=(90, 0), sticky="w", pady=3)

    antwort4 = "D: " + options[shuffled_array[3]]
    antwort4_btn = Button(root, text=antwort4, width=60, height=3, command=lambda: check_antwort(options[shuffled_array[3]],question_data["correct_answer"], antwort4_btn), bg="#3f0961", fg="white", bd=2, relief=tk.SOLID, font=("Helvetica", 12, "bold"))
    antwort4_btn.grid(row=7, column=2, columnspan=4, sticky="e", pady=3)

def check_antwort(antwort, richtige_antwort, btn):
    global konto_array
    global konto
    global frage
    global saveMoney
    global antwort1_btn
    global antwort2_btn
    global antwort3_btn
    global antwort4_btn

    btn.configure(bg="orange")
    root.update_idletasks()
    time.sleep(1)
    
    if antwort == richtige_antwort:
        konto = konto_array[frage-1]
        btn.configure(bg="green")
        root.update_idletasks()
        time.sleep(0.3)
        btn.configure(bg="orange")
        root.update_idletasks()
        time.sleep(0.3)
        btn.configure(bg="green")
        root.update_idletasks()
        time.sleep(0.3)
        btn.configure(bg="orange")
        root.update_idletasks()
        time.sleep(0.3)
        btn.configure(bg="green")
        root.update_idletasks()
        time.sleep(0.8)

        if frage < 5:
            frage += 1
            build_game()
        elif frage == 5:
            widget_clear()

    else:
        global verloren
        verloren = True
        btn.configure(bg="red")
        root.update_idletasks()
        time.sleep(0.8)

        try:
            a1 = antwort1_btn.cget("text").split(": ")[1]
        except IndexError:
            a1 = ""
        try:
            a2 = antwort2_btn.cget("text").split(": ")[1]
        except IndexError:
            a2 = ""
        try:
            a3 = antwort3_btn.cget("text").split(": ")[1]
        except IndexError:
            a3 = ""
        try:
            a4 = antwort4_btn.cget("text").split(": ")[1]
        except IndexError:
            a4 = ""


        if a1 == richtige_antwort:
            antwort1_btn.configure(bg="green")
            root.update_idletasks()
            time.sleep(0.3)
            antwort1_btn.configure(bg="#3f0961")
            root.update_idletasks()
            time.sleep(0.3)
            antwort1_btn.configure(bg="green")
            root.update_idletasks()
            time.sleep(0.3)
            antwort1_btn.configure(bg="#3f0961")
            root.update_idletasks()
            time.sleep(0.3)
            antwort1_btn.configure(bg="green")
        if a2 == richtige_antwort:
            antwort2_btn.configure(bg="green")
            root.update_idletasks()
            time.sleep(0.3)
            antwort2_btn.configure(bg="#3f0961")
            root.update_idletasks()
            time.sleep(0.3)
            antwort2_btn.configure(bg="green")
            root.update_idletasks()
            time.sleep(0.3)
            antwort2_btn.configure(bg="#3f0961")
            root.update_idletasks()
            time.sleep(0.3)
            antwort2_btn.configure(bg="green")
        if a3 == richtige_antwort:
            antwort3_btn.configure(bg="green")
            root.update_idletasks()
            time.sleep(0.3)
            antwort3_btn.configure(bg="#3f0961")
            root.update_idletasks()
            time.sleep(0.3)
            antwort3_btn.configure(bg="green")
            root.update_idletasks()
            time.sleep(0.3)
            antwort3_btn.configure(bg="#3f0961")
            root.update_idletasks()
            time.sleep(0.3)
            antwort3_btn.configure(bg="green")
        if a4 == richtige_antwort:
            antwort4_btn.configure(bg="green")
            root.update_idletasks()
            time.sleep(0.3)
            antwort4_btn.configure(bg="#3f0961")
            root.update_idletasks()
            time.sleep(0.3)
            antwort4_btn.configure(bg="green")
            root.update_idletasks()
            time.sleep(0.3)
            antwort4_btn.configure(bg="#3f0961")
            root.update_idletasks()
            time.sleep(0.3)
            antwort4_btn.configure(bg="green")

        root.update_idletasks()
        time.sleep(0.8)
        widget_clear()

def Joker(i):
    global joker1
    global joker2
    global antwort1_btn
    global antwort2_btn
    global antwort3_btn
    global antwort4_btn
    global frage
    global questions
    global joker1_btn
    global joker2_btn

    question_data = questions[frage-1]
    richtige_antwort = question_data["correct_answer"]

    if i == 1:

        r = int


        if antwort1_btn.cget("text").split(": ")[1] == richtige_antwort:
            r = 1

        if antwort2_btn.cget("text").split(": ")[1] == richtige_antwort:
            r = 2

        if antwort3_btn.cget("text").split(": ")[1] == richtige_antwort:
            r = 3

        if antwort4_btn.cget("text").split(": ")[1] == richtige_antwort:
            r = 4

        while True:
            j = random.randint(1, 4)
            if j != r:
                break

        if j == 1:
            antwort1_btn.config(text="", state="disabled")
        if j == 2:
            antwort2_btn.config(text="", state="disabled")
        if j == 3:
            antwort3_btn.config(text="", state="disabled")
        if j == 4:
            antwort4_btn.config(text="", state="disabled")

        joker1 = False
        
    elif i == 2:

        r = int


        if antwort1_btn.cget("text").split(": ")[1] == richtige_antwort:
            r = 1

        if antwort2_btn.cget("text").split(": ")[1] == richtige_antwort:
            r = 2

        if antwort3_btn.cget("text").split(": ")[1] == richtige_antwort:
            r = 3

        if antwort4_btn.cget("text").split(": ")[1] == richtige_antwort:
            r = 4

        while True:
            j1 = random.randint(1, 4)
            if j1 != r:
                break

        while True:
            j2 = random.randint(1, 4)
            if (j2 != r) and (j1 != j2):
                break

        if (j1 == 1) or (j2 ==1):
            antwort1_btn.config(text="", state="disabled")
        if (j1 == 2) or (j2 ==2):
            antwort2_btn.config(text="", state="disabled")
        if (j1 == 3) or (j2 ==3):
            antwort3_btn.config(text="", state="disabled")
        if (j1 == 4) or (j2 ==4):
            antwort4_btn.config(text="", state="disabled")

        joker2 = False
        

    #else:
     #   print("Error")
   
build_modus()
root.mainloop()