#!/usr/bin/python3

# A python Password Manager
# Developed by Elieroc
# Start of project : 19/10/2020
# Actual version : 1.0

# Modules locaux
from generator import generator
from crypter import *

# Modules externes
from prettytable import PrettyTable
import sys
import time
import csv

# Déclaration des variables globales
csv_file = "passwords_table.csv"
master_key = "trololo43"
tab_format = PrettyTable(["ID", "Application", "Mot de passe", "Date de modification"])

def create_app_table():
    id = get_new_id()
    application = str(input("Pour quel site/application voulez-vous définir un mot de passe :\n"))
    type_pasword_choice = str(input("Voulez-vous générer un nouveau mot de passe ou saisir le votre ? (a/m) "))
    if type_pasword_choice == "m":
        new_password = str(input("Saisissez votre mot de passe :\n"))
    else :
        lengt = int(input("Longueur de votre mot de passe (32 recommandé) : "))
        new_password = generator(lengt)
    creation_date = time.strftime("%H:%M:%S", time.localtime())
    table = [id, application, new_password, creation_date]
    return table

def get_new_id():
    # On tchec si le fichier existe, si non, l'id est 0, et si oui, l'id est égal au nb de tables du fichier + 1
    try:
        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            id = 0
            for row in reader:
                id+=1
            return id
    except:
        id = 0
        return id

def read_total_csv():
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        # On définit un tableau double dimension (chaque ligne va contenir une application avec son mot de passe)
        table = []
        for row in reader:
            table.append(row)
        # Maintenant que le tableau python est prêt, on le met au propre avec prettytable
        for row_2 in table:
            tab_format.add_row(row_2)
        return tab_format

def write_table_csv(table):
    with open(csv_file, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(table)

def main():
    

    print("----------------------GestioPy (CLI version)----------------------")
    new_table_for_app = create_app_table()
    write_table_csv(new_table_for_app)
    total_csv = read_total_csv()
    print(total_csv)
    
if __name__ == "__main__":
    main()
