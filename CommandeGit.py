# fichier pour les commandes git

import os
import subprocess
import sys
import re
import time
import shutil
import json
import requests

# Fonction pour lancer une commande git
def commandeGit(commande):
    try:
        # On lance la commande git
        process = subprocess.Popen(commande, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # On récupère le résultat de la commande
        result = process.communicate()
        # On retourne le résultat
        return result
    except Exception as e:
        # On retourne l'erreur
        return e
    
# Fonction pour cloner un dépôt
def cloneDepot(url, nomDepot):
    try:
        # On clone le dépôt
        result = commandeGit("git clone " + url + " " + nomDepot)
        # On retourne le résultat
        return result
    except Exception as e:
        # On retourne l'erreur
        return e
    
# Fonction pour récupérer les informations d'un dépôt
def infoDepot(nomDepot):
    try:
        # On récupère les informations du dépôt
        result = commandeGit("git --git-dir=" + nomDepot + "/.git log --pretty=format:\"%H %an %ae %ad %s\"")
        # On retourne le résultat
        return result
    except Exception as e:
        # On retourne l'erreur
        return e
    
    