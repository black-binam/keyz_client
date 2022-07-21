import xlsxwriter
import json
import pandas as pd


#workbook = xlsxwriter.Workbook('les_inscrits.xlsx')
#feuille = workbook.add_worksheet()
#feuille.write('A1', data_j[0]['nom'])




#df = df[[ 'nom', 'prenom', 'date', 'email', 'cours_de_jour', 'cours_du_soir']]

#df.to_excel('examen_28_09_2021.xlsx')
#dt.to_excel('les_inscrits.xlsx')


class data_gen:
	"""
	Cette classe permet de génrer des fichier excel exploitable.
	on retrouve les méthode suivantes:
	- list_stagiaire 
	"""

	with open('data_file.txt','r') as file:
		data = file.read()

	data=data.replace('}', "}},")
	data = data.split('},')

	data_j = [eval(n) for n in data if len(n)>0]
	dt = pd.DataFrame(data_j)
	

	def __init__(self):

		pass


	def search_exam():
		date_exam = input('Indiquez une date d\'examen: ')
		df = data_gen.dt.loc[data_gen.dt['date_exam'].str.contains( date_exam ) ]	# filtre du fichier par date d'examen
		df = df[~df['etat_dossier'].str.contains( 'Annule', na = False ) & ~df['etat_dossier'].str.contains(  'Archive' , na = False) ]

		return (df, date_exam.replace('/', '_'))

	def list_stagiaire():
		""" Génère la liste des stagiaire par examen hors e-learning """

		date_exam = input('Indiquez une date d\'examen: ')
		df = data_gen.dt.loc[data_gen.dt['date_exam'].str.contains( date_exam ) ]	# filtre du fichier par date d'examen
		df = df[~df['etat_dossier'].str.contains( 'Annule', na = False ) & ~df['etat_dossier'].str.contains(  'Archive' , na = False) ]

		for index, row in df.iterrows():
			if row['cours_de_jour'] == 'non' and row['cours_du_soir'] == 'non' and row['elearning'] == 'oui':
				df = df.drop(index)

		print(df['date_exam'])
		df = df[[ 'nom', 'prenom', 'date', 'email', 'cours_de_jour', 'cours_du_soir', 'elearning']]

		lst_cds = list(df['cours_du_soir'])
		horaire = []

		for rep in lst_cds:
			if rep == "oui":
				horaire.append(('18h - 22h', '54h'))
			else:
				horaire.append(('9h30 - 17h', '70h'))

		df['Horaires'] = [n[0] for n in horaire]
		df['Duree'] = [n[1] for n in horaire]

		date_exam_chge = date_exam.replace('/','_')
		df.to_excel('examen_'+ date_exam_chge +'.xlsx')

		return df

	def exam_pratique():

		df =  data_gen.search_exam() # search_examen renvoie un tuple (tableau , date_exam)
		df_tab = df[0]

		theo_success = df_tab.loc[df_tab['etat_dossier'].str.contains('exam_theo_ok')]

		new_tab = theo_success[['prenom', 'nom', 'email', 'tel']]
		new_tab['date_exam'],  new_tab['lieu_exam'], new_tab['heure_passage'], new_tab['type_vehicule'] = "" , "", "", ""

		new_tab.to_excel('examen_pratique_'+df[1]+'.xlsx', index = False)
		

		return new_tab


