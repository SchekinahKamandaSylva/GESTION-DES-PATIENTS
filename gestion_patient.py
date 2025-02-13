from subprocess import call
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import mysql.connector
import  os

def ajouter():
    matricule = entrematricule.get()
    nom = entrenom.get()
    prenom = entreprenom.get()
    age = entreage.get()
    adresse = entreadresse.get()
    telephonne = entretelephone.get()
    remarque = entreremarque.get()

    if matricule == "" or nom == "" or prenom == "" or remarque == "" or age == "" or adresse == "":
        messagebox.showerror("ERREUR", "Veuiller remplir toutes les cases")
    else:
        conn = mysql.connector.connect(host="localhost", user="root", password="", database="gestion_patient")
        cursor = conn.cursor()

    try:
        sql = 'INSERT INTO patient (code, nom, prenom, age, adresse, telephone, remarque)  VALUES(%s,%s, %s, %s, %s, %s, %s)'
        val = (matricule, nom, prenom, age, adresse, telephonne, remarque)
        cursor.execute(sql, val)
        conn.commit()
        dernierMatricule = cursor.lastrowid
        messagebox.showinfo("information", "patient ajouter")
        root.destroy()
        call(["python", "gestion_patient.py"])

    except Exception as e:
        print(e)
        # retour
        conn.rollback()
        conn.close()
        afficher()


def mofifier():
    matricule = entrematricule.get()
    nom = entrenom.get()
    prenom = entreprenom.get()
    age = entreage.get()
    adresse = entreadresse.get()
    telephonne = entretelephone.get()
    remarque = entreremarque.get()

    conn = mysql.connector.Connect(host='localhost', user='root', password="", database='gestion_patient')
    cursor = conn.cursor()

    try:
        sql = "update patient SET  nom=%s,where code= %s"
        val = (nom, matricule)
        cursor.execute(sql, val)
        conn.commit()
        derniereMatricule = cursor.lastrowid
        messagebox.showinfo("information", "patient modifier")
        root.destroy()
        call(["python", "gestion_patient.py"])


    except Exception as e:
        print(e)
        # retour
        conn.rollback()
        conn.close()




def afficher ():
    conn = mysql.connector.connect(host="localhost", user="root", password="", database="gestion_patient")
    cursor = conn.cursor()
    cursor.execute("select * from patient")
    result = cursor.fetchall()
    for row in result:
        table.insert('', END, value=row)
    cursor.close()
    conn.close()




def supprimer():
    reponse = messagebox.askyesno("Suprresion", "Vous le vous vraiment supprimer?")
    if reponse:
        selected_item = table.selection()  # Récupérer l’élément sélectionné dans le Treeview
        if selected_item:
             # Récupérer les données de l’élément sélectionné
            item_data = table.item(selected_item)['values']
            data_id = item_data[0]  # Supposons que l’identifiant se trouve à la première position

            # Supprimer l’élément de la base de données
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="", database="gestion_patient")
                cursor = conn.cursor()

                # Exécutez la requête pour supprimer l’élément de la base de données
                cursor.execute("DELETE FROM patient WHERE id = % s ", entrematricule.get())
                conn.commit()
                cursor.close()
            except mysql.connector.Error as error:
                messagebox.showerror("information", "patient supprimer")
            finally:
                if conn.is_connected():
                    conn.close()
                    # Supprimer l’élément du Treeview
                    table.delete(selected_item)

                else:
                    messagebox.showerror(" Aucun élément sélectionné ")



root= Tk()
root.title("GESTION DE PATIENTS")
root.geometry("1700x900+0+0")
root.configure(background="gray")

lbltitre = Label(root,bd=5, relief= RIDGE, text="GESTION DES PATIENTS HOPITAL SHEKINAH", font=("arial black",30),bg="black",fg="white")
lbltitre.place(x=0,y=0,width=1365)

frmegauche = Frame(root, bd=4, relief=RIDGE, bg="black")
frmegauche.place(x=0, y=90,  width=450,height=600)

frametable =Frame(root, bd=4, relief=RIDGE, bg="cyan")
frametable.place(x=480, y=90,  width=875,height=600)

lblmatricule= Label(frmegauche, text="INFORMATION SUR LE PATIENT", font=("arial",16, 'bold'),bg="cyan", fg="black",)
lblmatricule.pack(side=TOP, fill=X)


lblmatricule= Label(frmegauche, text="MATRICULE", font=("arial",16),bg="black", fg="white",)
lblmatricule.place(x=0, y=100,width=200)
entrematricule=Entry(frmegauche,font=("arial",16))
entrematricule.place(x=200, y=100,width=200,height=30)

lblnom=Label(frmegauche,text="NOM",font=("arial",16),bg="black", fg="white")
lblnom.place(x=0,y=150,width=200)

entrenom=Entry(frmegauche,font=("arial",16))
entrenom.place(x=200,y=150,width=200,height=30)

lblprenom=Label(frmegauche,text="PRENOM",font=("arial",16),bg="black", fg="white")
lblprenom.place(x=0,y=200,width=200)

entreprenom=Entry(frmegauche,font=("arial",16))
entreprenom.place(x=200,y=200,width=200,height=30)

lblage=Label(frmegauche,text="AGE",font=("arial",16),bg="black", fg="white")
lblage.place(x=0,y=250,width=200)
entreage=Entry(frmegauche,font=("arial",16))
entreage.place(x=200,y=250,width=200,height=30)

lbladresse=Label(frmegauche,text="ADRESSE",font=("arial",16),bg="black", fg="white")
lbladresse.place(x=0,y=300,width=200)

entreadresse=Entry(frmegauche,font=("arial",16))
entreadresse.place(x=200,y=300,width=200,height=30)


lbltelephone=Label(frmegauche,text="TELEPHONE",font=("arial",16),bg="black", fg="white")
lbltelephone.place(x=0,y=350,width=200)

entretelephone=Entry(frmegauche,font=("arial",16))
entretelephone.place(x=200,y=350,width=200,height=30)

lblremarque=Label(frmegauche,text="REMARQUE",font=("arial",16),bg="black", fg="white")
lblremarque.place(x=0,y=400,width=200)

entreremarque=Entry(frmegauche,font=("arial",16))
entreremarque.place(x=200,y=400,width=200,height=30)

#LES BOUTONS DE COMMANDE
btnenregistre = Button(frametable, text="Enregistrer", font=("arial",16),bg="green",fg="white",command=ajouter)
btnenregistre.place(x=20, y=540,width=200)

btnmodifier = Button(frametable, text="Modifier", font=("arial",16),bg="blue",fg="white", command=mofifier)
btnmodifier.place(x=300, y=540,width=200)

btnsuprime =Button(frametable, text="Supprimer", font=("arial",16),bg="red",fg="white",command=supprimer)
btnsuprime.place(x=550, y=540,width=200)

table= ttk.Treeview(frametable,columns = (1,2,3,4,5,6,7,8),height=5,show="headings")
table.place(x=10,y=5,width=850,height=530)

table.heading(1,text="ID")
table.heading(2,text="CODE")
table.heading(3,text="NOM")
table.heading(4,text="PRENOM")
table.heading(5,text="AGE")
table.heading(6,text="ADRESSE")
table.heading(7,text="TELEPHONE")
table.heading(8,text="REMARQUE")

table.column(1,width=100)
table.column(2,width=100)
table.column(3,width=100)
table.column(4,width=100)
table.column(5,width=100)
table.column(6,width=100)
table.column(7,width=100)
table.column(8,width=100)

conn= mysql.connector.Connect(host='localhost', user='root', password="", database='gestion_patient')
cursor= conn.cursor()
cursor.execute("select * from patient ")
result = cursor.fetchall()
for row in result:
    table.insert('', END, value=row)
cursor.close()
conn.close()




root.mainloop()
