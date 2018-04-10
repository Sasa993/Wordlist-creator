import os
import time

#1.parametar: rijec, odnosno naziv mreze
#2.parametar: rijec_original, odnosno naziv foldera
#3.parametar: txt_broj, odnosno naziv txt fajla, tj. wordlista || dictionary
neki_tamo_brojac = 0
def prva_numeric(rijec, rijec_original, txt_broj):
	global neki_tamo_brojac
	os.system("crunch {0} {0} -t {1}% -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 1,rijec, rijec_original, txt_broj))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj))
	os.system("crunch {0} {0} -t {1}%% -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 2,rijec, rijec_original, txt_broj + 1))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 1))
	os.system("crunch {0} {0} -t {1}%%% -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 2))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 2))
	os.system("crunch {0} {0} -t {1}%%%% -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 4,rijec, rijec_original, txt_broj + 3))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 3))

def druga_numeric(rijec, rijec_original, txt_broj):
	global neki_tamo_brojac
	os.system("crunch {0} {0} -t %{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 1,rijec, rijec_original, txt_broj))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj))
	os.system("crunch {0} {0} -t %%{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 2,rijec, rijec_original, txt_broj + 1))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 1))
	os.system("crunch {0} {0} -t %%%{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 2))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 2))
	os.system("crunch {0} {0} -t %%%%{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 4,rijec, rijec_original, txt_broj + 3))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 3))

def prva_lower_alpha(rijec, rijec_original, txt_broj):
	global neki_tamo_brojac
	os.system("crunch {0} {0} -t {1}@ -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 1,rijec, rijec_original, txt_broj))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj))
	os.system("crunch {0} {0} -t {1}@@ -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 2,rijec, rijec_original, txt_broj + 1))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 1))
	os.system("crunch {0} {0} -t {1}@@@ -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 2))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 2))
	os.system("crunch {0} {0} -t {1}@@@@ -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 4,rijec, rijec_original, txt_broj + 3))	
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 3))

def druga_lower_alpha(rijec, rijec_original, txt_broj):
	global neki_tamo_brojac
	os.system("crunch {0} {0} -t @{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 1,rijec, rijec_original, txt_broj))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj))
	os.system("crunch {0} {0} -t @@{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 2,rijec, rijec_original, txt_broj + 1))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 1))
	os.system("crunch {0} {0} -t @@@{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 2))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 2))
	os.system("crunch {0} {0} -t @@@@{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 4,rijec, rijec_original, txt_broj + 3))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 3))

def prva_upper_alpha(rijec, rijec_original, txt_broj):
	global neki_tamo_brojac
	os.system("crunch {0} {0} -t {1}, -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 1,rijec, rijec_original, txt_broj))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj))
	os.system("crunch {0} {0} -t {1},, -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 2,rijec, rijec_original, txt_broj + 1))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 1))
	os.system("crunch {0} {0} -t {1},,, -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 2))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 2))
	os.system("crunch {0} {0} -t {1},,,, -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 4,rijec, rijec_original, txt_broj + 3))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 3))

def druga_upper_alpha(rijec, rijec_original, txt_broj):
	global neki_tamo_brojac
	os.system("crunch {0} {0} -t ,{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 1,rijec, rijec_original, txt_broj))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj))
	os.system("crunch {0} {0} -t ,,{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 2,rijec, rijec_original, txt_broj + 1))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 1))
	os.system("crunch {0} {0} -t ,,,{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 2))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 2))
	os.system("crunch {0} {0} -t ,,,,{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 4,rijec, rijec_original, txt_broj + 3))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 3))

def prva_mix_upper_lower(rijec, rijec_original, txt_broj):
	global neki_tamo_brojac
	os.system("crunch {0} {0} -t ,@{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 2,rijec, rijec_original, txt_broj))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj))
	os.system("crunch {0} {0} -t @,{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 2,rijec, rijec_original, txt_broj + 1))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 1))
	os.system("crunch {0} {0} -t @,,{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 2))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 2))
	os.system("crunch {0} {0} -t ,@,{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 3))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 3))
	os.system("crunch {0} {0} -t ,,@{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 4))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 4))
	os.system("crunch {0} {0} -t @@,{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 5))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 5))
	os.system("crunch {0} {0} -t ,@@{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 6))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 6))
	os.system("crunch {0} {0} -t @,@{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 7))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 7))

def druga_mix_upper_lower(rijec, rijec_original, txt_broj):
	global neki_tamo_brojac
	os.system("crunch {0} {0} -t {1},@ -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 2,rijec, rijec_original, txt_broj))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj))
	os.system("crunch {0} {0} -t {1}@, -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 2,rijec, rijec_original, txt_broj + 1))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 1))
	os.system("crunch {0} {0} -t {1}@,, -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 2))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 2))
	os.system("crunch {0} {0} -t {1},@, -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 3))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 3))
	os.system("crunch {0} {0} -t {1},,@ -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 4))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 4))
	os.system("crunch {0} {0} -t {1}@@, -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 5))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 5))
	os.system("crunch {0} {0} -t {1},@@ -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 6))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 6))
	os.system("crunch {0} {0} -t {1}@,@ -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 7))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 7))

def prva_mix_upper_numeric(rijec, rijec_original, txt_broj):
	global neki_tamo_brojac
	os.system("crunch {0} {0} -t ,%{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 2,rijec, rijec_original, txt_broj))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj))
	os.system("crunch {0} {0} -t %,{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 2,rijec, rijec_original, txt_broj + 1))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 1))
	os.system("crunch {0} {0} -t %,,{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 2))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 2))
	os.system("crunch {0} {0} -t ,%,{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 3))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 3))
	os.system("crunch {0} {0} -t ,,%{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 4))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 4))
	os.system("crunch {0} {0} -t %%,{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 5))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 5))
	os.system("crunch {0} {0} -t ,%%{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 6))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 6))
	os.system("crunch {0} {0} -t %,%{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 7))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 7))

def druga_mix_upper_numeric(rijec, rijec_original, txt_broj):
	global neki_tamo_brojac
	os.system("crunch {0} {0} -t {1},% -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 2,rijec, rijec_original, txt_broj))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj))
	os.system("crunch {0} {0} -t {1}%, -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 2,rijec, rijec_original, txt_broj + 1))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 1))
	os.system("crunch {0} {0} -t {1}%,, -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 2))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 2))
	os.system("crunch {0} {0} -t {1},%, -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 3))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 3))
	os.system("crunch {0} {0} -t {1},,% -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 4))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 4))
	os.system("crunch {0} {0} -t {1}%%, -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 5))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 5))
	os.system("crunch {0} {0} -t {1},%% -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 6))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 6))
	os.system("crunch {0} {0} -t {1}%,% -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 7))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 7))

def prva_mix_lower_numeric(rijec, rijec_original, txt_broj):
	global neki_tamo_brojac
	os.system("crunch {0} {0} -t %@{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 2,rijec, rijec_original, txt_broj))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj))
	os.system("crunch {0} {0} -t @%{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 2,rijec, rijec_original, txt_broj + 1))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 1))
	os.system("crunch {0} {0} -t @%%{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 2))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 2))
	os.system("crunch {0} {0} -t %@%{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 3))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 3))
	os.system("crunch {0} {0} -t %%@{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 4))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 4))
	os.system("crunch {0} {0} -t @@%{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 5))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 5))
	os.system("crunch {0} {0} -t %@@{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 6))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 6))
	os.system("crunch {0} {0} -t @%@{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 7))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 7))

def druga_mix_lower_numeric(rijec, rijec_original, txt_broj):
	global neki_tamo_brojac
	os.system("crunch {0} {0} -t {1}%@ -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 2,rijec, rijec_original, txt_broj))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj))
	os.system("crunch {0} {0} -t {1}@% -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 2,rijec, rijec_original, txt_broj + 1))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 1))
	os.system("crunch {0} {0} -t {1}@%% -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 2))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 2))
	os.system("crunch {0} {0} -t {1}%@% -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 3))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 3))
	os.system("crunch {0} {0} -t {1}%%@ -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 4))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 4))
	os.system("crunch {0} {0} -t {1}@@% -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 5))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 5))
	os.system("crunch {0} {0} -t {1}%@@ -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 6))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 6))
	os.system("crunch {0} {0} -t {1}@%@ -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 7))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 7))

def prva_mix_lower_upper_numeric(rijec, rijec_original, txt_broj):
	global neki_tamo_brojac
	os.system("crunch {0} {0} -t @,%{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj))
	os.system("crunch {0} {0} -t @%,{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 1))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 1))
	os.system("crunch {0} {0} -t ,@%{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 2))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 2))
	os.system("crunch {0} {0} -t ,%@{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 3))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 3))
	os.system("crunch {0} {0} -t %@,{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 4))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 4))
	os.system("crunch {0} {0} -t %,@{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 5))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 5))
	
def druga_mix_lower_upper_numeric(rijec, rijec_original, txt_broj):
	global neki_tamo_brojac
	os.system("crunch {0} {0} -t {1}@,% -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj))
	os.system("crunch {0} {0} -t {1}@%, -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 1))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 1))
	os.system("crunch {0} {0} -t {1},@% -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 2))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 2))
	os.system("crunch {0} {0} -t {1},%@ -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 3))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 3))
	os.system("crunch {0} {0} -t {1}%@, -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 4))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 4))
	os.system("crunch {0} {0} -t {1}%,@ -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 5))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 5))
	
def prva_char(rijec, rijec_original, txt_broj):
	global neki_tamo_brojac
	os.system("crunch {0} {0} -t ^{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 1,rijec, rijec_original, txt_broj))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj))
	os.system("crunch {0} {0} -t ^^{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 2,rijec, rijec_original, txt_broj + 1))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 1))
	os.system("crunch {0} {0} -t ^^^{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 2))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 2))
	os.system("crunch {0} {0} -t ^^^^{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 4,rijec, rijec_original, txt_broj + 3))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 3))

def druga_char(rijec, rijec_original, txt_broj):
	global neki_tamo_brojac
	os.system("crunch {0} {0} -t {1}^ -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 1,rijec, rijec_original, txt_broj))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj))
	os.system("crunch {0} {0} -t {1}^^ -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 2,rijec, rijec_original, txt_broj + 1))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 1))
	os.system("crunch {0} {0} -t {1}^^^ -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 2))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 2))
	os.system("crunch {0} {0} -t {1}^^^^ -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 4,rijec, rijec_original, txt_broj + 3))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 3))

def prva_mix_upper_char(rijec, rijec_original, txt_broj):
	global neki_tamo_brojac
	os.system("crunch {0} {0} -t ,^{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 2,rijec, rijec_original, txt_broj))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj))
	os.system("crunch {0} {0} -t ^,{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 2,rijec, rijec_original, txt_broj + 1))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 1))
	os.system("crunch {0} {0} -t ^,,{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 2))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 2))
	os.system("crunch {0} {0} -t ,^,{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 3))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 3))
	os.system("crunch {0} {0} -t ,,^{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 4))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 4))
	os.system("crunch {0} {0} -t ^^,{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 5))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 5))
	os.system("crunch {0} {0} -t ,^^{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 6))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 6))
	os.system("crunch {0} {0} -t ^,^{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 7))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 7))

def druga_mix_upper_char(rijec, rijec_original, txt_broj):
	global neki_tamo_brojac
	os.system("crunch {0} {0} -t {1},^ -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 2,rijec, rijec_original, txt_broj))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj))
	os.system("crunch {0} {0} -t {1}^, -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 2,rijec, rijec_original, txt_broj + 1))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 1))
	os.system("crunch {0} {0} -t {1}^,, -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 2))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 2))
	os.system("crunch {0} {0} -t {1},^, -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 3))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 3))
	os.system("crunch {0} {0} -t {1},,^ -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 4))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 4))
	os.system("crunch {0} {0} -t {1}^^, -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 5))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 5))
	os.system("crunch {0} {0} -t {1},^^ -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 6))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 6))
	os.system("crunch {0} {0} -t {1}^,^ -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 7))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 7))

def prva_mix_lower_char(rijec, rijec_original, txt_broj):
	global neki_tamo_brojac
	os.system("crunch {0} {0} -t @^{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 2,rijec, rijec_original, txt_broj))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj))
	os.system("crunch {0} {0} -t ^@{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 2,rijec, rijec_original, txt_broj + 1))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 1))
	os.system("crunch {0} {0} -t ^@@{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 2))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 2))
	os.system("crunch {0} {0} -t @^@{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 3))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 3))
	os.system("crunch {0} {0} -t @@^{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 4))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 4))
	os.system("crunch {0} {0} -t ^^@{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 5))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 5))
	os.system("crunch {0} {0} -t @^^{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 6))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 6))
	os.system("crunch {0} {0} -t ^@^{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 7))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 7))

def druga_mix_lower_char(rijec, rijec_original, txt_broj):
	os.system("crunch {0} {0} -t {1}@^ -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 2,rijec, rijec_original, txt_broj))
	os.system("crunch {0} {0} -t {1}^@ -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 2,rijec, rijec_original, txt_broj + 1))
	os.system("crunch {0} {0} -t {1}^@@ -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 2))
	os.system("crunch {0} {0} -t {1}@^@ -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 3))
	os.system("crunch {0} {0} -t {1}@@^ -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 4))
	os.system("crunch {0} {0} -t {1}^^@ -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 5))
	os.system("crunch {0} {0} -t {1}@^^ -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 6))
	os.system("crunch {0} {0} -t {1}^@^ -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 7))

def prva_mix_numeric_char(rijec, rijec_original, txt_broj):
	os.system("crunch {0} {0} -t %^{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 2,rijec, rijec_original, txt_broj))
	os.system("crunch {0} {0} -t ^%{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 2,rijec, rijec_original, txt_broj + 1))
	os.system("crunch {0} {0} -t ^%%{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 2))
	os.system("crunch {0} {0} -t %^%{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 3))
	os.system("crunch {0} {0} -t %%^{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 4))
	os.system("crunch {0} {0} -t ^^%{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 5))
	os.system("crunch {0} {0} -t %^^{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 6))
	os.system("crunch {0} {0} -t ^%^{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 7))

def druga_mix_numeric_char(rijec, rijec_original, txt_broj):
	os.system("crunch {0} {0} -t {1}%^ -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 2,rijec, rijec_original, txt_broj))
	os.system("crunch {0} {0} -t {1}^% -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 2,rijec, rijec_original, txt_broj + 1))
	os.system("crunch {0} {0} -t {1}^%% -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 2))
	os.system("crunch {0} {0} -t {1}%^% -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 3))
	os.system("crunch {0} {0} -t {1}%%^ -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 4))
	os.system("crunch {0} {0} -t {1}^^% -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 5))
	os.system("crunch {0} {0} -t {1}%^^ -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 6))
	os.system("crunch {0} {0} -t {1}^%^ -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 7))

def prva_mix_upper_lower_char(rijec, rijec_original, txt_broj):
	os.system("crunch {0} {0} -t @,^{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj))
	os.system("crunch {0} {0} -t @^,{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 1))
	os.system("crunch {0} {0} -t ,@^{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 2))
	os.system("crunch {0} {0} -t ,^@{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 3))
	os.system("crunch {0} {0} -t ^@,{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 4))
	os.system("crunch {0} {0} -t ^,@{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 5))

def druga_mix_upper_lower_char(rijec, rijec_original, txt_broj):
	os.system("crunch {0} {0} -t {1}@,^ -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj))
	os.system("crunch {0} {0} -t {1}@^, -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 1))
	os.system("crunch {0} {0} -t {1},@^ -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 2))
	os.system("crunch {0} {0} -t {1},^@ -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 3))
	os.system("crunch {0} {0} -t {1}^@, -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 4))
	os.system("crunch {0} {0} -t {1}^,@ -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 5))

def prva_mix_upper_numeric_char(rijec, rijec_original, txt_broj):
	os.system("crunch {0} {0} -t %,^{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj))
	os.system("crunch {0} {0} -t %^,{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 1))
	os.system("crunch {0} {0} -t ,%^{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 2))
	os.system("crunch {0} {0} -t ,^%{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 3))
	os.system("crunch {0} {0} -t ^%,{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 4))
	os.system("crunch {0} {0} -t ^,%{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 5))

def druga_mix_upper_numeric_char(rijec, rijec_original, txt_broj):
	os.system("crunch {0} {0} -t {1}%,^ -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj))
	os.system("crunch {0} {0} -t {1}%^, -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 1))
	os.system("crunch {0} {0} -t {1},%^ -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 2))
	os.system("crunch {0} {0} -t {1},^% -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 3))
	os.system("crunch {0} {0} -t {1}^%, -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 4))
	os.system("crunch {0} {0} -t {1}^,% -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 5))

os.system("crunch")
time.sleep(2)

rijec = raw_input("Unesi nesto:")
rijec_duzina = len(rijec)

#os.system("cd /")
os.system("mkdir /root/Documents/{0}".format(rijec)) 									#kreiranje foldera po nazivu

rijec_prvo_slovo_upper = rijec[0].upper() + rijec[1:]
rijec_zadnje_slovo_upper = rijec[:(rijec_duzina - 1)] + rijec[(rijec_duzina - 1)].upper()
rijec_sva_slova_upper = rijec.upper()

prva_numeric(rijec, rijec, 1)
prva_numeric(rijec_prvo_slovo_upper, rijec, 5)
prva_numeric(rijec_zadnje_slovo_upper, rijec, 9)
prva_numeric(rijec_sva_slova_upper, rijec, 13)

druga_numeric(rijec, rijec, 17)
druga_numeric(rijec_prvo_slovo_upper, rijec, 21)
druga_numeric(rijec_zadnje_slovo_upper, rijec, 25)
druga_numeric(rijec_sva_slova_upper, rijec, 29)

prva_lower_alpha(rijec, rijec, 33)
prva_lower_alpha(rijec_prvo_slovo_upper, rijec, 37)
prva_lower_alpha(rijec_zadnje_slovo_upper, rijec, 41)
prva_lower_alpha(rijec_sva_slova_upper, rijec, 45)

#48 files - 21.8MB

druga_lower_alpha(rijec, rijec, 49)
druga_lower_alpha(rijec_prvo_slovo_upper, rijec, 53)
druga_lower_alpha(rijec_zadnje_slovo_upper, rijec, 57)
druga_lower_alpha(rijec_sva_slova_upper, rijec, 61)

prva_upper_alpha(rijec, rijec, 65)
prva_upper_alpha(rijec_prvo_slovo_upper, rijec, 69)
prva_upper_alpha(rijec_zadnje_slovo_upper, rijec, 73)
prva_upper_alpha(rijec_sva_slova_upper, rijec, 77)

druga_upper_alpha(rijec, rijec, 81)
druga_upper_alpha(rijec_prvo_slovo_upper, rijec, 85)
druga_upper_alpha(rijec_zadnje_slovo_upper, rijec, 89)
druga_upper_alpha(rijec_sva_slova_upper, rijec, 93)

#96 files - 72.9MB

prva_mix_upper_lower(rijec, rijec, 97)
print("\nVelicina foldera iznosi:\n{0:.2f}MB".format(float(neki_tamo_brojac)/1024/1024))
prva_mix_upper_lower(rijec_prvo_slovo_upper, rijec, 105)
print("\nVelicina foldera:\n{0:.2f}MB".format(float(neki_tamo_brojac)/1024/1024))
prva_mix_upper_lower(rijec_zadnje_slovo_upper, rijec, 113)
print("\nVelicina foldera:\n{0:.2f}MB".format(float(neki_tamo_brojac)/1024/1024))
prva_mix_upper_lower(rijec_sva_slova_upper, rijec, 121)
print("\nVelicina foldera:\n{0:.2f}MB".format(float(neki_tamo_brojac)/1024/1024))

#128 files - 78.9MB

druga_mix_upper_lower(rijec, rijec, 129)
druga_mix_upper_lower(rijec_prvo_slovo_upper, rijec, 137)
druga_mix_upper_lower(rijec_zadnje_slovo_upper, rijec, 145)
druga_mix_upper_lower(rijec_sva_slova_upper, rijec, 153)

prva_mix_upper_numeric(rijec, rijec, 161)
prva_mix_upper_numeric(rijec_prvo_slovo_upper, rijec, 169)
prva_mix_upper_numeric(rijec_zadnje_slovo_upper, rijec, 177)
prva_mix_upper_numeric(rijec_sva_slova_upper, rijec, 185)

druga_mix_upper_numeric(rijec, rijec, 193)
druga_mix_upper_numeric(rijec_prvo_slovo_upper, rijec, 201)
druga_mix_upper_numeric(rijec_zadnje_slovo_upper, rijec, 209)
druga_mix_upper_numeric(rijec_sva_slova_upper, rijec, 217)

#224 files - 87.4MB

prva_mix_lower_numeric(rijec, rijec, 225)
prva_mix_lower_numeric(rijec_prvo_slovo_upper, rijec, 233)
prva_mix_lower_numeric(rijec_zadnje_slovo_upper, rijec, 241)
prva_mix_lower_numeric(rijec_sva_slova_upper, rijec, 249)

druga_mix_lower_numeric(rijec, rijec, 257)
druga_mix_lower_numeric(rijec_prvo_slovo_upper, rijec, 265)
druga_mix_lower_numeric(rijec_zadnje_slovo_upper, rijec, 273)
druga_mix_lower_numeric(rijec_sva_slova_upper, rijec, 281)

#288 files - 89.7MB

prva_mix_lower_upper_numeric(rijec, rijec, 289)
prva_mix_lower_upper_numeric(rijec_prvo_slovo_upper, rijec, 295)
prva_mix_lower_upper_numeric(rijec_zadnje_slovo_upper, rijec, 301)
prva_mix_lower_upper_numeric(rijec_sva_slova_upper, rijec, 307)

druga_mix_lower_upper_numeric(rijec, rijec, 313)
druga_mix_lower_upper_numeric(rijec_prvo_slovo_upper, rijec, 319)
druga_mix_lower_upper_numeric(rijec_zadnje_slovo_upper, rijec, 325)
druga_mix_lower_upper_numeric(rijec_sva_slova_upper, rijec, 331)

#336 files - 92.6MB

prva_char(rijec, rijec, 337)
prva_char(rijec_prvo_slovo_upper, rijec, 341)
prva_char(rijec_zadnje_slovo_upper, rijec, 345)
prva_char(rijec_sva_slova_upper, rijec, 349)

druga_char(rijec, rijec, 353)
druga_char(rijec_prvo_slovo_upper, rijec, 357)
druga_char(rijec_zadnje_slovo_upper, rijec, 361)
druga_char(rijec_sva_slova_upper, rijec, 365)

prva_mix_upper_char(rijec, rijec, 369)
prva_mix_upper_char(rijec_prvo_slovo_upper, rijec, 377)
prva_mix_upper_char(rijec_zadnje_slovo_upper, rijec, 385)
prva_mix_upper_char(rijec_sva_slova_upper, rijec, 393)

druga_mix_upper_char(rijec, rijec, 401)
druga_mix_upper_char(rijec_prvo_slovo_upper, rijec, 409)
druga_mix_upper_char(rijec_zadnje_slovo_upper, rijec, 417)
druga_mix_upper_char(rijec_sva_slova_upper, rijec, 425)

prva_mix_lower_char(rijec, rijec, 433)
prva_mix_lower_char(rijec_prvo_slovo_upper, rijec, 441)
prva_mix_lower_char(rijec_zadnje_slovo_upper, rijec, 449)
prva_mix_lower_char(rijec_sva_slova_upper, rijec, 457)

druga_mix_lower_char(rijec, rijec, 465)
druga_mix_lower_char(rijec_prvo_slovo_upper, rijec, 473)
druga_mix_lower_char(rijec_zadnje_slovo_upper, rijec, 481)
druga_mix_lower_char(rijec_sva_slova_upper, rijec, 489)

prva_mix_numeric_char(rijec, rijec, 497)
prva_mix_numeric_char(rijec_prvo_slovo_upper, rijec, 505)
prva_mix_numeric_char(rijec_zadnje_slovo_upper, rijec, 513)
prva_mix_numeric_char(rijec_sva_slova_upper, rijec, 521)

druga_mix_numeric_char(rijec, rijec, 529)
druga_mix_numeric_char(rijec_prvo_slovo_upper, rijec, 537)
druga_mix_numeric_char(rijec_zadnje_slovo_upper, rijec, 545)
druga_mix_numeric_char(rijec_sva_slova_upper, rijec, 553)

#560 files - 202.7MB

prva_mix_upper_lower_char(rijec, rijec, 561)
prva_mix_upper_lower_char(rijec_prvo_slovo_upper, rijec, 567)
prva_mix_upper_lower_char(rijec_zadnje_slovo_upper, rijec, 573)
prva_mix_upper_lower_char(rijec_sva_slova_upper, rijec, 579)

druga_mix_upper_lower_char(rijec, rijec, 585)
druga_mix_upper_lower_char(rijec_prvo_slovo_upper, rijec, 591)
druga_mix_upper_lower_char(rijec_zadnje_slovo_upper, rijec, 597)
druga_mix_upper_lower_char(rijec_sva_slova_upper, rijec, 603)

prva_mix_upper_numeric_char(rijec, rijec, 609)
prva_mix_upper_numeric_char(rijec_prvo_slovo_upper, rijec, 615)
prva_mix_upper_numeric_char(rijec_zadnje_slovo_upper, rijec, 621)
prva_mix_upper_numeric_char(rijec_sva_slova_upper, rijec, 627)

druga_mix_upper_numeric_char(rijec, rijec, 633)
druga_mix_upper_numeric_char(rijec_prvo_slovo_upper, rijec, 639)
druga_mix_upper_numeric_char(rijec_zadnje_slovo_upper, rijec, 645)
druga_mix_upper_numeric_char(rijec_sva_slova_upper, rijec, 651)

#656 files - 214.6MB

#testiramo nesto
# def main_funkcija(ime_funkcije, broj_skokova):
# 	global brojac, rijec, rijec_prvo_slovo_upper, rijec_zadnje_slovo_upper, rijec_sva_slova_upper

# 	brojac += broj_skokova
# 	ime_funkcije(rijec, rijec, brojac)
# 	brojac += broj_skokova
# 	ime_funkcije(rijec_prvo_slovo_upper, rijec, brojac)
# 	brojac += broj_skokova
# 	ime_funkcije(rijec_zadnje_slovo_upper, rijec, brojac)
# 	brojac += broj_skokova
# 	ime_funkcije(rijec_sva_slova_upper, rijec, brojac)
# 	brojac += broj_skokova


