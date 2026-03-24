import pandas as pd


def main():
    return 0

def chargement_des_donnes (nom_fichier_csv):
    data=pd.read_csv(nom_fichier_csv, sep=",", encoding="utf8")
    print ("données chargées : ")
    print(data.head)


chargement_des_donnes("Data/student-por.csv")

