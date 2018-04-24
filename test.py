import os
import time

#1.parameter: rijec - word
#2.parameter: rijec_original - name of the folder
#3.parameter: txt_broj - name of the .txt file which is created by that function

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
	global neki_tamo_brojac

	os.system("crunch {0} {0} -t {1}@^ -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 2,rijec, rijec_original, txt_broj))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj))
	os.system("crunch {0} {0} -t {1}^@ -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 2,rijec, rijec_original, txt_broj + 1))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 1))
	os.system("crunch {0} {0} -t {1}^@@ -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 2))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 2))
	os.system("crunch {0} {0} -t {1}@^@ -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 3))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 3))
	os.system("crunch {0} {0} -t {1}@@^ -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 4))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 4))
	os.system("crunch {0} {0} -t {1}^^@ -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 5))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 5))
	os.system("crunch {0} {0} -t {1}@^^ -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 6))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 6))
	os.system("crunch {0} {0} -t {1}^@^ -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 7))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 7))

def prva_mix_numeric_char(rijec, rijec_original, txt_broj):
	global neki_tamo_brojac

	os.system("crunch {0} {0} -t %^{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 2,rijec, rijec_original, txt_broj))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj))
	os.system("crunch {0} {0} -t ^%{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 2,rijec, rijec_original, txt_broj + 1))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 1))
	os.system("crunch {0} {0} -t ^%%{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 2))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 2))
	os.system("crunch {0} {0} -t %^%{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 3))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 3))
	os.system("crunch {0} {0} -t %%^{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 4))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 4))
	os.system("crunch {0} {0} -t ^^%{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 5))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 5))
	os.system("crunch {0} {0} -t %^^{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 6))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 6))
	os.system("crunch {0} {0} -t ^%^{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 7))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 7))

def druga_mix_numeric_char(rijec, rijec_original, txt_broj):
	global neki_tamo_brojac

	os.system("crunch {0} {0} -t {1}%^ -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 2,rijec, rijec_original, txt_broj))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj))
	os.system("crunch {0} {0} -t {1}^% -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 2,rijec, rijec_original, txt_broj + 1))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 1))
	os.system("crunch {0} {0} -t {1}^%% -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 2))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 2))
	os.system("crunch {0} {0} -t {1}%^% -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 3))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 3))
	os.system("crunch {0} {0} -t {1}%%^ -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 4))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 4))
	os.system("crunch {0} {0} -t {1}^^% -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 5))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 5))
	os.system("crunch {0} {0} -t {1}%^^ -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 6))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 6))
	os.system("crunch {0} {0} -t {1}^%^ -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 7))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 7))

def prva_mix_upper_lower_char(rijec, rijec_original, txt_broj):
	global neki_tamo_brojac

	os.system("crunch {0} {0} -t @,^{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj))
	os.system("crunch {0} {0} -t @^,{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 1))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 1))
	os.system("crunch {0} {0} -t ,@^{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 2))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 2))
	os.system("crunch {0} {0} -t ,^@{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 3))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 3))
	os.system("crunch {0} {0} -t ^@,{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 4))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 4))
	os.system("crunch {0} {0} -t ^,@{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 5))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 5))

def druga_mix_upper_lower_char(rijec, rijec_original, txt_broj):
	global neki_tamo_brojac

	os.system("crunch {0} {0} -t {1}@,^ -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj))
	os.system("crunch {0} {0} -t {1}@^, -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 1))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 1))
	os.system("crunch {0} {0} -t {1},@^ -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 2))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 2))
	os.system("crunch {0} {0} -t {1},^@ -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 3))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 3))
	os.system("crunch {0} {0} -t {1}^@, -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 4))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 4))
	os.system("crunch {0} {0} -t {1}^,@ -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 5))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 5))

def prva_mix_upper_numeric_char(rijec, rijec_original, txt_broj):
	global neki_tamo_brojac

	os.system("crunch {0} {0} -t %,^{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj))
	os.system("crunch {0} {0} -t %^,{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 1))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 1))
	os.system("crunch {0} {0} -t ,%^{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 2))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 2))
	os.system("crunch {0} {0} -t ,^%{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 3))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 3))
	os.system("crunch {0} {0} -t ^%,{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 4))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 4))
	os.system("crunch {0} {0} -t ^,%{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 5))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 5))

def druga_mix_upper_numeric_char(rijec, rijec_original, txt_broj):
	global neki_tamo_brojac
	
	os.system("crunch {0} {0} -t {1}%,^ -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj))
	os.system("crunch {0} {0} -t {1}%^, -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 1))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 1))
	os.system("crunch {0} {0} -t {1},%^ -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 2))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 2))
	os.system("crunch {0} {0} -t {1},^% -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 3))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 3))
	os.system("crunch {0} {0} -t {1}^%, -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 4))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 4))
	os.system("crunch {0} {0} -t {1}^,% -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 5))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(rijec_original, txt_broj + 5))

#functions with 2 words start here

def dvije_rijeci_prva_numeric(prva_rijec, druga_rijec, folder, rijecnik, txt_broj):
	global neki_tamo_brojac

	os.system("crunch {0} {0} -t {1}{2}% -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 1, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder, txt_broj))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj))
	os.system("crunch {0} {0} -t {1}{2}%% -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder, txt_broj + 1))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 1))
	os.system("crunch {0} {0} -t {1}{2}%%% -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder, txt_broj + 2))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 2))
	os.system("crunch {0} {0} -t {1}{2}%%%% -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder, txt_broj + 3))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 3))
	os.system("crunch {0} {0} -t {1}%{2} -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 1, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder, txt_broj + 4))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 4))
	os.system("crunch {0} {0} -t {1}%%{2} -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder, txt_broj + 5))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 5))
	os.system("crunch {0} {0} -t {1}%%%{2} -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder, txt_broj + 6))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 6))
	os.system("crunch {0} {0} -t {1}%%%%{2} -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder, txt_broj + 7))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 7))
	os.system("crunch {0} {0} -t {1}%{2}% -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder, txt_broj + 8))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 8))
	os.system("crunch {0} {0} -t {1}%%{2}% -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder, txt_broj + 9))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 9))
	os.system("crunch {0} {0} -t {1}%{2}%% -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder, txt_broj + 10))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 10))
	os.system("crunch {0} {0} -t {1}%%%{2}% -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder, txt_broj + 11))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 11))
	os.system("crunch {0} {0} -t {1}%%{2}%% -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder, txt_broj + 12))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 12))
	os.system("crunch {0} {0} -t {1}%{2}%%% -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder, txt_broj + 13))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 13))
	#combo 2 names
	os.system("crunch {0} {0} -t {1}{2}% -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 1, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder, txt_broj + 14))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 14))
	os.system("crunch {0} {0} -t {1}{2}%% -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder, txt_broj + 15))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 15))
	os.system("crunch {0} {0} -t {1}{2}%%% -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder, txt_broj + 16))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 16))
	os.system("crunch {0} {0} -t {1}{2}%%%% -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder, txt_broj + 17))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 17))
	os.system("crunch {0} {0} -t {1}%{2} -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 1, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder, txt_broj + 18))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 18))
	os.system("crunch {0} {0} -t {1}%%{2} -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder, txt_broj + 19))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 19))
	os.system("crunch {0} {0} -t {1}%%%{2} -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder, txt_broj + 20))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 20))
	os.system("crunch {0} {0} -t {1}%%%%{2} -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder, txt_broj + 21))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 21))
	os.system("crunch {0} {0} -t {1}%{2}% -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder, txt_broj + 22))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 22))
	os.system("crunch {0} {0} -t {1}%%{2}% -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder, txt_broj + 23))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 23))
	os.system("crunch {0} {0} -t {1}%{2}%% -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder, txt_broj + 24))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 24))
	os.system("crunch {0} {0} -t {1}%%%{2}% -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder, txt_broj + 25))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 25))
	os.system("crunch {0} {0} -t {1}%%{2}%% -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder, txt_broj + 26))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 26))
	os.system("crunch {0} {0} -t {1}%{2}%%% -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder, txt_broj + 27))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 27))

def dvije_rijeci_druga_numeric(rijec, folder, rijecnik, txt_broj):
	global neki_tamo_brojac

	os.system("crunch {0} {0} -t %{1}{2} -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 1, rijecnik[0][rijec], rijecnik[1][rijec], folder, txt_broj))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj))
	os.system("crunch {0} {0} -t %%{1}{2} -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][rijec], rijecnik[1][rijec], folder, txt_broj + 1))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 1))
	os.system("crunch {0} {0} -t %%%{1}{2} -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][rijec], rijecnik[1][rijec], folder, txt_broj + 2))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 2))
	os.system("crunch {0} {0} -t %%%%{1}{2} -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[0][rijec], rijecnik[1][rijec], folder, txt_broj + 3))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 3))
	os.system("crunch {0} {0} -t %{1}%{2} -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][rijec], rijecnik[1][rijec], folder, txt_broj + 4))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 4))
	os.system("crunch {0} {0} -t %%{1}%{2} -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][rijec], rijecnik[1][rijec], folder, txt_broj + 5))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 5))
	os.system("crunch {0} {0} -t %{1}%%{2} -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][rijec], rijecnik[1][rijec], folder, txt_broj + 6))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 6))
	os.system("crunch {0} {0} -t %{1}%%%{2} -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[0][rijec], rijecnik[1][rijec], folder, txt_broj + 7))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 7))
	os.system("crunch {0} {0} -t %%{1}%%{2} -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[0][rijec], rijecnik[1][rijec], folder, txt_broj + 8))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 8))
	os.system("crunch {0} {0} -t %%%{1}%{2} -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[0][rijec], rijecnik[1][rijec], folder, txt_broj + 9))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 9))
	os.system("crunch {0} {0} -t %{1}{2}% -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][rijec], rijecnik[1][rijec], folder, txt_broj + 10))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 10))
	os.system("crunch {0} {0} -t %%{1}{2}% -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][rijec], rijecnik[1][rijec], folder, txt_broj + 11))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 11))
	os.system("crunch {0} {0} -t %{1}{2}%% -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][rijec], rijecnik[1][rijec], folder, txt_broj + 12))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 12))
	os.system("crunch {0} {0} -t %%{1}{2}%% -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[0][rijec], rijecnik[1][rijec], folder, txt_broj + 13))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 13))
	os.system("crunch {0} {0} -t %%%{1}{2}% -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[0][rijec], rijecnik[1][rijec], folder, txt_broj + 14))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 14))
	os.system("crunch {0} {0} -t %{1}{2}%%% -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[0][rijec], rijecnik[1][rijec], folder, txt_broj + 15))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 15))
	#combo 2 names
	os.system("crunch {0} {0} -t %{1}{2} -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 1, rijecnik[1][rijec], rijecnik[0][rijec], folder, txt_broj + 16))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 16))
	os.system("crunch {0} {0} -t %%{1}{2} -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[1][rijec], rijecnik[0][rijec], folder, txt_broj + 17))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 17))
	os.system("crunch {0} {0} -t %%%{1}{2} -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][rijec], rijecnik[0][rijec], folder, txt_broj + 18))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 18))
	os.system("crunch {0} {0} -t %%%%{1}{2} -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[1][rijec], rijecnik[0][rijec], folder, txt_broj + 19))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 19))
	os.system("crunch {0} {0} -t %{1}%{2} -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[1][rijec], rijecnik[0][rijec], folder, txt_broj + 20))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 20))
	os.system("crunch {0} {0} -t %%{1}%{2} -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][rijec], rijecnik[0][rijec], folder, txt_broj + 21))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 21))
	os.system("crunch {0} {0} -t %{1}%%{2} -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][rijec], rijecnik[0][rijec], folder, txt_broj + 22))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 22))
	os.system("crunch {0} {0} -t %{1}%%%{2} -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[1][rijec], rijecnik[0][rijec], folder, txt_broj + 23))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 23))
	os.system("crunch {0} {0} -t %%{1}%%{2} -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[1][rijec], rijecnik[0][rijec], folder, txt_broj + 24))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 24))
	os.system("crunch {0} {0} -t %%%{1}%{2} -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[1][rijec], rijecnik[0][rijec], folder, txt_broj + 25))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 25))
	os.system("crunch {0} {0} -t %{1}{2}% -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[1][rijec], rijecnik[0][rijec], folder, txt_broj + 26))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 26))
	os.system("crunch {0} {0} -t %%{1}{2}% -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][rijec], rijecnik[0][rijec], folder, txt_broj + 27))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 27))
	os.system("crunch {0} {0} -t %{1}{2}%% -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][rijec], rijecnik[0][rijec], folder, txt_broj + 28))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 28))
	os.system("crunch {0} {0} -t %%{1}{2}%% -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[1][rijec], rijecnik[0][rijec], folder, txt_broj + 29))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 29))
	os.system("crunch {0} {0} -t %%%{1}{2}% -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[1][rijec], rijecnik[0][rijec], folder, txt_broj + 30))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 30))
	os.system("crunch {0} {0} -t %{1}{2}%%% -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[1][rijec], rijecnik[0][rijec], folder, txt_broj + 31))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 31))


#functions with 3 words start here

def dvije_rijeci_lower_alpha(broj_rijeci, folder, rijecnik, txt_broj):
	global neki_tamo_brojac

	os.system("crunch {0} {0} -t {1}{2}@ -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 1, rijecnik[0]['rijec'], rijecnik[1]['rijec'], folder, txt_broj))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj))
	os.system("crunch {0} {0} -t {1}{2}@@ -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0]['rijec'], rijecnik[1]['rijec'], folder, txt_broj + 1))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 1))
	os.system("crunch {0} {0} -t {1}{2}@@@ -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0]['rijec'], rijecnik[1]['rijec'], folder, txt_broj + 2))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 2))
	os.system("crunch {0} {0} -t {1}{2}@@@@ -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[0]['rijec'], rijecnik[1]['rijec'], folder, txt_broj + 3))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 3))
	os.system("crunch {0} {0} -t {1}@{2} -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 1, rijecnik[0]['rijec'], rijecnik[1]['rijec'], folder, txt_broj + 4))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 4))
	os.system("crunch {0} {0} -t {1}@@{2} -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0]['rijec'], rijecnik[1]['rijec'], folder, txt_broj + 5))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 5))
	os.system("crunch {0} {0} -t {1}@@@{2} -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0]['rijec'], rijecnik[1]['rijec'], folder, txt_broj + 6))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 6))
	os.system("crunch {0} {0} -t {1}@@@@{2} -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[0]['rijec'], rijecnik[1]['rijec'], folder, txt_broj + 7))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 7))
	os.system("crunch {0} {0} -t {1}@{2}@ -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0]['rijec'], rijecnik[1]['rijec'], folder, txt_broj + 8))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 8))
	os.system("crunch {0} {0} -t {1}@@{2}@ -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0]['rijec'], rijecnik[1]['rijec'], folder, txt_broj + 9))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 9))
	os.system("crunch {0} {0} -t {1}@{2}@@ -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0]['rijec'], rijecnik[1]['rijec'], folder, txt_broj + 10))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 10))
	os.system("crunch {0} {0} -t {1}@@@{2}@ -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[0]['rijec'], rijecnik[1]['rijec'], folder, txt_broj + 11))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 11))
	os.system("crunch {0} {0} -t {1}@@{2}@@ -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[0]['rijec'], rijecnik[1]['rijec'], folder, txt_broj + 12))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 12))
	os.system("crunch {0} {0} -t {1}@{2}@@@ -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[0]['rijec'], rijecnik[1]['rijec'], folder, txt_broj + 13))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 13))
	os.system("crunch {0} {0} -t @{1}{2} -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 1, rijecnik[0]['rijec'], rijecnik[1]['rijec'], folder, txt_broj + 14))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 14))
	os.system("crunch {0} {0} -t @@{1}{2} -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0]['rijec'], rijecnik[1]['rijec'], folder, txt_broj + 15))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 15))
	os.system("crunch {0} {0} -t @@@{1}{2} -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0]['rijec'], rijecnik[1]['rijec'], folder, txt_broj + 16))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 16))
	os.system("crunch {0} {0} -t @@@@{1}{2} -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[0]['rijec'], rijecnik[1]['rijec'], folder, txt_broj + 17))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 17))
	os.system("crunch {0} {0} -t @{1}@{2} -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0]['rijec'], rijecnik[1]['rijec'], folder, txt_broj + 18))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 18))
	os.system("crunch {0} {0} -t @@{1}@{2} -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0]['rijec'], rijecnik[1]['rijec'], folder, txt_broj + 19))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 19))
	os.system("crunch {0} {0} -t @{1}@@{2} -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0]['rijec'], rijecnik[1]['rijec'], folder, txt_broj + 20))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 20))
	os.system("crunch {0} {0} -t @{1}@@@{2} -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[0]['rijec'], rijecnik[1]['rijec'], folder, txt_broj + 21))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 21))
	os.system("crunch {0} {0} -t @@{1}@@{2} -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[0]['rijec'], rijecnik[1]['rijec'], folder, txt_broj + 22))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 22))
	os.system("crunch {0} {0} -t @@@{1}@{2} -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[0]['rijec'], rijecnik[1]['rijec'], folder, txt_broj + 23))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 23))
	os.system("crunch {0} {0} -t @{1}{2}@ -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0]['rijec'], rijecnik[1]['rijec'], folder, txt_broj + 24))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 24))
	os.system("crunch {0} {0} -t @@{1}{2}@ -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0]['rijec'], rijecnik[1]['rijec'], folder, txt_broj + 25))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 25))
	os.system("crunch {0} {0} -t @{1}{2}@@ -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0]['rijec'], rijecnik[1]['rijec'], folder, txt_broj + 26))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 26))
	os.system("crunch {0} {0} -t @@{1}{2}@@ -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[0]['rijec'], rijecnik[1]['rijec'], folder, txt_broj + 27))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 27))
	os.system("crunch {0} {0} -t @@@{1}{2}@ -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[0]['rijec'], rijecnik[1]['rijec'], folder, txt_broj + 28))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 28))
	os.system("crunch {0} {0} -t @{1}{2}@@@ -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[0]['rijec'], rijecnik[1]['rijec'], folder, txt_broj + 29))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 29))
	#combo 2 names
	os.system("crunch {0} {0} -t {1}{2}@ -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 1, rijecnik[1]['rijec'], rijecnik[0]['rijec'], folder, txt_broj + 30))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 30))
	os.system("crunch {0} {0} -t {1}{2}@@ -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[1]['rijec'], rijecnik[0]['rijec'], folder, txt_broj + 31))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 31))
	os.system("crunch {0} {0} -t {1}{2}@@@ -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1]['rijec'], rijecnik[0]['rijec'], folder, txt_broj + 32))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 32))
	os.system("crunch {0} {0} -t {1}{2}@@@@ -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[1]['rijec'], rijecnik[0]['rijec'], folder, txt_broj + 33))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 33))
	os.system("crunch {0} {0} -t {1}@{2} -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 1, rijecnik[1]['rijec'], rijecnik[0]['rijec'], folder, txt_broj + 34))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 34))
	os.system("crunch {0} {0} -t {1}@@{2} -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[1]['rijec'], rijecnik[0]['rijec'], folder, txt_broj + 35))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 35))
	os.system("crunch {0} {0} -t {1}@@@{2} -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1]['rijec'], rijecnik[0]['rijec'], folder, txt_broj + 36))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 36))
	os.system("crunch {0} {0} -t {1}@@@@{2} -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[1]['rijec'], rijecnik[0]['rijec'], folder, txt_broj + 37))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 37))
	os.system("crunch {0} {0} -t {1}@{2}@ -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[1]['rijec'], rijecnik[0]['rijec'], folder, txt_broj + 38))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 38))
	os.system("crunch {0} {0} -t {1}@@{2}@ -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1]['rijec'], rijecnik[0]['rijec'], folder, txt_broj + 39))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 39))
	os.system("crunch {0} {0} -t {1}@{2}@@ -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1]['rijec'], rijecnik[0]['rijec'], folder, txt_broj + 40))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 40))
	os.system("crunch {0} {0} -t {1}@@@{2}@ -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[1]['rijec'], rijecnik[0]['rijec'], folder, txt_broj + 41))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 41))
	os.system("crunch {0} {0} -t {1}@@{2}@@ -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[1]['rijec'], rijecnik[0]['rijec'], folder, txt_broj + 42))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 42))
	os.system("crunch {0} {0} -t {1}@{2}@@@ -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[1]['rijec'], rijecnik[0]['rijec'], folder, txt_broj + 43))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 43))
	os.system("crunch {0} {0} -t @{1}{2} -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 1, rijecnik[1]['rijec'], rijecnik[0]['rijec'], folder, txt_broj + 44))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 44))
	os.system("crunch {0} {0} -t @@{1}{2} -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[1]['rijec'], rijecnik[0]['rijec'], folder, txt_broj + 45))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 45))
	os.system("crunch {0} {0} -t @@@{1}{2} -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1]['rijec'], rijecnik[0]['rijec'], folder, txt_broj + 46))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 46))
	os.system("crunch {0} {0} -t @@@@{1}{2} -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[1]['rijec'], rijecnik[0]['rijec'], folder, txt_broj + 47))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 47))
	os.system("crunch {0} {0} -t @{1}@{2} -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[1]['rijec'], rijecnik[0]['rijec'], folder, txt_broj + 48))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 48))
	os.system("crunch {0} {0} -t @@{1}@{2} -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1]['rijec'], rijecnik[0]['rijec'], folder, txt_broj + 49))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 49))
	os.system("crunch {0} {0} -t @{1}@@{2} -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1]['rijec'], rijecnik[0]['rijec'], folder, txt_broj + 50))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 50))
	os.system("crunch {0} {0} -t @{1}@@@{2} -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[1]['rijec'], rijecnik[0]['rijec'], folder, txt_broj + 51))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 51))
	os.system("crunch {0} {0} -t @@{1}@@{2} -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[1]['rijec'], rijecnik[0]['rijec'], folder, txt_broj + 52))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 52))
	os.system("crunch {0} {0} -t @@@{1}@{2} -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[1]['rijec'], rijecnik[0]['rijec'], folder, txt_broj + 53))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 53))
	os.system("crunch {0} {0} -t @{1}{2}@ -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[1]['rijec'], rijecnik[0]['rijec'], folder, txt_broj + 54))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 54))
	os.system("crunch {0} {0} -t @@{1}{2}@ -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1]['rijec'], rijecnik[0]['rijec'], folder, txt_broj + 55))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 55))
	os.system("crunch {0} {0} -t @{1}{2}@@ -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1]['rijec'], rijecnik[0]['rijec'], folder, txt_broj + 56))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 56))
	os.system("crunch {0} {0} -t @@{1}{2}@@ -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[1]['rijec'], rijecnik[0]['rijec'], folder, txt_broj + 57))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 57))
	os.system("crunch {0} {0} -t @@@{1}{2}@ -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[1]['rijec'], rijecnik[0]['rijec'], folder, txt_broj + 58))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 58))
	os.system("crunch {0} {0} -t @{1}{2}@@@ -o /root/Documents/{3}/{4}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[1]['rijec'], rijecnik[0]['rijec'], folder, txt_broj + 59))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 59))

#functions with 3 words start here 

def tri_rijeci_prva_numeric(broj_rijeci, folder, rijecnik, txt_broj):
	global neki_tamo_brojac

	os.system("crunch {0} {0} -t {1}{2}{3}% -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 1, rijecnik[0]['rijec'], rijecnik[1]['rijec'], rijecnik[2]['rijec'], folder, txt_broj))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj))
	os.system("crunch {0} {0} -t {1}{2}{3}%% -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 2, rijecnik[0]['rijec'], rijecnik[1]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 1))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 1))
	os.system("crunch {0} {0} -t {1}{2}{3}%%% -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 3, rijecnik[0]['rijec'], rijecnik[1]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 2))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 2))
	os.system("crunch {0} {0} -t {1}{2}{3}%%%% -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 4, rijecnik[0]['rijec'], rijecnik[1]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 3))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 3))
	os.system("crunch {0} {0} -t {1}{2}%{3} -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 1, rijecnik[0]['rijec'], rijecnik[1]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 4))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 4))
	os.system("crunch {0} {0} -t {1}{2}%%{3} -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 2, rijecnik[0]['rijec'], rijecnik[1]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 5))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 5))
	os.system("crunch {0} {0} -t {1}{2}%%%{3} -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 3, rijecnik[0]['rijec'], rijecnik[1]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 6))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 6))
	os.system("crunch {0} {0} -t {1}{2}%%%%{3} -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 4, rijecnik[0]['rijec'], rijecnik[1]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 7))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 7))
	os.system("crunch {0} {0} -t {1}{2}%{3}% -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 2, rijecnik[0]['rijec'], rijecnik[1]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 8))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 8))
	os.system("crunch {0} {0} -t {1}{2}%%{3}% -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 3, rijecnik[0]['rijec'], rijecnik[1]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 9))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 9))
	os.system("crunch {0} {0} -t {1}{2}%{3}%% -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 3, rijecnik[0]['rijec'], rijecnik[1]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 10))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 10))
	os.system("crunch {0} {0} -t {1}{2}%%{3}%% -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 4, rijecnik[0]['rijec'], rijecnik[1]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 11))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 11))
	os.system("crunch {0} {0} -t {1}{2}%%%{3}% -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 4, rijecnik[0]['rijec'], rijecnik[1]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 12))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 12))
	os.system("crunch {0} {0} -t {1}{2}%{3}%%% -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 4, rijecnik[0]['rijec'], rijecnik[1]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 13))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 13))
	os.system("crunch {0} {0} -t {1}%{2}{3} -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 1, rijecnik[0]['rijec'], rijecnik[1]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 14))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 14))
	os.system("crunch {0} {0} -t {1}%%{2}{3} -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 2, rijecnik[0]['rijec'], rijecnik[1]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 15))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 15))
	os.system("crunch {0} {0} -t {1}%%%{2}{3} -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 3, rijecnik[0]['rijec'], rijecnik[1]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 16))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 16))
	os.system("crunch {0} {0} -t {1}%%%%{2}{3} -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 4, rijecnik[0]['rijec'], rijecnik[1]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 17))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 17))
	os.system("crunch {0} {0} -t {1}%{2}%{3} -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 2, rijecnik[0]['rijec'], rijecnik[1]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 18))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 18))
	os.system("crunch {0} {0} -t {1}%{2}{3}% -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 2, rijecnik[0]['rijec'], rijecnik[1]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 19))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 19))
	os.system("crunch {0} {0} -t {1}%{2}%%{3} -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 3, rijecnik[0]['rijec'], rijecnik[1]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 20))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 20))
	os.system("crunch {0} {0} -t {1}%%{2}%{3} -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 3, rijecnik[0]['rijec'], rijecnik[1]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 21))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 21))
	os.system("crunch {0} {0} -t {1}%{2}%{3}% -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 3, rijecnik[0]['rijec'], rijecnik[1]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 22))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 22))
	os.system("crunch {0} {0} -t {1}%{2}{3}%% -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 3, rijecnik[0]['rijec'], rijecnik[1]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 23))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 23))
	os.system("crunch {0} {0} -t {1}%%{2}{3}% -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 3, rijecnik[0]['rijec'], rijecnik[1]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 24))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 24))
	os.system("crunch {0} {0} -t {1}%%{2}%{3}% -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 4, rijecnik[0]['rijec'], rijecnik[1]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 25))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 25))
	os.system("crunch {0} {0} -t {1}%{2}%%{3}% -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 4, rijecnik[0]['rijec'], rijecnik[1]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 26))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 26))
	os.system("crunch {0} {0} -t {1}%{2}%{3}%% -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 4, rijecnik[0]['rijec'], rijecnik[1]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 27))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 27))
	os.system("crunch {0} {0} -t {1}%%%{2}%{3} -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 4, rijecnik[0]['rijec'], rijecnik[1]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 28))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 28))
	os.system("crunch {0} {0} -t {1}%%%{2}{3}% -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 4, rijecnik[0]['rijec'], rijecnik[1]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 29))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 29))
	os.system("crunch {0} {0} -t {1}%%{2}%%{3} -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 4, rijecnik[0]['rijec'], rijecnik[1]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 30))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 30))
	os.system("crunch {0} {0} -t {1}%%{2}{3}%% -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 4, rijecnik[0]['rijec'], rijecnik[1]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 31))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 31))
	os.system("crunch {0} {0} -t {1}%{2}{3}%%% -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 4, rijecnik[0]['rijec'], rijecnik[1]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 32))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 32))
	os.system("crunch {0} {0} -t %{1}{2}{3} -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 1, rijecnik[0]['rijec'], rijecnik[1]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 33))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 33))
	os.system("crunch {0} {0} -t %%{1}{2}{3} -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 2, rijecnik[0]['rijec'], rijecnik[1]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 34))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 34))
	os.system("crunch {0} {0} -t %%%{1}{2}{3} -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 3, rijecnik[0]['rijec'], rijecnik[1]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 35))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 35))
	os.system("crunch {0} {0} -t %%%%{1}{2}{3} -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 4, rijecnik[0]['rijec'], rijecnik[1]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 36))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 36))
	os.system("crunch {0} {0} -t %{1}%{2}{3} -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 2, rijecnik[0]['rijec'], rijecnik[1]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 37))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 37))
	os.system("crunch {0} {0} -t %{1}{2}%{3} -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 2, rijecnik[0]['rijec'], rijecnik[1]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 38))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 38))
	os.system("crunch {0} {0} -t %{1}{2}{3}% -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 2, rijecnik[0]['rijec'], rijecnik[1]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 39))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 39))
	os.system("crunch {0} {0} -t %{1}%%{2}{3} -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 3, rijecnik[0]['rijec'], rijecnik[1]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 40))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 40))
	os.system("crunch {0} {0} -t %{1}{2}%%{3} -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 3, rijecnik[0]['rijec'], rijecnik[1]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 41))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 41))
	os.system("crunch {0} {0} -t %{1}{2}{3}%% -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 3, rijecnik[0]['rijec'], rijecnik[1]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 42))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 42))
	os.system("crunch {0} {0} -t %%{1}%{2}{3} -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 3, rijecnik[0]['rijec'], rijecnik[1]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 43))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 43))
	os.system("crunch {0} {0} -t %%{1}{2}%{3} -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 3, rijecnik[0]['rijec'], rijecnik[1]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 44))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 44))
	os.system("crunch {0} {0} -t %%{1}{2}{3}% -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 3, rijecnik[0]['rijec'], rijecnik[1]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 45))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 45))
	os.system("crunch {0} {0} -t %%{1}%{2}%{3} -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 4, rijecnik[0]['rijec'], rijecnik[1]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 46))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 46))
	os.system("crunch {0} {0} -t %%{1}%{2}{3}% -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 4, rijecnik[0]['rijec'], rijecnik[1]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 47))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 47))
	os.system("crunch {0} {0} -t %%{1}{2}%{3}% -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 4, rijecnik[0]['rijec'], rijecnik[1]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 48))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 48))
	os.system("crunch {0} {0} -t %{1}%%{2}%{3} -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 4, rijecnik[0]['rijec'], rijecnik[1]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 49))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 49))
	os.system("crunch {0} {0} -t %{1}%{2}%%{3} -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 4, rijecnik[0]['rijec'], rijecnik[1]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 50))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 50))
	os.system("crunch {0} {0} -t %%%{1}%{2}{3} -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 4, rijecnik[0]['rijec'], rijecnik[1]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 51))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 51))
	os.system("crunch {0} {0} -t %%%{1}{2}?{3} -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 4, rijecnik[0]['rijec'], rijecnik[1]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 52))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 52))
	os.system("crunch {0} {0} -t %%%{1}{2}{3}% -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 4, rijecnik[0]['rijec'], rijecnik[1]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 53))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 53))
	os.system("crunch {0} {0} -t %{1}%%%{2}{3} -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 4, rijecnik[0]['rijec'], rijecnik[1]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 54))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 54))
	os.system("crunch {0} {0} -t %{1}{2}%%%{3} -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 4, rijecnik[0]['rijec'], rijecnik[1]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 55))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 55))
	os.system("crunch {0} {0} -t %{1}{2}{3}%%% -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 4, rijecnik[0]['rijec'], rijecnik[1]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 56))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 56))
	#1st combo 3 names
	os.system("crunch {0} {0} -t {1}{2}{3}% -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 1, rijecnik[1]['rijec'], rijecnik[0]['rijec'], rijecnik[2]['rijec'], folder, txt_broj))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj))
	os.system("crunch {0} {0} -t {1}{2}{3}%% -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 2, rijecnik[1]['rijec'], rijecnik[0]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 1))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 1))
	os.system("crunch {0} {0} -t {1}{2}{3}%%% -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 3, rijecnik[1]['rijec'], rijecnik[0]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 2))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 2))
	os.system("crunch {0} {0} -t {1}{2}{3}%%%% -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 4, rijecnik[1]['rijec'], rijecnik[0]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 3))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 3))
	os.system("crunch {0} {0} -t {1}{2}%{3} -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 1, rijecnik[1]['rijec'], rijecnik[0]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 4))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 4))
	os.system("crunch {0} {0} -t {1}{2}%%{3} -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 2, rijecnik[1]['rijec'], rijecnik[0]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 5))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 5))
	os.system("crunch {0} {0} -t {1}{2}%%%{3} -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 3, rijecnik[1]['rijec'], rijecnik[0]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 6))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 6))
	os.system("crunch {0} {0} -t {1}{2}%%%%{3} -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 4, rijecnik[1]['rijec'], rijecnik[0]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 7))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 7))
	os.system("crunch {0} {0} -t {1}{2}%{3}% -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 2, rijecnik[1]['rijec'], rijecnik[0]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 8))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 8))
	os.system("crunch {0} {0} -t {1}{2}%%{3}% -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 3, rijecnik[1]['rijec'], rijecnik[0]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 9))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 9))
	os.system("crunch {0} {0} -t {1}{2}%{3}%% -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 3, rijecnik[1]['rijec'], rijecnik[0]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 10))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 10))
	os.system("crunch {0} {0} -t {1}{2}%%{3}%% -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 4, rijecnik[1]['rijec'], rijecnik[0]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 11))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 11))
	os.system("crunch {0} {0} -t {1}{2}%%%{3}% -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 4, rijecnik[1]['rijec'], rijecnik[0]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 12))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 12))
	os.system("crunch {0} {0} -t {1}{2}%{3}%%% -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 4, rijecnik[1]['rijec'], rijecnik[0]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 13))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 13))
	os.system("crunch {0} {0} -t {1}%{2}{3} -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 1, rijecnik[1]['rijec'], rijecnik[0]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 14))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 14))
	os.system("crunch {0} {0} -t {1}%%{2}{3} -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 2, rijecnik[1]['rijec'], rijecnik[0]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 15))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 15))
	os.system("crunch {0} {0} -t {1}%%%{2}{3} -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 3, rijecnik[1]['rijec'], rijecnik[0]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 16))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 16))
	os.system("crunch {0} {0} -t {1}%%%%{2}{3} -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 4, rijecnik[1]['rijec'], rijecnik[0]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 17))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 17))
	os.system("crunch {0} {0} -t {1}%{2}%{3} -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 2, rijecnik[1]['rijec'], rijecnik[0]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 18))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 18))
	os.system("crunch {0} {0} -t {1}%{2}{3}% -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 2, rijecnik[1]['rijec'], rijecnik[0]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 19))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 19))
	os.system("crunch {0} {0} -t {1}%{2}%%{3} -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 3, rijecnik[1]['rijec'], rijecnik[0]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 20))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 20))
	os.system("crunch {0} {0} -t {1}%%{2}%{3} -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 3, rijecnik[1]['rijec'], rijecnik[0]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 21))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 21))
	os.system("crunch {0} {0} -t {1}%{2}%{3}% -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 3, rijecnik[1]['rijec'], rijecnik[0]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 22))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 22))
	os.system("crunch {0} {0} -t {1}%{2}{3}%% -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 3, rijecnik[1]['rijec'], rijecnik[0]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 23))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 23))
	os.system("crunch {0} {0} -t {1}%%{2}{3}% -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 3, rijecnik[1]['rijec'], rijecnik[0]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 24))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 24))
	os.system("crunch {0} {0} -t {1}%%{2}%{3}% -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 4, rijecnik[1]['rijec'], rijecnik[0]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 25))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 25))
	os.system("crunch {0} {0} -t {1}%{2}%%{3}% -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 4, rijecnik[1]['rijec'], rijecnik[0]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 26))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 26))
	os.system("crunch {0} {0} -t {1}%{2}%{3}%% -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 4, rijecnik[1]['rijec'], rijecnik[0]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 27))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 27))
	os.system("crunch {0} {0} -t {1}%%%{2}%{3} -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 4, rijecnik[1]['rijec'], rijecnik[0]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 28))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 28))
	os.system("crunch {0} {0} -t {1}%%%{2}{3}% -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 4, rijecnik[1]['rijec'], rijecnik[0]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 29))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 29))
	os.system("crunch {0} {0} -t {1}%%{2}%%{3} -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 4, rijecnik[1]['rijec'], rijecnik[0]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 30))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 30))
	os.system("crunch {0} {0} -t {1}%%{2}{3}%% -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 4, rijecnik[1]['rijec'], rijecnik[0]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 31))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 31))
	os.system("crunch {0} {0} -t {1}%{2}{3}%%% -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 4, rijecnik[1]['rijec'], rijecnik[0]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 32))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 32))
	os.system("crunch {0} {0} -t %{1}{2}{3} -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 1, rijecnik[1]['rijec'], rijecnik[0]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 33))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 33))
	os.system("crunch {0} {0} -t %%{1}{2}{3} -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 2, rijecnik[1]['rijec'], rijecnik[0]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 34))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 34))
	os.system("crunch {0} {0} -t %%%{1}{2}{3} -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 3, rijecnik[1]['rijec'], rijecnik[0]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 35))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 35))
	os.system("crunch {0} {0} -t %%%%{1}{2}{3} -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 4, rijecnik[1]['rijec'], rijecnik[0]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 36))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 36))
	os.system("crunch {0} {0} -t %{1}%{2}{3} -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 2, rijecnik[1]['rijec'], rijecnik[0]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 37))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 37))
	os.system("crunch {0} {0} -t %{1}{2}%{3} -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 2, rijecnik[1]['rijec'], rijecnik[0]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 38))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 38))
	os.system("crunch {0} {0} -t %{1}{2}{3}% -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 2, rijecnik[1]['rijec'], rijecnik[0]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 39))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 39))
	os.system("crunch {0} {0} -t %{1}%%{2}{3} -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 3, rijecnik[1]['rijec'], rijecnik[0]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 40))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 40))
	os.system("crunch {0} {0} -t %{1}{2}%%{3} -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 3, rijecnik[1]['rijec'], rijecnik[0]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 41))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 41))
	os.system("crunch {0} {0} -t %{1}{2}{3}%% -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 3, rijecnik[1]['rijec'], rijecnik[0]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 42))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 42))
	os.system("crunch {0} {0} -t %%{1}%{2}{3} -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 3, rijecnik[1]['rijec'], rijecnik[0]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 43))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 43))
	os.system("crunch {0} {0} -t %%{1}{2}%{3} -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 3, rijecnik[1]['rijec'], rijecnik[0]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 44))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 44))
	os.system("crunch {0} {0} -t %%{1}{2}{3}% -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 3, rijecnik[1]['rijec'], rijecnik[0]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 45))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 45))
	os.system("crunch {0} {0} -t %%{1}%{2}%{3} -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 4, rijecnik[1]['rijec'], rijecnik[0]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 46))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 46))
	os.system("crunch {0} {0} -t %%{1}%{2}{3}% -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 4, rijecnik[1]['rijec'], rijecnik[0]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 47))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 47))
	os.system("crunch {0} {0} -t %%{1}{2}%{3}% -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 4, rijecnik[1]['rijec'], rijecnik[0]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 48))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 48))
	os.system("crunch {0} {0} -t %{1}%%{2}%{3} -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 4, rijecnik[1]['rijec'], rijecnik[0]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 49))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 49))
	os.system("crunch {0} {0} -t %{1}%{2}%%{3} -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 4, rijecnik[1]['rijec'], rijecnik[0]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 50))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 50))
	os.system("crunch {0} {0} -t %%%{1}%{2}{3} -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 4, rijecnik[1]['rijec'], rijecnik[0]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 51))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 51))
	os.system("crunch {0} {0} -t %%%{1}{2}?{3} -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 4, rijecnik[1]['rijec'], rijecnik[0]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 52))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 52))
	os.system("crunch {0} {0} -t %%%{1}{2}{3}% -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 4, rijecnik[1]['rijec'], rijecnik[0]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 53))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 53))
	os.system("crunch {0} {0} -t %{1}%%%{2}{3} -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 4, rijecnik[1]['rijec'], rijecnik[0]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 54))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 54))
	os.system("crunch {0} {0} -t %{1}{2}%%%{3} -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 4, rijecnik[1]['rijec'], rijecnik[0]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 55))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 55))
	os.system("crunch {0} {0} -t %{1}{2}{3}%%% -o /root/Documents/{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + rijecnik[2]['rijec_duzina'] + 4, rijecnik[1]['rijec'], rijecnik[0]['rijec'], rijecnik[2]['rijec'], folder, txt_broj + 56))
	neki_tamo_brojac += os.path.getsize('/root/Documents/{0}/{1}.txt'.format(folder, txt_broj + 56))
	#2nd combo 3 names

	
os.system("crunch")
time.sleep(1)

#looping to make sure that the user enters min 1 and max 5 words

while(True):
	broj_ukupnih_rijeci = input("Unesite broj ukupnih rijeci:")

	if (1 <= int(broj_ukupnih_rijeci) < 6):
		break

	print("Minimalan broj rijeci je 1, a maksimalan 5.\nMolimo Vas, pokusajte ponovo!\n")

if (broj_ukupnih_rijeci == 1):
	neki_tamo_brojac = 0
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

	print("\nVelicina foldera iznosi:\n{0:.2f}MB".format(float(neki_tamo_brojac)/1024/1024))

	druga_numeric(rijec, rijec, 17)
	druga_numeric(rijec_prvo_slovo_upper, rijec, 21)
	druga_numeric(rijec_zadnje_slovo_upper, rijec, 25)
	druga_numeric(rijec_sva_slova_upper, rijec, 29)

	print("\nVelicina foldera iznosi:\n{0:.2f}MB".format(float(neki_tamo_brojac)/1024/1024))

	prva_lower_alpha(rijec, rijec, 33)
	prva_lower_alpha(rijec_prvo_slovo_upper, rijec, 37)
	prva_lower_alpha(rijec_zadnje_slovo_upper, rijec, 41)
	prva_lower_alpha(rijec_sva_slova_upper, rijec, 45)

	print("\nVelicina foldera iznosi:\n{0:.2f}MB".format(float(neki_tamo_brojac)/1024/1024))

	#48 files - 21.8MB

	druga_lower_alpha(rijec, rijec, 49)
	druga_lower_alpha(rijec_prvo_slovo_upper, rijec, 53)
	druga_lower_alpha(rijec_zadnje_slovo_upper, rijec, 57)
	druga_lower_alpha(rijec_sva_slova_upper, rijec, 61)

	print("\nVelicina foldera iznosi:\n{0:.2f}MB".format(float(neki_tamo_brojac)/1024/1024))

	prva_upper_alpha(rijec, rijec, 65)
	prva_upper_alpha(rijec_prvo_slovo_upper, rijec, 69)
	prva_upper_alpha(rijec_zadnje_slovo_upper, rijec, 73)
	prva_upper_alpha(rijec_sva_slova_upper, rijec, 77)

	print("\nVelicina foldera iznosi:\n{0:.2f}MB".format(float(neki_tamo_brojac)/1024/1024))

	druga_upper_alpha(rijec, rijec, 81)
	druga_upper_alpha(rijec_prvo_slovo_upper, rijec, 85)
	druga_upper_alpha(rijec_zadnje_slovo_upper, rijec, 89)
	druga_upper_alpha(rijec_sva_slova_upper, rijec, 93)

	print("\nVelicina foldera iznosi:\n{0:.2f}MB".format(float(neki_tamo_brojac)/1024/1024))

	#96 files - 72.9MB

	prva_mix_upper_lower(rijec, rijec, 97)
	prva_mix_upper_lower(rijec_prvo_slovo_upper, rijec, 105)
	prva_mix_upper_lower(rijec_zadnje_slovo_upper, rijec, 113)
	prva_mix_upper_lower(rijec_sva_slova_upper, rijec, 121)

	print("\nVelicina foldera iznosi:\n{0:.2f}MB".format(float(neki_tamo_brojac)/1024/1024))

	#128 files - 78.9MB

	druga_mix_upper_lower(rijec, rijec, 129)
	druga_mix_upper_lower(rijec_prvo_slovo_upper, rijec, 137)
	druga_mix_upper_lower(rijec_zadnje_slovo_upper, rijec, 145)
	druga_mix_upper_lower(rijec_sva_slova_upper, rijec, 153)

	print("\nVelicina foldera iznosi:\n{0:.2f}MB".format(float(neki_tamo_brojac)/1024/1024))

	prva_mix_upper_numeric(rijec, rijec, 161)
	prva_mix_upper_numeric(rijec_prvo_slovo_upper, rijec, 169)
	prva_mix_upper_numeric(rijec_zadnje_slovo_upper, rijec, 177)
	prva_mix_upper_numeric(rijec_sva_slova_upper, rijec, 185)

	print("\nVelicina foldera iznosi:\n{0:.2f}MB".format(float(neki_tamo_brojac)/1024/1024))

	druga_mix_upper_numeric(rijec, rijec, 193)
	druga_mix_upper_numeric(rijec_prvo_slovo_upper, rijec, 201)
	druga_mix_upper_numeric(rijec_zadnje_slovo_upper, rijec, 209)
	druga_mix_upper_numeric(rijec_sva_slova_upper, rijec, 217)

	print("\nVelicina foldera iznosi:\n{0:.2f}MB".format(float(neki_tamo_brojac)/1024/1024))

	#224 files - 87.4MB

	prva_mix_lower_numeric(rijec, rijec, 225)
	prva_mix_lower_numeric(rijec_prvo_slovo_upper, rijec, 233)
	prva_mix_lower_numeric(rijec_zadnje_slovo_upper, rijec, 241)
	prva_mix_lower_numeric(rijec_sva_slova_upper, rijec, 249)

	print("\nVelicina foldera iznosi:\n{0:.2f}MB".format(float(neki_tamo_brojac)/1024/1024))

	druga_mix_lower_numeric(rijec, rijec, 257)
	druga_mix_lower_numeric(rijec_prvo_slovo_upper, rijec, 265)
	druga_mix_lower_numeric(rijec_zadnje_slovo_upper, rijec, 273)
	druga_mix_lower_numeric(rijec_sva_slova_upper, rijec, 281)

	print("\nVelicina foldera iznosi:\n{0:.2f}MB".format(float(neki_tamo_brojac)/1024/1024))

	#288 files - 89.7MB

	prva_mix_lower_upper_numeric(rijec, rijec, 289)
	prva_mix_lower_upper_numeric(rijec_prvo_slovo_upper, rijec, 295)
	prva_mix_lower_upper_numeric(rijec_zadnje_slovo_upper, rijec, 301)
	prva_mix_lower_upper_numeric(rijec_sva_slova_upper, rijec, 307)

	print("\nVelicina foldera iznosi:\n{0:.2f}MB".format(float(neki_tamo_brojac)/1024/1024))

	druga_mix_lower_upper_numeric(rijec, rijec, 313)
	druga_mix_lower_upper_numeric(rijec_prvo_slovo_upper, rijec, 319)
	druga_mix_lower_upper_numeric(rijec_zadnje_slovo_upper, rijec, 325)
	druga_mix_lower_upper_numeric(rijec_sva_slova_upper, rijec, 331)

	print("\nVelicina foldera iznosi:\n{0:.2f}MB".format(float(neki_tamo_brojac)/1024/1024))

	#336 files - 92.6MB

	prva_char(rijec, rijec, 337)
	prva_char(rijec_prvo_slovo_upper, rijec, 341)
	prva_char(rijec_zadnje_slovo_upper, rijec, 345)
	prva_char(rijec_sva_slova_upper, rijec, 349)

	print("\nVelicina foldera iznosi:\n{0:.2f}MB".format(float(neki_tamo_brojac)/1024/1024))

	druga_char(rijec, rijec, 353)
	druga_char(rijec_prvo_slovo_upper, rijec, 357)
	druga_char(rijec_zadnje_slovo_upper, rijec, 361)
	druga_char(rijec_sva_slova_upper, rijec, 365)

	print("\nVelicina foldera iznosi:\n{0:.2f}MB".format(float(neki_tamo_brojac)/1024/1024))

	prva_mix_upper_char(rijec, rijec, 369)
	prva_mix_upper_char(rijec_prvo_slovo_upper, rijec, 377)
	prva_mix_upper_char(rijec_zadnje_slovo_upper, rijec, 385)
	prva_mix_upper_char(rijec_sva_slova_upper, rijec, 393)

	print("\nVelicina foldera iznosi:\n{0:.2f}MB".format(float(neki_tamo_brojac)/1024/1024))

	druga_mix_upper_char(rijec, rijec, 401)
	druga_mix_upper_char(rijec_prvo_slovo_upper, rijec, 409)
	druga_mix_upper_char(rijec_zadnje_slovo_upper, rijec, 417)
	druga_mix_upper_char(rijec_sva_slova_upper, rijec, 425)

	print("\nVelicina foldera iznosi:\n{0:.2f}MB".format(float(neki_tamo_brojac)/1024/1024))

	prva_mix_lower_char(rijec, rijec, 433)
	prva_mix_lower_char(rijec_prvo_slovo_upper, rijec, 441)
	prva_mix_lower_char(rijec_zadnje_slovo_upper, rijec, 449)
	prva_mix_lower_char(rijec_sva_slova_upper, rijec, 457)

	print("\nVelicina foldera iznosi:\n{0:.2f}MB".format(float(neki_tamo_brojac)/1024/1024))

	druga_mix_lower_char(rijec, rijec, 465)
	druga_mix_lower_char(rijec_prvo_slovo_upper, rijec, 473)
	druga_mix_lower_char(rijec_zadnje_slovo_upper, rijec, 481)
	druga_mix_lower_char(rijec_sva_slova_upper, rijec, 489)

	print("\nVelicina foldera iznosi:\n{0:.2f}MB".format(float(neki_tamo_brojac)/1024/1024))

	prva_mix_numeric_char(rijec, rijec, 497)
	prva_mix_numeric_char(rijec_prvo_slovo_upper, rijec, 505)
	prva_mix_numeric_char(rijec_zadnje_slovo_upper, rijec, 513)
	prva_mix_numeric_char(rijec_sva_slova_upper, rijec, 521)

	print("\nVelicina foldera iznosi:\n{0:.2f}MB".format(float(neki_tamo_brojac)/1024/1024))

	druga_mix_numeric_char(rijec, rijec, 529)
	druga_mix_numeric_char(rijec_prvo_slovo_upper, rijec, 537)
	druga_mix_numeric_char(rijec_zadnje_slovo_upper, rijec, 545)
	druga_mix_numeric_char(rijec_sva_slova_upper, rijec, 553)

	print("\nVelicina foldera iznosi:\n{0:.2f}MB".format(float(neki_tamo_brojac)/1024/1024))

	#560 files - 202.7MB

	prva_mix_upper_lower_char(rijec, rijec, 561)
	prva_mix_upper_lower_char(rijec_prvo_slovo_upper, rijec, 567)
	prva_mix_upper_lower_char(rijec_zadnje_slovo_upper, rijec, 573)
	prva_mix_upper_lower_char(rijec_sva_slova_upper, rijec, 579)

	print("\nVelicina foldera iznosi:\n{0:.2f}MB".format(float(neki_tamo_brojac)/1024/1024))

	druga_mix_upper_lower_char(rijec, rijec, 585)
	druga_mix_upper_lower_char(rijec_prvo_slovo_upper, rijec, 591)
	druga_mix_upper_lower_char(rijec_zadnje_slovo_upper, rijec, 597)
	druga_mix_upper_lower_char(rijec_sva_slova_upper, rijec, 603)

	print("\nVelicina foldera iznosi:\n{0:.2f}MB".format(float(neki_tamo_brojac)/1024/1024))

	prva_mix_upper_numeric_char(rijec, rijec, 609)
	prva_mix_upper_numeric_char(rijec_prvo_slovo_upper, rijec, 615)
	prva_mix_upper_numeric_char(rijec_zadnje_slovo_upper, rijec, 621)
	prva_mix_upper_numeric_char(rijec_sva_slova_upper, rijec, 627)

	print("\nVelicina foldera iznosi:\n{0:.2f}MB".format(float(neki_tamo_brojac)/1024/1024))

	druga_mix_upper_numeric_char(rijec, rijec, 633)
	druga_mix_upper_numeric_char(rijec_prvo_slovo_upper, rijec, 639)
	druga_mix_upper_numeric_char(rijec_zadnje_slovo_upper, rijec, 645)
	druga_mix_upper_numeric_char(rijec_sva_slova_upper, rijec, 651)

	print("\nVelicina foldera iznosi:\n{0:.2f}MB".format(float(neki_tamo_brojac)/1024/1024))

	#656 files - 214.6MB

elif (broj_ukupnih_rijeci == 2):
	neki_tamo_brojac = 0
	sve_rijeci_dictionary = {}
	naziv_foldera = ""

	for x in range(broj_ukupnih_rijeci):
		rijec = raw_input("Unesite {0}. rijec:".format(x + 1))
		rijec_duzina = len(rijec)

		sve_rijeci_dictionary[x] = {}
		sve_rijeci_dictionary[x]["rijec"] = rijec
		sve_rijeci_dictionary[x]["rijec_duzina"] = rijec_duzina
		sve_rijeci_dictionary[x]["rijec_prvo_slovo_upper"] = rijec[0].upper() + rijec[1:]
		sve_rijeci_dictionary[x]["rijec_zadnje_slovo_upper"] = rijec[:(rijec_duzina - 1)] + rijec[(rijec_duzina) - 1].upper()
		sve_rijeci_dictionary[x]["rijec_sva_slova_upper"] = rijec.upper()

		naziv_foldera += rijec

	os.system("mkdir /root/Documents/{0}".format(naziv_foldera))

	dvije_rijeci_prva_numeric("rijec", "rijec", naziv_foldera, sve_rijeci_dictionary, 1)
	dvije_rijeci_prva_numeric("rijec_prvo_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 29)
	dvije_rijeci_prva_numeric("rijec_prvo_slovo_upper", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 57)
	dvije_rijeci_prva_numeric("rijec", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 85)

	dvije_rijeci_prva_numeric("rijec_zadnje_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 113)
	dvije_rijeci_prva_numeric("rijec_zadnje_slovo_upper", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 141)
	dvije_rijeci_prva_numeric("rijec", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 169)

	dvije_rijeci_prva_numeric("rijec_sva_slova_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 197)
	dvije_rijeci_prva_numeric("rijec_sva_slova_upper", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 225)
	dvije_rijeci_prva_numeric("rijec", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 253)

	print("\nVelicina foldera iznosi:\n{0:.2f}MB".format(float(neki_tamo_brojac)/1024/1024))

	# dvije_rijeci_druga_numeric("rijec", naziv_foldera, sve_rijeci_dictionary, 113)
	# dvije_rijeci_druga_numeric("rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 145)
	# dvije_rijeci_druga_numeric("rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 177)
	# dvije_rijeci_druga_numeric("rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 209)

elif (broj_ukupnih_rijeci == 3):
	pass

elif (broj_ukupnih_rijeci == 4):
	pass

else:
	pass

##############################testiramo nesto#######################################################
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


