def hej(imie):
	if imie == 'Ola':
		print('Hej Ola!')
	elif imie == 'Sonja':
		print('Hej Sonja!')
	else:
		print('Hej nieznajoma!')

lista_imion=['Ola', 'Sonja', 'Ela']
#for i in range(0,3):
#	hej(lista_imion[i])
for imie in lista_imion:
	hej(imie)
	print("kolejna dziewczyna")
