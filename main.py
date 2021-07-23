#!/usr/bin/python3

# A python Password Manager
# Developed by Elieroc
# Start of project : 19/10/2020
# Actual version : 1.2

# Modules locaux
from generator import generator
from crypter import *
from banner import banner

# Modules externes
from prettytable import PrettyTable
import getpass
import argparse
import sys
import time
import csv

def arg_manager():
    parser = argparse.ArgumentParser()

    # Arg NEW
    parser.add_argument(
        "--new",
        help="Créer une nouvelle entrée dans la table",
        nargs=2,
        metavar=('[APP NAME]', '<[OWN_PASSWORD]|[auto:LENGT]>')
    )

    # Arg SEARCH
    parser.add_argument(
        "--search",
        help="Recherche d'élément dans la table",
        nargs=2,
        metavar=('[SEARCH TYPE]', '<[ID]|[APP]>')
    )

    # Arg ALL
    parser.add_argument(
        "-A", "--all",
        help="Affiche l'intégralité de la table", 
        action="store_true"
    )

    # Arg SHOW-PASSWORD
    parser.add_argument(
        "-sp", "--show-password", 
        help="Active l'affichage des mots de passe lors d'une recherche",
        action="store_true"
    )
    
    args = parser.parse_args()

    if args.new:

        success_message = "L'ajout du compte dans la table est une véritable réussite !"

        if args.new[1].split(":")[0] == "auto" :
            new_password = generator(int(args.new[1].split(":")[1]))
            new_table_for_app = create_app_table(args.new[0], new_password)
            write_table_csv(new_table_for_app)
            print(success_message)
        else:
            new_table_for_app = create_app_table(args.new[0], args.new[1])
            write_table_csv(new_table_for_app)
            print(success_message)

    if args.search:
        result = search_element_in_table(args.search[0], args.search[1])
        print(result)
    if args.all:
        # Si option --show-password active
        if args.show_password:
            clear_table = read_total_csv(True)
            print(clear_table)
        else:
            blurred_table = read_total_csv(False)
            print(blurred_table)
    else:
        try:
            # On regarde si un argument existe
            arg_exist = sys.argv[1]
        except:
            print("Merci de consulter la page d'aide grâce aux arguments --help ou -h")

def search_element_in_table(search_type, element):

    no_result = "\n[-] Aucun résultat pour votre recherche"

    # Recherche par ID
    if search_type.lower() == "id":
        total_table = read_total_csv(True)
        print(f"[+] Résultat pour l'id {element} :")
        try:
            result = total_table[int(element)]
            return result
        except:
            return no_result

    # Recherche par nom d'application
    elif search_type.lower() == "app":
        total_table = read_total_csv(True, False)
        print(f"[+] Résultat pour l'application {element} :")

        i=0
        for application in total_table:
            if total_table[i][1].lower() == element.lower():
                tab_format.add_row(total_table[i])
                return tab_format
            else:
                i+=1
        # Si aucun résultat alors on renvoie un message <<d'erreur>>
        return no_result

    else:
        error_message = """
        Usage : -s [SEARCH TYPE] <[ID]|[APP]>
        Exemples : -s id 6
                   -s app Signal
        """
        return error_message

def create_app_table(app_name, password):
    id = get_new_id()
    creation_date = time.strftime("%H:%M:%S", time.localtime())
    table = [id, app_name, password, creation_date]
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

def read_total_csv(show_password=False, pretty=True):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)

        """
        On définit un tableau double dimension 
        (chaque ligne va contenir une application avec son mot de passe)
        """

        table = []
        for row in reader:
            table.append(row)

        """ 
        Dans le cas où l'utilisateur ne veut pas afficher le mot de passe (par défaut), 
        on remplace chaque mot de passe de la table par des étoiles
        """

        if show_password == False:
            i = 0
            for row in table:
                table[i][2] = "********"
                i+=1

        # Maintenant que le tableau python est prêt, on le met au propre avec prettytable
        if pretty == True:
            for row_2 in table:
                tab_format.add_row(row_2)
            return tab_format
        elif pretty == False:
            return table

def write_table_csv(table):
    with open(csv_file, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(table)

def init():

    # Déclaration des variables globales
    global csv_file, master_key, tab_format
    csv_file = "passwords_table.csv"
    master_key = "trololo43"
    tab_format = PrettyTable(["ID", "Application", "Mot de passe", "Date de modification"])

    banner()
    arg_manager()

def main():
    

    init()
    #new_table_for_app = create_app_table()
    #write_table_csv(new_table_for_app)
    #total_csv = read_total_csv()
    #print(total_csv)
    
if __name__ == "__main__":
    main()
