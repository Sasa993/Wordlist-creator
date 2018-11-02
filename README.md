# Wordlist-Creator
A `Python` script which takes an input, and based on it, opens Crunch and makes a huge wordlist. 
Wordlist can be used for aircrack, bruteforcing, etc.<br><br>

_Wordlist-Creator is not usable on any other OS other then `Linux`. Before using this script, you need to install <strong>Crunch</strong> (some Linux Distributions already have Crunch installed, for instance `Kali Linux`)._<br><br>
<strong>To install or upgrade Crunch on an Ubuntu or Debian system:</strong></br>
`$ sudo apt-get install crunch`<br>
<strong>To install or upgrade Crunch on a Red Hat system:</strong><br>
`$ sudo yum install crunch`<br>
  <strong>To install or upgrade Crunch on an Ubuntu or Debian system:</strong><br>
`$ sudo apt-get install crunch`

After executing this script, you will be asked to chose if you want to have your dictionary based on 1 or 2 words. 
If you chose 1, 700 files (aproximatly) will be created, with size of 200MB. At the end of the execution, all of those files (with different possible combinations of inserted word) will be placed into one file, which will be available for further use.
If you choose to insert 2 words, 12 000 files (aproximatly) will be created, with size of 4.5GB.
