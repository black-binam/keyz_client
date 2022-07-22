import profile
from flask import Flask, request, session, make_response, flash,render_template, url_for, redirect, jsonify
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, RadioField, DateField, SelectField
from wtforms.validators import DataRequired, Email
from wtforms.fields.html5 import EmailField
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from time import sleep
import json
from wtforms.widgets import Input
#from fpdf import FPDF
from pdf_generator.pdf_generation import PDF  
from pdf_generator.function import pdfgen
import os
from functions import *




app = Flask(__name__)
app.config['SECRET_KEY'] = "moimeme"

def evalbox(num, mot_pass, confirm_mot_pass):
	driver = webdriver.Chrome()
	driver.get('https://depot.evalbox.com/#!/register')
	sleep(0.5)
	identifiant = driver.find_element_by_xpath("//input[@name='login']")
	identifiant.clear()
	identifiant.send_keys(num)
	sleep(0.5)
	mp = driver.find_element_by_xpath("//input[@name='password']")
	mp.clear()
	mp.send_keys(mot_pass)
	sleep(0.5)
	confirm_mp = driver.find_element_by_xpath("//input[@name='confirmPassword']")
	confirm_mp.clear()
	confirm_mp.send_keys(confirm_mot_pass)
	sleep(2)
	btn_enregistrer = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/form/button')


class ButtonField(BooleanField):
    widget = Input(input_type='button')


class id_client_test(FlaskForm):
	nom = StringField('Nom', validators = [DataRequired()])
	prenom = StringField('Prenom', validators = [DataRequired()])
	tel = StringField('Telephone', validators = [DataRequired()])
	#email = EmailField('Email', validators = [DataRequired()])
	#rue = StringField('rue', validators = [DataRequired()])
	#code_postal = StringField('code_postal', validators = [DataRequired()])
	submit = SubmitField('valider')
	button = ButtonField()


class id_client(FlaskForm):
	nom = StringField('Nom', validators = [DataRequired()])
	prenom = StringField('Prenom', validators = [DataRequired()])
	tel = StringField('Telephone', validators = [DataRequired()])
	email = EmailField('Email', validators = [DataRequired()])
	rue = StringField('rue', validators = [DataRequired()])
	code_postal = StringField('code_postal', validators = [DataRequired()])
	date_exam = SelectField( choices = [('selectionnez', 'selectionnez'),('27/09/2022', '27/09/2022'),('28/06/2022', '28/06/2022'),('26/04/2022', '26/04/2022'),('24/02/2022', '24/02/2022') , ('25/01/2022', '25/01/2022'), ('30/06/2020', '30/06/2020'), ('28/07/2020', '28/07/2020') ,('29/09/2020', '29/09/2020'), ('27/10/2020', '27/10/2020'),
	 ('24/11/2020', '24/11/2020'), ('26/01/2021', '26/01/2021'), ('23/02/2021', '23/02/2021'), ('27/04/2021', '27/04/2021'), 
	 ('29/06/2021', '29/06/2021'), ('28/09/2021', '28/09/2021'), ('26/10/2021', '26/10/2021'), ('30/11/2021', '30/11/2021')], validators = [DataRequired()]) 
	
	submit = SubmitField('valider')
	button = ButtonField()

	


class choix_forma(FlaskForm):
	check_box = BooleanField(id = 'oui',default = None,  validators = [DataRequired()])
	radio = RadioField('radio_name',choices = [('oui','oui')], validators = [DataRequired()])
	date = DateField(format='%d-%m-%Y', validators = [DataRequired()])
	financement = SelectField(choices = [('selectionnez', 'selectionnez'),('CPF', 'CPF'), ('Financement personnel', 'Personnel'), ('pole_emploi', 'Pole Emploie')], validators = [DataRequired()])
	accompte = StringField('accompte', validators = [DataRequired()])
	ristourne = StringField('ristourne', validators = [DataRequired()])
	prix = StringField('prix', validators = [DataRequired()])
	solde_cpf = StringField('solde_cpf', validators = [DataRequired()])
	reste_a_payer = StringField('reste_a_payer', validators = [DataRequired()])



class dossier(FlaskForm):
	radio = RadioField('radio_name',choices = [('oui','Oui'), ('non','Non')], validators = [DataRequired()])
	doc_up = RadioField('radio_name',choices = [('oui','Oui'), ('non','Non')], validators = [DataRequired()])
	fr_cma = RadioField('radio_name',choices = [('oui','Oui'), ('non','Non')], validators = [DataRequired()])
	fr_cma_pay = RadioField('radio_name',choices = [('client','Client'), ('keyzf','Le centre')], validators = [DataRequired()])
	etat_dossier = SelectField(choices = [('Tout_etat', 'Tout_etat'),('selectionnez', 'selectionnez'),('En cours', 'En cours'), ('Annule', 'Annulé'), ('Archive', 'Archivé'),
		('Formation terminée', 'Formation terminée'), ('Cma validé', 'Cma validé'), ('dossier cma créé', 'dossier cma créé'), 
		('Dos Cma incomplet', 'Dos Cma incomplet'), ('Cma payé', 'Cma payé') , ('exam_theo_ok', 'Theorie reussi') , ('exam_theo_non', 'Theorie échouée')
		, ('exam_pra_ok', 'Pratique reussi') , ('exam_pra_non', 'Pratique échouée')], validators = [DataRequired()])

class search(FlaskForm):
	nom_client = StringField('Chercher un candidat')
	submit_btn = SubmitField("reserch_btn")
	date_session = StringField('date_session', validators = [DataRequired()])


		
def open_base():
	data = open('data_file.txt', 'r').read()
	data = data.replace('}', '}},')
	data = data.replace('\n', '')
	data = data.split('},')
	del data[-1]
	lst_data = []

	for i in data:
		
		lst_data.append(eval(i))

	#on rajoute dans chaque dictionnaire la clef: 'etat_dossier'
	for i in lst_data:
		try:
			if i['date_exam'] :
				pass
		except KeyError:
			i.update({"date_exam":"selectionez"})

	return lst_data


@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def ac_client():
	recherche = search()
	client_form = id_client()
	choix_formation = choix_forma()
	info_dossier = dossier()
	data_profile_pic = open_json() # a list
	session['profile_pic'] = data_profile_pic[1]
	
	if request.method =='POST':
		session['user_data'] =  dict(request.form)

		pdfgen(PDF)


	
	if client_form.validate_on_submit():
		
		#rad1 = request.form['cours_de_jour']
		#entree = request.form['date_entree']
		#sortie = request.form['date_sortie']
		
		if request.method == 'POST':
			
			with open("data_file.txt", "a+") as write_file: #"data_file.txt"
				data =dict(request.form)
				del data['csrf_token']
				data['mot_de_pass'] = 'Keyz'+request.form['nom']+'0'
				
				json.dump(data, write_file, indent=4)

			evalbox(request.form['tel'], 'Keyz'+request.form['nom']+'0', 'Keyz'+request.form['nom']+'0')

			session['data'] = dict(request.form)
			return redirect(url_for('dossier_client'))
	

	return render_template('ac_client.html', client_form = client_form,id_client = client_form,
	 choix_formation = choix_formation, recherche = recherche, dossier = info_dossier, profile_pic = data_profile_pic[1])


@app.route('/dossier_client', methods=['GET', 'POST'])
def dossier_client():
	dossier_cli = dossier()

	if dossier_cli.validate_on_submit():
		session['data'].update(request.form)
		return session['data']
	
	return render_template('dossier_cma.html', dossier = dossier_cli)



@app.route('/contrat')
def contrat():
	try:
		user = session['user_data']['nom'].lower()
		#pdfkit.from_url("google.com", 'contrat.pdf', configuration = pdfkit_config)
		return render_template('contrat_formation.html', user = user + '_pdf_contrat.pdf')
	except:
		flash("Les chanps sont vides")

		return redirect('home')

@app.route('/erase_session')
def erase_session():
	session.pop('data', None)
	session['data'] = dict()


@app.route('/inscription_cma', methods=['POST', 'GET'])
def inscription_cma():
	evalbox(request.form['tel'], 'Keyz'+request.form['nom']+'0', 'Keyz'+request.form['nom']+'0')
	


	return redirect(url_for('ac_client'))


@app.route('/les_inscrits', methods = ['POST', 'GET'])
def les_inscrits():
	
	recherche = search()

	client = id_client()
	choix_formation = choix_forma()
	info_dossier = dossier()

	data = open('data_file.txt', 'r').read()
	data = data.replace('}', '}},')
	data = data.replace('\n', '')
	data = data.split('},')
	del data[-1]
	lst_data = []
	les_sessions = []
	
	session['lst_data'] = lst_data

	# rajout dans lst_data des donnees transformées en dictionnaire
	for i in data:
		lst_data.append(eval(i))
	#-----------------------------------------------


	#-----------------------------------------------
	#on rajoute dans chaque dictionnaire la clef: 'etat_dossier'
	for i in lst_data:
		try:
			if i['etat_dossier'] :
				pass
		except KeyError:
			i.update({"etat_dossier":"selectionnez"})


	#on rajoute dans chaque dictionnaire la clef: 'date_exam'
	for i in lst_data:
		try:
			if i['date_exam'] :
				pass
		except KeyError:
			i.update({"date_exam":"selectionnez"})
	#-----------------------------------------------


	#-----------------------------------------------
	#on récupère toutes les sessions existante
	for dico in lst_data:
		if dico['date'] not in les_sessions:
			les_sessions.append(dico['date'])

	#-----------------------------------------------


	if request.method=="POST":
		
		donnee = request.form

		# on récupère la date entrée dans le champ pour générer  
		# la liste des inscrits
		try:
			etat_dossier = donnee['etat_dossier']
			if 'date_session' in donnee:
				date_fr = donnee['date_session']
				split_date = date_fr.split('/')
				date_ang = split_date[-1]+"-"+split_date[1]+"-"+split_date[0]
				

				return render_template('les_inscrits.html', data_file = lst_data, id_client = client,
					choix_formation = choix_formation, dossier = info_dossier, les_sessions = les_sessions, recherche = recherche, 
					date_fr  = date_fr, date_ang  = date_ang, etat_dossier = etat_dossier)

			else:
				#------------------------------------------------
				for dico in lst_data:
					if donnee['tel']== dico['tel'] and donnee['date'] == dico['date_entree'] :

						
						donnee = dict(donnee)

						if "csrf_token" in donnee:
							del donnee['csrf_token']
						elif "submit" in donnee:
							del donnee['submit']
						dico.update(donnee)

				#-------------------------------------------------

				donnee_json = json.dumps(lst_data, indent=4)

				data_to_save = str()

				#-------------------------------------------------
				for dico in lst_data:
					json_dico = json.dumps(dico, indent = 4)
					data_to_save = data_to_save+json_dico
				#-------------------------------------------------

				with open('data_file.txt', 'w') as file:
					file.write(data_to_save)

				session.pop('lst_data', None)
				return redirect(url_for('les_inscrits'))

		except UnboundLocalError:
			date_ang= '2021-02-11'
			date_fr= '11/02/2021'

		

	
	return render_template('les_inscrits.html', data_file = lst_data, id_client = client,
		choix_formation = choix_formation, dossier = info_dossier, les_sessions = les_sessions, recherche = recherche,
		 date_ang = '2021-02-11', profile_pic = session.get('profile_pic'))



@app.route('/test_html', methods=['GET', 'POST'])
def test_html():
	
	form = id_client_test()
	
	if form.validate_on_submit():
		donnee = request.form
		
		return donnee
	
	return render_template('test.html', form = form)


@app.route('/layout', methods = ['GET', 'POST'])
def layout():
	recherche = search()
	client = id_client()
	choix_formation = choix_forma()
	info_dossier = dossier()

	
	if request.method == "POST":

		lst_data = open_base()
		data = request.form
		nom_client = data['nom_client'].lower()
		lst_client = [dico for dico in lst_data if nom_client in dico['nom'].lower() ]

		data = open('data_file.txt', 'r').read()
		data = data.replace('}', '}},')
		data = data.replace('\n', '')
		data = data.split('},')
		del data[-1]
		lst_data = [eval(n) for n in data]

		

		return render_template('info_par_client.html',id_client = client,
		choix_formation = choix_formation, dossier = info_dossier, recherche = recherche, lst_client = lst_client)




	return render_template('layout.html', recherche = recherche, dossier = info_dossier, id_client = client)


@app.route('/home_layout', methods=['GET'])
def home_layout():

	recherche = search()
	client = id_client()
	choix_formation = choix_forma()
	info_dossier = dossier()

	return render_template('home_layout.html', id_client = client,
		choix_formation = choix_formation, dossier = info_dossier, recherche = recherche )

@app.route('/search_forms', methods=['GET'])
def search_forms():

	recherche = search()
	client = id_client()
	choix_formation = choix_forma()
	info_dossier = dossier()

	return render_template('home_layout.html', id_client = client,
		choix_formation = choix_formation, dossier = info_dossier, recherche = recherche )


@app.route('/date_exam', methods = ['POST', 'GET'])
def date_exam():
	recherche = search()

	client = id_client()
	choix_formation = choix_forma()
	info_dossier = dossier()

	data = open('data_file.txt', 'r').read()
	data = data.replace('}', '}},')
	data = data.replace('\n', '')
	data = data.split('},')
	del data[-1]
	lst_data = [eval(n) for n in data]

	date_ang = lst_data[0]['date_entree']
	date_fr = lst_data[0]['date']

	if request.method=="POST":
		
		donnee = request.form

		#return donnee
		date_exam = donnee['date_exam']
		etat_dossier = donnee['etat_dossier']

		try:
			if etat_dossier == 'Tout_etat':
				lst_data = [dico for dico in lst_data if dico['etat_dossier'] not in ['Annule', 'Archive']]
			else:
				lst_data = [dico for dico in lst_data if dico['etat_dossier'] == etat_dossier]
		except KeyError:
			pass

		
		
		#------------------------------------------------
		try:
			for dico in lst_data:
				if donnee['tel']== dico['tel']:
					donnee = dict(donnee)

					if "csrf_token" in donnee:
						del donnee['csrf_token']
					elif "submit" in donnee:
						del donnee['submit']
					dico.update(donnee)
			#-------------------------------------------------

			donnee_json = json.dumps(lst_data, indent=4)

			data_to_save = str()

			#-------------------------------------------------
			for dico in lst_data:
				json_dico = json.dumps(dico, indent = 4)
				data_to_save = data_to_save+json_dico
			#-------------------------------------------------

			with open('data_file.txt', 'w') as file:
				file.write(data_to_save)
		except:
			pass


		return  render_template('les_inscrits.html', data_file = lst_data, id_client = client,
			choix_formation = choix_formation, dossier = info_dossier,
			 recherche = recherche, date_exam = date_exam, etat_dossier = etat_dossier)


@app.route('/download')
def download():

	return "<a href='/static/img/ges.pdf' download> Salut</a>"
		

@app.route('/pdfgen', methods = ['POST'])
def test_pdf():
	if request.method =='POST':
		pdfgen()	
		
		return request.form


	 	
@app.route('/generate_contract', methods=['POST'])
def generate_contract():

	if request.method =='POST':
		

		user = dict(request.form)

		# ouvre la base de donnee
		lst_data = open_base()
		# renvoie le dico correspondant au user
		user_data = [dico for dico in lst_data if user['email'] == dico['email']  and user['date_examen'] == dico['date_exam']][0]
		
		session['user_data'] = user_data
		pdfgen(PDF)
		
		"""
			pour télécharger le document, soit faire un overlay avec btn download ou faire download avec javascript
		"""

		return redirect(url_for('contrat'))
	
@app.route("/logo", methods=['POST'])
def logo_upload():
	
	if request.method =='POST':
		file = request.files['file']
		extension =file.filename[[index for index in range(len(file.filename)) if file.filename[index]=='.'][-1]+1:]
		file_name=file.filename[:[index for index in range(len(file.filename)) if file.filename[index]=='.'][-1]]
		resize_img(upload_file(file), f'{file_name}.{extension}')

		pic_data = open_json()
		pic_data[0]['last_pic'] = pic_data[1]['new_pic']
		pic_data[1]['new_pic'] = file_name+'.'+extension


		save_json('profile_picture.json', pic_data)
		
	return jsonify({'profile_pic_name':f'{file_name}.{extension}'})


if __name__ == '__main__':
	app.run(debug = True, port = 1000)