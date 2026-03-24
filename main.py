import pandas as pd
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

def main():
    return 0

def chargement_des_donnes (nom_fichier_csv):
    data=pd.read_csv(nom_fichier_csv, sep=",", encoding="utf8")
    print ("données chargées : ")
    print(data.head)
    return data

def traitement_des_donnees(data_brut, choix=0):
    data=data_brut
    # Ajout de la moyenne annuelle + est ce qu'il passe l'année
    data["Moyenne_annuelle"] = (data["G1"]+data["G2"]+data["G3"])/3
    data["passe l'annee"] = (data["Moyenne_annuelle"]/20).round().astype(int)

    # Remplacement des données vers du numerique

    data["school"] = data["school"].replace("GP", 0)
    data["school"] = data["school"].replace("MS", 1)

    data["sex"] = data["sex"].replace("F", 0)
    data["sex"] = data["sex"].replace("M", 1)

    data["address"] = data["address"].replace("U", 0)
    data["address"] = data["address"].replace("R", 1)

    data["famsize"] = data["famsize"].replace("GT3", 0)
    data["famsize"] = data["famsize"].replace("LE3", 1)

    data["Pstatus"] = data["Pstatus"].replace("T", 0)
    data["Pstatus"] = data["Pstatus"].replace("A", 1) 

    data["Mjob"] = data["Mjob"].replace("teacher", 0)
    data["Mjob"] = data["Mjob"].replace("health", 1)
    data["Mjob"] = data["Mjob"].replace("services", 2)
    data["Mjob"] = data["Mjob"].replace("at_home", 3)
    data["Mjob"] = data["Mjob"].replace("other", 4)

    data["Fjob"] = data["Fjob"].replace("teacher", 0)
    data["Fjob"] = data["Fjob"].replace("health", 1)
    data["Fjob"] = data["Fjob"].replace("services", 2)
    data["Fjob"] = data["Fjob"].replace("at_home", 3)
    data["Fjob"] = data["Fjob"].replace("other", 4)

    data["reason"] = data["reason"].replace("home", 0)
    data["reason"] = data["reason"].replace("reputation", 1)
    data["reason"] = data["reason"].replace("course", 2)
    data["reason"] = data["reason"].replace("other", 3)

    data["guardian"] = data["guardian"].replace("father", 0)
    data["guardian"] = data["guardian"].replace("mother", 1)
    data["guardian"] = data["guardian"].replace("other", 2)

    data["schoolsup"] = data["schoolsup"].replace("yes", 0)
    data["schoolsup"] = data["schoolsup"].replace("no", 1)

    data["famsup"] = data["famsup"].replace("yes", 0)
    data["famsup"] = data["famsup"].replace("no", 1)

    data["paid"] = data["paid"].replace("yes", 0)
    data["paid"] = data["paid"].replace("no", 1)

    data["activities"] = data["activities"].replace("yes", 0)
    data["activities"] = data["activities"].replace("no", 1)

    data["nursery"] = data["nursery"].replace("yes", 0)
    data["nursery"] = data["nursery"].replace("no", 1)

    data["higher"] = data["higher"].replace("yes", 0)
    data["higher"] = data["higher"].replace("no", 1)

    data["internet"] = data["internet"].replace("yes", 0)
    data["internet"] = data["internet"].replace("no", 1)

    data["romantic"] = data["romantic"].replace("yes", 0)
    data["romantic"] = data["romantic"].replace("no", 1)

    data["G1"] = data["G1"].astype(int)
    data["G1"] = data["G1"].astype(int)

    data["G2"] = data["G2"].astype(int)
    data["G2"] = data["G2"].astype(int)

    data["G3"] = data["G3"].astype(int)
    data["G3"] = data["G3"].astype(int)

    data.to_csv("données_transformées.csv", index=False, sep=";", encoding="utf-8")
    print ("données traitées : ")
    print(data.head)
    if (choix == 0):
        return data



traitement_des_donnees(chargement_des_donnes("Data/student-por.csv"))

