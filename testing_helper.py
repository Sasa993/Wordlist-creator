import os

while (True):
	broj_rijeci = int(input("Unesi broj rijeci:"))

	if (1 <= broj_rijeci < 6):
		break

	print("Minimalan broj rijeci je 1, a maksimalan 5.\nMolimo Vas, pokusajte ponovo!\n")

rijecnik = {}
naziv_foldera = ""

for x in range(broj_rijeci):
	rijec = input("Unesi {0} rijec:".format(x + 1))
	duzina_rijeci = len(rijec)

	rijecnik[x] = {}
	rijecnik[x]["rijec"] = rijec
	rijecnik[x]["duzina_rijeci"] = duzina_rijeci
	rijecnik[x]["prvo_slovo_upper"] = rijec[0].upper() + rijec[1:]
	rijecnik[x]["zadnje_slovo_upper"] = rijec[:(duzina_rijeci - 1)] + rijec[(duzina_rijeci - 1)].upper()
	rijecnik[x]["sva_slova_upper"] = rijec.upper()

	naziv_foldera += rijec

def testna_funkcija(rijecnik):
	print("Lesa care napusi se kare, i onda kazem da je rijec \n{0} kada se pretvori da bude prvo slovo upper onda je:\n{1}\nA kad je sve veliko onda je:\n{2}".format(rijecnik[0]['rijec'], rijecnik[0]['prvo_slovo_upper'], rijecnik[1]['sva_slova_upper']))

def testna_funkcija_dva(rijec, sva_slova_upper):
	print("Lesa care napusi se kare, i onda kazem da je rijec \n{0} kada se pretvori da budu sva slova upper onda je:\n{1}".format(rijec, sva_slova_upper))

# print(rijecnik[0]['prvo_slovo_upper'])

os.system("mkdir {0}".format(naziv_foldera))

# for y in range(broj_rijeci):
testna_funkcija(rijecnik)
	# testna_funkcija_dva(rijecnik[y]['rijec'], rijecnik[y]['sva_slova_upper'])
