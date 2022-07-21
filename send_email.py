from flask import Flask
from flask_mail import Mail, Message
import os
import pandas as pd

app = Flask(__name__)

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": 'keyz.formation@gmail.com',
    "MAIL_PASSWORD": 'Bonif@ce91481'
}


data = open('data_file.txt', 'r').read()
data = data.replace('}', '}},')
data = data.replace('\n', '')
data = data.split('},')
del data[-1]

lst_data = []

for i in data:
  lst_data.append(eval(i))

date_exam = '29/06/2021'

df = pd.read_excel('examen_pratique_'+date_exam.replace('/','_')+'.xlsx')


"""
lst_data=[{'nom': 'Blanc', 'prenom': 'Chrisner',
 'tel': '0769004376',
  'email': 'keyz.formation@gmail.com',
  'rue': '30-36 rue GuÃ©roux Espace salvador allende',
   'code_postal': '93380 Pierrefitte-sur-seine', 'submit': 'valider',
    'cours_de_jour': 'oui', 'cours_du_soir': 'non', 'elearning': 'oui',
     'date_entree': '31/08/2020', 'date': '11/08/2020', 'date_sortie': '2020-07-31',
      'financement': 'cpf', 'accompte': '0', 'ristourne': '0', 'check_box': 'y'
      , 'mot_de_pass': 'KeyzBlanc0', 'solde_cpf': '792', 'fr_cma_paye': 'oui',
       'reste_a_payer': '230', 'doc_upload': 'oui'}]
"""
class send_mail:

 
  def __init__(self):
    pass

  def convoc_theo_msg (email,prenom, nom, duree, date_formation, horaire):

    msg = Message(subject="Convocation Formation VTC",
                          sender=app.config.get("MAIL_USERNAME"),
                          recipients=[email], # replace with your email for testing

                          body="".join((f"Bonjour Mr/Mme {prenom} {nom}, \n\n",
                           "Afin d’encourager la professionnalisation, nous avons décidé\n", "de vous permettre d’accéder à ",
                           "la formation de Voiture de Transport avec Chauffeur. \nCelle-ci vous permettra de mieux ",
                           "appréhender l’examen VTC.\n\n",
                           "Vous trouverez ci-après tous les détails relatifs à cette formation.\n",
                           "Veuillez-vous munir d’un cahier de 100 pages, un stylo de couleur.\n\n",
                           "Lieu de la formation: 43 Rue du commandant Rolland, 93350 Le Bourget\n",
                           f"\tDurée:{duree}\n",
                           f"\tDate: {date_formation}\n",
                           f"\tHoraire: {horaire}\n\n",

                           "Patrick\n",
                           "Responsable Keyz Formation"
                            ))

                          )


    date_fr = "05/10/2020"
    date_ang = "2020-10-05"
    for client_dict in lst_data:
      if client_dict['cours_de_jour'] == 'oui' and (client_dict['date'] == date_fr or client_dict['date'] == date_ang):
        heure = 'de 9h15 à 17h'
        duree ="70h"

        msg = message(client_dict['email'], client_dict['prenom'], client_dict['nom'],
          duree, client_dict['date'], heure)

        mail.send(msg)

      elif client_dict['cours_du_soir'] == 'oui' and (client_dict['date'] == date_fr or client_dict['date'] == date_ang):
        duree = "54h"
        heure = 'de 18h à 22h'
        msg = message(client_dict['email'], client_dict['prenom'], client_dict['nom'],
          duree, client_dict['date'], heure)
        mail.send(msg)

    return msg



  def convoc_pratique_msg (email,prenom, nom):
    
    duree = '1h30'
    date_formation = '28/08/2021'
    

    msg = Message (subject = 'Convocation Formation Pratique', sender = app.config.get('MAIL_USERNAME'), recipients = [email], body= "".join((f"Bonjour Mr/Mme {prenom} {nom}, \n\n ",
                        "Vous avez reussi vontre examen Théorique VTC, à présent \n\n",
                        "l'examen Pratique se met au travers de votre chemin.\n\n",
                        f"Ainsi, je vous invite le {date_formation} à {horaire} \n\n",
                        f"pour une durée de {duree} de formation pratique.", 
                        "Je vous invite à vous munir d'un stylo.\n\n\n Bien cordialement,\n Patrick\n Tel: 0614842316 \n keyz.formation@gmail.com" )))

    return msg



app.config.update(mail_settings)
mail = Mail(app)

if __name__ == '__main__':
    with app.app_context():
      horaires = ['12h00', '14h']
      emails = list(df['email'])
      for index, candidat in enumerate(list(df['nom'])):
        email = emails[index]
        if index > len(list(df['nom']))//2:
          horaire = horaires[1]
          msg = send_mail.convoc_pratique_msg(list(df['email'])[index], list(df['prenom'])[index], list(df['nom'])[index])

          #msg = message(list(df['email'])[index], list(df['prenom'])[index], list(df['nom'])[index], duree, date_formation, horaire[1] )
          mail.send(msg)

        else:
          horaire = horaires[0]
          msg = send_mail.convoc_pratique_msg(list(df['email'])[index], list(df['prenom'])[index], list(df['nom'])[index])
          #msg = message(list(df['email'])[index], list(df['prenom'])[index], list(df['nom'])[index], duree, date_formation, horaire[0] )
          mail.send(msg)
      

     

