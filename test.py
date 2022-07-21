"""
def pick_two(lst):
    len_lst = len(lst)
    cop = lst.copy()
    sorted_lst =[]
    i =0
    
    while i <= len_lst-1:
        check = lst[i]
        cop.remove(lst[i])
        for n in cop:
            if check + n ==1000 :
                sorted_lst.append([check, n])
        cop = lst.copy()        
        i+=1

                
    if len(sorted_lst ) ==0:
        return []
    else:
        return sorted_lst[0]


lst = [500, 3, 500, 510]
print(pick_two(lst))
"""
"""
def palyndrome(str):
	start = 0
	last = -1
	word = []
	for i,l in enumerate(str):
		if str[start] == str[last]:
			word.insert(last,str[last])
			
		start +=1
		last -=1
	if list(str) == word:
		return f"{str} is a palyndrome"
	else:
		return f"{str} is not a palyndrome"

	return word

m=palyndrome('otto')
"""

"""
def count_word(str):
	lst_str = str.split(' ')
	word_count = [lst_str.count(n) for n in lst_str  ]
	lst_tup =[]

	for i,n in enumerate(lst_str):
		lst_tup.append((n,word_count[i]))


	print(list(set(lst_tup)))
	return list(set(lst_tup))

count_word('je suis le meilleur et je ne suis pas avec vous ')
"""
"""
lst = [-1 , 150,190,170,-1,-1,160,180]

def sort_t(lst):

	n_list = [n for n in lst if n>0]
	n_list.sort()
	for i,n in enumerate(lst):
		if n<0:
			n_list.insert(i,n)

	#n_list.sort(key=lambda x:x[-1])
	print(n_list)

	return n_list

l=sort_t(lst)
"""

def bonjour():

	prenom = input('Quel est ton prénom ?: ')
	print(f'Bonjour {prenom}\n')

	age = input('Quel âge as-tu? :')
	print(f"C'est vrai que tu a {age} \n")

def ordi():
	#-----------------------------------------------------------------------------
	sx = input("Tu es une fille ou un garcon? Entre 'F' pour 'fille' ou 'G' pour 'garcon' :")
	if 'g' in sx.lower():
		print('Génial!! Il est trop cool ton prénom pour un garcon\n')
	if 'f' in sx.lower():
		print('Génial!! Il est trop cool ton prénom pour une fille\n')
	#-----------------------------------------------------------------------------

	#-----------------------------------------------------------------------------
	ordi_age = input('devine mon âge:...')

	if '32' in ordi_age:
		if 'g' in sx.lower():
			print("Bravoooooo. Waoo tu es trop intélligent")
		elif 'f' in sx.lower():
			print("Bravoooooo. Waoo tu es trop intélligente")
	else:
		print(f" :-) tu t'ai trompé je n'ai pas {ordi_age}. \n j'ai juste 32 ans comme ton Papa\n")
	#-----------------------------------------------------------------------------

	#-----------------------------------------------------------------------------
	classe = input('tu es en quelle classe? ')

	if 'cm1' in classe.lower():
		print(f" c'est vrai?") 
		prof = input('tu connais Mr Mignard? ')
		if 'oui' in prof:
			print("Waoooo moi aussi!! C'est mon maitre.\n Bon Il faut que j'aille faire pipi et caca, à bientôt \n\n")
		else:
			print(" mais c'est le maitre en CM1 A!!!!\n")

	if 'cp' in classe:
		print(f" c'est vrai?") 
		prof = input('tu connais Mme David? ')
		if 'oui' in prof:
			print("Waoooo moi aussi, c'est ma maitresse\n Il faut que j'aille faire caca, à bientôt\n")
	#-----------------------------------------------------------------------------



c = True

while c== True:
	deb = input("Vous voulez parler avec moi?\n Appuyez sur 'O' pour 'oui' ou 'N' pour 'non' : ")

	if 'o' in deb.lower():

		bonjour()
		ordi()
	elif 'n' in deb.lower():
		print('Aurevoir et à bientôt !!!')
		c= False
	cont = input("Voulez vous encore recommencer? Appuyez sur 'O' pour 'oui' ou 'N' pour 'non': ")

	if 'o' in cont.lower():
		continue
	elif 'n' in cont.lower():
		print('Aurevoir!!!!')
		c = False
