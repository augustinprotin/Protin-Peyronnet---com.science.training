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
    #Choix = 0 -> passage de l'année ?
    #Choix = 1 -> Prediction Moyenne générale ?
    #Choix = 2 -> /

    data=data_brut

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
        data["Moyenne_annuelle"] = (data["G1"]+data["G2"]+data["G3"])/3
        data["passe l'annee"] = (data["Moyenne_annuelle"]/20).round().astype(int)
        data.drop(columns=["Moyenne_annuelle", "G1", "G2", "G3"],inplace=True)
        data.to_csv("données_transformées.csv", index=False, sep=";", encoding="utf-8")
        return data
    
    if (choix == 1):
        data["Moyenne_annuelle"] = (data["G1"]+data["G2"]+data["G3"])/3
        data.drop(columns=["G1", "G2", "G3"],inplace=True)
        data.to_csv("données_transformées.csv", index=False, sep=";", encoding="utf-8")
        return data

    if (choix == 2):
        data["Moyenne_annuelle"] = (data["G1"]+data["G2"]+data["G3"])/3
        data["passe l'annee"] = (data["Moyenne_annuelle"]/20).round().astype(int)
        data.to_csv("données_transformées.csv", index=False, sep=";", encoding="utf-8")
        return data


def traitement_inverse(data_brut, choix=0):
    data=data_brut

    # Remplacement des données vers du numerique
    data["school"] = data["school"].replace(0, "GP")
    data["school"] = data["school"].replace(1, "MS")

    data["sex"] = data["sex"].replace(0, "F")
    data["sex"] = data["sex"].replace(1, "M")

    data["address"] = data["address"].replace(0,"U")
    data["address"] = data["address"].replace(1,"R")

    data["famsize"] = data["famsize"].replace(0,"GT3")
    data["famsize"] = data["famsize"].replace(1,"LE3")

    data["Pstatus"] = data["Pstatus"].replace(0,"T")
    data["Pstatus"] = data["Pstatus"].replace(1,"A") 

    data["Mjob"] = data["Mjob"].replace(0,"teacher")
    data["Mjob"] = data["Mjob"].replace(1,"health")
    data["Mjob"] = data["Mjob"].replace(2,"services")
    data["Mjob"] = data["Mjob"].replace(3,"at_home")
    data["Mjob"] = data["Mjob"].replace(4,"other")

    data["Fjob"] = data["Fjob"].replace(0,"teacher")
    data["Fjob"] = data["Fjob"].replace(1,"health")
    data["Fjob"] = data["Fjob"].replace(2,"services")
    data["Fjob"] = data["Fjob"].replace(3,"at_home")
    data["Fjob"] = data["Fjob"].replace(4,"other")

    data["reason"] = data["reason"].replace(0,"home")
    data["reason"] = data["reason"].replace(1,"reputation")
    data["reason"] = data["reason"].replace(2,"course")
    data["reason"] = data["reason"].replace(3,"other")

    data["guardian"] = data["guardian"].replace(0, "father")
    data["guardian"] = data["guardian"].replace(1, "mother")
    data["guardian"] = data["guardian"].replace(2, "other")

    data["schoolsup"] = data["schoolsup"].replace(0, "yes")
    data["schoolsup"] = data["schoolsup"].replace(1, "no")

    data["famsup"] = data["famsup"].replace(0, "yes")
    data["famsup"] = data["famsup"].replace(1, "no")

    data["paid"] = data["paid"].replace(0,"yes")
    data["paid"] = data["paid"].replace(1, "no")

    data["activities"] = data["activities"].replace(0,"yes")
    data["activities"] = data["activities"].replace(1, "no")

    data["nursery"] = data["nursery"].replace(0, "yes")
    data["nursery"] = data["nursery"].replace(1, "no")

    data["higher"] = data["higher"].replace(0, "yes")
    data["higher"] = data["higher"].replace(1, "no")

    data["internet"] = data["internet"].replace(0, "yes")
    data["internet"] = data["internet"].replace(1, "no")

    data["romantic"] = data["romantic"].replace(0, "yes")
    data["romantic"] = data["romantic"].replace(1, "no")

    data.to_csv("données_transformées_2.csv", index=False, sep=";", encoding="utf-8")
    print ("données traitées : ")
    print(data.head)


traitement_inverse(traitement_des_donnees(chargement_des_donnes("Data/student-por.csv")))