from flask import session
import time

def pdfgen(PDF):
	gmt = time.localtime()
	jour = str(gmt.tm_mday) # récupere le jour
	mois = str(gmt.tm_mon) # récupère le mois
	annee = str(gmt.tm_year)
	date = jour + '/'+ mois + '/' + annee

	data ={
	    	"nom": "nom_client",
		    "prenom": "prenom_client",
		    "tel": "tel",
		    "email": "email",
		    "rue": "adresse_client",
		    "code_postal": "code_postal",
		    "date_entree": "date_debut_formation",
		    "duree_formation": "",
		    "date_sortie": "date_fin_formation",
		    "date_exam": "date_exam",
		    "prix": "prix_formation",
		    "financement": "financement",
		    "solde_cpf": "somme_mobilise",
		    "reste_a_payer": "reste_a_payer",
		    "accompte": "accompte",
		    "ristourne": "ristourne",
		    "mot_de_pass": "mot_de_pass",
		    "prenom_formateur":"Patrick",
		    "nom_formateur": "Binam",
		    'date':date,
		    'horaires': "",
			
		}

	if session['user_data']:

		user = session['user_data']
		
		if int(user['prix']) <= int(user['solde_cpf']):
			user['solde_cpf'] = user['prix']
			user['reste_a_payer'] = '0'

		if int(user['prix']) > int(user['solde_cpf']):
			user['reste_a_payer'] = int(user['prix']) - int(user['solde_cpf'])

		if user['cours_de_jour'] == 'oui':
			data['horaires'] ='9h30 à 17h30'
			data['duree_formation'] = '70'

		elif user['cours_du_soir'] == 'oui':
			data['horaires'] == '18h à 22h'
			data['duree_formation'] = '54'
	
		
		with open('pdf_generator/contrat_pro.txt', 'r', encoding='latin-1') as file:
			txt = file.read()

		#txt = txt.format(prenom_client, nom_client,adresse)
		#print(txt.format(nom_client=nom_client, prenom_client=prenom_client, adresse=adresse))

		pdf = PDF(orientation='P', format='A4')

		# nouvelle page
		# dimension d'une page A4 largeur = 210mm, Longueur = 297mm
		# pour ajouter des éléments sur la page on utilise des coordonnées (x,y)

		pdf_w = 210
		pdf_h = 297
		pdf.add_page()
		pdf.set_auto_page_break(auto=True, margin=25)
		pdf.img()
		pdf.titles()

		txt_lines = [n for n in txt.split('\n') if n !='\n' ]
		for line in txt_lines:
			if 'Article' in line:
				pdf.sub_titles(line)
			else:
				try:
					pdf.paraf(line.format(nom_client=user['nom'].upper(),
					 prenom_client = user['prenom'],
					 adresse_client_rue = user['rue'],
					 code_postal = user['code_postal'],
					 accompte = user['accompte'] ,
					 nom_formateur = data['nom_formateur'],
					 prenom_formateur = data['prenom_formateur'],
					 somme_mobilise = user['solde_cpf'],
					 mode_financement = user['financement'],
					 prix_formation = user['prix'],
					 somme_fi_perso = user['reste_a_payer'],
					 date_signature = data['date'],
					 date_debut_formation = user['date_entree'],
					 date_fin_formation = user['date_sortie'],
					 horaire_formation = data['horaires'],
					 duree_formation = data['duree_formation']

					   ))
				except:
					pdf.paraf(line)


		name_file = user['nom']+'_pdf_contrat.pdf'
		# pour enregistrer ou générer le fichier
		pdf.output('static/gen_contract/'+name_file, 'F')
