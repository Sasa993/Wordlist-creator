import os
import time

#1.parametar: rijec, odnosno naziv mreze
#2.parametar: rijec_original, odnosno naziv foldera
#3.parametar: txt_broj, odnosno naziv txt fajla, tj. wordlista || dictionary
def prva_numeric(rijec, rijec_original, txt_broj):
	os.system("crunch {0} {0} -t {1}% -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 1,rijec, rijec_original, txt_broj))
	os.system("crunch {0} {0} -t {1}%% -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 2,rijec, rijec_original, txt_broj + 1))
	os.system("crunch {0} {0} -t {1}%%% -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 2))
	os.system("crunch {0} {0} -t {1}%%%% -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 4,rijec, rijec_original, txt_broj + 3))

def druga_numeric(rijec, rijec_original, txt_broj):
	os.system("crunch {0} {0} -t %{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 1,rijec, rijec_original, txt_broj))
	os.system("crunch {0} {0} -t %%{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 2,rijec, rijec_original, txt_broj + 1))
	os.system("crunch {0} {0} -t %%%{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 2))
	os.system("crunch {0} {0} -t %%%%{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 4,rijec, rijec_original, txt_broj + 3))

def prva_lower_alpha(rijec, rijec_original, txt_broj):
	os.system("crunch {0} {0} -t {1}@ -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 1,rijec, rijec_original, txt_broj))
	os.system("crunch {0} {0} -t {1}@@ -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 2,rijec, rijec_original, txt_broj + 1))
	os.system("crunch {0} {0} -t {1}@@@ -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 2))
	os.system("crunch {0} {0} -t {1}@@@@ -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 4,rijec, rijec_original, txt_broj + 3))

def druga_lower_alpha(rijec, rijec_original, txt_broj):
	os.system("crunch {0} {0} -t @{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 1,rijec, rijec_original, txt_broj))
	os.system("crunch {0} {0} -t @@{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 2,rijec, rijec_original, txt_broj + 1))
	os.system("crunch {0} {0} -t @@@{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 2))
	os.system("crunch {0} {0} -t @@@@{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 4,rijec, rijec_original, txt_broj + 3))

def prva_upper_alpha(rijec, rijec_original, txt_broj):
	os.system("crunch {0} {0} -t {1}, -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 1,rijec, rijec_original, txt_broj))
	os.system("crunch {0} {0} -t {1},, -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 2,rijec, rijec_original, txt_broj + 1))
	os.system("crunch {0} {0} -t {1},,, -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 2))
	os.system("crunch {0} {0} -t {1},,,, -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 4,rijec, rijec_original, txt_broj + 3))

def druga_upper_alpha(rijec, rijec_original, txt_broj):
	os.system("crunch {0} {0} -t ,{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 1,rijec, rijec_original, txt_broj))
	os.system("crunch {0} {0} -t ,,{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 2,rijec, rijec_original, txt_broj + 1))
	os.system("crunch {0} {0} -t ,,,{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 2))
	os.system("crunch {0} {0} -t ,,,,{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 4,rijec, rijec_original, txt_broj + 3))

def prva_mix_upper_lower(rijec, rijec_original, txt_broj):
	os.system("crunch {0} {0} -t ,@{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 2,rijec, rijec_original, txt_broj))
	os.system("crunch {0} {0} -t @,{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 2,rijec, rijec_original, txt_broj + 1))
	os.system("crunch {0} {0} -t @,,{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 2))
	os.system("crunch {0} {0} -t ,@,{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 3))
	os.system("crunch {0} {0} -t ,,@{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 4))
	os.system("crunch {0} {0} -t @@,{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 5))
	os.system("crunch {0} {0} -t ,@@{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 6))
	os.system("crunch {0} {0} -t @,@{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 7))

def druga_mix_upper_lower(rijec, rijec_original, txt_broj):
	os.system("crunch {0} {0} -t {1},@ -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 2,rijec, rijec_original, txt_broj))
	os.system("crunch {0} {0} -t {1}@, -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 2,rijec, rijec_original, txt_broj + 1))
	os.system("crunch {0} {0} -t {1}@,, -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 2))
	os.system("crunch {0} {0} -t {1},@, -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 3))
	os.system("crunch {0} {0} -t {1},,@ -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 4))
	os.system("crunch {0} {0} -t {1}@@, -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 5))
	os.system("crunch {0} {0} -t {1},@@ -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 6))
	os.system("crunch {0} {0} -t {1}@,@ -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 7))

def prva_mix_upper_numeric(rijec, rijec_original, txt_broj):
	os.system("crunch {0} {0} -t ,%{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 2,rijec, rijec_original, txt_broj))
	os.system("crunch {0} {0} -t %,{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 2,rijec, rijec_original, txt_broj + 1))
	os.system("crunch {0} {0} -t %,,{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 2))
	os.system("crunch {0} {0} -t ,%,{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 3))
	os.system("crunch {0} {0} -t ,,%{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 4))
	os.system("crunch {0} {0} -t %%,{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 5))
	os.system("crunch {0} {0} -t ,%%{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 6))
	os.system("crunch {0} {0} -t %,%{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 7))

def druga_mix_upper_numeric(rijec, rijec_original, txt_broj):
	os.system("crunch {0} {0} -t {1},% -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 2,rijec, rijec_original, txt_broj))
	os.system("crunch {0} {0} -t {1}%, -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 2,rijec, rijec_original, txt_broj + 1))
	os.system("crunch {0} {0} -t {1}%,, -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 2))
	os.system("crunch {0} {0} -t {1},%, -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 3))
	os.system("crunch {0} {0} -t {1},,% -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 4))
	os.system("crunch {0} {0} -t {1}%%, -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 5))
	os.system("crunch {0} {0} -t {1},%% -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 6))
	os.system("crunch {0} {0} -t {1}%,% -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 7))

def prva_mix_lower_numeric(rijec, rijec_original, txt_broj):
	os.system("crunch {0} {0} -t %@{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 2,rijec, rijec_original, txt_broj))
	os.system("crunch {0} {0} -t @%{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 2,rijec, rijec_original, txt_broj + 1))
	os.system("crunch {0} {0} -t @%%{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 2))
	os.system("crunch {0} {0} -t %@%{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 3))
	os.system("crunch {0} {0} -t %%@{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 4))
	os.system("crunch {0} {0} -t @@%{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 5))
	os.system("crunch {0} {0} -t %@@{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 6))
	os.system("crunch {0} {0} -t @%@{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 7))

def druga_mix_lower_numeric(rijec, rijec_original, txt_broj):
	os.system("crunch {0} {0} -t {1}%@ -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 2,rijec, rijec_original, txt_broj))
	os.system("crunch {0} {0} -t {1}@% -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 2,rijec, rijec_original, txt_broj + 1))
	os.system("crunch {0} {0} -t {1}@%% -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 2))
	os.system("crunch {0} {0} -t {1}%@% -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 3))
	os.system("crunch {0} {0} -t {1}%%@ -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 4))
	os.system("crunch {0} {0} -t {1}@@% -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 5))
	os.system("crunch {0} {0} -t {1}%@@ -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 6))
	os.system("crunch {0} {0} -t {1}@%@ -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 7))

def prva_mix_lower_upper_numeric(rijec, rijec_original, txt_broj):
	os.system("crunch {0} {0} -t @,%{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj))
	os.system("crunch {0} {0} -t @%,{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 1))
	os.system("crunch {0} {0} -t ,@%{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 2))
	os.system("crunch {0} {0} -t ,%@{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 3))
	os.system("crunch {0} {0} -t %@,{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 4))
	os.system("crunch {0} {0} -t %,@{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 5))
	
def druga_mix_lower_upper_numeric(rijec, rijec_original, txt_broj):
	os.system("crunch {0} {0} -t {1}@,% -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj))
	os.system("crunch {0} {0} -t {1}@%, -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 1))
	os.system("crunch {0} {0} -t {1},@% -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 2))
	os.system("crunch {0} {0} -t {1},%@ -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 3))
	os.system("crunch {0} {0} -t {1}%@, -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 4))
	os.system("crunch {0} {0} -t {1}%,@ -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 5))
	
def prva_char(rijec, rijec_original, txt_broj):
	os.system("crunch {0} {0} -t ^{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 1,rijec, rijec_original, txt_broj))
	os.system("crunch {0} {0} -t ^^{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 2,rijec, rijec_original, txt_broj + 1))
	os.system("crunch {0} {0} -t ^^^{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 2))
	os.system("crunch {0} {0} -t ^^^^{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 4,rijec, rijec_original, txt_broj + 3))

def druga_char(rijec, rijec_original, txt_broj):
	os.system("crunch {0} {0} -t {1}^ -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 1,rijec, rijec_original, txt_broj))
	os.system("crunch {0} {0} -t {1}^^ -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 2,rijec, rijec_original, txt_broj + 1))
	os.system("crunch {0} {0} -t {1}^^^ -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 2))
	os.system("crunch {0} {0} -t {1}^^^^ -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 4,rijec, rijec_original, txt_broj + 3))

def prva_mix_upper_char(rijec, rijec_original, txt_broj):
	os.system("crunch {0} {0} -t ,^{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 2,rijec, rijec_original, txt_broj))
	os.system("crunch {0} {0} -t ^,{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 2,rijec, rijec_original, txt_broj + 1))
	os.system("crunch {0} {0} -t ^,,{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 2))
	os.system("crunch {0} {0} -t ,^,{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 3))
	os.system("crunch {0} {0} -t ,,^{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 4))
	os.system("crunch {0} {0} -t ^^,{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 5))
	os.system("crunch {0} {0} -t ,^^{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 6))
	os.system("crunch {0} {0} -t ^,^{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 7))

def druga_mix_upper_char(rijec, rijec_original, txt_broj):
	os.system("crunch {0} {0} -t {1},^ -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 2,rijec, rijec_original, txt_broj))
	os.system("crunch {0} {0} -t {1}^, -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 2,rijec, rijec_original, txt_broj + 1))
	os.system("crunch {0} {0} -t {1}^,, -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 2))
	os.system("crunch {0} {0} -t {1},^, -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 3))
	os.system("crunch {0} {0} -t {1},,^ -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 4))
	os.system("crunch {0} {0} -t {1}^^, -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 5))
	os.system("crunch {0} {0} -t {1},^^ -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 6))
	os.system("crunch {0} {0} -t {1}^,^ -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 7))

def prva_mix_lower_char(rijec, rijec_original, txt_broj):
	os.system("crunch {0} {0} -t @^{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 2,rijec, rijec_original, txt_broj))
	os.system("crunch {0} {0} -t ^@{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 2,rijec, rijec_original, txt_broj + 1))
	os.system("crunch {0} {0} -t ^@@{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 2))
	os.system("crunch {0} {0} -t @^@{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 3))
	os.system("crunch {0} {0} -t @@^{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 4))
	os.system("crunch {0} {0} -t ^^@{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 5))
	os.system("crunch {0} {0} -t @^^{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 6))
	os.system("crunch {0} {0} -t ^@^{1} -o /root/Documents/{2}/{3}.txt".format(rijec_duzina + 3,rijec, rijec_original, txt_broj + 7))

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

prva_mix_upper_lower(rijec, rijec, 97)
prva_mix_upper_lower(rijec_prvo_slovo_upper, rijec, 105)
prva_mix_upper_lower(rijec_zadnje_slovo_upper, rijec, 113)
prva_mix_upper_lower(rijec_sva_slova_upper, rijec, 121)

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

prva_mix_lower_numeric(rijec, rijec, 225)
prva_mix_lower_numeric(rijec_prvo_slovo_upper, rijec, 233)
prva_mix_lower_numeric(rijec_zadnje_slovo_upper, rijec, 241)
prva_mix_lower_numeric(rijec_sva_slova_upper, rijec, 249)

druga_mix_lower_numeric(rijec, rijec, 257)
druga_mix_lower_numeric(rijec_prvo_slovo_upper, rijec, 265)
druga_mix_lower_numeric(rijec_zadnje_slovo_upper, rijec, 273)
druga_mix_lower_numeric(rijec_sva_slova_upper, rijec, 281)


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


