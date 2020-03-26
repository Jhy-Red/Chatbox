#! /usr/bin/python3

# Import 
import re
from datetime import datetime
from textblob import TextBlob
import pandas as pd

 
#Caractéristique ChatBot
project = 'Iris'
prénom = 'Arsene Lapin'
health = 'Pourrais allez mieux' #TODO Should be variable
health1 = 'Je vais bien :)'
health2 = 'ca va ... :/'
born = datetime(2020,3,26,16,30,00)
age = date = datetime.now() - born
chanson = "Three day Grace - Never too late"
localisation = "Sur ton ordinateur"
occupation = "I.A de niveau 1"

# Message d'attente
user_waiting_reponse = "Réponse :"

#Bot phrase
Welcome = """Bienvenu, Bienvenu sur le projet {project}. 
    Que puis-je pour vous ? : """.format(project = project)

# Discussion - Question # TODO critères if ? in text_user = research in Question
q_age = r"age|ages"
q_prenom = r"prénom|prenom|t'appelles"
q_naissance = r"née|naissance|quand es tu"
q_health = r"comment vas tu|ca va ?"
q_musique = r"musique"
q_localisation = r"ou|localisation"
q_occupation = r"que fais tu|occupation"

# Break Words
goodbye = 'Aurvoir','Ciao','Hasta la vista','A+',"++",'Bye'

# Discussion - Réponse
msg = 'La réponse est 42'
msg_q_age = 'Je suis agés de {jours} jours, mais pour êtré précis : {age}' .format(jours = age.days, age=age)
msg_q_prenom = "Je m'apelle {Prénom}" .format(Prénom=prénom)
msg_q_naissance = "Je suis née le {jour}/{mois}/{année}" .format(jour=born.day, mois = born.month, année = born.year)
msg_q_musique = "Ma musique préféré est {Musique}" .format(Musique = chanson)
msg_q_health = health
msg_q_localisation = localisation
msg_q_occupation = "Je suis une {occupation}".format(occupation=occupation)

# Discussion - Cloture

exit_word = r'quitter|quit|aurvoir|ciao|hasta la vista|bye|exit'
Iris_msg_exit = 'Merci pour cette discussion, {Bye}'.format(Bye=goodbye[0])
stop_word = " "

#Bot Lancement
def iris():
    flag = True
    print(Welcome)
    pos = lambda x: TextBlob(x).sentiment.polarity
    sub = lambda x: TextBlob(x).sentiment.subjectivity


    while (flag == True):
        text_user = input(user_waiting_reponse).lower()
        analyse =  TextBlob(text_user).sentiment.polarity + TextBlob(text_user).sentiment.subjectivity 

        if (re.search(exit_word, text_user)) :
            print(Iris_msg_exit)
            flag = False

        elif (re.search(q_age, text_user)) :
            print(msg_q_age)

        elif (re.search(q_prenom, text_user))  :
            print(msg_q_prenom)

        elif (re.search(q_naissance, text_user))  :
            print(msg_q_naissance)

        elif (re.search(q_health, text_user)) :
            if analyse > 1 :
                print(health1)
            elif analyse < 0 :
                print(health2)
            else:
                print(msg_q_health)
        
        elif (re.search(q_localisation, text_user)):
            print(msg_q_localisation)
        
        elif (re.search(q_occupation, text_user)) :
            print(msg_q_occupation)
        
        elif (re.search(q_musique, text_user)) :
            print(msg_q_musique)
        
        else:
            print(msg)
iris()