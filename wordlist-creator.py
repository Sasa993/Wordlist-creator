import os
import time

#1.parameter: rijec - word
#2.parameter: rijec_original - name of the folder
#3.parameter: txt_broj - name of the .txt file which is created by that function
folder_path = ""
os.chdir("..")

def prva_numeric(rijec, rijec_original, txt_broj):
	os.system("crunch {0} {0} -t {1}% -o {2}{3}/{4}.txt".format(rijec_duzina + 1,rijec, folder_path, rijec_original, txt_broj))	
	os.system("crunch {0} {0} -t {1}%% -o {2}{3}/{4}.txt".format(rijec_duzina + 2,rijec, folder_path, rijec_original, txt_broj + 1))	
	os.system("crunch {0} {0} -t {1}%%% -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 2))	
	os.system("crunch {0} {0} -t {1}%%%% -o {2}{3}/{4}.txt".format(rijec_duzina + 4,rijec, folder_path, rijec_original, txt_broj + 3))	

def druga_numeric(rijec, rijec_original, txt_broj):
	os.system("crunch {0} {0} -t %{1} -o {2}{3}/{4}.txt".format(rijec_duzina + 1,rijec, folder_path, rijec_original, txt_broj))	
	os.system("crunch {0} {0} -t %%{1} -o {2}{3}/{4}.txt".format(rijec_duzina + 2,rijec, folder_path, rijec_original, txt_broj + 1))	
	os.system("crunch {0} {0} -t %%%{1} -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 2))	
	os.system("crunch {0} {0} -t %%%%{1} -o {2}{3}/{4}.txt".format(rijec_duzina + 4,rijec, folder_path, rijec_original, txt_broj + 3))	

def prva_lower_alpha(rijec, rijec_original, txt_broj):
	os.system("crunch {0} {0} -t {1}@ -o {2}{3}/{4}.txt".format(rijec_duzina + 1,rijec, folder_path, rijec_original, txt_broj))	
	os.system("crunch {0} {0} -t {1}@@ -o {2}{3}/{4}.txt".format(rijec_duzina + 2,rijec, folder_path, rijec_original, txt_broj + 1))	
	os.system("crunch {0} {0} -t {1}@@@ -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 2))	
	os.system("crunch {0} {0} -t {1}@@@@ -o {2}{3}/{4}.txt".format(rijec_duzina + 4,rijec, folder_path, rijec_original, txt_broj + 3))	

def druga_lower_alpha(rijec, rijec_original, txt_broj):
	os.system("crunch {0} {0} -t @{1} -o {2}{3}/{4}.txt".format(rijec_duzina + 1,rijec, folder_path, rijec_original, txt_broj))	
	os.system("crunch {0} {0} -t @@{1} -o {2}{3}/{4}.txt".format(rijec_duzina + 2,rijec, folder_path, rijec_original, txt_broj + 1))	
	os.system("crunch {0} {0} -t @@@{1} -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 2))	
	os.system("crunch {0} {0} -t @@@@{1} -o {2}{3}/{4}.txt".format(rijec_duzina + 4,rijec, folder_path, rijec_original, txt_broj + 3))

def prva_upper_alpha(rijec, rijec_original, txt_broj):
	os.system("crunch {0} {0} -t {1}, -o {2}{3}/{4}.txt".format(rijec_duzina + 1,rijec, folder_path, rijec_original, txt_broj))	
	os.system("crunch {0} {0} -t {1},, -o {2}{3}/{4}.txt".format(rijec_duzina + 2,rijec, folder_path, rijec_original, txt_broj + 1))	
	os.system("crunch {0} {0} -t {1},,, -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 2))	
	os.system("crunch {0} {0} -t {1},,,, -o {2}{3}/{4}.txt".format(rijec_duzina + 4,rijec, folder_path, rijec_original, txt_broj + 3))
	

def druga_upper_alpha(rijec, rijec_original, txt_broj):
	os.system("crunch {0} {0} -t ,{1} -o {2}{3}/{4}.txt".format(rijec_duzina + 1,rijec, folder_path, rijec_original, txt_broj))	
	os.system("crunch {0} {0} -t ,,{1} -o {2}{3}/{4}.txt".format(rijec_duzina + 2,rijec, folder_path, rijec_original, txt_broj + 1))	
	os.system("crunch {0} {0} -t ,,,{1} -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 2))	
	os.system("crunch {0} {0} -t ,,,,{1} -o {2}{3}/{4}.txt".format(rijec_duzina + 4,rijec, folder_path, rijec_original, txt_broj + 3))	

def prva_mix_upper_lower(rijec, rijec_original, txt_broj):
	os.system("crunch {0} {0} -t ,@{1} -o {2}{3}/{4}.txt".format(rijec_duzina + 2,rijec, folder_path, rijec_original, txt_broj))	
	os.system("crunch {0} {0} -t @,{1} -o {2}{3}/{4}.txt".format(rijec_duzina + 2,rijec, folder_path, rijec_original, txt_broj + 1))	
	os.system("crunch {0} {0} -t @,,{1} -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 2))	
	os.system("crunch {0} {0} -t ,@,{1} -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 3))	
	os.system("crunch {0} {0} -t ,,@{1} -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 4))	
	os.system("crunch {0} {0} -t @@,{1} -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 5))	
	os.system("crunch {0} {0} -t ,@@{1} -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 6))	
	os.system("crunch {0} {0} -t @,@{1} -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 7))	

def druga_mix_upper_lower(rijec, rijec_original, txt_broj):
	os.system("crunch {0} {0} -t {1},@ -o {2}{3}/{4}.txt".format(rijec_duzina + 2,rijec, folder_path, rijec_original, txt_broj))	
	os.system("crunch {0} {0} -t {1}@, -o {2}{3}/{4}.txt".format(rijec_duzina + 2,rijec, folder_path, rijec_original, txt_broj + 1))	
	os.system("crunch {0} {0} -t {1}@,, -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 2))	
	os.system("crunch {0} {0} -t {1},@, -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 3))	
	os.system("crunch {0} {0} -t {1},,@ -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 4))	
	os.system("crunch {0} {0} -t {1}@@, -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 5))	
	os.system("crunch {0} {0} -t {1},@@ -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 6))	
	os.system("crunch {0} {0} -t {1}@,@ -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 7))	

def prva_mix_upper_numeric(rijec, rijec_original, txt_broj):
	os.system("crunch {0} {0} -t ,%{1} -o {2}{3}/{4}.txt".format(rijec_duzina + 2,rijec, folder_path, rijec_original, txt_broj))	
	os.system("crunch {0} {0} -t %,{1} -o {2}{3}/{4}.txt".format(rijec_duzina + 2,rijec, folder_path, rijec_original, txt_broj + 1))	
	os.system("crunch {0} {0} -t %,,{1} -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 2))	
	os.system("crunch {0} {0} -t ,%,{1} -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 3))	
	os.system("crunch {0} {0} -t ,,%{1} -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 4))	
	os.system("crunch {0} {0} -t %%,{1} -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 5))	
	os.system("crunch {0} {0} -t ,%%{1} -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 6))	
	os.system("crunch {0} {0} -t %,%{1} -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 7))	

def druga_mix_upper_numeric(rijec, rijec_original, txt_broj):
	os.system("crunch {0} {0} -t {1},% -o {2}{3}/{4}.txt".format(rijec_duzina + 2,rijec, folder_path, rijec_original, txt_broj))	
	os.system("crunch {0} {0} -t {1}%, -o {2}{3}/{4}.txt".format(rijec_duzina + 2,rijec, folder_path, rijec_original, txt_broj + 1))	
	os.system("crunch {0} {0} -t {1}%,, -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 2))	
	os.system("crunch {0} {0} -t {1},%, -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 3))	
	os.system("crunch {0} {0} -t {1},,% -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 4))	
	os.system("crunch {0} {0} -t {1}%%, -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 5))	
	os.system("crunch {0} {0} -t {1},%% -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 6))	
	os.system("crunch {0} {0} -t {1}%,% -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 7))	

def prva_mix_lower_numeric(rijec, rijec_original, txt_broj):
	

	os.system("crunch {0} {0} -t %@{1} -o {2}{3}/{4}.txt".format(rijec_duzina + 2,rijec, folder_path, rijec_original, txt_broj))
	
	os.system("crunch {0} {0} -t @%{1} -o {2}{3}/{4}.txt".format(rijec_duzina + 2,rijec, folder_path, rijec_original, txt_broj + 1))
	
	os.system("crunch {0} {0} -t @%%{1} -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 2))
	
	os.system("crunch {0} {0} -t %@%{1} -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 3))
	
	os.system("crunch {0} {0} -t %%@{1} -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 4))
	
	os.system("crunch {0} {0} -t @@%{1} -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 5))
	
	os.system("crunch {0} {0} -t %@@{1} -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 6))
	
	os.system("crunch {0} {0} -t @%@{1} -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 7))
	

def druga_mix_lower_numeric(rijec, rijec_original, txt_broj):
	

	os.system("crunch {0} {0} -t {1}%@ -o {2}{3}/{4}.txt".format(rijec_duzina + 2,rijec, folder_path, rijec_original, txt_broj))
	
	os.system("crunch {0} {0} -t {1}@% -o {2}{3}/{4}.txt".format(rijec_duzina + 2,rijec, folder_path, rijec_original, txt_broj + 1))
	
	os.system("crunch {0} {0} -t {1}@%% -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 2))
	
	os.system("crunch {0} {0} -t {1}%@% -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 3))
	
	os.system("crunch {0} {0} -t {1}%%@ -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 4))
	
	os.system("crunch {0} {0} -t {1}@@% -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 5))
	
	os.system("crunch {0} {0} -t {1}%@@ -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 6))
	
	os.system("crunch {0} {0} -t {1}@%@ -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 7))
	

def prva_mix_lower_upper_numeric(rijec, rijec_original, txt_broj):
	

	os.system("crunch {0} {0} -t @,%{1} -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj))
	
	os.system("crunch {0} {0} -t @%,{1} -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 1))
	
	os.system("crunch {0} {0} -t ,@%{1} -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 2))
	
	os.system("crunch {0} {0} -t ,%@{1} -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 3))
	
	os.system("crunch {0} {0} -t %@,{1} -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 4))
	
	os.system("crunch {0} {0} -t %,@{1} -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 5))
	
	
def druga_mix_lower_upper_numeric(rijec, rijec_original, txt_broj):
	

	os.system("crunch {0} {0} -t {1}@,% -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj))
	
	os.system("crunch {0} {0} -t {1}@%, -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 1))
	
	os.system("crunch {0} {0} -t {1},@% -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 2))
	
	os.system("crunch {0} {0} -t {1},%@ -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 3))
	
	os.system("crunch {0} {0} -t {1}%@, -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 4))
	
	os.system("crunch {0} {0} -t {1}%,@ -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 5))
	
	
def prva_char(rijec, rijec_original, txt_broj):
	

	os.system("crunch {0} {0} -t ^{1} -o {2}{3}/{4}.txt".format(rijec_duzina + 1,rijec, folder_path, rijec_original, txt_broj))
	
	os.system("crunch {0} {0} -t ^^{1} -o {2}{3}/{4}.txt".format(rijec_duzina + 2,rijec, folder_path, rijec_original, txt_broj + 1))
	
	os.system("crunch {0} {0} -t ^^^{1} -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 2))
	
	os.system("crunch {0} {0} -t ^^^^{1} -o {2}{3}/{4}.txt".format(rijec_duzina + 4,rijec, folder_path, rijec_original, txt_broj + 3))
	

def druga_char(rijec, rijec_original, txt_broj):
	

	os.system("crunch {0} {0} -t {1}^ -o {2}{3}/{4}.txt".format(rijec_duzina + 1,rijec, folder_path, rijec_original, txt_broj))
	
	os.system("crunch {0} {0} -t {1}^^ -o {2}{3}/{4}.txt".format(rijec_duzina + 2,rijec, folder_path, rijec_original, txt_broj + 1))
	
	os.system("crunch {0} {0} -t {1}^^^ -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 2))
	
	os.system("crunch {0} {0} -t {1}^^^^ -o {2}{3}/{4}.txt".format(rijec_duzina + 4,rijec, folder_path, rijec_original, txt_broj + 3))
	

def prva_mix_upper_char(rijec, rijec_original, txt_broj):
	

	os.system("crunch {0} {0} -t ,^{1} -o {2}{3}/{4}.txt".format(rijec_duzina + 2,rijec, folder_path, rijec_original, txt_broj))
	
	os.system("crunch {0} {0} -t ^,{1} -o {2}{3}/{4}.txt".format(rijec_duzina + 2,rijec, folder_path, rijec_original, txt_broj + 1))
	
	os.system("crunch {0} {0} -t ^,,{1} -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 2))
	
	os.system("crunch {0} {0} -t ,^,{1} -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 3))
	
	os.system("crunch {0} {0} -t ,,^{1} -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 4))
	
	os.system("crunch {0} {0} -t ^^,{1} -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 5))
	
	os.system("crunch {0} {0} -t ,^^{1} -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 6))
	
	os.system("crunch {0} {0} -t ^,^{1} -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 7))
	

def druga_mix_upper_char(rijec, rijec_original, txt_broj):
	

	os.system("crunch {0} {0} -t {1},^ -o {2}{3}/{4}.txt".format(rijec_duzina + 2,rijec, folder_path, rijec_original, txt_broj))
	
	os.system("crunch {0} {0} -t {1}^, -o {2}{3}/{4}.txt".format(rijec_duzina + 2,rijec, folder_path, rijec_original, txt_broj + 1))
	
	os.system("crunch {0} {0} -t {1}^,, -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 2))
	
	os.system("crunch {0} {0} -t {1},^, -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 3))
	
	os.system("crunch {0} {0} -t {1},,^ -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 4))
	
	os.system("crunch {0} {0} -t {1}^^, -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 5))
	
	os.system("crunch {0} {0} -t {1},^^ -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 6))
	
	os.system("crunch {0} {0} -t {1}^,^ -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 7))
	

def prva_mix_lower_char(rijec, rijec_original, txt_broj):
	

	os.system("crunch {0} {0} -t @^{1} -o {2}{3}/{4}.txt".format(rijec_duzina + 2,rijec, folder_path, rijec_original, txt_broj))
	
	os.system("crunch {0} {0} -t ^@{1} -o {2}{3}/{4}.txt".format(rijec_duzina + 2,rijec, folder_path, rijec_original, txt_broj + 1))
	
	os.system("crunch {0} {0} -t ^@@{1} -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 2))
	
	os.system("crunch {0} {0} -t @^@{1} -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 3))
	
	os.system("crunch {0} {0} -t @@^{1} -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 4))
	
	os.system("crunch {0} {0} -t ^^@{1} -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 5))
	
	os.system("crunch {0} {0} -t @^^{1} -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 6))
	
	os.system("crunch {0} {0} -t ^@^{1} -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 7))
	

def druga_mix_lower_char(rijec, rijec_original, txt_broj):
	

	os.system("crunch {0} {0} -t {1}@^ -o {2}{3}/{4}.txt".format(rijec_duzina + 2,rijec, folder_path, rijec_original, txt_broj))
	
	os.system("crunch {0} {0} -t {1}^@ -o {2}{3}/{4}.txt".format(rijec_duzina + 2,rijec, folder_path, rijec_original, txt_broj + 1))
	
	os.system("crunch {0} {0} -t {1}^@@ -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 2))
	
	os.system("crunch {0} {0} -t {1}@^@ -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 3))
	
	os.system("crunch {0} {0} -t {1}@@^ -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 4))
	
	os.system("crunch {0} {0} -t {1}^^@ -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 5))
	
	os.system("crunch {0} {0} -t {1}@^^ -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 6))
	
	os.system("crunch {0} {0} -t {1}^@^ -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 7))
	

def prva_mix_numeric_char(rijec, rijec_original, txt_broj):
	

	os.system("crunch {0} {0} -t %^{1} -o {2}{3}/{4}.txt".format(rijec_duzina + 2,rijec, folder_path, rijec_original, txt_broj))
	
	os.system("crunch {0} {0} -t ^%{1} -o {2}{3}/{4}.txt".format(rijec_duzina + 2,rijec, folder_path, rijec_original, txt_broj + 1))
	
	os.system("crunch {0} {0} -t ^%%{1} -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 2))
	
	os.system("crunch {0} {0} -t %^%{1} -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 3))
	
	os.system("crunch {0} {0} -t %%^{1} -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 4))
	
	os.system("crunch {0} {0} -t ^^%{1} -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 5))
	
	os.system("crunch {0} {0} -t %^^{1} -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 6))
	
	os.system("crunch {0} {0} -t ^%^{1} -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 7))
	

def druga_mix_numeric_char(rijec, rijec_original, txt_broj):
	

	os.system("crunch {0} {0} -t {1}%^ -o {2}{3}/{4}.txt".format(rijec_duzina + 2,rijec, folder_path, rijec_original, txt_broj))
	
	os.system("crunch {0} {0} -t {1}^% -o {2}{3}/{4}.txt".format(rijec_duzina + 2,rijec, folder_path, rijec_original, txt_broj + 1))
	
	os.system("crunch {0} {0} -t {1}^%% -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 2))
	
	os.system("crunch {0} {0} -t {1}%^% -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 3))
	
	os.system("crunch {0} {0} -t {1}%%^ -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 4))
	
	os.system("crunch {0} {0} -t {1}^^% -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 5))
	
	os.system("crunch {0} {0} -t {1}%^^ -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 6))
	
	os.system("crunch {0} {0} -t {1}^%^ -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 7))
	

def prva_mix_upper_lower_char(rijec, rijec_original, txt_broj):
	

	os.system("crunch {0} {0} -t @,^{1} -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj))
	
	os.system("crunch {0} {0} -t @^,{1} -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 1))
	
	os.system("crunch {0} {0} -t ,@^{1} -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 2))
	
	os.system("crunch {0} {0} -t ,^@{1} -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 3))
	
	os.system("crunch {0} {0} -t ^@,{1} -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 4))
	
	os.system("crunch {0} {0} -t ^,@{1} -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 5))
	

def druga_mix_upper_lower_char(rijec, rijec_original, txt_broj):
	

	os.system("crunch {0} {0} -t {1}@,^ -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj))
	
	os.system("crunch {0} {0} -t {1}@^, -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 1))
	
	os.system("crunch {0} {0} -t {1},@^ -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 2))
	
	os.system("crunch {0} {0} -t {1},^@ -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 3))
	
	os.system("crunch {0} {0} -t {1}^@, -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 4))
	
	os.system("crunch {0} {0} -t {1}^,@ -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 5))
	

def prva_mix_upper_numeric_char(rijec, rijec_original, txt_broj):
	

	os.system("crunch {0} {0} -t %,^{1} -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj))
	
	os.system("crunch {0} {0} -t %^,{1} -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 1))
	
	os.system("crunch {0} {0} -t ,%^{1} -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 2))
	
	os.system("crunch {0} {0} -t ,^%{1} -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 3))
	
	os.system("crunch {0} {0} -t ^%,{1} -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 4))
	
	os.system("crunch {0} {0} -t ^,%{1} -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 5))
	

def druga_mix_upper_numeric_char(rijec, rijec_original, txt_broj):
	
	
	os.system("crunch {0} {0} -t {1}%,^ -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj))
	
	os.system("crunch {0} {0} -t {1}%^, -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 1))
	
	os.system("crunch {0} {0} -t {1},%^ -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 2))
	
	os.system("crunch {0} {0} -t {1},^% -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 3))
	
	os.system("crunch {0} {0} -t {1}^%, -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 4))
	
	os.system("crunch {0} {0} -t {1}^,% -o {2}{3}/{4}.txt".format(rijec_duzina + 3,rijec, folder_path, rijec_original, txt_broj + 5))
	

#functions with 2 words start here

def dvije_rijeci_prva_numeric(prva_rijec, druga_rijec, folder, rijecnik, txt_broj):
	

	os.system("crunch {0} {0} -t {1}{2}% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 1, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj))
	
	os.system("crunch {0} {0} -t {1}{2}%% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 1))
	
	os.system("crunch {0} {0} -t {1}{2}%%% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 2))
	
	os.system("crunch {0} {0} -t {1}{2}%%%% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 3))
	
	os.system("crunch {0} {0} -t {1}%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 1, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 4))
	
	os.system("crunch {0} {0} -t {1}%%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 5))
	
	os.system("crunch {0} {0} -t {1}%%%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 6))
	
	os.system("crunch {0} {0} -t {1}%%%%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 7))
	
	os.system("crunch {0} {0} -t {1}%{2}% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 8))
	
	os.system("crunch {0} {0} -t {1}%%{2}% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 9))
	
	os.system("crunch {0} {0} -t {1}%{2}%% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 10))
	
	os.system("crunch {0} {0} -t {1}%%%{2}% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 11))
	
	os.system("crunch {0} {0} -t {1}%%{2}%% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 12))
	
	os.system("crunch {0} {0} -t {1}%{2}%%% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 13))
	
	#combo 2 names
	os.system("crunch {0} {0} -t {1}{2}% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 1, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 14))
	
	os.system("crunch {0} {0} -t {1}{2}%% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 15))
	
	os.system("crunch {0} {0} -t {1}{2}%%% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 16))
	
	os.system("crunch {0} {0} -t {1}{2}%%%% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 17))
	
	os.system("crunch {0} {0} -t {1}%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 1, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 18))
	os.system("crunch {0} {0} -t {1}%%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 19))
	
	os.system("crunch {0} {0} -t {1}%%%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 20))
	
	os.system("crunch {0} {0} -t {1}%%%%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 21))
	
	os.system("crunch {0} {0} -t {1}%{2}% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 22))
	
	os.system("crunch {0} {0} -t {1}%%{2}% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 23))
	
	os.system("crunch {0} {0} -t {1}%{2}%% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 24))
	
	os.system("crunch {0} {0} -t {1}%%%{2}% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 25))
	
	os.system("crunch {0} {0} -t {1}%%{2}%% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 26))
	
	os.system("crunch {0} {0} -t {1}%{2}%%% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 27))
	

def dvije_rijeci_druga_numeric(prva_rijec, druga_rijec, folder, rijecnik, txt_broj):
	

	os.system("crunch {0} {0} -t %{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 1, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj))
	
	os.system("crunch {0} {0} -t %%{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 1))
	
	os.system("crunch {0} {0} -t %%%{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 2))
	
	os.system("crunch {0} {0} -t %%%%{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 3))
	
	os.system("crunch {0} {0} -t %{1}%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 4))
	
	os.system("crunch {0} {0} -t %%{1}%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 5))
	
	os.system("crunch {0} {0} -t %{1}%%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 6))
	
	os.system("crunch {0} {0} -t %{1}%%%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 7))
	
	os.system("crunch {0} {0} -t %%{1}%%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 8))
	
	os.system("crunch {0} {0} -t %%%{1}%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 9))
	
	os.system("crunch {0} {0} -t %{1}{2}% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 10))
	
	os.system("crunch {0} {0} -t %%{1}{2}% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 11))
	
	os.system("crunch {0} {0} -t %{1}{2}%% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 12))
	
	os.system("crunch {0} {0} -t %%{1}{2}%% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 13))
	
	os.system("crunch {0} {0} -t %%%{1}{2}% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 14))
	
	os.system("crunch {0} {0} -t %{1}{2}%%% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 15))
	
	#combo 2 names
	os.system("crunch {0} {0} -t %{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 1, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 16))
	
	os.system("crunch {0} {0} -t %%{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 17))
	
	os.system("crunch {0} {0} -t %%%{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 18))
	
	os.system("crunch {0} {0} -t %%%%{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 19))
	
	os.system("crunch {0} {0} -t %{1}%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 20))
	
	os.system("crunch {0} {0} -t %%{1}%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 21))
	
	os.system("crunch {0} {0} -t %{1}%%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 22))
	
	os.system("crunch {0} {0} -t %{1}%%%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 23))
	
	os.system("crunch {0} {0} -t %%{1}%%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 24))
	
	os.system("crunch {0} {0} -t %%%{1}%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 25))
	
	os.system("crunch {0} {0} -t %{1}{2}% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 26))
	
	os.system("crunch {0} {0} -t %%{1}{2}% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 27))
	
	os.system("crunch {0} {0} -t %{1}{2}%% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 28))
	
	os.system("crunch {0} {0} -t %%{1}{2}%% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 29))
	
	os.system("crunch {0} {0} -t %%%{1}{2}% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 30))
	
	os.system("crunch {0} {0} -t %{1}{2}%%% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 31))
	

def dvije_rijeci_prva_lower_alpha(prva_rijec, druga_rijec, folder, rijecnik, txt_broj):
	

	os.system("crunch {0} {0} -t {1}{2}@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 1, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj))
	
	os.system("crunch {0} {0} -t {1}{2}@@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 1))
	
	os.system("crunch {0} {0} -t {1}{2}@@@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 2))
	
	os.system("crunch {0} {0} -t {1}{2}@@@@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 3))
	
	os.system("crunch {0} {0} -t {1}@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 1, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 4))
	
	os.system("crunch {0} {0} -t {1}@@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 5))
	
	os.system("crunch {0} {0} -t {1}@@@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 6))
	
	os.system("crunch {0} {0} -t {1}@@@@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 7))
	
	os.system("crunch {0} {0} -t {1}@{2}@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 8))
	
	os.system("crunch {0} {0} -t {1}@@{2}@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 9))
	
	os.system("crunch {0} {0} -t {1}@{2}@@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 10))
	
	os.system("crunch {0} {0} -t {1}@@@{2}@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 11))
	
	os.system("crunch {0} {0} -t {1}@@{2}@@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 12))
	
	os.system("crunch {0} {0} -t {1}@{2}@@@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 13))
	
	#combo 2 names
	os.system("crunch {0} {0} -t {1}{2}@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 1, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 14))
	
	os.system("crunch {0} {0} -t {1}{2}@@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 15))
	
	os.system("crunch {0} {0} -t {1}{2}@@@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 16))
	
	os.system("crunch {0} {0} -t {1}{2}@@@@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 17))
	
	os.system("crunch {0} {0} -t {1}@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 1, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 18))
	
	os.system("crunch {0} {0} -t {1}@@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 19))
	
	os.system("crunch {0} {0} -t {1}@@@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 20))
	
	os.system("crunch {0} {0} -t {1}@@@@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 21))
	
	os.system("crunch {0} {0} -t {1}@{2}@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 22))
	
	os.system("crunch {0} {0} -t {1}@@{2}@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 23))
	
	os.system("crunch {0} {0} -t {1}@{2}@@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 24))
	
	os.system("crunch {0} {0} -t {1}@@@{2}@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 25))
	
	os.system("crunch {0} {0} -t {1}@@{2}@@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 26))
	
	os.system("crunch {0} {0} -t {1}@{2}@@@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 27))
	

def dvije_rijeci_druga_lower_alpha(prva_rijec, druga_rijec, folder, rijecnik, txt_broj):
	

	os.system("crunch {0} {0} -t @{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 1, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj))
	
	os.system("crunch {0} {0} -t @@{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 1))
	
	os.system("crunch {0} {0} -t @@@{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 2))
	
	os.system("crunch {0} {0} -t @@@@{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 3))
	
	os.system("crunch {0} {0} -t @{1}@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 4))
	
	os.system("crunch {0} {0} -t @@{1}@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 5))
	
	os.system("crunch {0} {0} -t @{1}@@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 6))
	
	os.system("crunch {0} {0} -t @{1}@@@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 7))
	
	os.system("crunch {0} {0} -t @@{1}@@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 8))
	
	os.system("crunch {0} {0} -t @@@{1}@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 9))
	
	os.system("crunch {0} {0} -t @{1}{2}@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 10))
	
	os.system("crunch {0} {0} -t @@{1}{2}@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 11))
	
	os.system("crunch {0} {0} -t @{1}{2}@@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 12))
	
	os.system("crunch {0} {0} -t @@{1}{2}@@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 13))
	
	os.system("crunch {0} {0} -t @@@{1}{2}@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 14))
	
	os.system("crunch {0} {0} -t @{1}{2}@@@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 15))
	
	#combo 2 names
	os.system("crunch {0} {0} -t @{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 1, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 16))
	
	os.system("crunch {0} {0} -t @@{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 17))
	
	os.system("crunch {0} {0} -t @@@{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 18))
	
	os.system("crunch {0} {0} -t @@@@{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 19))
	
	os.system("crunch {0} {0} -t @{1}@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 20))
	
	os.system("crunch {0} {0} -t @@{1}@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 21))
	
	os.system("crunch {0} {0} -t @{1}@@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 22))
	
	os.system("crunch {0} {0} -t @{1}@@@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 23))
	
	os.system("crunch {0} {0} -t @@{1}@@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 24))
	
	os.system("crunch {0} {0} -t @@@{1}@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 25))
	
	os.system("crunch {0} {0} -t @{1}{2}@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 26))
	
	os.system("crunch {0} {0} -t @@{1}{2}@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 27))
	
	os.system("crunch {0} {0} -t @{1}{2}@@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 28))
	
	os.system("crunch {0} {0} -t @@{1}{2}@@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 29))
	
	os.system("crunch {0} {0} -t @@@{1}{2}@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 30))
	
	os.system("crunch {0} {0} -t @{1}{2}@@@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 31))
	

def dvije_rijeci_prva_upper_alpha(prva_rijec, druga_rijec, folder, rijecnik, txt_broj):
	

	os.system("crunch {0} {0} -t {1}{2}, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 1, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj))
	
	os.system("crunch {0} {0} -t {1}{2},, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 1))
	
	os.system("crunch {0} {0} -t {1}{2},,, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 2))
	
	os.system("crunch {0} {0} -t {1}{2},,,, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 3))
	
	os.system("crunch {0} {0} -t {1},{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 1, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 4))
	
	os.system("crunch {0} {0} -t {1},,{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 5))
	
	os.system("crunch {0} {0} -t {1},,,{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 6))
	
	os.system("crunch {0} {0} -t {1},,,,{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 7))
	
	os.system("crunch {0} {0} -t {1},{2}, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 8))
	
	os.system("crunch {0} {0} -t {1},,{2}, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 9))
	
	os.system("crunch {0} {0} -t {1},{2},, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 10))
	
	os.system("crunch {0} {0} -t {1},,,{2}, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 11))
	
	os.system("crunch {0} {0} -t {1},,{2},, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 12))
	
	os.system("crunch {0} {0} -t {1},{2},,, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 13))
	
	#combo 2 names
	os.system("crunch {0} {0} -t {1}{2}, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 1, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 14))
	
	os.system("crunch {0} {0} -t {1}{2},, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 15))
	
	os.system("crunch {0} {0} -t {1}{2},,, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 16))
	
	os.system("crunch {0} {0} -t {1}{2},,,, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 17))
	
	os.system("crunch {0} {0} -t {1},{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 1, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 18))
	
	os.system("crunch {0} {0} -t {1},,{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 19))
	
	os.system("crunch {0} {0} -t {1},,,{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 20))
	
	os.system("crunch {0} {0} -t {1},,,,{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 21))
	
	os.system("crunch {0} {0} -t {1},{2}, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 22))
	
	os.system("crunch {0} {0} -t {1},,{2}, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 23))
	
	os.system("crunch {0} {0} -t {1},{2},, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 24))
	
	os.system("crunch {0} {0} -t {1},,,{2}, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 25))
	
	os.system("crunch {0} {0} -t {1},,{2},, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 26))
	
	os.system("crunch {0} {0} -t {1},{2},,, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 27))
	

def dvije_rijeci_druga_upper_alpha(prva_rijec, druga_rijec, folder, rijecnik, txt_broj):
	

	os.system("crunch {0} {0} -t ,{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 1, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj))
	
	os.system("crunch {0} {0} -t ,,{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 1))
	
	os.system("crunch {0} {0} -t ,,,{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 2))
	
	os.system("crunch {0} {0} -t ,,,,{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 3))
	
	os.system("crunch {0} {0} -t ,{1},{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 4))
	
	os.system("crunch {0} {0} -t ,,{1},{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 5))
	
	os.system("crunch {0} {0} -t ,{1},,{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 6))
	
	os.system("crunch {0} {0} -t ,{1},,,{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 7))
	
	os.system("crunch {0} {0} -t ,,{1},,{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 8))
	
	os.system("crunch {0} {0} -t ,,,{1},{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 9))
	
	os.system("crunch {0} {0} -t ,{1}{2}, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 10))
	
	os.system("crunch {0} {0} -t ,,{1}{2}, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 11))
	
	os.system("crunch {0} {0} -t ,{1}{2},, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 12))
	
	os.system("crunch {0} {0} -t ,,{1}{2},, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 13))
	
	os.system("crunch {0} {0} -t ,,,{1}{2}, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 14))
	
	os.system("crunch {0} {0} -t ,{1}{2},,, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 15))
	
	#combo 2 names
	os.system("crunch {0} {0} -t ,{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 1, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 16))
	
	os.system("crunch {0} {0} -t ,,{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 17))
	
	os.system("crunch {0} {0} -t ,,,{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 18))
	
	os.system("crunch {0} {0} -t ,,,,{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 19))
	
	os.system("crunch {0} {0} -t ,{1},{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 20))
	
	os.system("crunch {0} {0} -t ,,{1},{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 21))
	
	os.system("crunch {0} {0} -t ,{1},,{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 22))
	
	os.system("crunch {0} {0} -t ,{1},,,{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 23))
	
	os.system("crunch {0} {0} -t ,,{1},,{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 24))
	
	os.system("crunch {0} {0} -t ,,,{1},{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 25))
	
	os.system("crunch {0} {0} -t ,{1}{2}, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 26))
	
	os.system("crunch {0} {0} -t ,,{1}{2}, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 27))
	
	os.system("crunch {0} {0} -t ,{1}{2},, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 28))
	
	os.system("crunch {0} {0} -t ,,{1}{2},, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 29))
	
	os.system("crunch {0} {0} -t ,,,{1}{2}, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 30))
	
	os.system("crunch {0} {0} -t ,{1}{2},,, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 4, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 31))
	

def dvije_rijeci_prva_mix_upper_lower(prva_rijec, druga_rijec, folder, rijecnik, txt_broj):
	

	os.system("crunch {0} {0} -t ,@{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj))
	
	os.system("crunch {0} {0} -t @,{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 1))
	
	os.system("crunch {0} {0} -t ,{1}@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 2))
	
	os.system("crunch {0} {0} -t @{1},{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 3))
	
	os.system("crunch {0} {0} -t {1},@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 4))
	
	os.system("crunch {0} {0} -t {1}@,{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 5))
	
	os.system("crunch {0} {0} -t {1},,@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 6))
	
	os.system("crunch {0} {0} -t {1},@,{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 7))
	
	os.system("crunch {0} {0} -t {1},@@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 8))
	
	os.system("crunch {0} {0} -t {1}@,,{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 9))
	
	os.system("crunch {0} {0} -t {1}@@,{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 10))
	
	os.system("crunch {0} {0} -t {1}@,@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 11))
	
	os.system("crunch {0} {0} -t @,,{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 12))
	
	os.system("crunch {0} {0} -t ,@,{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 13))
	
	os.system("crunch {0} {0} -t ,,@{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 14))
	
	os.system("crunch {0} {0} -t @@,{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 15))
	
	os.system("crunch {0} {0} -t ,@@{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 16))
	
	os.system("crunch {0} {0} -t @,@{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 17))
	
	os.system("crunch {0} {0} -t @{1},,{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 18))
	
	os.system("crunch {0} {0} -t @{1},@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 19))
	
	os.system("crunch {0} {0} -t @{1}@,{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 20))
	
	os.system("crunch {0} {0} -t ,{1}@@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 21))
	
	os.system("crunch {0} {0} -t ,{1},@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 22))
	
	os.system("crunch {0} {0} -t ,{1}@,{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 23))
	
	os.system("crunch {0} {0} -t ,@{1},{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 24))
	
	os.system("crunch {0} {0} -t ,@{1}@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 25))
	
	os.system("crunch {0} {0} -t @,{1},{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 26))
	
	os.system("crunch {0} {0} -t @,{1}@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 27))
	
	#combo 2 names
	os.system("crunch {0} {0} -t ,@{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 28))
	
	os.system("crunch {0} {0} -t @,{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 29))
	
	os.system("crunch {0} {0} -t ,{1}@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 30))
	
	os.system("crunch {0} {0} -t @{1},{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 31))
	
	os.system("crunch {0} {0} -t {1},@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 32))
	
	os.system("crunch {0} {0} -t {1}@,{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 33))
	
	os.system("crunch {0} {0} -t {1},,@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 34))
	
	os.system("crunch {0} {0} -t {1},@,{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 35))
	
	os.system("crunch {0} {0} -t {1},@@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 36))
	
	os.system("crunch {0} {0} -t {1}@,,{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 37))
	
	os.system("crunch {0} {0} -t {1}@@,{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 38))
	
	os.system("crunch {0} {0} -t {1}@,@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 39))
	
	os.system("crunch {0} {0} -t @,,{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 40))
	
	os.system("crunch {0} {0} -t ,@,{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 41))
	
	os.system("crunch {0} {0} -t ,,@{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 42))
	
	os.system("crunch {0} {0} -t @@,{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 43))
	
	os.system("crunch {0} {0} -t ,@@{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 44))
	
	os.system("crunch {0} {0} -t @,@{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 45))
	
	os.system("crunch {0} {0} -t @{1},,{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 46))
	
	os.system("crunch {0} {0} -t @{1},@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 47))
	
	os.system("crunch {0} {0} -t @{1}@,{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 48))
	
	os.system("crunch {0} {0} -t ,{1}@@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 49))
	
	os.system("crunch {0} {0} -t ,{1},@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 50))
	
	os.system("crunch {0} {0} -t ,{1}@,{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 51))
	
	os.system("crunch {0} {0} -t ,@{1},{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 52))
	
	os.system("crunch {0} {0} -t ,@{1}@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 53))
	
	os.system("crunch {0} {0} -t @,{1},{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 54))
	
	os.system("crunch {0} {0} -t @,{1}@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 55))
	

def dvije_rijeci_druga_mix_upper_lower(prva_rijec, druga_rijec, folder, rijecnik, txt_broj):
	

	os.system("crunch {0} {0} -t {1}{2},@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj))
	
	os.system("crunch {0} {0} -t {1}{2}@, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 1))
	
	os.system("crunch {0} {0} -t {1}{2},,@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 2))
	
	os.system("crunch {0} {0} -t {1}{2},@, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 3))
	
	os.system("crunch {0} {0} -t {1}{2}@,, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 4))
	
	os.system("crunch {0} {0} -t {1}{2},@@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 5))
	
	os.system("crunch {0} {0} -t {1}{2}@,@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 6))
	
	os.system("crunch {0} {0} -t {1}{2}@@, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 7))
	
	os.system("crunch {0} {0} -t {1}@{2}, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 8))
	
	os.system("crunch {0} {0} -t {1},{2}@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 9))
	
	os.system("crunch {0} {0} -t {1},,{2}@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 10))
	
	os.system("crunch {0} {0} -t {1},@{2}, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 11))
	
	os.system("crunch {0} {0} -t {1}@,{2}, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 12))
	
	os.system("crunch {0} {0} -t {1}@@{2}, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 13))
	
	os.system("crunch {0} {0} -t {1}@,{2}@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 14))
	
	os.system("crunch {0} {0} -t {1},@{2}, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 15))
	
	os.system("crunch {0} {0} -t ,{1}{2}@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 16))
	
	os.system("crunch {0} {0} -t @{1}{2}, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 17))
	
	os.system("crunch {0} {0} -t ,{1}{2},@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 18))
	
	os.system("crunch {0} {0} -t ,{1}{2}@, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 19))
	
	os.system("crunch {0} {0} -t ,,{1}{2}@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 20))
	
	os.system("crunch {0} {0} -t ,@{1}{2}, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 21))
	
	os.system("crunch {0} {0} -t @,{1}{2}, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 22))
	
	os.system("crunch {0} {0} -t ,@{1}{2}@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 23))
	
	os.system("crunch {0} {0} -t @,{1}{2}@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 24))
	
	os.system("crunch {0} {0} -t @@{1}{2}, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 25))
	
	#combo 2 names
	os.system("crunch {0} {0} -t {1}{2},@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 26))
	
	os.system("crunch {0} {0} -t {1}{2}@, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 27))
	
	os.system("crunch {0} {0} -t {1}{2},,@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 28))
	
	os.system("crunch {0} {0} -t {1}{2},@, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 29))
	
	os.system("crunch {0} {0} -t {1}{2}@,, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 30))
	
	os.system("crunch {0} {0} -t {1}{2},@@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 31))
	
	os.system("crunch {0} {0} -t {1}{2}@,@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 32))
	
	os.system("crunch {0} {0} -t {1}{2}@@, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 33))
	
	os.system("crunch {0} {0} -t {1}@{2}, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 34))
	
	os.system("crunch {0} {0} -t {1},{2}@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 35))
	
	os.system("crunch {0} {0} -t {1},,{2}@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 36))
	
	os.system("crunch {0} {0} -t {1},@{2}, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 37))
	
	os.system("crunch {0} {0} -t {1}@,{2}, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 38))
	
	os.system("crunch {0} {0} -t {1}@@{2}, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 39))
	
	os.system("crunch {0} {0} -t {1}@,{2}@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 40))
	
	os.system("crunch {0} {0} -t {1},@{2}, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 41))
	
	os.system("crunch {0} {0} -t ,{1}{2}@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 42))
	
	os.system("crunch {0} {0} -t @{1}{2}, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 43))
	
	os.system("crunch {0} {0} -t ,{1}{2},@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 44))
	
	os.system("crunch {0} {0} -t ,{1}{2}@, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 45))
	
	os.system("crunch {0} {0} -t ,,{1}{2}@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 46))
	
	os.system("crunch {0} {0} -t ,@{1}{2}, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 47))
	
	os.system("crunch {0} {0} -t @,{1}{2}, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 48))
	
	os.system("crunch {0} {0} -t ,@{1}{2}@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 49))
	
	os.system("crunch {0} {0} -t @,{1}{2}@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 50))
	
	os.system("crunch {0} {0} -t @@{1}{2}, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 51))
	

def dvije_rijeci_prva_mix_upper_numeric(prva_rijec, druga_rijec, folder, rijecnik, txt_broj):
	

	os.system("crunch {0} {0} -t ,%{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj))
	
	os.system("crunch {0} {0} -t %,{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 1))
	
	os.system("crunch {0} {0} -t ,{1}%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 2))
	
	os.system("crunch {0} {0} -t %{1},{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 3))
	
	os.system("crunch {0} {0} -t {1},%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 4))
	
	os.system("crunch {0} {0} -t {1}%,{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 5))
	
	os.system("crunch {0} {0} -t {1},,%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 6))
	
	os.system("crunch {0} {0} -t {1},%,{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 7))
	
	os.system("crunch {0} {0} -t {1}%,,{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 8))
	
	os.system("crunch {0} {0} -t {1}%%,{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 9))
	
	os.system("crunch {0} {0} -t {1}%,%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 10))
	
	os.system("crunch {0} {0} -t {1},%%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 11))
	
	os.system("crunch {0} {0} -t ,,%{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 12))
	
	os.system("crunch {0} {0} -t ,%,{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 13))
	
	os.system("crunch {0} {0} -t %,,{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 14))
	
	os.system("crunch {0} {0} -t %%,{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 15))
	
	os.system("crunch {0} {0} -t %,%{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 16))
	
	os.system("crunch {0} {0} -t ,%%{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 17))
	
	os.system("crunch {0} {0} -t ,,{1}%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 18))
	
	os.system("crunch {0} {0} -t ,%{1},{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 19))
	
	os.system("crunch {0} {0} -t %,{1},{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 20))
	
	os.system("crunch {0} {0} -t %%{1},{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 21))
	
	os.system("crunch {0} {0} -t %,{1}%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 22))
	
	os.system("crunch {0} {0} -t ,%{1}%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 23))
	
	os.system("crunch {0} {0} -t ,{1},%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 24))
	
	os.system("crunch {0} {0} -t ,{1}%,{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 25))
	
	os.system("crunch {0} {0} -t %{1},,{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 26))
	
	os.system("crunch {0} {0} -t %{1}%,{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 27))
	
	os.system("crunch {0} {0} -t %{1},%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 28))
	
	os.system("crunch {0} {0} -t ,{1}%%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 29))
	
	os.system("crunch {0} {0} -t {1},,%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 30))
	
	os.system("crunch {0} {0} -t {1},%,{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 31))
	
	os.system("crunch {0} {0} -t {1}%,,{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 32))
	
	os.system("crunch {0} {0} -t {1}%%,{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 33))
	
	os.system("crunch {0} {0} -t {1}%,%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 34))
	
	os.system("crunch {0} {0} -t {1},%%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 35))
	
	#combo 2 names
	os.system("crunch {0} {0} -t ,%{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 36))
	
	os.system("crunch {0} {0} -t %,{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 37))
	
	os.system("crunch {0} {0} -t ,{1}%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 38))
	
	os.system("crunch {0} {0} -t %{1},{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 39))
	
	os.system("crunch {0} {0} -t {1},%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 40))
	
	os.system("crunch {0} {0} -t {1}%,{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 41))
	
	os.system("crunch {0} {0} -t {1},,%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 42))
	
	os.system("crunch {0} {0} -t {1},%,{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 43))
	
	os.system("crunch {0} {0} -t {1}%,,{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 44))
	
	os.system("crunch {0} {0} -t {1}%%,{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 45))
	
	os.system("crunch {0} {0} -t {1}%,%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 46))
	
	os.system("crunch {0} {0} -t {1},%%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 47))
	
	os.system("crunch {0} {0} -t ,,%{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 48))
	
	os.system("crunch {0} {0} -t ,%,{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 49))
	
	os.system("crunch {0} {0} -t %,,{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 50))
	
	os.system("crunch {0} {0} -t %%,{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 51))
	
	os.system("crunch {0} {0} -t %,%{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 52))
	
	os.system("crunch {0} {0} -t ,%%{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 53))
	
	os.system("crunch {0} {0} -t ,,{1}%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 54))
	
	os.system("crunch {0} {0} -t ,%{1},{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 55))
	
	os.system("crunch {0} {0} -t %,{1},{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 56))
	
	os.system("crunch {0} {0} -t %%{1},{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 57))
	
	os.system("crunch {0} {0} -t %,{1}%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 58))
	
	os.system("crunch {0} {0} -t ,%{1}%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 59))
	
	os.system("crunch {0} {0} -t ,{1},%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 60))
	
	os.system("crunch {0} {0} -t ,{1}%,{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 61))
	
	os.system("crunch {0} {0} -t %{1},,{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 62))
	
	os.system("crunch {0} {0} -t %{1}%,{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 63))
	
	os.system("crunch {0} {0} -t %{1},%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 64))
	
	os.system("crunch {0} {0} -t ,{1}%%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 65))
	
	os.system("crunch {0} {0} -t {1},,%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 66))
	
	os.system("crunch {0} {0} -t {1},%,{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 67))
	
	os.system("crunch {0} {0} -t {1}%,,{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 68))
	
	os.system("crunch {0} {0} -t {1}%%,{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 69))
	
	os.system("crunch {0} {0} -t {1}%,%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 70))
	
	os.system("crunch {0} {0} -t {1},%%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 71))
	

def dvije_rijeci_druga_mix_upper_numeric(prva_rijec, druga_rijec, folder, rijecnik, txt_broj):
	

	os.system("crunch {0} {0} -t {1},{2}% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj))
	
	os.system("crunch {0} {0} -t {1}%{2}, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 1))
	
	os.system("crunch {0} {0} -t ,{1}{2}% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 2))
	
	os.system("crunch {0} {0} -t %{1}{2}, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 3))
	
	os.system("crunch {0} {0} -t {1},{2},% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 4))
	
	os.system("crunch {0} {0} -t {1},{2}%, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 5))
	
	os.system("crunch {0} {0} -t {1},{2}%% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 6))
	
	os.system("crunch {0} {0} -t {1}%{2},, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 7))
	
	os.system("crunch {0} {0} -t {1}%{2}%, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 8))
	
	os.system("crunch {0} {0} -t {1}%{2},% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 9))
	
	os.system("crunch {0} {0} -t {1},,{2}% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 10))
	
	os.system("crunch {0} {0} -t {1},%{2}, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 11))
	
	os.system("crunch {0} {0} -t {1}%,{2}, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 12))
	
	os.system("crunch {0} {0} -t {1}%%{2}, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 13))
	
	os.system("crunch {0} {0} -t {1}%,{2}% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 14))
	
	os.system("crunch {0} {0} -t {1},%{2}% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 15))
	
	os.system("crunch {0} {0} -t {1}{2}%, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 16))
	
	os.system("crunch {0} {0} -t {1}{2},% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 17))
	
	os.system("crunch {0} {0} -t {1}{2},,% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 18))
	
	os.system("crunch {0} {0} -t {1}{2},%, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 19))
	
	os.system("crunch {0} {0} -t {1}{2}%,, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 20))
	
	os.system("crunch {0} {0} -t {1}{2}%%, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 21))
	
	os.system("crunch {0} {0} -t {1}{2}%,% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 22))
	
	os.system("crunch {0} {0} -t {1}{2},%% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 23))
	
	#combo 2 names
	os.system("crunch {0} {0} -t {1},{2}% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 24))
	
	os.system("crunch {0} {0} -t {1}%{2}, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 25))
	
	os.system("crunch {0} {0} -t ,{1}{2}% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 26))
	
	os.system("crunch {0} {0} -t %{1}{2}, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 27))
	
	os.system("crunch {0} {0} -t {1},{2},% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 28))
	
	os.system("crunch {0} {0} -t {1},{2}%, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 29))
	
	os.system("crunch {0} {0} -t {1},{2}%% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 30))
	
	os.system("crunch {0} {0} -t {1}%{2},, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 31))
	
	os.system("crunch {0} {0} -t {1}%{2}%, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 32))
	
	os.system("crunch {0} {0} -t {1}%{2},% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 33))
	
	os.system("crunch {0} {0} -t {1},,{2}% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 34))
	
	os.system("crunch {0} {0} -t {1},%{2}, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 35))
	
	os.system("crunch {0} {0} -t {1}%,{2}, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 36))
	
	os.system("crunch {0} {0} -t {1}%%{2}, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 37))
	
	os.system("crunch {0} {0} -t {1}%,{2}% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 38))
	
	os.system("crunch {0} {0} -t {1},%{2}% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 39))
	
	os.system("crunch {0} {0} -t {1}{2}%, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 40))
	
	os.system("crunch {0} {0} -t {1}{2},% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 41))
	
	os.system("crunch {0} {0} -t {1}{2},,% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 42))
	
	os.system("crunch {0} {0} -t {1}{2},%, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 43))
	
	os.system("crunch {0} {0} -t {1}{2}%,, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 44))
	
	os.system("crunch {0} {0} -t {1}{2}%%, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 45))
	
	os.system("crunch {0} {0} -t {1}{2}%,% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 46))
	
	os.system("crunch {0} {0} -t {1}{2},%% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 47))
	

def dvije_rijeci_prva_mix_lower_numeric(prva_rijec, druga_rijec, folder, rijecnik, txt_broj):
	

	os.system("crunch {0} {0} -t @%{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj))
	
	os.system("crunch {0} {0} -t %@{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 1))
	
	os.system("crunch {0} {0} -t @{1}%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 2))
	
	os.system("crunch {0} {0} -t %{1}@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 3))
	
	os.system("crunch {0} {0} -t {1}@%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 4))
	
	os.system("crunch {0} {0} -t {1}%@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 5))
	
	os.system("crunch {0} {0} -t {1}@@%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 6))
	
	os.system("crunch {0} {0} -t {1}@%@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 7))
	
	os.system("crunch {0} {0} -t {1}%@@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 8))
	
	os.system("crunch {0} {0} -t {1}%%@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 9))
	
	os.system("crunch {0} {0} -t {1}%@%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 10))
	
	os.system("crunch {0} {0} -t {1}@%%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 11))
	
	os.system("crunch {0} {0} -t @@%{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 12))
	
	os.system("crunch {0} {0} -t @%@{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 13))
	
	os.system("crunch {0} {0} -t %@@{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 14))
	
	os.system("crunch {0} {0} -t %%@{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 15))
	
	os.system("crunch {0} {0} -t %@%{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 16))
	
	os.system("crunch {0} {0} -t @%%{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 17))
	
	os.system("crunch {0} {0} -t @@{1}%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 18))
	
	os.system("crunch {0} {0} -t @%{1}@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 19))
	
	os.system("crunch {0} {0} -t %@{1}@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 20))
	
	os.system("crunch {0} {0} -t %%{1}@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 21))
	
	os.system("crunch {0} {0} -t %@{1}%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 22))
	
	os.system("crunch {0} {0} -t @%{1}%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 23))
	
	os.system("crunch {0} {0} -t @{1}@%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 24))
	
	os.system("crunch {0} {0} -t @{1}%@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 25))
	
	os.system("crunch {0} {0} -t %{1}@@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 26))
	
	os.system("crunch {0} {0} -t %{1}%@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 27))
	
	os.system("crunch {0} {0} -t %{1}@%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 28))
	
	os.system("crunch {0} {0} -t @{1}%%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 29))
	
	os.system("crunch {0} {0} -t {1}@@%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 30))
	
	os.system("crunch {0} {0} -t {1}@%@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 31))
	
	os.system("crunch {0} {0} -t {1}%@@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 32))
	
	os.system("crunch {0} {0} -t {1}%%@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 33))
	
	os.system("crunch {0} {0} -t {1}%@%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 34))
	
	os.system("crunch {0} {0} -t {1}@%%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 35))
	
	#combo 2 names
	os.system("crunch {0} {0} -t @%{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 36))
	
	os.system("crunch {0} {0} -t %@{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 37))
	
	os.system("crunch {0} {0} -t @{1}%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 38))
	
	os.system("crunch {0} {0} -t %{1}@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 39))
	
	os.system("crunch {0} {0} -t {1}@%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 40))
	
	os.system("crunch {0} {0} -t {1}%@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 41))
	
	os.system("crunch {0} {0} -t {1}@@%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 42))
	
	os.system("crunch {0} {0} -t {1}@%@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 43))
	
	os.system("crunch {0} {0} -t {1}%@@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 44))
	
	os.system("crunch {0} {0} -t {1}%%@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 45))
	
	os.system("crunch {0} {0} -t {1}%@%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 46))
	
	os.system("crunch {0} {0} -t {1}@%%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 47))
	
	os.system("crunch {0} {0} -t @@%{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 48))
	
	os.system("crunch {0} {0} -t @%@{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 49))
	
	os.system("crunch {0} {0} -t %@@{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 50))
	
	os.system("crunch {0} {0} -t %%@{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 51))
	
	os.system("crunch {0} {0} -t %@%{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 52))
	
	os.system("crunch {0} {0} -t @%%{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 53))
	
	os.system("crunch {0} {0} -t @@{1}%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 54))
	
	os.system("crunch {0} {0} -t @%{1}@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 55))
	
	os.system("crunch {0} {0} -t %@{1}@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 56))
	
	os.system("crunch {0} {0} -t %%{1}@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 57))
	
	os.system("crunch {0} {0} -t %@{1}%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 58))
	
	os.system("crunch {0} {0} -t @%{1}%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 59))
	
	os.system("crunch {0} {0} -t @{1}@%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 60))
	
	os.system("crunch {0} {0} -t @{1}%@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 61))
	
	os.system("crunch {0} {0} -t %{1}@@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 62))
	
	os.system("crunch {0} {0} -t %{1}%@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 63))
	
	os.system("crunch {0} {0} -t %{1}@%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 64))
	
	os.system("crunch {0} {0} -t @{1}%%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 65))
	
	os.system("crunch {0} {0} -t {1}@@%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 66))
	
	os.system("crunch {0} {0} -t {1}@%@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 67))
	
	os.system("crunch {0} {0} -t {1}%@@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 68))
	
	os.system("crunch {0} {0} -t {1}%%@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 69))
	
	os.system("crunch {0} {0} -t {1}%@%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 70))
	
	os.system("crunch {0} {0} -t {1}@%%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 71))
	

def dvije_rijeci_druga_mix_lower_numeric(prva_rijec, druga_rijec, folder, rijecnik, txt_broj):
	

	os.system("crunch {0} {0} -t {1}@{2}% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj))
	
	os.system("crunch {0} {0} -t {1}%{2}@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 1))
	
	os.system("crunch {0} {0} -t @{1}{2}% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 2))
	
	os.system("crunch {0} {0} -t %{1}{2}@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 3))
	
	os.system("crunch {0} {0} -t {1}@{2}@% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 4))
	
	os.system("crunch {0} {0} -t {1}@{2}%@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 5))
	
	os.system("crunch {0} {0} -t {1}@{2}%% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 6))
	
	os.system("crunch {0} {0} -t {1}%{2}@@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 7))
	
	os.system("crunch {0} {0} -t {1}%{2}%@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 8))
	
	os.system("crunch {0} {0} -t {1}%{2}@% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 9))
	
	os.system("crunch {0} {0} -t {1}@@{2}% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 10))
	
	os.system("crunch {0} {0} -t {1}@%{2}@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 11))
	
	os.system("crunch {0} {0} -t {1}%@{2}@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 12))
	
	os.system("crunch {0} {0} -t {1}%%{2}@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 13))
	
	os.system("crunch {0} {0} -t {1}%@{2}% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 14))
	
	os.system("crunch {0} {0} -t {1}@%{2}% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 15))
	
	os.system("crunch {0} {0} -t {1}{2}%@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 16))
	
	os.system("crunch {0} {0} -t {1}{2}@% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 17))
	
	os.system("crunch {0} {0} -t {1}{2}@@% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 18))
	
	os.system("crunch {0} {0} -t {1}{2}@%@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 19))
	
	os.system("crunch {0} {0} -t {1}{2}%@@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 20))
	
	os.system("crunch {0} {0} -t {1}{2}%%@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 21))
	
	os.system("crunch {0} {0} -t {1}{2}%@% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 22))
	
	os.system("crunch {0} {0} -t {1}{2}@%% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 23))
	
	#combo 2 names
	os.system("crunch {0} {0} -t {1}@{2}% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 24))
	
	os.system("crunch {0} {0} -t {1}%{2}@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 25))
	
	os.system("crunch {0} {0} -t @{1}{2}% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 26))
	
	os.system("crunch {0} {0} -t %{1}{2}@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 27))
	
	os.system("crunch {0} {0} -t {1}@{2}@% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 28))
	
	os.system("crunch {0} {0} -t {1}@{2}%@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 29))
	
	os.system("crunch {0} {0} -t {1}@{2}%% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 30))
	
	os.system("crunch {0} {0} -t {1}%{2}@@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 31))
	
	os.system("crunch {0} {0} -t {1}%{2}%@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 32))
	
	os.system("crunch {0} {0} -t {1}%{2}@% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 33))
	
	os.system("crunch {0} {0} -t {1}@@{2}% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 34))
	
	os.system("crunch {0} {0} -t {1}@%{2}@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 35))
	
	os.system("crunch {0} {0} -t {1}%@{2}@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 36))
	
	os.system("crunch {0} {0} -t {1}%%{2}@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 37))
	
	os.system("crunch {0} {0} -t {1}%@{2}% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 38))
	
	os.system("crunch {0} {0} -t {1}@%{2}% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 39))
	
	os.system("crunch {0} {0} -t {1}{2}%@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 40))
	
	os.system("crunch {0} {0} -t {1}{2}@% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 41))
	
	os.system("crunch {0} {0} -t {1}{2}@@% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 42))
	
	os.system("crunch {0} {0} -t {1}{2}@%@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 43))
	
	os.system("crunch {0} {0} -t {1}{2}%@@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 44))
	
	os.system("crunch {0} {0} -t {1}{2}%%@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 45))
	
	os.system("crunch {0} {0} -t {1}{2}%@% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 46))
	
	os.system("crunch {0} {0} -t {1}{2}@%% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 47))
	

def dvije_rijeci_prva_mix_lower_upper_numeric(prva_rijec, druga_rijec, folder, rijecnik, txt_broj):
	

	os.system("crunch {0} {0} -t @,%{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj))
	
	os.system("crunch {0} {0} -t @%,{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 1))
	
	os.system("crunch {0} {0} -t %@,{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 2))
	
	os.system("crunch {0} {0} -t %,@{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 3))
	
	os.system("crunch {0} {0} -t ,@%{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 4))
	
	os.system("crunch {0} {0} -t ,%@{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 5))
	
	os.system("crunch {0} {0} -t @{1},%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 6))
	
	os.system("crunch {0} {0} -t @{1}%,{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 7))
	
	os.system("crunch {0} {0} -t %{1}@,{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 8))
	
	os.system("crunch {0} {0} -t %{1},@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 9))
	
	os.system("crunch {0} {0} -t ,{1}@%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 10))
	
	os.system("crunch {0} {0} -t ,{1}%@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 11))
	
	os.system("crunch {0} {0} -t @,{1}%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 12))
	
	os.system("crunch {0} {0} -t @%{1},{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 13))
	
	os.system("crunch {0} {0} -t %@{1},{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 14))
	
	os.system("crunch {0} {0} -t %,{1}@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 15))
	
	os.system("crunch {0} {0} -t ,@{1}%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 16))
	
	os.system("crunch {0} {0} -t ,%{1}@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 17))
	
	os.system("crunch {0} {0} -t {1}@,%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 18))
	
	os.system("crunch {0} {0} -t {1}@%,{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 19))
	
	os.system("crunch {0} {0} -t {1}%@,{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 20))
	
	os.system("crunch {0} {0} -t {1}%,@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 21))
	
	os.system("crunch {0} {0} -t {1},@%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 22))
	
	os.system("crunch {0} {0} -t {1},%@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 23))
	
	#combo 2 names
	os.system("crunch {0} {0} -t @,%{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 24))
	
	os.system("crunch {0} {0} -t @%,{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 25))
	
	os.system("crunch {0} {0} -t %@,{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 26))
	
	os.system("crunch {0} {0} -t %,@{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 27))
	
	os.system("crunch {0} {0} -t ,@%{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 28))
	
	os.system("crunch {0} {0} -t ,%@{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 29))
	
	os.system("crunch {0} {0} -t @{1},%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 30))
	
	os.system("crunch {0} {0} -t @{1}%,{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 31))
	
	os.system("crunch {0} {0} -t %{1}@,{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 32))
	
	os.system("crunch {0} {0} -t %{1},@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 33))
	
	os.system("crunch {0} {0} -t ,{1}@%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 34))
	
	os.system("crunch {0} {0} -t ,{1}%@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 35))
	
	os.system("crunch {0} {0} -t @,{1}%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 36))
	
	os.system("crunch {0} {0} -t @%{1},{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 37))
	
	os.system("crunch {0} {0} -t %@{1},{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 38))
	
	os.system("crunch {0} {0} -t %,{1}@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 39))
	
	os.system("crunch {0} {0} -t ,@{1}%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 40))
	
	os.system("crunch {0} {0} -t ,%{1}@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 41))
	
	os.system("crunch {0} {0} -t {1}@,%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 42))
	
	os.system("crunch {0} {0} -t {1}@%,{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 43))
	
	os.system("crunch {0} {0} -t {1}%@,{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 44))
	
	os.system("crunch {0} {0} -t {1}%,@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 45))
	
	os.system("crunch {0} {0} -t {1},@%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 46))
	
	os.system("crunch {0} {0} -t {1},%@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 47))
	

def dvije_rijeci_druga_mix_lower_upper_numeric(prva_rijec, druga_rijec, folder, rijecnik, txt_broj):
	

	os.system("crunch {0} {0} -t {1}{2}@,% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj))
	
	os.system("crunch {0} {0} -t {1}{2}@%, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 1))
	
	os.system("crunch {0} {0} -t {1}{2}%@, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 2))
	
	os.system("crunch {0} {0} -t {1}{2}%,@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 3))
	
	os.system("crunch {0} {0} -t {1}{2},@% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 4))
	
	os.system("crunch {0} {0} -t {1}{2},%@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 5))
	
	os.system("crunch {0} {0} -t {1}@{2},% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 6))
	
	os.system("crunch {0} {0} -t {1}@{2}%, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 7))
	
	os.system("crunch {0} {0} -t {1}%{2}@, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 8))
	
	os.system("crunch {0} {0} -t {1}%{2},@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 9))
	
	os.system("crunch {0} {0} -t {1},{2}@% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 10))
	
	os.system("crunch {0} {0} -t {1},{2}%@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 11))
	
	os.system("crunch {0} {0} -t {1}@,{2}% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 12))
	
	os.system("crunch {0} {0} -t {1}@%{2}, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 13))
	
	os.system("crunch {0} {0} -t {1}%@{2}, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 14))
	
	os.system("crunch {0} {0} -t {1}%,{2}@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 15))
	
	os.system("crunch {0} {0} -t {1},@{2}% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 16))
	
	os.system("crunch {0} {0} -t {1},%{2}@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 17))
	
	os.system("crunch {0} {0} -t @{1},{2}% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 18))
	
	os.system("crunch {0} {0} -t @{1}%{2}, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 19))
	
	os.system("crunch {0} {0} -t %{1}@{2}, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 20))
	
	os.system("crunch {0} {0} -t %{1},{2}@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 21))
	
	os.system("crunch {0} {0} -t ,{1}@{2}% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 22))
	
	os.system("crunch {0} {0} -t ,{1}%{2}@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 23))
	
	#combo 2 names
	os.system("crunch {0} {0} -t {1}{2}@,% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 24))
	
	os.system("crunch {0} {0} -t {1}{2}@%, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 25))
	
	os.system("crunch {0} {0} -t {1}{2}%@, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 26))
	
	os.system("crunch {0} {0} -t {1}{2}%,@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 27))
	
	os.system("crunch {0} {0} -t {1}{2},@% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 28))
	
	os.system("crunch {0} {0} -t {1}{2},%@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 29))
	
	os.system("crunch {0} {0} -t {1}@{2},% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 30))
	
	os.system("crunch {0} {0} -t {1}@{2}%, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 31))
	
	os.system("crunch {0} {0} -t {1}%{2}@, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 32))
	
	os.system("crunch {0} {0} -t {1}%{2},@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 33))
	
	os.system("crunch {0} {0} -t {1},{2}@% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 34))
	
	os.system("crunch {0} {0} -t {1},{2}%@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 35))
	
	os.system("crunch {0} {0} -t {1}@,{2}% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 36))
	
	os.system("crunch {0} {0} -t {1}@%{2}, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 37))
	
	os.system("crunch {0} {0} -t {1}%@{2}, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 38))
	
	os.system("crunch {0} {0} -t {1}%,{2}@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 39))
	
	os.system("crunch {0} {0} -t {1},@{2}% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 40))
	
	os.system("crunch {0} {0} -t {1},%{2}@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 41))
	
	os.system("crunch {0} {0} -t @{1},{2}% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 42))
	
	os.system("crunch {0} {0} -t @{1}%{2}, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 43))
	
	os.system("crunch {0} {0} -t %{1}@{2}, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 44))
	
	os.system("crunch {0} {0} -t %{1},{2}@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 45))
	
	os.system("crunch {0} {0} -t ,{1}@{2}% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 46))
	
	os.system("crunch {0} {0} -t ,{1}%{2}@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 47))
	

def dvije_rijeci_char(prva_rijec, druga_rijec, folder, rijecnik, txt_broj):
	

	os.system("crunch {0} {0} -t {1}{2}^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 1, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj))
	
	os.system("crunch {0} {0} -t {1}{2}^^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 1))
	
	os.system("crunch {0} {0} -t {1}{2}^^^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 2))
	
	os.system("crunch {0} {0} -t {1}^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 1, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 3))
	
	os.system("crunch {0} {0} -t {1}^{2}^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 4))
	
	os.system("crunch {0} {0} -t {1}^{2}^^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 5))
	
	os.system("crunch {0} {0} -t {1}^^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 6))
	
	os.system("crunch {0} {0} -t {1}^^{2}^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 7))
	
	os.system("crunch {0} {0} -t {1}^^^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 8))
	
	os.system("crunch {0} {0} -t ^{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 1, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 9))
	
	os.system("crunch {0} {0} -t ^^{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj +10))
	
	os.system("crunch {0} {0} -t ^^^{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 11))
	
	os.system("crunch {0} {0} -t ^{1}{2}^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 12))
	
	os.system("crunch {0} {0} -t ^{1}{2}^^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 13))
	
	os.system("crunch {0} {0} -t ^^{1}{2}^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 14))
	
	os.system("crunch {0} {0} -t ^{1}^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 15))
	
	os.system("crunch {0} {0} -t ^{1}^^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 16))
	
	os.system("crunch {0} {0} -t ^^{1}^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 17))
	
	os.system("crunch {0} {0} -t ^{1}^{2}^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 18))
	
	#combo 2 names
	os.system("crunch {0} {0} -t {1}{2}^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 1, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 19))
	
	os.system("crunch {0} {0} -t {1}{2}^^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 20))
	
	os.system("crunch {0} {0} -t {1}{2}^^^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 21))
	
	os.system("crunch {0} {0} -t {1}^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 1, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 22))
	
	os.system("crunch {0} {0} -t {1}^{2}^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 23))
	
	os.system("crunch {0} {0} -t {1}^{2}^^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 24))
	
	os.system("crunch {0} {0} -t {1}^^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 25))
	
	os.system("crunch {0} {0} -t {1}^^{2}^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 26))
	
	os.system("crunch {0} {0} -t {1}^^^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 27))
	
	os.system("crunch {0} {0} -t ^{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 1, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 28))
	
	os.system("crunch {0} {0} -t ^^{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 29))
	
	os.system("crunch {0} {0} -t ^^^{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 30))
	
	os.system("crunch {0} {0} -t ^{1}{2}^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 31))
	
	os.system("crunch {0} {0} -t ^{1}{2}^^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 32))
	
	os.system("crunch {0} {0} -t ^^{1}{2}^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 33))
	
	os.system("crunch {0} {0} -t ^{1}^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 34))
	
	os.system("crunch {0} {0} -t ^{1}^^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 35))
	
	os.system("crunch {0} {0} -t ^^{1}^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 36))
	
	os.system("crunch {0} {0} -t ^{1}^{2}^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 37))
	

def dvije_rijeci_prva_mix_upper_char(prva_rijec, druga_rijec, folder, rijecnik, txt_broj):
	

	os.system("crunch {0} {0} -t ,^{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj))
	
	os.system("crunch {0} {0} -t ^,{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 1))
	
	os.system("crunch {0} {0} -t ,{1}^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 2))
	
	os.system("crunch {0} {0} -t ^{1},{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 3))
	
	os.system("crunch {0} {0} -t {1},^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 4))
	
	os.system("crunch {0} {0} -t {1}^,{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 5))
	
	os.system("crunch {0} {0} -t {1},,^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 6))
	
	os.system("crunch {0} {0} -t {1},^,{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 7))
	
	os.system("crunch {0} {0} -t {1},^^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 8))
	
	os.system("crunch {0} {0} -t {1}^,,{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 9))
	
	os.system("crunch {0} {0} -t {1}^^,{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 10))
	
	os.system("crunch {0} {0} -t {1}^,^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 11))
	
	os.system("crunch {0} {0} -t ^,,{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 12))
	
	os.system("crunch {0} {0} -t ,^,{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 13))
	
	os.system("crunch {0} {0} -t ,,^{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 14))
	
	os.system("crunch {0} {0} -t ^^,{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 15))
	
	os.system("crunch {0} {0} -t ,^^{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 16))
	
	os.system("crunch {0} {0} -t ^,^{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 17))
	
	os.system("crunch {0} {0} -t ^{1},,{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 18))
	
	os.system("crunch {0} {0} -t ^{1},^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 19))
	
	os.system("crunch {0} {0} -t ^{1}^,{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 20))
	
	os.system("crunch {0} {0} -t ,{1}^^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 21))
	
	os.system("crunch {0} {0} -t ,{1},^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 22))
	
	os.system("crunch {0} {0} -t ,{1}^,{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 23))
	
	os.system("crunch {0} {0} -t ,^{1},{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 24))
	
	os.system("crunch {0} {0} -t ,^{1}^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 25))
	
	os.system("crunch {0} {0} -t ^,{1},{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 26))
	
	os.system("crunch {0} {0} -t ^,{1}^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 27))
	
	#combo 2 names
	os.system("crunch {0} {0} -t ,^{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 28))
	
	os.system("crunch {0} {0} -t ^,{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 29))
	
	os.system("crunch {0} {0} -t ,{1}^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 30))
	
	os.system("crunch {0} {0} -t ^{1},{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 31))
	
	os.system("crunch {0} {0} -t {1},^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 32))
	
	os.system("crunch {0} {0} -t {1}^,{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 33))
	
	os.system("crunch {0} {0} -t {1},,^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 34))
	
	os.system("crunch {0} {0} -t {1},^,{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 35))
	
	os.system("crunch {0} {0} -t {1},^^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 36))
	
	os.system("crunch {0} {0} -t {1}^,,{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 37))
	
	os.system("crunch {0} {0} -t {1}^^,{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 38))
	
	os.system("crunch {0} {0} -t {1}^,^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 39))
	
	os.system("crunch {0} {0} -t ^,,{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 40))
	
	os.system("crunch {0} {0} -t ,^,{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 41))
	
	os.system("crunch {0} {0} -t ,,^{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 42))
	
	os.system("crunch {0} {0} -t ^^,{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 43))
	
	os.system("crunch {0} {0} -t ,^^{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 44))
	
	os.system("crunch {0} {0} -t ^,^{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 45))
	
	os.system("crunch {0} {0} -t ^{1},,{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 46))
	
	os.system("crunch {0} {0} -t ^{1},^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 47))
	
	os.system("crunch {0} {0} -t ^{1}^,{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 48))
	
	os.system("crunch {0} {0} -t ,{1}^^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 49))
	
	os.system("crunch {0} {0} -t ,{1},^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 50))
	
	os.system("crunch {0} {0} -t ,{1}^,{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 51))
	
	os.system("crunch {0} {0} -t ,^{1},{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 52))
	
	os.system("crunch {0} {0} -t ,^{1}^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 53))
	
	os.system("crunch {0} {0} -t ^,{1},{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 54))
	
	os.system("crunch {0} {0} -t ^,{1}^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 55))
	

def dvije_rijeci_druga_mix_upper_char(prva_rijec, druga_rijec, folder, rijecnik, txt_broj):
	

	os.system("crunch {0} {0} -t {1}{2},^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj))
	
	os.system("crunch {0} {0} -t {1}{2}^, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 1))
	
	os.system("crunch {0} {0} -t {1}{2},,^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 2))
	
	os.system("crunch {0} {0} -t {1}{2},^, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 3))
	
	os.system("crunch {0} {0} -t {1}{2}^,, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 4))
	
	os.system("crunch {0} {0} -t {1}{2},^^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 5))
	
	os.system("crunch {0} {0} -t {1}{2}^,^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 6))
	
	os.system("crunch {0} {0} -t {1}{2}^^, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 7))
	
	os.system("crunch {0} {0} -t {1}^{2}, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 8))
	
	os.system("crunch {0} {0} -t {1},{2}^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 9))
	
	os.system("crunch {0} {0} -t {1},,{2}^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 10))
	
	os.system("crunch {0} {0} -t {1},^{2}, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 11))
	
	os.system("crunch {0} {0} -t {1}^,{2}, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 12))
	
	os.system("crunch {0} {0} -t {1}^^{2}, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 13))
	
	os.system("crunch {0} {0} -t {1}^,{2}^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 14))
	
	os.system("crunch {0} {0} -t {1},^{2}, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 15))
	
	os.system("crunch {0} {0} -t ,{1}{2}^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 16))
	
	os.system("crunch {0} {0} -t ^{1}{2}, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 17))
	
	os.system("crunch {0} {0} -t ,{1}{2},^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 18))
	
	os.system("crunch {0} {0} -t ,{1}{2}^, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 19))
	
	os.system("crunch {0} {0} -t ,,{1}{2}^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 20))
	
	os.system("crunch {0} {0} -t ,^{1}{2}, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 21))
	
	os.system("crunch {0} {0} -t ^,{1}{2}, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 22))
	
	os.system("crunch {0} {0} -t ,^{1}{2}^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 23))
	
	os.system("crunch {0} {0} -t ^,{1}{2}^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 24))
	
	os.system("crunch {0} {0} -t ^^{1}{2}, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 25))
	
	#combo 2 names
	os.system("crunch {0} {0} -t {1}{2},^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 26))
	
	os.system("crunch {0} {0} -t {1}{2}^, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 27))
	
	os.system("crunch {0} {0} -t {1}{2},,^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 28))
	
	os.system("crunch {0} {0} -t {1}{2},^, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 29))
	
	os.system("crunch {0} {0} -t {1}{2}^,, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 30))
	
	os.system("crunch {0} {0} -t {1}{2},^^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 31))
	
	os.system("crunch {0} {0} -t {1}{2}^,^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 32))
	
	os.system("crunch {0} {0} -t {1}{2}^^, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 33))
	
	os.system("crunch {0} {0} -t {1}^{2}, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 34))
	
	os.system("crunch {0} {0} -t {1},{2}^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 35))
	
	os.system("crunch {0} {0} -t {1},,{2}^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 36))
	
	os.system("crunch {0} {0} -t {1},^{2}, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 37))
	
	os.system("crunch {0} {0} -t {1}^,{2}, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 38))
	
	os.system("crunch {0} {0} -t {1}^^{2}, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 39))
	
	os.system("crunch {0} {0} -t {1}^,{2}^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 40))
	
	os.system("crunch {0} {0} -t {1},^{2}, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 41))
	
	os.system("crunch {0} {0} -t ,{1}{2}^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 42))
	
	os.system("crunch {0} {0} -t ^{1}{2}, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 43))
	
	os.system("crunch {0} {0} -t ,{1}{2},^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 44))
	
	os.system("crunch {0} {0} -t ,{1}{2}^, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 45))
	
	os.system("crunch {0} {0} -t ,,{1}{2}^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 46))
	
	os.system("crunch {0} {0} -t ,^{1}{2}, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 47))
	
	os.system("crunch {0} {0} -t ^,{1}{2}, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 48))
	
	os.system("crunch {0} {0} -t ,^{1}{2}^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 49))
	
	os.system("crunch {0} {0} -t ^,{1}{2}^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 50))
	
	os.system("crunch {0} {0} -t ^^{1}{2}, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 51))
	

def dvije_rijeci_prva_mix_lower_char(prva_rijec, druga_rijec, folder, rijecnik, txt_broj):
	

	os.system("crunch {0} {0} -t @^{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj))
	
	os.system("crunch {0} {0} -t ^@{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 1))
	
	os.system("crunch {0} {0} -t @{1}^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 2))
	
	os.system("crunch {0} {0} -t ^{1}@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 3))
	
	os.system("crunch {0} {0} -t {1}@^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 4))
	
	os.system("crunch {0} {0} -t {1}^@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 5))
	
	os.system("crunch {0} {0} -t {1}@@^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 6))
	
	os.system("crunch {0} {0} -t {1}@^@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 7))
	
	os.system("crunch {0} {0} -t {1}@^^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 8))
	
	os.system("crunch {0} {0} -t {1}^@@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 9))
	
	os.system("crunch {0} {0} -t {1}^^@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 10))
	
	os.system("crunch {0} {0} -t {1}^@^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 11))
	
	os.system("crunch {0} {0} -t ^@@{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 12))
	
	os.system("crunch {0} {0} -t @^@{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 13))
	
	os.system("crunch {0} {0} -t @@^{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 14))
	
	os.system("crunch {0} {0} -t ^^@{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 15))
	
	os.system("crunch {0} {0} -t @^^{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 16))
	
	os.system("crunch {0} {0} -t ^@^{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 17))
	
	os.system("crunch {0} {0} -t ^{1}@@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 18))
	
	os.system("crunch {0} {0} -t ^{1}@^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 19))
	
	os.system("crunch {0} {0} -t ^{1}^@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 20))
	
	os.system("crunch {0} {0} -t @{1}^^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 21))
	
	os.system("crunch {0} {0} -t @{1}@^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 22))
	
	os.system("crunch {0} {0} -t @{1}^@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 23))
	
	os.system("crunch {0} {0} -t @^{1}@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 24))
	
	os.system("crunch {0} {0} -t @^{1}^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 25))
	
	os.system("crunch {0} {0} -t ^@{1}@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 26))
	
	os.system("crunch {0} {0} -t ^@{1}^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 27))
	
	#combo 2 names
	os.system("crunch {0} {0} -t @^{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 28))
	
	os.system("crunch {0} {0} -t ^@{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 29))
	
	os.system("crunch {0} {0} -t @{1}^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 30))
	
	os.system("crunch {0} {0} -t ^{1}@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 31))
	
	os.system("crunch {0} {0} -t {1}@^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 32))
	
	os.system("crunch {0} {0} -t {1}^@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 33))
	
	os.system("crunch {0} {0} -t {1}@@^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 34))
	
	os.system("crunch {0} {0} -t {1}@^@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 35))
	
	os.system("crunch {0} {0} -t {1}@^^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 36))
	
	os.system("crunch {0} {0} -t {1}^@@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 37))
	
	os.system("crunch {0} {0} -t {1}^^@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 38))
	
	os.system("crunch {0} {0} -t {1}^@^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 39))
	
	os.system("crunch {0} {0} -t ^@@{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 40))
	
	os.system("crunch {0} {0} -t @^@{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 41))
	
	os.system("crunch {0} {0} -t @@^{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 42))
	
	os.system("crunch {0} {0} -t ^^@{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 43))
	
	os.system("crunch {0} {0} -t @^^{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 44))
	
	os.system("crunch {0} {0} -t ^@^{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 45))
	
	os.system("crunch {0} {0} -t ^{1}@@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 46))
	
	os.system("crunch {0} {0} -t ^{1}@^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 47))
	
	os.system("crunch {0} {0} -t ^{1}^@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 48))
	
	os.system("crunch {0} {0} -t @{1}^^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 49))
	
	os.system("crunch {0} {0} -t @{1}@^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 50))
	
	os.system("crunch {0} {0} -t @{1}^@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 51))
	
	os.system("crunch {0} {0} -t @^{1}@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 52))
	
	os.system("crunch {0} {0} -t @^{1}^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 53))
	
	os.system("crunch {0} {0} -t ^@{1}@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 54))
	
	os.system("crunch {0} {0} -t ^@{1}^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 55))
	

def dvije_rijeci_druga_mix_lower_char(prva_rijec, druga_rijec, folder, rijecnik, txt_broj):
	

	os.system("crunch {0} {0} -t {1}{2}@^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj))
	
	os.system("crunch {0} {0} -t {1}{2}^@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 1))
	
	os.system("crunch {0} {0} -t {1}{2}@@^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 2))
	
	os.system("crunch {0} {0} -t {1}{2}@^@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 3))
	
	os.system("crunch {0} {0} -t {1}{2}^@@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 4))
	
	os.system("crunch {0} {0} -t {1}{2}@^^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 5))
	
	os.system("crunch {0} {0} -t {1}{2}^@^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 6))
	
	os.system("crunch {0} {0} -t {1}{2}^^@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 7))
	
	os.system("crunch {0} {0} -t {1}^{2}@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 8))
	
	os.system("crunch {0} {0} -t {1}@{2}^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 9))
	
	os.system("crunch {0} {0} -t {1}@@{2}^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 10))
	
	os.system("crunch {0} {0} -t {1}@^{2}@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 11))
	
	os.system("crunch {0} {0} -t {1}^@{2}@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 12))
	
	os.system("crunch {0} {0} -t {1}^^{2}@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 13))
	
	os.system("crunch {0} {0} -t {1}^@{2}^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 14))
	
	os.system("crunch {0} {0} -t {1}@^{2}@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 15))
	
	os.system("crunch {0} {0} -t @{1}{2}^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 16))
	
	os.system("crunch {0} {0} -t ^{1}{2}@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 17))
	
	os.system("crunch {0} {0} -t @{1}{2}@^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 18))
	
	os.system("crunch {0} {0} -t @{1}{2}^@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 19))
	
	os.system("crunch {0} {0} -t @@{1}{2}^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 20))
	
	os.system("crunch {0} {0} -t @^{1}{2}@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 21))
	
	os.system("crunch {0} {0} -t ^@{1}{2}@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 22))
	
	os.system("crunch {0} {0} -t @^{1}{2}^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 23))
	
	os.system("crunch {0} {0} -t ^@{1}{2}^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 24))
	
	os.system("crunch {0} {0} -t ^^{1}{2}@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 25))
	
	#combo 2 names
	os.system("crunch {0} {0} -t {1}{2}@^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 26))
	
	os.system("crunch {0} {0} -t {1}{2}^@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 27))
	
	os.system("crunch {0} {0} -t {1}{2}@@^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 28))
	
	os.system("crunch {0} {0} -t {1}{2}@^@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 29))
	
	os.system("crunch {0} {0} -t {1}{2}^@@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 30))
	
	os.system("crunch {0} {0} -t {1}{2}@^^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 31))
	
	os.system("crunch {0} {0} -t {1}{2}^@^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 32))
	
	os.system("crunch {0} {0} -t {1}{2}^^@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 33))
	
	os.system("crunch {0} {0} -t {1}^{2}@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 34))
	
	os.system("crunch {0} {0} -t {1}@{2}^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 35))
	
	os.system("crunch {0} {0} -t {1}@@{2}^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 36))
	
	os.system("crunch {0} {0} -t {1}@^{2}@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 37))
	
	os.system("crunch {0} {0} -t {1}^@{2}@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 38))
	
	os.system("crunch {0} {0} -t {1}^^{2}@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 39))
	
	os.system("crunch {0} {0} -t {1}^@{2}^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 40))
	
	os.system("crunch {0} {0} -t {1}@^{2}@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 41))
	
	os.system("crunch {0} {0} -t @{1}{2}^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 42))
	
	os.system("crunch {0} {0} -t ^{1}{2}@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 43))
	
	os.system("crunch {0} {0} -t @{1}{2}@^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 44))
	
	os.system("crunch {0} {0} -t @{1}{2}^@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 45))
	
	os.system("crunch {0} {0} -t @@{1}{2}^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 46))
	
	os.system("crunch {0} {0} -t @^{1}{2}@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 47))
	
	os.system("crunch {0} {0} -t ^@{1}{2}@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 48))
	
	os.system("crunch {0} {0} -t @^{1}{2}^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 49))
	
	os.system("crunch {0} {0} -t ^@{1}{2}^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 50))
	
	os.system("crunch {0} {0} -t ^^{1}{2}@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 51))
	

def dvije_rijeci_prva_mix_numeric_char(prva_rijec, druga_rijec, folder, rijecnik, txt_broj):
	

	os.system("crunch {0} {0} -t %^{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj))
	
	os.system("crunch {0} {0} -t ^%{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 1))
	
	os.system("crunch {0} {0} -t %{1}^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 2))
	
	os.system("crunch {0} {0} -t ^{1}%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 3))
	
	os.system("crunch {0} {0} -t {1}%^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 4))
	
	os.system("crunch {0} {0} -t {1}^%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 5))
	
	os.system("crunch {0} {0} -t {1}%%^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 6))
	
	os.system("crunch {0} {0} -t {1}%^%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 7))
	
	os.system("crunch {0} {0} -t {1}%^^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 8))
	
	os.system("crunch {0} {0} -t {1}^%%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 9))
	
	os.system("crunch {0} {0} -t {1}^^%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 10))
	
	os.system("crunch {0} {0} -t {1}^%^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 11))
	
	os.system("crunch {0} {0} -t ^%%{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 12))
	
	os.system("crunch {0} {0} -t %^%{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 13))
	
	os.system("crunch {0} {0} -t %%^{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 14))
	
	os.system("crunch {0} {0} -t ^^%{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 15))
	
	os.system("crunch {0} {0} -t %^^{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 16))
	
	os.system("crunch {0} {0} -t ^%^{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 17))
	
	os.system("crunch {0} {0} -t ^{1}%%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 18))
	
	os.system("crunch {0} {0} -t ^{1}%^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 19))
	
	os.system("crunch {0} {0} -t ^{1}^%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 20))
	
	os.system("crunch {0} {0} -t %{1}^^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 21))
	
	os.system("crunch {0} {0} -t %{1}%^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 22))
	
	os.system("crunch {0} {0} -t %{1}^%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 23))
	
	os.system("crunch {0} {0} -t %^{1}%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 24))
	
	os.system("crunch {0} {0} -t %^{1}^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 25))
	
	os.system("crunch {0} {0} -t ^%{1}%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 26))
	
	os.system("crunch {0} {0} -t ^%{1}^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 27))
	
	#combo 2 names
	os.system("crunch {0} {0} -t %^{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 28))
	
	os.system("crunch {0} {0} -t ^%{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 29))
	
	os.system("crunch {0} {0} -t %{1}^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 30))
	
	os.system("crunch {0} {0} -t ^{1}%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 31))
	
	os.system("crunch {0} {0} -t {1}%^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 32))
	
	os.system("crunch {0} {0} -t {1}^%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 33))
	
	os.system("crunch {0} {0} -t {1}%%^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 34))
	
	os.system("crunch {0} {0} -t {1}%^%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 35))
	
	os.system("crunch {0} {0} -t {1}%^^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 36))
	
	os.system("crunch {0} {0} -t {1}^%%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 37))
	
	os.system("crunch {0} {0} -t {1}^^%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 38))
	
	os.system("crunch {0} {0} -t {1}^%^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 39))
	
	os.system("crunch {0} {0} -t ^%%{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 40))
	
	os.system("crunch {0} {0} -t %^%{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 41))
	
	os.system("crunch {0} {0} -t %%^{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 42))
	
	os.system("crunch {0} {0} -t ^^%{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 43))
	
	os.system("crunch {0} {0} -t %^^{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 44))
	
	os.system("crunch {0} {0} -t ^%^{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 45))
	
	os.system("crunch {0} {0} -t ^{1}%%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 46))
	
	os.system("crunch {0} {0} -t ^{1}%^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 47))
	
	os.system("crunch {0} {0} -t ^{1}^%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 48))
	
	os.system("crunch {0} {0} -t %{1}^^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 49))
	
	os.system("crunch {0} {0} -t %{1}%^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 50))
	
	os.system("crunch {0} {0} -t %{1}^%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 51))
	
	os.system("crunch {0} {0} -t %^{1}%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 52))
	
	os.system("crunch {0} {0} -t %^{1}^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 53))
	
	os.system("crunch {0} {0} -t ^%{1}%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 54))
	
	os.system("crunch {0} {0} -t ^%{1}^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 55))
	

def dvije_rijeci_druga_mix_numeric_char(prva_rijec, druga_rijec, folder, rijecnik, txt_broj):
	

	os.system("crunch {0} {0} -t {1}{2}%^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj))
	
	os.system("crunch {0} {0} -t {1}{2}^% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 1))
	
	os.system("crunch {0} {0} -t {1}{2}%%^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 2))
	
	os.system("crunch {0} {0} -t {1}{2}%^% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 3))
	
	os.system("crunch {0} {0} -t {1}{2}^%% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 4))
	
	os.system("crunch {0} {0} -t {1}{2}%^^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 5))
	
	os.system("crunch {0} {0} -t {1}{2}^%^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 6))
	
	os.system("crunch {0} {0} -t {1}{2}^^% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 7))
	
	os.system("crunch {0} {0} -t {1}^{2}% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 8))
	
	os.system("crunch {0} {0} -t {1}%{2}^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 9))
	
	os.system("crunch {0} {0} -t {1}%%{2}^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 10))
	
	os.system("crunch {0} {0} -t {1}%^{2}% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 11))
	
	os.system("crunch {0} {0} -t {1}^%{2}% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 12))
	
	os.system("crunch {0} {0} -t {1}^^{2}% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 13))
	
	os.system("crunch {0} {0} -t {1}^%{2}^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 14))
	
	os.system("crunch {0} {0} -t {1}%^{2}% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 15))
	
	os.system("crunch {0} {0} -t %{1}{2}^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 16))
	
	os.system("crunch {0} {0} -t ^{1}{2}% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 17))
	
	os.system("crunch {0} {0} -t %{1}{2}%^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 18))
	
	os.system("crunch {0} {0} -t %{1}{2}^% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 19))
	
	os.system("crunch {0} {0} -t %%{1}{2}^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 20))
	
	os.system("crunch {0} {0} -t %^{1}{2}% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 21))
	
	os.system("crunch {0} {0} -t ^%{1}{2}% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 22))
	
	os.system("crunch {0} {0} -t %^{1}{2}^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 23))
	
	os.system("crunch {0} {0} -t ^%{1}{2}^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 24))
	
	os.system("crunch {0} {0} -t ^^{1}{2}% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 25))
	
	#combo 2 names
	os.system("crunch {0} {0} -t {1}{2}%^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 26))
	
	os.system("crunch {0} {0} -t {1}{2}^% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 27))
	
	os.system("crunch {0} {0} -t {1}{2}%%^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 28))
	
	os.system("crunch {0} {0} -t {1}{2}%^% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 29))
	
	os.system("crunch {0} {0} -t {1}{2}^%% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 30))
	
	os.system("crunch {0} {0} -t {1}{2}%^^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 31))
	
	os.system("crunch {0} {0} -t {1}{2}^%^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 32))
	
	os.system("crunch {0} {0} -t {1}{2}^^% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 33))
	
	os.system("crunch {0} {0} -t {1}^{2}% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 34))
	
	os.system("crunch {0} {0} -t {1}%{2}^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 35))
	
	os.system("crunch {0} {0} -t {1}%%{2}^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 36))
	
	os.system("crunch {0} {0} -t {1}%^{2}% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 37))
	
	os.system("crunch {0} {0} -t {1}^%{2}% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 38))
	
	os.system("crunch {0} {0} -t {1}^^{2}% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 39))
	
	os.system("crunch {0} {0} -t {1}^%{2}^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 40))
	
	os.system("crunch {0} {0} -t {1}%^{2}% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 41))
	
	os.system("crunch {0} {0} -t %{1}{2}^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 42))
	
	os.system("crunch {0} {0} -t ^{1}{2}% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 2, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 43))
	
	os.system("crunch {0} {0} -t %{1}{2}%^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 44))
	
	os.system("crunch {0} {0} -t %{1}{2}^% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 45))
	
	os.system("crunch {0} {0} -t %%{1}{2}^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 46))
	
	os.system("crunch {0} {0} -t %^{1}{2}% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 47))
	
	os.system("crunch {0} {0} -t ^%{1}{2}% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 48))
	
	os.system("crunch {0} {0} -t %^{1}{2}^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 49))
	
	os.system("crunch {0} {0} -t ^%{1}{2}^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 50))
	
	os.system("crunch {0} {0} -t ^^{1}{2}% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 51))
	

def dvije_rijeci_prva_mix_upper_lower_char(prva_rijec, druga_rijec, folder, rijecnik, txt_broj):
	

	os.system("crunch {0} {0} -t @,^{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj))
	
	os.system("crunch {0} {0} -t @^,{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 1))
	
	os.system("crunch {0} {0} -t ^@,{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 2))
	
	os.system("crunch {0} {0} -t ^,@{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 3))
	
	os.system("crunch {0} {0} -t ,@^{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 4))
	
	os.system("crunch {0} {0} -t ,^@{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 5))
	
	os.system("crunch {0} {0} -t @{1},^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 6))
	
	os.system("crunch {0} {0} -t @{1}^,{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 7))
	
	os.system("crunch {0} {0} -t ^{1}@,{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 8))
	
	os.system("crunch {0} {0} -t ^{1},@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 9))
	
	os.system("crunch {0} {0} -t ,{1}@^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 10))
	
	os.system("crunch {0} {0} -t ,{1}^@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 11))
	
	os.system("crunch {0} {0} -t @,{1}^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 12))
	
	os.system("crunch {0} {0} -t @^{1},{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 13))
	
	os.system("crunch {0} {0} -t ^@{1},{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 14))
	
	os.system("crunch {0} {0} -t ^,{1}@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 15))
	
	os.system("crunch {0} {0} -t ,@{1}^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 16))
	
	os.system("crunch {0} {0} -t ,^{1}@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 17))
	
	os.system("crunch {0} {0} -t {1}@,^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 18))
	
	os.system("crunch {0} {0} -t {1}@^,{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 19))
	
	os.system("crunch {0} {0} -t {1}^@,{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 20))
	
	os.system("crunch {0} {0} -t {1}^,@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 21))
	
	os.system("crunch {0} {0} -t {1},@^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 22))
	
	os.system("crunch {0} {0} -t {1},^@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 23))
	
	#combo 2 names
	os.system("crunch {0} {0} -t @,^{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 24))
	
	os.system("crunch {0} {0} -t @^,{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 25))
	
	os.system("crunch {0} {0} -t ^@,{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 26))
	
	os.system("crunch {0} {0} -t ^,@{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 27))
	
	os.system("crunch {0} {0} -t ,@^{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 28))
	
	os.system("crunch {0} {0} -t ,^@{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 29))
	
	os.system("crunch {0} {0} -t @{1},^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 30))
	
	os.system("crunch {0} {0} -t @{1}^,{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 31))
	
	os.system("crunch {0} {0} -t ^{1}@,{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 32))
	
	os.system("crunch {0} {0} -t ^{1},@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 33))
	
	os.system("crunch {0} {0} -t ,{1}@^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 34))
	
	os.system("crunch {0} {0} -t ,{1}^@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 35))
	
	os.system("crunch {0} {0} -t @,{1}^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 36))
	
	os.system("crunch {0} {0} -t @^{1},{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 37))
	
	os.system("crunch {0} {0} -t ^@{1},{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 38))
	
	os.system("crunch {0} {0} -t ^,{1}@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 39))
	
	os.system("crunch {0} {0} -t ,@{1}^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 40))
	
	os.system("crunch {0} {0} -t ,^{1}@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 41))
	
	os.system("crunch {0} {0} -t {1}@,^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 42))
	
	os.system("crunch {0} {0} -t {1}@^,{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 43))
	
	os.system("crunch {0} {0} -t {1}^@,{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 44))
	
	os.system("crunch {0} {0} -t {1}^,@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 45))
	
	os.system("crunch {0} {0} -t {1},@^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 46))
	
	os.system("crunch {0} {0} -t {1},^@{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 47))
	

def dvije_rijeci_druga_mix_upper_lower_char(prva_rijec, druga_rijec, folder, rijecnik, txt_broj):
	

	os.system("crunch {0} {0} -t {1}{2}@,^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj))
	
	os.system("crunch {0} {0} -t {1}{2}@^, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 1))
	
	os.system("crunch {0} {0} -t {1}{2}^@, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 2))
	
	os.system("crunch {0} {0} -t {1}{2}^,@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 3))
	
	os.system("crunch {0} {0} -t {1}{2},@^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 4))
	
	os.system("crunch {0} {0} -t {1}{2},^@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 5))
	
	os.system("crunch {0} {0} -t {1}@{2},^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 6))
	
	os.system("crunch {0} {0} -t {1}@{2}^, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 7))
	
	os.system("crunch {0} {0} -t {1}^{2}@, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 8))
	
	os.system("crunch {0} {0} -t {1}^{2},@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 9))
	
	os.system("crunch {0} {0} -t {1},{2}@^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 10))
	
	os.system("crunch {0} {0} -t {1},{2}^@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 11))
	
	os.system("crunch {0} {0} -t {1}@,{2}^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 12))
	
	os.system("crunch {0} {0} -t {1}@^{2}, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 13))
	
	os.system("crunch {0} {0} -t {1}^@{2}, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 14))
	
	os.system("crunch {0} {0} -t {1}^,{2}@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 15))
	
	os.system("crunch {0} {0} -t {1},@{2}^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 16))
	
	os.system("crunch {0} {0} -t {1},^{2}@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 17))
	
	os.system("crunch {0} {0} -t @{1},{2}^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 18))
	
	os.system("crunch {0} {0} -t @{1}^{2}, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 19))
	
	os.system("crunch {0} {0} -t ^{1}@{2}, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 20))
	
	os.system("crunch {0} {0} -t ^{1},{2}@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 21))
	
	os.system("crunch {0} {0} -t ,{1}@{2}^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 22))
	
	os.system("crunch {0} {0} -t ,{1}^{2}@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 23))
	
	#combo 2 names
	os.system("crunch {0} {0} -t {1}{2}@,^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 24))
	
	os.system("crunch {0} {0} -t {1}{2}@^, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 25))
	
	os.system("crunch {0} {0} -t {1}{2}^@, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 26))
	
	os.system("crunch {0} {0} -t {1}{2}^,@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 27))
	
	os.system("crunch {0} {0} -t {1}{2},@^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 28))
	
	os.system("crunch {0} {0} -t {1}{2},^@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 29))
	
	os.system("crunch {0} {0} -t {1}@{2},^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 30))
	
	os.system("crunch {0} {0} -t {1}@{2}^, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 31))
	
	os.system("crunch {0} {0} -t {1}^{2}@, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 32))
	
	os.system("crunch {0} {0} -t {1}^{2},@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 33))
	
	os.system("crunch {0} {0} -t {1},{2}@^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 34))
	
	os.system("crunch {0} {0} -t {1},{2}^@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 35))
	
	os.system("crunch {0} {0} -t {1}@,{2}^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 36))
	
	os.system("crunch {0} {0} -t {1}@^{2}, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 37))
	
	os.system("crunch {0} {0} -t {1}^@{2}, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 38))
	
	os.system("crunch {0} {0} -t {1}^,{2}@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 39))
	
	os.system("crunch {0} {0} -t {1},@{2}^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 40))
	
	os.system("crunch {0} {0} -t {1},^{2}@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 41))
	
	os.system("crunch {0} {0} -t @{1},{2}^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 42))
	
	os.system("crunch {0} {0} -t @{1}^{2}, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 43))
	
	os.system("crunch {0} {0} -t ^{1}@{2}, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 44))
	
	os.system("crunch {0} {0} -t ^{1},{2}@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 45))
	
	os.system("crunch {0} {0} -t ,{1}@{2}^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 46))
	
	os.system("crunch {0} {0} -t ,{1}^{2}@ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 47))
	

def dvije_rijeci_prva_mix_upper_numeric_char(prva_rijec, druga_rijec, folder, rijecnik, txt_broj):
	

	os.system("crunch {0} {0} -t ^,%{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj))
	
	os.system("crunch {0} {0} -t ^%,{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 1))
	
	os.system("crunch {0} {0} -t %^,{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 2))
	
	os.system("crunch {0} {0} -t %,^{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 3))
	
	os.system("crunch {0} {0} -t ,^%{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 4))
	
	os.system("crunch {0} {0} -t ,%^{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 5))
	
	os.system("crunch {0} {0} -t ^{1},%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 6))
	
	os.system("crunch {0} {0} -t ^{1}%,{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 7))
	
	os.system("crunch {0} {0} -t %{1}^,{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 8))
	
	os.system("crunch {0} {0} -t %{1},^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 9))
	
	os.system("crunch {0} {0} -t ,{1}^%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 10))
	
	os.system("crunch {0} {0} -t ,{1}%^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 11))
	
	os.system("crunch {0} {0} -t ^,{1}%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 12))
	
	os.system("crunch {0} {0} -t ^%{1},{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 13))
	
	os.system("crunch {0} {0} -t %^{1},{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 14))
	
	os.system("crunch {0} {0} -t %,{1}^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 15))
	
	os.system("crunch {0} {0} -t ,^{1}%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 16))
	
	os.system("crunch {0} {0} -t ,%{1}^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 17))
	
	os.system("crunch {0} {0} -t {1}^,%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 18))
	
	os.system("crunch {0} {0} -t {1}^%,{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 19))
	
	os.system("crunch {0} {0} -t {1}%^,{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 20))
	
	os.system("crunch {0} {0} -t {1}%,^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 21))
	
	os.system("crunch {0} {0} -t {1},^%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 22))
	
	os.system("crunch {0} {0} -t {1},%^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 23))
	
	#combo 2 names
	os.system("crunch {0} {0} -t ^,%{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 24))
	
	os.system("crunch {0} {0} -t ^%,{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 25))
	
	os.system("crunch {0} {0} -t %^,{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 26))
	
	os.system("crunch {0} {0} -t %,^{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 27))
	
	os.system("crunch {0} {0} -t ,^%{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 28))
	
	os.system("crunch {0} {0} -t ,%^{1}{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 29))
	
	os.system("crunch {0} {0} -t ^{1},%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 30))
	
	os.system("crunch {0} {0} -t ^{1}%,{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 31))
	
	os.system("crunch {0} {0} -t %{1}^,{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 32))
	
	os.system("crunch {0} {0} -t %{1},^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 33))
	
	os.system("crunch {0} {0} -t ,{1}^%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 34))
	
	os.system("crunch {0} {0} -t ,{1}%^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 35))
	
	os.system("crunch {0} {0} -t ^,{1}%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 36))
	
	os.system("crunch {0} {0} -t ^%{1},{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 37))
	
	os.system("crunch {0} {0} -t %^{1},{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 38))
	
	os.system("crunch {0} {0} -t %,{1}^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 39))
	
	os.system("crunch {0} {0} -t ,^{1}%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 40))
	
	os.system("crunch {0} {0} -t ,%{1}^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 41))
	
	os.system("crunch {0} {0} -t {1}^,%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 42))
	
	os.system("crunch {0} {0} -t {1}^%,{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 43))
	
	os.system("crunch {0} {0} -t {1}%^,{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 44))
	
	os.system("crunch {0} {0} -t {1}%,^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 45))
	
	os.system("crunch {0} {0} -t {1},^%{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 46))
	
	os.system("crunch {0} {0} -t {1},%^{2} -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 47))
	

def dvije_rijeci_druga_mix_upper_numeric_char(prva_rijec, druga_rijec, folder, rijecnik, txt_broj):
	

	os.system("crunch {0} {0} -t {1}{2}^,% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj))
	
	os.system("crunch {0} {0} -t {1}{2}^%, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 1))
	
	os.system("crunch {0} {0} -t {1}{2}%^, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 2))
	
	os.system("crunch {0} {0} -t {1}{2}%,^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 3))
	
	os.system("crunch {0} {0} -t {1}{2},^% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 4))
	
	os.system("crunch {0} {0} -t {1}{2},%^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 5))
	
	os.system("crunch {0} {0} -t {1}^{2},% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 6))
	
	os.system("crunch {0} {0} -t {1}^{2}%, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 7))
	
	os.system("crunch {0} {0} -t {1}%{2}^, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 8))
	
	os.system("crunch {0} {0} -t {1}%{2},^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 9))
	
	os.system("crunch {0} {0} -t {1},{2}^% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 10))
	
	os.system("crunch {0} {0} -t {1},{2}%^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 11))
	
	os.system("crunch {0} {0} -t {1}^,{2}% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 12))
	
	os.system("crunch {0} {0} -t {1}^%{2}, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 13))
	
	os.system("crunch {0} {0} -t {1}%^{2}, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 14))
	
	os.system("crunch {0} {0} -t {1}%,{2}^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 15))
	
	os.system("crunch {0} {0} -t {1},^{2}% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 16))
	
	os.system("crunch {0} {0} -t {1},%{2}^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 17))
	
	os.system("crunch {0} {0} -t ^{1},{2}% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 18))
	
	os.system("crunch {0} {0} -t ^{1}%{2}, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 19))
	
	os.system("crunch {0} {0} -t %{1}^{2}, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 20))
	
	os.system("crunch {0} {0} -t %{1},{2}^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 21))
	
	os.system("crunch {0} {0} -t ,{1}^{2}% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 22))
	
	os.system("crunch {0} {0} -t ,{1}%{2}^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[0][prva_rijec], rijecnik[1][druga_rijec], folder_path, folder, txt_broj + 23))
	
	#combo 2 names
	os.system("crunch {0} {0} -t {1}{2}^,% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 24))
	
	os.system("crunch {0} {0} -t {1}{2}^%, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 25))
	
	os.system("crunch {0} {0} -t {1}{2}%^, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 26))
	
	os.system("crunch {0} {0} -t {1}{2}%,^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 27))
	
	os.system("crunch {0} {0} -t {1}{2},^% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 28))
	
	os.system("crunch {0} {0} -t {1}{2},%^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 29))
	
	os.system("crunch {0} {0} -t {1}^{2},% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 30))
	
	os.system("crunch {0} {0} -t {1}^{2}%, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 31))
	
	os.system("crunch {0} {0} -t {1}%{2}^, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 32))
	
	os.system("crunch {0} {0} -t {1}%{2},^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 33))
	
	os.system("crunch {0} {0} -t {1},{2}^% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 34))
	
	os.system("crunch {0} {0} -t {1},{2}%^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 35))
	
	os.system("crunch {0} {0} -t {1}^,{2}% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 36))
	
	os.system("crunch {0} {0} -t {1}^%{2}, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 37))
	
	os.system("crunch {0} {0} -t {1}%^{2}, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 38))
	
	os.system("crunch {0} {0} -t {1}%,{2}^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 39))
	
	os.system("crunch {0} {0} -t {1},^{2}% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 40))
	
	os.system("crunch {0} {0} -t {1},%{2}^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 41))
	
	os.system("crunch {0} {0} -t ^{1},{2}% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 42))
	
	os.system("crunch {0} {0} -t ^{1}%{2}, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 43))
	
	os.system("crunch {0} {0} -t %{1}^{2}, -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 44))
	
	os.system("crunch {0} {0} -t %{1},{2}^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 45))
	
	os.system("crunch {0} {0} -t ,{1}^{2}% -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 46))
	
	os.system("crunch {0} {0} -t ,{1}%{2}^ -o {3}{4}/{5}.txt".format(rijecnik[0]['rijec_duzina'] + rijecnik[1]['rijec_duzina'] + 3, rijecnik[1][prva_rijec], rijecnik[0][druga_rijec], folder_path, folder, txt_broj + 47))
	

os.system("crunch")
time.sleep(1)

#looping to make sure that the user enters min 1 and max 2 words

while(True):
	broj_ukupnih_rijeci = input("Do you want to create a dictionary based on 1 or 2 words? (type in 1 or 2):")

	if (1 <= int(broj_ukupnih_rijeci) < 3):
		break

	print("We're sorry. You have to type in 1 or 2. Try again, please.\n")

if (broj_ukupnih_rijeci == 1):
	rijec = raw_input("Insert your word:")
	rijec_duzina = len(rijec)

	#os.system("cd /")
	os.system("mkdir {0}{1}".format(folder_path, rijec)) 									#kreiranje foldera po nazivu

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
	prva_mix_upper_lower(rijec_prvo_slovo_upper, rijec, 105)
	prva_mix_upper_lower(rijec_zadnje_slovo_upper, rijec, 113)
	prva_mix_upper_lower(rijec_sva_slova_upper, rijec, 121)

	

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
	#sve spajamo u jedan finalni fajl i brisemo sve ostale fajlove
	os.chdir(rijec)
	os.system("mkdir temp && cat *.txt > temp/{0}_dictionary.txt".format(rijec))
	os.system("rm *.txt && mv temp/{0}_dictionary.txt {0}_dictionary.txt && rmdir temp".format(rijec))

elif (broj_ukupnih_rijeci == 2):
	sve_rijeci_dictionary = {}
	naziv_foldera = ""

	for x in range(broj_ukupnih_rijeci):
		rijec = raw_input("Insert {0}. word:".format(x + 1))
		rijec_duzina = len(rijec)

		sve_rijeci_dictionary[x] = {}
		sve_rijeci_dictionary[x]["rijec"] = rijec
		sve_rijeci_dictionary[x]["rijec_duzina"] = rijec_duzina
		sve_rijeci_dictionary[x]["rijec_prvo_slovo_upper"] = rijec[0].upper() + rijec[1:]
		sve_rijeci_dictionary[x]["rijec_zadnje_slovo_upper"] = rijec[:(rijec_duzina - 1)] + rijec[(rijec_duzina) - 1].upper()
		sve_rijeci_dictionary[x]["rijec_sva_slova_upper"] = rijec.upper()

		naziv_foldera += rijec

	os.system("mkdir {0}{1}".format(folder_path, naziv_foldera))

	while(True):
		memory_pitanje = input('Do you have at least 6GB of free memory space?(type 0 for "no" and 1 for "yes"): ')

		if (0 <= int(memory_pitanje) < 2):
			break

		print("We're sorry. You have to type in 1 or 2. Try again, please.\n")

	if (memory_pitanje == 1):

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

		

		dvije_rijeci_druga_numeric("rijec", "rijec", naziv_foldera, sve_rijeci_dictionary, 281)
		dvije_rijeci_druga_numeric("rijec_prvo_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 313)
		dvije_rijeci_druga_numeric("rijec_prvo_slovo_upper", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 345)
		dvije_rijeci_druga_numeric("rijec", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 377)

		

		dvije_rijeci_druga_numeric("rijec_zadnje_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 409)
		dvije_rijeci_druga_numeric("rijec_zadnje_slovo_upper", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 441)
		dvije_rijeci_druga_numeric("rijec", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 473)

		

		dvije_rijeci_druga_numeric("rijec_sva_slova_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 505)
		dvije_rijeci_druga_numeric("rijec_sva_slova_upper", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 537)
		dvije_rijeci_druga_numeric("rijec", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 569)

		

		dvije_rijeci_prva_lower_alpha("rijec", "rijec", naziv_foldera, sve_rijeci_dictionary, 601)
		dvije_rijeci_prva_lower_alpha("rijec_prvo_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 629)
		dvije_rijeci_prva_lower_alpha("rijec_prvo_slovo_upper", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 657)
		dvije_rijeci_prva_lower_alpha("rijec", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 685)

		

		dvije_rijeci_prva_lower_alpha("rijec_zadnje_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 713)
		dvije_rijeci_prva_lower_alpha("rijec_zadnje_slovo_upper", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 741)
		dvije_rijeci_prva_lower_alpha("rijec", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 769)

		

		dvije_rijeci_prva_lower_alpha("rijec_sva_slova_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 797)
		dvije_rijeci_prva_lower_alpha("rijec_sva_slova_upper", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 825)
		dvije_rijeci_prva_lower_alpha("rijec", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 853)

		

		dvije_rijeci_druga_lower_alpha("rijec", "rijec", naziv_foldera, sve_rijeci_dictionary, 881)
		dvije_rijeci_druga_lower_alpha("rijec_prvo_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 913)
		dvije_rijeci_druga_lower_alpha("rijec_prvo_slovo_upper", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 945)
		dvije_rijeci_druga_lower_alpha("rijec", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 977)

		

		dvije_rijeci_druga_lower_alpha("rijec_zadnje_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 1009)
		dvije_rijeci_druga_lower_alpha("rijec_zadnje_slovo_upper", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 1041)
		dvije_rijeci_druga_lower_alpha("rijec", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 1073)

		

		dvije_rijeci_druga_lower_alpha("rijec_sva_slova_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 1105)
		dvije_rijeci_druga_lower_alpha("rijec_sva_slova_upper", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 1137)
		dvije_rijeci_druga_lower_alpha("rijec", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 1169)

		

		dvije_rijeci_prva_upper_alpha("rijec", "rijec", naziv_foldera, sve_rijeci_dictionary, 1201)
		dvije_rijeci_prva_upper_alpha("rijec_prvo_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 1229)
		dvije_rijeci_prva_upper_alpha("rijec_prvo_slovo_upper", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 1257)
		dvije_rijeci_prva_upper_alpha("rijec", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 1285)

		

		dvije_rijeci_prva_upper_alpha("rijec_zadnje_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 1313)
		dvije_rijeci_prva_upper_alpha("rijec_zadnje_slovo_upper", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 1341)
		dvije_rijeci_prva_upper_alpha("rijec", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 1369)

		

		dvije_rijeci_prva_upper_alpha("rijec_sva_slova_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 1397)
		dvije_rijeci_prva_upper_alpha("rijec_sva_slova_upper", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 1425)
		dvije_rijeci_prva_upper_alpha("rijec", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 1453)

		

		dvije_rijeci_druga_upper_alpha("rijec", "rijec", naziv_foldera, sve_rijeci_dictionary, 1481)
		dvije_rijeci_druga_upper_alpha("rijec_prvo_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 1513)
		dvije_rijeci_druga_upper_alpha("rijec_prvo_slovo_upper", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 1545)
		dvije_rijeci_druga_upper_alpha("rijec", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 1577)

		

		dvije_rijeci_druga_upper_alpha("rijec_zadnje_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 1609)
		dvije_rijeci_druga_upper_alpha("rijec_zadnje_slovo_upper", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 1641)
		dvije_rijeci_druga_upper_alpha("rijec", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 1673)

		

		dvije_rijeci_druga_upper_alpha("rijec_sva_slova_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 1705)
		dvije_rijeci_druga_upper_alpha("rijec_sva_slova_upper", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 1737)
		dvije_rijeci_druga_upper_alpha("rijec", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 1769)

		

		dvije_rijeci_prva_mix_upper_lower("rijec", "rijec", naziv_foldera, sve_rijeci_dictionary, 1801)
		dvije_rijeci_prva_mix_upper_lower("rijec_prvo_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 1857)
		dvije_rijeci_prva_mix_upper_lower("rijec_prvo_slovo_upper", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 1913)
		dvije_rijeci_prva_mix_upper_lower("rijec", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 1969)

		

		dvije_rijeci_prva_mix_upper_lower("rijec_zadnje_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 2025)
		dvije_rijeci_prva_mix_upper_lower("rijec_zadnje_slovo_upper", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 2081)
		dvije_rijeci_prva_mix_upper_lower("rijec", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 2137)

		

		dvije_rijeci_prva_mix_upper_lower("rijec_sva_slova_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 2193)
		dvije_rijeci_prva_mix_upper_lower("rijec_sva_slova_upper", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 2249)
		dvije_rijeci_prva_mix_upper_lower("rijec", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 2305)

		

		dvije_rijeci_druga_mix_upper_lower("rijec", "rijec", naziv_foldera, sve_rijeci_dictionary, 2361)
		dvije_rijeci_druga_mix_upper_lower("rijec_prvo_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 2413)
		dvije_rijeci_druga_mix_upper_lower("rijec_prvo_slovo_upper", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 2465)
		dvije_rijeci_druga_mix_upper_lower("rijec", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 2517)

		

		dvije_rijeci_druga_mix_upper_lower("rijec_zadnje_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 2569)
		dvije_rijeci_druga_mix_upper_lower("rijec_zadnje_slovo_upper", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 2621)
		dvije_rijeci_druga_mix_upper_lower("rijec", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 2673)

		

		dvije_rijeci_druga_mix_upper_lower("rijec_sva_slova_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 2725)
		dvije_rijeci_druga_mix_upper_lower("rijec_sva_slova_upper", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 2777)
		dvije_rijeci_druga_mix_upper_lower("rijec", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 2829)

		
		
		dvije_rijeci_prva_mix_upper_numeric("rijec", "rijec", naziv_foldera, sve_rijeci_dictionary, 2881)
		dvije_rijeci_prva_mix_upper_numeric("rijec_prvo_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 2953)
		dvije_rijeci_prva_mix_upper_numeric("rijec_prvo_slovo_upper", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 3025)
		dvije_rijeci_prva_mix_upper_numeric("rijec", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 3097)

		

		dvije_rijeci_prva_mix_upper_numeric("rijec_zadnje_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 3169)
		dvije_rijeci_prva_mix_upper_numeric("rijec_zadnje_slovo_upper", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 3241)
		dvije_rijeci_prva_mix_upper_numeric("rijec", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 3313)

		

		dvije_rijeci_prva_mix_upper_numeric("rijec_sva_slova_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 3385)
		dvije_rijeci_prva_mix_upper_numeric("rijec_sva_slova_upper", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 3457)
		dvije_rijeci_prva_mix_upper_numeric("rijec", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 3529)

		

		#3640 files - 3.2GB

		dvije_rijeci_druga_mix_upper_numeric("rijec", "rijec", naziv_foldera, sve_rijeci_dictionary, 3601)
		dvije_rijeci_druga_mix_upper_numeric("rijec_prvo_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 3649)
		dvije_rijeci_druga_mix_upper_numeric("rijec_prvo_slovo_upper", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 3697)
		dvije_rijeci_druga_mix_upper_numeric("rijec", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 3745)

		

		dvije_rijeci_druga_mix_upper_numeric("rijec_zadnje_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 3793)
		dvije_rijeci_druga_mix_upper_numeric("rijec_zadnje_slovo_upper", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 3841)
		dvije_rijeci_druga_mix_upper_numeric("rijec", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 3889)

		

		dvije_rijeci_druga_mix_upper_numeric("rijec_sva_slova_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 3937)
		dvije_rijeci_druga_mix_upper_numeric("rijec_sva_slova_upper", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 3985)
		dvije_rijeci_druga_mix_upper_numeric("rijec", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 4033)
		
		dvije_rijeci_prva_mix_lower_numeric("rijec", "rijec", naziv_foldera, sve_rijeci_dictionary, 4081)
		dvije_rijeci_prva_mix_lower_numeric("rijec_prvo_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 4153)
		dvije_rijeci_prva_mix_lower_numeric("rijec_prvo_slovo_upper", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 4225)
		dvije_rijeci_prva_mix_lower_numeric("rijec", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 4297)

		

		dvije_rijeci_prva_mix_lower_numeric("rijec_zadnje_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 4369)
		dvije_rijeci_prva_mix_lower_numeric("rijec_zadnje_slovo_upper", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 4441)
		dvije_rijeci_prva_mix_lower_numeric("rijec", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 4513)

		

		dvije_rijeci_prva_mix_lower_numeric("rijec_sva_slova_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 4585)
		dvije_rijeci_prva_mix_lower_numeric("rijec_sva_slova_upper", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 4657)
		dvije_rijeci_prva_mix_lower_numeric("rijec", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 4729)

		dvije_rijeci_druga_mix_lower_numeric("rijec", "rijec", naziv_foldera, sve_rijeci_dictionary, 4801)
		dvije_rijeci_druga_mix_lower_numeric("rijec_prvo_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 4849)
		dvije_rijeci_druga_mix_lower_numeric("rijec_prvo_slovo_upper", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 4897)
		dvije_rijeci_druga_mix_lower_numeric("rijec", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 4945)

		

		dvije_rijeci_druga_mix_lower_numeric("rijec_zadnje_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 4993)
		dvije_rijeci_druga_mix_lower_numeric("rijec_zadnje_slovo_upper", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 5041)
		dvije_rijeci_druga_mix_lower_numeric("rijec", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 5089)

		

		dvije_rijeci_druga_mix_lower_numeric("rijec_sva_slova_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 5137)
		dvije_rijeci_druga_mix_lower_numeric("rijec_sva_slova_upper", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 5185)
		dvije_rijeci_druga_mix_lower_numeric("rijec", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 5233)

		

		dvije_rijeci_prva_mix_lower_upper_numeric("rijec", "rijec", naziv_foldera, sve_rijeci_dictionary, 5281)
		dvije_rijeci_prva_mix_lower_upper_numeric("rijec_prvo_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 5329)
		dvije_rijeci_prva_mix_lower_upper_numeric("rijec_prvo_slovo_upper", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 5377)
		dvije_rijeci_prva_mix_lower_upper_numeric("rijec", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 5425)

		

		dvije_rijeci_prva_mix_lower_upper_numeric("rijec_zadnje_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 5473)
		dvije_rijeci_prva_mix_lower_upper_numeric("rijec_zadnje_slovo_upper", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 5473)
		dvije_rijeci_prva_mix_lower_upper_numeric("rijec", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 5569)

		

		dvije_rijeci_prva_mix_lower_upper_numeric("rijec_sva_slova_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 5617)
		dvije_rijeci_prva_mix_lower_upper_numeric("rijec_sva_slova_upper", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 5665)
		dvije_rijeci_prva_mix_lower_upper_numeric("rijec", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 5713)

		

		dvije_rijeci_druga_mix_lower_upper_numeric("rijec", "rijec", naziv_foldera, sve_rijeci_dictionary, 5761)
		dvije_rijeci_druga_mix_lower_upper_numeric("rijec_prvo_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 5809)
		dvije_rijeci_druga_mix_lower_upper_numeric("rijec_prvo_slovo_upper", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 5857)
		dvije_rijeci_druga_mix_lower_upper_numeric("rijec", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 5905)

		

		dvije_rijeci_druga_mix_lower_upper_numeric("rijec_zadnje_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 5953)
		dvije_rijeci_druga_mix_lower_upper_numeric("rijec_zadnje_slovo_upper", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 6001)
		dvije_rijeci_druga_mix_lower_upper_numeric("rijec", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 6049)

		

		dvije_rijeci_druga_mix_lower_upper_numeric("rijec_sva_slova_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 6097)
		dvije_rijeci_druga_mix_lower_upper_numeric("rijec_sva_slova_upper", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 6145)
		dvije_rijeci_druga_mix_lower_upper_numeric("rijec", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 6193)

		

		dvije_rijeci_char("rijec", "rijec", naziv_foldera, sve_rijeci_dictionary, 6241)
		dvije_rijeci_char("rijec_prvo_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 6279)
		dvije_rijeci_char("rijec_prvo_slovo_upper", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 6317)
		dvije_rijeci_char("rijec", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 6355)

		

		dvije_rijeci_char("rijec_zadnje_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 6393)
		dvije_rijeci_char("rijec_zadnje_slovo_upper", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 6431)
		dvije_rijeci_char("rijec", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 6469)

		

		dvije_rijeci_char("rijec_sva_slova_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 6507)
		dvije_rijeci_char("rijec_sva_slova_upper", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 6545)
		dvije_rijeci_char("rijec", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 6583)

		

		dvije_rijeci_prva_mix_upper_char("rijec", "rijec", naziv_foldera, sve_rijeci_dictionary, 6621)
		dvije_rijeci_prva_mix_upper_char("rijec_prvo_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 6677)
		dvije_rijeci_prva_mix_upper_char("rijec_prvo_slovo_upper", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 6733)
		dvije_rijeci_prva_mix_upper_char("rijec", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 6789)

		

		dvije_rijeci_prva_mix_upper_char("rijec_zadnje_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 6845)
		dvije_rijeci_prva_mix_upper_char("rijec_zadnje_slovo_upper", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 6901)
		dvije_rijeci_prva_mix_upper_char("rijec", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 6957)

		

		dvije_rijeci_prva_mix_upper_char("rijec_sva_slova_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 7013)
		dvije_rijeci_prva_mix_upper_char("rijec_sva_slova_upper", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 7069)
		dvije_rijeci_prva_mix_upper_char("rijec", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 7125)

		

		dvije_rijeci_druga_mix_upper_char("rijec", "rijec", naziv_foldera, sve_rijeci_dictionary, 7181)
		dvije_rijeci_druga_mix_upper_char("rijec_prvo_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 7233)
		dvije_rijeci_druga_mix_upper_char("rijec_prvo_slovo_upper", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 7285)
		dvije_rijeci_druga_mix_upper_char("rijec", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 7337)

		

		dvije_rijeci_druga_mix_upper_char("rijec_zadnje_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 7389)
		dvije_rijeci_druga_mix_upper_char("rijec_zadnje_slovo_upper", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 7441)
		dvije_rijeci_druga_mix_upper_char("rijec", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 7493)

		

		dvije_rijeci_druga_mix_upper_char("rijec_sva_slova_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 7545)
		dvije_rijeci_druga_mix_upper_char("rijec_sva_slova_upper", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 7597)
		dvije_rijeci_druga_mix_upper_char("rijec", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 7649)

		

		dvije_rijeci_prva_mix_lower_char("rijec", "rijec", naziv_foldera, sve_rijeci_dictionary, 7701)
		dvije_rijeci_prva_mix_lower_char("rijec_prvo_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 7753)
		dvije_rijeci_prva_mix_lower_char("rijec_prvo_slovo_upper", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 7805)
		dvije_rijeci_prva_mix_lower_char("rijec", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 7857)

		

		dvije_rijeci_prva_mix_lower_char("rijec_zadnje_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 7909)
		dvije_rijeci_prva_mix_lower_char("rijec_zadnje_slovo_upper", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 7961)
		dvije_rijeci_prva_mix_lower_char("rijec", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 8013)

		

		dvije_rijeci_prva_mix_lower_char("rijec_sva_slova_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 8065)
		dvije_rijeci_prva_mix_lower_char("rijec_sva_slova_upper", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 8117)
		dvije_rijeci_prva_mix_lower_char("rijec", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 8169)

		

		dvije_rijeci_druga_mix_lower_char("rijec", "rijec", naziv_foldera, sve_rijeci_dictionary, 7701)
		dvije_rijeci_druga_mix_lower_char("rijec_prvo_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 7753)
		dvije_rijeci_druga_mix_lower_char("rijec_prvo_slovo_upper", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 7805)
		dvije_rijeci_druga_mix_lower_char("rijec", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 7857)

		

		dvije_rijeci_druga_mix_lower_char("rijec_zadnje_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 7909)
		dvije_rijeci_druga_mix_lower_char("rijec_zadnje_slovo_upper", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 7961)
		dvije_rijeci_druga_mix_lower_char("rijec", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 8013)

		

		dvije_rijeci_druga_mix_lower_char("rijec_sva_slova_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 8065)
		dvije_rijeci_druga_mix_lower_char("rijec_sva_slova_upper", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 8117)
		dvije_rijeci_druga_mix_lower_char("rijec", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 8169)

		

		dvije_rijeci_prva_mix_numeric_char("rijec", "rijec", naziv_foldera, sve_rijeci_dictionary, 8221)
		dvije_rijeci_prva_mix_numeric_char("rijec_prvo_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 8277)
		dvije_rijeci_prva_mix_numeric_char("rijec_prvo_slovo_upper", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 8333)
		dvije_rijeci_prva_mix_numeric_char("rijec", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 8389)

		

		dvije_rijeci_prva_mix_numeric_char("rijec_zadnje_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 8445)
		dvije_rijeci_prva_mix_numeric_char("rijec_zadnje_slovo_upper", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 8501)
		dvije_rijeci_prva_mix_numeric_char("rijec", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 8557)

		

		dvije_rijeci_prva_mix_numeric_char("rijec_sva_slova_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 8613)
		dvije_rijeci_prva_mix_numeric_char("rijec_sva_slova_upper", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 8669)
		dvije_rijeci_prva_mix_numeric_char("rijec", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 8725)

		

		dvije_rijeci_druga_mix_numeric_char("rijec", "rijec", naziv_foldera, sve_rijeci_dictionary, 8781)
		dvije_rijeci_druga_mix_numeric_char("rijec_prvo_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 8833)
		dvije_rijeci_druga_mix_numeric_char("rijec_prvo_slovo_upper", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 8885)
		dvije_rijeci_druga_mix_numeric_char("rijec", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 8937)

		

		dvije_rijeci_druga_mix_numeric_char("rijec_zadnje_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 8989)
		dvije_rijeci_druga_mix_numeric_char("rijec_zadnje_slovo_upper", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 9041)
		dvije_rijeci_druga_mix_numeric_char("rijec", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 9093)

		

		dvije_rijeci_druga_mix_numeric_char("rijec_sva_slova_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 9145)
		dvije_rijeci_druga_mix_numeric_char("rijec_sva_slova_upper", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 9197)
		dvije_rijeci_druga_mix_numeric_char("rijec", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 9249)

		

		dvije_rijeci_prva_mix_upper_lower_char("rijec", "rijec", naziv_foldera, sve_rijeci_dictionary, 9301)
		dvije_rijeci_prva_mix_upper_lower_char("rijec_prvo_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 9349)
		dvije_rijeci_prva_mix_upper_lower_char("rijec_prvo_slovo_upper", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 9397)
		dvije_rijeci_prva_mix_upper_lower_char("rijec", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 9445)

		

		dvije_rijeci_prva_mix_upper_lower_char("rijec_zadnje_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 9493)
		dvije_rijeci_prva_mix_upper_lower_char("rijec_zadnje_slovo_upper", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 9541)
		dvije_rijeci_prva_mix_upper_lower_char("rijec", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 9589)

		

		dvije_rijeci_prva_mix_upper_lower_char("rijec_sva_slova_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 9637)
		dvije_rijeci_prva_mix_upper_lower_char("rijec_sva_slova_upper", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 9685)
		dvije_rijeci_prva_mix_upper_lower_char("rijec", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 9733)

		

		dvije_rijeci_druga_mix_upper_lower_char("rijec", "rijec", naziv_foldera, sve_rijeci_dictionary, 9781)
		dvije_rijeci_druga_mix_upper_lower_char("rijec_prvo_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 9829)
		dvije_rijeci_druga_mix_upper_lower_char("rijec_prvo_slovo_upper", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 9877)
		dvije_rijeci_druga_mix_upper_lower_char("rijec", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 9925)

		

		dvije_rijeci_druga_mix_upper_lower_char("rijec_zadnje_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 9973)
		dvije_rijeci_druga_mix_upper_lower_char("rijec_zadnje_slovo_upper", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 10021)
		dvije_rijeci_druga_mix_upper_lower_char("rijec", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 10069)

		

		dvije_rijeci_druga_mix_upper_lower_char("rijec_sva_slova_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 10117)
		dvije_rijeci_druga_mix_upper_lower_char("rijec_sva_slova_upper", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 10165)
		dvije_rijeci_druga_mix_upper_lower_char("rijec", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 10213)

		

		dvije_rijeci_prva_mix_upper_numeric_char("rijec", "rijec", naziv_foldera, sve_rijeci_dictionary, 10261)
		dvije_rijeci_prva_mix_upper_numeric_char("rijec_prvo_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 10309)
		dvije_rijeci_prva_mix_upper_numeric_char("rijec_prvo_slovo_upper", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 10357)
		dvije_rijeci_prva_mix_upper_numeric_char("rijec", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 10405)

		

		dvije_rijeci_prva_mix_upper_numeric_char("rijec_zadnje_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 10453)
		dvije_rijeci_prva_mix_upper_numeric_char("rijec_zadnje_slovo_upper", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 10501)
		dvije_rijeci_prva_mix_upper_numeric_char("rijec", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 10549)

		

		dvije_rijeci_prva_mix_upper_numeric_char("rijec_sva_slova_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 10597)
		dvije_rijeci_prva_mix_upper_numeric_char("rijec_sva_slova_upper", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 10645)
		dvije_rijeci_prva_mix_upper_numeric_char("rijec", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 10693)

		

		dvije_rijeci_druga_mix_upper_numeric_char("rijec", "rijec", naziv_foldera, sve_rijeci_dictionary, 10741)
		dvije_rijeci_druga_mix_upper_numeric_char("rijec_prvo_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 10789)
		dvije_rijeci_druga_mix_upper_numeric_char("rijec_prvo_slovo_upper", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 10837)
		dvije_rijeci_druga_mix_upper_numeric_char("rijec", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 10885)

		

		dvije_rijeci_druga_mix_upper_numeric_char("rijec_zadnje_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 10933)
		dvije_rijeci_druga_mix_upper_numeric_char("rijec_zadnje_slovo_upper", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 10981)
		dvije_rijeci_druga_mix_upper_numeric_char("rijec", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 11029)

		

		dvije_rijeci_druga_mix_upper_numeric_char("rijec_sva_slova_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 11077)
		dvije_rijeci_druga_mix_upper_numeric_char("rijec_sva_slova_upper", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 11125)
		dvije_rijeci_druga_mix_upper_numeric_char("rijec", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 11173)

		#11220 files - 4.3GB
		#sve spajamo u jedan finalni fajl i brisemo sve ostale fajlove
		os.chdir(naziv_foldera)
		os.system("mkdir temp && cat *.txt > temp/{0}_dictionary.txt".format(naziv_foldera))
		os.system("rm *.txt && mv temp/{0}_dictionary.txt {0}_dictionary.txt && rmdir temp".format(naziv_foldera))

	else:
		# dvije_rijeci_prva_numeric("rijec", "rijec", naziv_foldera, sve_rijeci_dictionary, 1)
		# dvije_rijeci_prva_numeric("rijec_prvo_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 29)
		# dvije_rijeci_prva_numeric("rijec_prvo_slovo_upper", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 57)
		# dvije_rijeci_prva_numeric("rijec", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 85)

		

		# dvije_rijeci_prva_numeric("rijec_zadnje_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 113)
		# dvije_rijeci_prva_numeric("rijec_zadnje_slovo_upper", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 141)
		# dvije_rijeci_prva_numeric("rijec", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 169)

		

		# dvije_rijeci_prva_numeric("rijec_sva_slova_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 197)
		# dvije_rijeci_prva_numeric("rijec_sva_slova_upper", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 225)
		# dvije_rijeci_prva_numeric("rijec", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 253)

		

		# dvije_rijeci_druga_numeric("rijec", "rijec", naziv_foldera, sve_rijeci_dictionary, 281)
		# dvije_rijeci_druga_numeric("rijec_prvo_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 313)
		# dvije_rijeci_druga_numeric("rijec_prvo_slovo_upper", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 345)
		# dvije_rijeci_druga_numeric("rijec", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 377)

		

		# dvije_rijeci_druga_numeric("rijec_zadnje_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 409)
		# dvije_rijeci_druga_numeric("rijec_zadnje_slovo_upper", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 441)
		# dvije_rijeci_druga_numeric("rijec", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 473)

		

		# dvije_rijeci_druga_numeric("rijec_sva_slova_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 505)
		# dvije_rijeci_druga_numeric("rijec_sva_slova_upper", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 537)
		# dvije_rijeci_druga_numeric("rijec", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 569)

		

		# dvije_rijeci_prva_lower_alpha("rijec", "rijec", naziv_foldera, sve_rijeci_dictionary, 601)
		# dvije_rijeci_prva_lower_alpha("rijec_prvo_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 629)
		# dvije_rijeci_prva_lower_alpha("rijec_prvo_slovo_upper", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 657)
		# dvije_rijeci_prva_lower_alpha("rijec", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 685)

		

		# dvije_rijeci_prva_lower_alpha("rijec_zadnje_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 713)
		# dvije_rijeci_prva_lower_alpha("rijec_zadnje_slovo_upper", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 741)
		# dvije_rijeci_prva_lower_alpha("rijec", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 769)

		

		# dvije_rijeci_prva_lower_alpha("rijec_sva_slova_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 797)
		# dvije_rijeci_prva_lower_alpha("rijec_sva_slova_upper", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 825)
		# dvije_rijeci_prva_lower_alpha("rijec", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 853)

		

		# dvije_rijeci_druga_lower_alpha("rijec", "rijec", naziv_foldera, sve_rijeci_dictionary, 881)
		# dvije_rijeci_druga_lower_alpha("rijec_prvo_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 913)
		# dvije_rijeci_druga_lower_alpha("rijec_prvo_slovo_upper", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 945)
		# dvije_rijeci_druga_lower_alpha("rijec", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 977)

		

		# dvije_rijeci_druga_lower_alpha("rijec_zadnje_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 1009)
		# dvije_rijeci_druga_lower_alpha("rijec_zadnje_slovo_upper", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 1041)
		# dvije_rijeci_druga_lower_alpha("rijec", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 1073)

		

		dvije_rijeci_druga_lower_alpha("rijec_sva_slova_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 1105)
		dvije_rijeci_druga_lower_alpha("rijec_sva_slova_upper", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 1137)
		dvije_rijeci_druga_lower_alpha("rijec", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 1169)

		

		#sve spajamo u jedan finalni fajl i brisemo sve ostale fajlove
		os.chdir(naziv_foldera)
		os.system("mkdir temp && cat *.txt > temp/{0}_dictionary.txt".format(naziv_foldera))
		os.system("rm *.txt && mv temp/{0}_dictionary.txt {0}_dictionary.txt && rmdir temp".format(naziv_foldera))

		while (True):
			nastavak_pitanje = raw_input('Once you\'re finished with created dictionary, type in "y" and we will continue to create dictionaries.\n')

			if (nastavak_pitanje == "y"):
				break

		#deletes everything in current folder and empties the Trash
		os.system("rm *.txt && rm -rf ~/.local/share/Trash/*")
		os.chdir("..")
		nastavak_pitanje = ""

		dvije_rijeci_prva_upper_alpha("rijec", "rijec", naziv_foldera, sve_rijeci_dictionary, 1201)
		dvije_rijeci_prva_upper_alpha("rijec_prvo_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 1229)
		dvije_rijeci_prva_upper_alpha("rijec_prvo_slovo_upper", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 1257)
		dvije_rijeci_prva_upper_alpha("rijec", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 1285)

		

		dvije_rijeci_prva_upper_alpha("rijec_zadnje_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 1313)
		dvije_rijeci_prva_upper_alpha("rijec_zadnje_slovo_upper", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 1341)
		dvije_rijeci_prva_upper_alpha("rijec", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 1369)

		

		dvije_rijeci_prva_upper_alpha("rijec_sva_slova_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 1397)
		dvije_rijeci_prva_upper_alpha("rijec_sva_slova_upper", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 1425)
		dvije_rijeci_prva_upper_alpha("rijec", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 1453)

		

		dvije_rijeci_druga_upper_alpha("rijec", "rijec", naziv_foldera, sve_rijeci_dictionary, 1481)
		dvije_rijeci_druga_upper_alpha("rijec_prvo_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 1513)
		dvije_rijeci_druga_upper_alpha("rijec_prvo_slovo_upper", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 1545)
		dvije_rijeci_druga_upper_alpha("rijec", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 1577)

		

		dvije_rijeci_druga_upper_alpha("rijec_zadnje_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 1609)
		dvije_rijeci_druga_upper_alpha("rijec_zadnje_slovo_upper", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 1641)
		dvije_rijeci_druga_upper_alpha("rijec", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 1673)

		

		dvije_rijeci_druga_upper_alpha("rijec_sva_slova_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 1705)
		dvije_rijeci_druga_upper_alpha("rijec_sva_slova_upper", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 1737)
		dvije_rijeci_druga_upper_alpha("rijec", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 1769)

		

		dvije_rijeci_prva_mix_upper_lower("rijec", "rijec", naziv_foldera, sve_rijeci_dictionary, 1801)
		dvije_rijeci_prva_mix_upper_lower("rijec_prvo_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 1857)
		dvije_rijeci_prva_mix_upper_lower("rijec_prvo_slovo_upper", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 1913)
		dvije_rijeci_prva_mix_upper_lower("rijec", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 1969)

		

		dvije_rijeci_prva_mix_upper_lower("rijec_zadnje_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 2025)
		dvije_rijeci_prva_mix_upper_lower("rijec_zadnje_slovo_upper", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 2081)
		dvije_rijeci_prva_mix_upper_lower("rijec", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 2137)

		

		dvije_rijeci_prva_mix_upper_lower("rijec_sva_slova_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 2193)
		dvije_rijeci_prva_mix_upper_lower("rijec_sva_slova_upper", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 2249)
		dvije_rijeci_prva_mix_upper_lower("rijec", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 2305)

		

		dvije_rijeci_druga_mix_upper_lower("rijec", "rijec", naziv_foldera, sve_rijeci_dictionary, 2361)
		dvije_rijeci_druga_mix_upper_lower("rijec_prvo_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 2413)
		dvije_rijeci_druga_mix_upper_lower("rijec_prvo_slovo_upper", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 2465)
		dvije_rijeci_druga_mix_upper_lower("rijec", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 2517)

		

		#sve spajamo u jedan finalni fajl i brisemo sve ostale fajlove
		os.chdir(naziv_foldera)
		os.system("mkdir temp && cat *.txt > temp/{0}_dictionary.txt".format(naziv_foldera))
		os.system("rm *.txt && mv temp/{0}_dictionary.txt {0}_dictionary.txt && rmdir temp".format(naziv_foldera))

		while (True):
			nastavak_pitanje = raw_input('Once you\'re finished with created dictionary, type in "y" and we will continue to create dictionaries.\n')

			if (nastavak_pitanje == "y"):
				break

		#deletes everything in current folder and empties the Trash
		os.system("rm *.txt && rm -rf ~/.local/share/Trash/*")
		os.chdir("..")
		nastavak_pitanje = ""

		dvije_rijeci_druga_mix_upper_lower("rijec_zadnje_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 2569)
		dvije_rijeci_druga_mix_upper_lower("rijec_zadnje_slovo_upper", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 2621)
		dvije_rijeci_druga_mix_upper_lower("rijec", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 2673)

		

		dvije_rijeci_druga_mix_upper_lower("rijec_sva_slova_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 2725)
		dvije_rijeci_druga_mix_upper_lower("rijec_sva_slova_upper", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 2777)
		dvije_rijeci_druga_mix_upper_lower("rijec", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 2829)

		
		
		dvije_rijeci_prva_mix_upper_numeric("rijec", "rijec", naziv_foldera, sve_rijeci_dictionary, 2881)
		dvije_rijeci_prva_mix_upper_numeric("rijec_prvo_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 2953)
		dvije_rijeci_prva_mix_upper_numeric("rijec_prvo_slovo_upper", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 3025)
		dvije_rijeci_prva_mix_upper_numeric("rijec", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 3097)

		

		dvije_rijeci_prva_mix_upper_numeric("rijec_zadnje_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 3169)
		dvije_rijeci_prva_mix_upper_numeric("rijec_zadnje_slovo_upper", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 3241)
		dvije_rijeci_prva_mix_upper_numeric("rijec", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 3313)

		

		dvije_rijeci_prva_mix_upper_numeric("rijec_sva_slova_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 3385)
		dvije_rijeci_prva_mix_upper_numeric("rijec_sva_slova_upper", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 3457)
		dvije_rijeci_prva_mix_upper_numeric("rijec", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 3529)

		

		#3640 files - 3.2GB

		dvije_rijeci_druga_mix_upper_numeric("rijec", "rijec", naziv_foldera, sve_rijeci_dictionary, 3601)
		dvije_rijeci_druga_mix_upper_numeric("rijec_prvo_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 3649)
		dvije_rijeci_druga_mix_upper_numeric("rijec_prvo_slovo_upper", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 3697)
		dvije_rijeci_druga_mix_upper_numeric("rijec", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 3745)

		

		dvije_rijeci_druga_mix_upper_numeric("rijec_zadnje_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 3793)
		dvije_rijeci_druga_mix_upper_numeric("rijec_zadnje_slovo_upper", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 3841)
		dvije_rijeci_druga_mix_upper_numeric("rijec", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 3889)

		

		dvije_rijeci_druga_mix_upper_numeric("rijec_sva_slova_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 3937)
		dvije_rijeci_druga_mix_upper_numeric("rijec_sva_slova_upper", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 3985)
		dvije_rijeci_druga_mix_upper_numeric("rijec", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 4033)
		
		dvije_rijeci_prva_mix_lower_numeric("rijec", "rijec", naziv_foldera, sve_rijeci_dictionary, 4081)
		dvije_rijeci_prva_mix_lower_numeric("rijec_prvo_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 4153)
		dvije_rijeci_prva_mix_lower_numeric("rijec_prvo_slovo_upper", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 4225)
		dvije_rijeci_prva_mix_lower_numeric("rijec", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 4297)

		

		dvije_rijeci_prva_mix_lower_numeric("rijec_zadnje_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 4369)
		dvije_rijeci_prva_mix_lower_numeric("rijec_zadnje_slovo_upper", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 4441)
		dvije_rijeci_prva_mix_lower_numeric("rijec", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 4513)

		

		#sve spajamo u jedan finalni fajl i brisemo sve ostale fajlove
		os.chdir(naziv_foldera)
		os.system("mkdir temp && cat *.txt > temp/{0}_dictionary.txt".format(naziv_foldera))
		os.system("rm *.txt && mv temp/{0}_dictionary.txt {0}_dictionary.txt && rmdir temp".format(naziv_foldera))

		while (True):
			nastavak_pitanje = raw_input('Once you\'re finished with created dictionary, type in "y" and we will continue to create dictionaries.\n')

			if (nastavak_pitanje == "y"):
				break

		#deletes everything in current folder and empties the Trash
		os.system("rm *.txt && rm -rf ~/.local/share/Trash/*")
		os.chdir("..")
		nastavak_pitanje = ""

		dvije_rijeci_prva_mix_lower_numeric("rijec_sva_slova_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 4585)
		dvije_rijeci_prva_mix_lower_numeric("rijec_sva_slova_upper", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 4657)
		dvije_rijeci_prva_mix_lower_numeric("rijec", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 4729)

		dvije_rijeci_druga_mix_lower_numeric("rijec", "rijec", naziv_foldera, sve_rijeci_dictionary, 4801)
		dvije_rijeci_druga_mix_lower_numeric("rijec_prvo_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 4849)
		dvije_rijeci_druga_mix_lower_numeric("rijec_prvo_slovo_upper", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 4897)
		dvije_rijeci_druga_mix_lower_numeric("rijec", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 4945)

		

		dvije_rijeci_druga_mix_lower_numeric("rijec_zadnje_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 4993)
		dvije_rijeci_druga_mix_lower_numeric("rijec_zadnje_slovo_upper", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 5041)
		dvije_rijeci_druga_mix_lower_numeric("rijec", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 5089)

		

		dvije_rijeci_druga_mix_lower_numeric("rijec_sva_slova_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 5137)
		dvije_rijeci_druga_mix_lower_numeric("rijec_sva_slova_upper", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 5185)
		dvije_rijeci_druga_mix_lower_numeric("rijec", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 5233)

		

		dvije_rijeci_prva_mix_lower_upper_numeric("rijec", "rijec", naziv_foldera, sve_rijeci_dictionary, 5281)
		dvije_rijeci_prva_mix_lower_upper_numeric("rijec_prvo_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 5329)
		dvije_rijeci_prva_mix_lower_upper_numeric("rijec_prvo_slovo_upper", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 5377)
		dvije_rijeci_prva_mix_lower_upper_numeric("rijec", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 5425)

		

		dvije_rijeci_prva_mix_lower_upper_numeric("rijec_zadnje_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 5473)
		dvije_rijeci_prva_mix_lower_upper_numeric("rijec_zadnje_slovo_upper", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 5473)
		dvije_rijeci_prva_mix_lower_upper_numeric("rijec", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 5569)

		

		dvije_rijeci_prva_mix_lower_upper_numeric("rijec_sva_slova_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 5617)
		dvije_rijeci_prva_mix_lower_upper_numeric("rijec_sva_slova_upper", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 5665)
		dvije_rijeci_prva_mix_lower_upper_numeric("rijec", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 5713)

		

		dvije_rijeci_druga_mix_lower_upper_numeric("rijec", "rijec", naziv_foldera, sve_rijeci_dictionary, 5761)
		dvije_rijeci_druga_mix_lower_upper_numeric("rijec_prvo_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 5809)
		dvije_rijeci_druga_mix_lower_upper_numeric("rijec_prvo_slovo_upper", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 5857)
		dvije_rijeci_druga_mix_lower_upper_numeric("rijec", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 5905)

		

		dvije_rijeci_druga_mix_lower_upper_numeric("rijec_zadnje_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 5953)
		dvije_rijeci_druga_mix_lower_upper_numeric("rijec_zadnje_slovo_upper", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 6001)
		dvije_rijeci_druga_mix_lower_upper_numeric("rijec", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 6049)

		

		dvije_rijeci_druga_mix_lower_upper_numeric("rijec_sva_slova_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 6097)
		dvije_rijeci_druga_mix_lower_upper_numeric("rijec_sva_slova_upper", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 6145)
		dvije_rijeci_druga_mix_lower_upper_numeric("rijec", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 6193)

		#sve spajamo u jedan finalni fajl i brisemo sve ostale fajlove
		os.chdir(naziv_foldera)
		os.system("mkdir temp && cat *.txt > temp/{0}_dictionary.txt".format(naziv_foldera))
		os.system("rm *.txt && mv temp/{0}_dictionary.txt {0}_dictionary.txt && rmdir temp".format(naziv_foldera))

		while (True):
			nastavak_pitanje = raw_input('Once you\'re finished with created dictionary, type in "y" and we will continue to create dictionaries.\n')

			if (nastavak_pitanje == "y"):
				break

		#deletes everything in current folder and empties the Trash
		os.system("rm *.txt && rm -rf ~/.local/share/Trash/*")
		os.chdir("..")
		nastavak_pitanje = ""

		dvije_rijeci_char("rijec", "rijec", naziv_foldera, sve_rijeci_dictionary, 6241)
		dvije_rijeci_char("rijec_prvo_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 6279)
		dvije_rijeci_char("rijec_prvo_slovo_upper", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 6317)
		dvije_rijeci_char("rijec", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 6355)

		

		dvije_rijeci_char("rijec_zadnje_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 6393)
		dvije_rijeci_char("rijec_zadnje_slovo_upper", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 6431)
		dvije_rijeci_char("rijec", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 6469)

		

		dvije_rijeci_char("rijec_sva_slova_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 6507)
		dvije_rijeci_char("rijec_sva_slova_upper", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 6545)
		dvije_rijeci_char("rijec", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 6583)

		

		dvije_rijeci_prva_mix_upper_char("rijec", "rijec", naziv_foldera, sve_rijeci_dictionary, 6621)
		dvije_rijeci_prva_mix_upper_char("rijec_prvo_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 6677)
		dvije_rijeci_prva_mix_upper_char("rijec_prvo_slovo_upper", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 6733)
		dvije_rijeci_prva_mix_upper_char("rijec", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 6789)

		

		dvije_rijeci_prva_mix_upper_char("rijec_zadnje_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 6845)
		dvije_rijeci_prva_mix_upper_char("rijec_zadnje_slovo_upper", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 6901)
		dvije_rijeci_prva_mix_upper_char("rijec", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 6957)

		

		dvije_rijeci_prva_mix_upper_char("rijec_sva_slova_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 7013)
		dvije_rijeci_prva_mix_upper_char("rijec_sva_slova_upper", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 7069)
		dvije_rijeci_prva_mix_upper_char("rijec", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 7125)

		

		dvije_rijeci_druga_mix_upper_char("rijec", "rijec", naziv_foldera, sve_rijeci_dictionary, 7181)
		dvije_rijeci_druga_mix_upper_char("rijec_prvo_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 7233)
		dvije_rijeci_druga_mix_upper_char("rijec_prvo_slovo_upper", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 7285)
		dvije_rijeci_druga_mix_upper_char("rijec", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 7337)

		

		dvije_rijeci_druga_mix_upper_char("rijec_zadnje_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 7389)
		dvije_rijeci_druga_mix_upper_char("rijec_zadnje_slovo_upper", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 7441)
		dvije_rijeci_druga_mix_upper_char("rijec", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 7493)

		

		dvije_rijeci_druga_mix_upper_char("rijec_sva_slova_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 7545)
		dvije_rijeci_druga_mix_upper_char("rijec_sva_slova_upper", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 7597)
		dvije_rijeci_druga_mix_upper_char("rijec", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 7649)

		

		dvije_rijeci_prva_mix_lower_char("rijec", "rijec", naziv_foldera, sve_rijeci_dictionary, 7701)
		dvije_rijeci_prva_mix_lower_char("rijec_prvo_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 7753)
		dvije_rijeci_prva_mix_lower_char("rijec_prvo_slovo_upper", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 7805)
		dvije_rijeci_prva_mix_lower_char("rijec", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 7857)

		

		dvije_rijeci_prva_mix_lower_char("rijec_zadnje_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 7909)
		dvije_rijeci_prva_mix_lower_char("rijec_zadnje_slovo_upper", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 7961)
		dvije_rijeci_prva_mix_lower_char("rijec", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 8013)

		

		#sve spajamo u jedan finalni fajl i brisemo sve ostale fajlove
		os.chdir(naziv_foldera)
		os.system("mkdir temp && cat *.txt > temp/{0}_dictionary.txt".format(naziv_foldera))
		os.system("rm *.txt && mv temp/{0}_dictionary.txt {0}_dictionary.txt && rmdir temp".format(naziv_foldera))

		while (True):
			nastavak_pitanje = raw_input('Once you\'re finished with created dictionary, type in "y" and we will continue to create dictionaries.\n')

			if (nastavak_pitanje == "y"):
				break

		#deletes everything in current folder and empties the Trash
		os.system("rm *.txt && rm -rf ~/.local/share/Trash/*")
		os.chdir("..")
		nastavak_pitanje = ""

		dvije_rijeci_prva_mix_lower_char("rijec_sva_slova_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 8065)
		dvije_rijeci_prva_mix_lower_char("rijec_sva_slova_upper", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 8117)
		dvije_rijeci_prva_mix_lower_char("rijec", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 8169)

		

		dvije_rijeci_druga_mix_lower_char("rijec", "rijec", naziv_foldera, sve_rijeci_dictionary, 7701)
		dvije_rijeci_druga_mix_lower_char("rijec_prvo_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 7753)
		dvije_rijeci_druga_mix_lower_char("rijec_prvo_slovo_upper", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 7805)
		dvije_rijeci_druga_mix_lower_char("rijec", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 7857)

		

		dvije_rijeci_druga_mix_lower_char("rijec_zadnje_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 7909)
		dvije_rijeci_druga_mix_lower_char("rijec_zadnje_slovo_upper", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 7961)
		dvije_rijeci_druga_mix_lower_char("rijec", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 8013)

		

		dvije_rijeci_druga_mix_lower_char("rijec_sva_slova_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 8065)
		dvije_rijeci_druga_mix_lower_char("rijec_sva_slova_upper", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 8117)
		dvije_rijeci_druga_mix_lower_char("rijec", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 8169)

		

		dvije_rijeci_prva_mix_numeric_char("rijec", "rijec", naziv_foldera, sve_rijeci_dictionary, 8221)
		dvije_rijeci_prva_mix_numeric_char("rijec_prvo_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 8277)
		dvije_rijeci_prva_mix_numeric_char("rijec_prvo_slovo_upper", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 8333)
		dvije_rijeci_prva_mix_numeric_char("rijec", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 8389)

		

		dvije_rijeci_prva_mix_numeric_char("rijec_zadnje_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 8445)
		dvije_rijeci_prva_mix_numeric_char("rijec_zadnje_slovo_upper", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 8501)
		dvije_rijeci_prva_mix_numeric_char("rijec", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 8557)

		

		dvije_rijeci_prva_mix_numeric_char("rijec_sva_slova_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 8613)
		dvije_rijeci_prva_mix_numeric_char("rijec_sva_slova_upper", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 8669)
		dvije_rijeci_prva_mix_numeric_char("rijec", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 8725)

		

		dvije_rijeci_druga_mix_numeric_char("rijec", "rijec", naziv_foldera, sve_rijeci_dictionary, 8781)
		dvije_rijeci_druga_mix_numeric_char("rijec_prvo_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 8833)
		dvije_rijeci_druga_mix_numeric_char("rijec_prvo_slovo_upper", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 8885)
		dvije_rijeci_druga_mix_numeric_char("rijec", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 8937)

		

		dvije_rijeci_druga_mix_numeric_char("rijec_zadnje_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 8989)
		dvije_rijeci_druga_mix_numeric_char("rijec_zadnje_slovo_upper", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 9041)
		dvije_rijeci_druga_mix_numeric_char("rijec", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 9093)

		

		dvije_rijeci_druga_mix_numeric_char("rijec_sva_slova_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 9145)
		dvije_rijeci_druga_mix_numeric_char("rijec_sva_slova_upper", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 9197)
		dvije_rijeci_druga_mix_numeric_char("rijec", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 9249)

		

		dvije_rijeci_prva_mix_upper_lower_char("rijec", "rijec", naziv_foldera, sve_rijeci_dictionary, 9301)
		dvije_rijeci_prva_mix_upper_lower_char("rijec_prvo_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 9349)
		dvije_rijeci_prva_mix_upper_lower_char("rijec_prvo_slovo_upper", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 9397)
		dvije_rijeci_prva_mix_upper_lower_char("rijec", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 9445)

		

		dvije_rijeci_prva_mix_upper_lower_char("rijec_zadnje_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 9493)
		dvije_rijeci_prva_mix_upper_lower_char("rijec_zadnje_slovo_upper", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 9541)
		dvije_rijeci_prva_mix_upper_lower_char("rijec", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 9589)

		

		dvije_rijeci_prva_mix_upper_lower_char("rijec_sva_slova_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 9637)
		dvije_rijeci_prva_mix_upper_lower_char("rijec_sva_slova_upper", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 9685)
		dvije_rijeci_prva_mix_upper_lower_char("rijec", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 9733)

		

		dvije_rijeci_druga_mix_upper_lower_char("rijec", "rijec", naziv_foldera, sve_rijeci_dictionary, 9781)
		dvije_rijeci_druga_mix_upper_lower_char("rijec_prvo_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 9829)
		dvije_rijeci_druga_mix_upper_lower_char("rijec_prvo_slovo_upper", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 9877)
		dvije_rijeci_druga_mix_upper_lower_char("rijec", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 9925)

		

		dvije_rijeci_druga_mix_upper_lower_char("rijec_zadnje_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 9973)
		dvije_rijeci_druga_mix_upper_lower_char("rijec_zadnje_slovo_upper", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 10021)
		dvije_rijeci_druga_mix_upper_lower_char("rijec", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 10069)

		

		dvije_rijeci_druga_mix_upper_lower_char("rijec_sva_slova_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 10117)
		dvije_rijeci_druga_mix_upper_lower_char("rijec_sva_slova_upper", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 10165)
		dvije_rijeci_druga_mix_upper_lower_char("rijec", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 10213)

		

		dvije_rijeci_prva_mix_upper_numeric_char("rijec", "rijec", naziv_foldera, sve_rijeci_dictionary, 10261)
		dvije_rijeci_prva_mix_upper_numeric_char("rijec_prvo_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 10309)
		dvije_rijeci_prva_mix_upper_numeric_char("rijec_prvo_slovo_upper", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 10357)
		dvije_rijeci_prva_mix_upper_numeric_char("rijec", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 10405)

		

		dvije_rijeci_prva_mix_upper_numeric_char("rijec_zadnje_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 10453)
		dvije_rijeci_prva_mix_upper_numeric_char("rijec_zadnje_slovo_upper", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 10501)
		dvije_rijeci_prva_mix_upper_numeric_char("rijec", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 10549)

		

		dvije_rijeci_prva_mix_upper_numeric_char("rijec_sva_slova_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 10597)
		dvije_rijeci_prva_mix_upper_numeric_char("rijec_sva_slova_upper", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 10645)
		dvije_rijeci_prva_mix_upper_numeric_char("rijec", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 10693)

		

		dvije_rijeci_druga_mix_upper_numeric_char("rijec", "rijec", naziv_foldera, sve_rijeci_dictionary, 10741)
		dvije_rijeci_druga_mix_upper_numeric_char("rijec_prvo_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 10789)
		dvije_rijeci_druga_mix_upper_numeric_char("rijec_prvo_slovo_upper", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 10837)
		dvije_rijeci_druga_mix_upper_numeric_char("rijec", "rijec_prvo_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 10885)

		

		dvije_rijeci_druga_mix_upper_numeric_char("rijec_zadnje_slovo_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 10933)
		dvije_rijeci_druga_mix_upper_numeric_char("rijec_zadnje_slovo_upper", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 10981)
		dvije_rijeci_druga_mix_upper_numeric_char("rijec", "rijec_zadnje_slovo_upper", naziv_foldera, sve_rijeci_dictionary, 11029)

		

		dvije_rijeci_druga_mix_upper_numeric_char("rijec_sva_slova_upper", "rijec", naziv_foldera, sve_rijeci_dictionary, 11077)
		dvije_rijeci_druga_mix_upper_numeric_char("rijec_sva_slova_upper", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 11125)
		dvije_rijeci_druga_mix_upper_numeric_char("rijec", "rijec_sva_slova_upper", naziv_foldera, sve_rijeci_dictionary, 11173)

		#sve spajamo u jedan finalni fajl i brisemo sve ostale fajlove
		os.chdir(naziv_foldera)
		os.system("mkdir temp && cat *.txt > temp/{0}_dictionary.txt".format(naziv_foldera))
		os.system("rm *.txt && mv temp/{0}_dictionary.txt {0}_dictionary.txt && rmdir temp".format(naziv_foldera))
else:
	pass
