from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import re

driver = webdriver.Chrome()
actions = ActionChains(driver)
#adresse = 'https://mesdemarches.emploi.gouv.fr/identification/login?service=https%3A%2F%2Fmesdemarches.emploi.gouv.fr%2Fidentification%2Foauth2.0%2FcallbackAuthorize%3Fclient_id%3Dprod-edof%26redirect_uri%3Dhttps%253A%252F%252Fwww.of.moncompteformation.gouv.fr%252Fidp%252Fedof%252Fcallback%26response_type%3Dcode%26client_name%3DCasOAuthClient'
adresse = 'https://www.of.moncompteformation.gouv.fr/espace-prive/html/#/landing'
adresse_paiement ='https://www.of.moncompteformation.gouv.fr/espace-prive/html/#/payment/list/all'
driver.get(adresse)
sleep(4)
connexion_button = driver.find_element_by_xpath('//*[@id="landing-task-section-id"]/div[2]/a')

connexion_button.click()
sleep(2)
mail_input = driver.find_element_by_id('username')
pass_input = driver.find_element_by_id('password')
conncect_button = driver.find_element_by_name('submit')
mail_input.clear()
mail_input.send_keys('keyz.formation@gmail.com')
sleep(0.5)

pass_input.clear()
pass_input.send_keys('Bonif@ce91480')

sleep(0.5)
conncect_button.click()
sleep(2)
driver.get(adresse_paiement)
sleep(2)

# on click sur le bouton des paiements émis
paiement_emis_button = driver.find_element_by_xpath('/html/body/sl7-app/sl7-payment/main/div[1]/sl7-payment-list/section/section/div/button[2]').click()
sleep(1)

# on fait disparaitre la bande de du cookie ----------------
ok_cookie_btn = driver.find_element_by_xpath('/html/body/div/div/a')
sleep(0.5)
ok_cookie_btn.click()
#---------------------------------------------------------------------

last_page = driver.find_elements_by_class_name('pagination__nav-arrow')
sleep(1)

actions.move_to_element(last_page[-1])
actions.click(last_page[-1])
actions.perform()
sleep(1)
nbre_page = driver.find_elements_by_class_name('button--link-primary')
nbre_max_page = int(nbre_page[-1].text)

driver.back()
sleep(1)
driver.forward()
sleep(1)
paiement_emis_button = driver.find_element_by_xpath('/html/body/sl7-app/sl7-payment/main/div[1]/sl7-payment-list/section/section/div/button[2]').click()
sleep(1)

lst_table = []
lst_table_txt = ''
lst_chiffre = []
total_ca = 0

for n in list(range(0, nbre_max_page)):
	next_btn = driver.find_elements_by_class_name('pagination__nav-arrow')[-2].click()
	sleep(1)
	table = driver.find_elements_by_tag_name('tr')
	lst_table.extend([row.text for row in table])

for info in lst_table:
	lst_table_txt += info

lst_chiffre = re.findall('(\d\s\d{3})*', lst_table_txt)

for ca_txt in lst_chiffre:

	total_ca +=int(ca_txt)

print(total_ca)
#driver.refresh()
