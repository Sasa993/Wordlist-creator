import os
import time

#1.parametar: rijec, odnosno naziv mreze
#2.parametar: rijec_original, odnosno naziv foldera
#3.parametar: txt_broj, odnosno naziv txt fajla, tj. wordlista || dictionary
def prva(rijec, rijec_original, txt_broj):
	os.system("crunch {0} {0} -t {1}% -o /home/lesa/Documents/{2}/{3}.txt".format(rijec_duzina + 1,rijec, rijec_original, txt_broj))
	os.system("crunch {0} {0} -t {1}%% -o /home/lesa/Documents/{2}/{3}.txt".format(rijec_duzina + 2,rijec, rijec_original, txt_broj + 1))
	os.system("crunch {0} {0} -t {1}%%% -o /home/lesa/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 2))
	os.system("crunch {0} {0} -t {1}%%%% -o /home/lesa/Documents/{2}/{3}.txt".format(rijec_duzina + 4,rijec, rijec_original, txt_broj + 3))

os.system("crunch")
time.sleep(2)

rijec = raw_input("Unesi nesto:")
rijec_duzina = len(rijec)

os.system("mkdir /home/lesa/Documents/{0}".format(rijec)) 									#kreiranje foldera po nazivu

prva(rijec, rijec, 1)
rijec_prvo_slovo_upper = rijec[0].upper() + rijec[1:]
prva(rijec_prvo_slovo_upper, rijec, 5)
rijec_zadnje_slovo_upper = rijec[:(rijec_duzina - 1)] + rijec[(rijec_duzina - 1)].upper()
prva(rijec_zadnje_slovo_upper, rijec, 9)
rijec_sva_slova_upper = rijec.upper()
prva(rijec_sva_slova_upper, rijec, 13)

# print("Gotovo je bato i izgleda ovako:\n")
# os.system("cat wordlist.txt")


