import csv
import tkinter as tk
from tkinter import ttk
from colorama import Fore, Style, init

init()

class ProfilMetalic:
    def __init__(self,nume):
        self.nume = nume
        self.latime = int(nume[3:5])
        self.lungime = int(nume[6:])
    def suprafata_vopsita(self):
        return self.latime * self.lungime * 6

class Flansa:
    def __init__(self, lungime, latime, grosime, suprafata_decupata, numar_fete_vopsite):
        self.lungime = lungime
        self.latime = latime
        self.grosime = grosime
        self.suprafata_decupata = suprafata_decupata
        self.numar_fete_vopsite = numar_fete_vopsite
    def suprafata_vopsita(self):
        return (self.lungime * self.latime * self.numar_fete_vopsite) - self.suprafata_decupata
    
class ElementSingular:
    def __init__(self, suprafata_vopsita_per_bucata):
        self.suprafata_vopsita_per_bucata = suprafata_vopsita_per_bucata
    def suprafata_vopsita(self):
        return self.suprafata_vopsita_per_bucata

class PozitieSecundara:
    def __init__(self, nume):
        self.nume = nume
        self.elemente = []
    def adauga_element(self, element):
        self.elemente.append(element)
    def calculeaza_suprafata_vopsita(self):
        total_suprafata_vopsita = 0
        for element in self.elemente:
            total_suprafata_vopsita += element.suprafata_vopsita()
        return total_suprafata_vopsita

class PozitiePrincipala:
    def __init__(self, nume):
        self.nume = nume
        self.pozitii_secundare = []
    def adauga_pozitie_secundara(self, pozitie):
        self.pozitii_secundare.append(pozitie)
    def calculeaza_suprafata_vopsita(self):
        total_suprafata_vopsita = 0
        for pozitie in self.pozitii_secundare:
            total_suprafata_vopsita += pozitie.calculeaza_suprafata_vopsita()
        return total_suprafata_vopsita

class Plansa:
    def __init__(self, nume):
        self.nume = nume
        self.pozitii_principale = []
    def adauga_pozitie_principala(self, pozitie):
        self.pozitii_principale.append(pozitie)
    def calculeaza_suprafata_vopsita(self):
        total_suprafata_vopsita = 0
        for pozitie in self.pozitii_principale:
            total_suprafata_vopsita += pozitie.calculeaza_suprafata_vopsita()
        return total_suprafata_vopsita
    
class Obiect:
    def __init__(self, nume):
        self.nume = nume
        self.planse = []
    def adauga_plansa(self, plansa):
        self.planse.append(plansa)
    def calculeaza_suprafata_vopsita(self):
        total_suprafata_vopsita = 0
        for plansa in self.planse:
            total_suprafata_vopsita += plansa.calculeaza_suprafata_vopsita()
        return total_suprafata_vopsita

class Proiect:
    def __init__(self, nume):
        self.nume = nume
        self.obiecte = []
    def adauga_obiect(self, obiect):
        self.obiecte.append(obiect)
    def calculeaza_suprafata_vopsita(self):
        total_suprafata_vopsita = 0
        for obiect in self.obiecte:
            total_suprafata_vopsita += obiect.calculeaza_suprafata_vopsita()
        return total_suprafata_vopsita
    def printeaza_in_csv(self, nume_fisier):
        with open(nume_fisier, "a", newline="\n") as fisier_csv:
            scriitor_csv = csv.writer(fisier_csv)
            scriitor_csv.writerow(["Entitate","Nume","Suprafata vopsita[mp]"])
            for obiect in self.obiecte:
                for plansa in obiect.planse:
                    for pozitie_principala in plansa.pozitii_principale:
                        for pozitie_secundara in pozitie_principala.pozitii_secundare:
                            scriitor_csv.writerow(["Pozitie secundara", pozitie_secundara.nume, pozitie_secundara.calculeaza_suprafata_vopsita()])
                        scriitor_csv.writerow(["Pozitie principala", pozitie_principala.nume, pozitie_principala.calculeaza_suprafata_vopsita()])
                    scriitor_csv.writerow(["Plansa", plansa.nume, plansa.calculeaza_suprafata_vopsita()])
                scriitor_csv.writerow(["Obiect", obiect.nume, obiect.calculeaza_suprafata_vopsita()])
            scriitor_csv.writerow(["Proiect", self.nume, self.calculeaza_suprafata_vopsita()])

def citeste_proiect():
    nume_proiect = input("Introduceti numele proiectului: ")
    proiect = Proiect(nume_proiect)
    numar_obiecte = int(input(Fore.RED + "Introduceti numarul de obiecte: "))
    
    for _ in range(numar_obiecte):
        nume_obiect = input("->Numele obiectului: ")
        obiect = Obiect(nume_obiect)

        numar_planse = int(input(Style.RESET_ALL + Fore.BLACK + f"-->Numarul de planse pentru {nume_obiect}: "))
        for _ in range(numar_planse):
            nume_plansa = input("--->Numele plansei: ")
            plansa = Plansa(nume_plansa)

            numar_pozitii_principale = int(input(Style.RESET_ALL + Fore.BLUE + f"---->Numarul de pozitii principale pentru {nume_plansa}: "))
            for _ in range(numar_pozitii_principale):
                nume_pozitie_principala = input("----->Numele pozitiei principale: ")
                pozitie_principala = PozitiePrincipala(nume_pozitie_principala)

                numar_pozitii_secundare = int(input(Style.RESET_ALL + Fore.MAGENTA + f"------>Numărul de pozitii secundare pentru {nume_pozitie_principala}: "))
                for _ in range(numar_pozitii_secundare):
                    nume_pozitie_secundare = input("------->Numele pozitiei secundare: ")
                    pozitie_secundara = PozitieSecundara(nume_pozitie_secundare)

                    numar_elemente = int(input(Style.RESET_ALL + Fore.CYAN + f"-------->Numarul de elemente pentru {nume_pozitie_secundare}: " ))
                    for _ in range(numar_elemente):
                        tip_element = input("--------->Tip element (profil, flansa, singular): ").lower()
                        if tip_element == "profil":
                            nume_profil = input(Style.RESET_ALL + Fore.LIGHTGREEN_EX + "---------->Nume profil(ex. HEA10x100): ")
                            Style.RESET_ALL
                            pozitie_secundara.adauga_element(ProfilMetalic(nume_profil))
                        elif tip_element == "flansa":
                            lungime = int(input(Fore.YELLOW + "---------->Lungime[mm]: "))
                            latime = int(input("---------->Latime[mm]: "))
                            grosime = int(input("---------->Grosime[mm]: "))
                            suprafata_decupata = float(input("---------->Suprafata decupata[mp]: "))
                            numar_fete = int(input("---------->Numar fete vopsite: "))
                            Style.RESET_ALL
                            pozitie_secundara.adauga_element(Flansa(lungime, latime, grosime, suprafata_decupata, numar_fete))
                        elif tip_element == "singular":
                            suprafata = float(input(Fore.LIGHTBLUE_EX + "---------->Suprafata vopsita per bucata[mp]: "))
                            Style.RESET_ALL
                            pozitie_secundara.adauga_element(ElementSingular(suprafata))

                    pozitie_principala.adauga_pozitie_secundara(pozitie_secundara)
                plansa.adauga_pozitie_principala(pozitie_principala)
            obiect.adauga_plansa(plansa)
        proiect.adauga_obiect(obiect)
    return proiect


if __name__ == "__main__":
    proiect = citeste_proiect()
    Style.RESET_ALL
    print(Fore.WHITE + f"\nSuprafata vopsita la proiect: {proiect.calculeaza_suprafata_vopsita()} mp")
    fisier_csv = input("Introduceti numele fisierului CSV in care doriti sa salvati proiectul: ")
    proiect.printeaza_in_csv(fisier_csv)
    print(f"Proiectul a fost salvat cu succes in {fisier_csv}.")
    Style.RESET_ALL
