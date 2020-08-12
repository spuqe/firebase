# firebase
Firebase database finder + wordlist generator

# What the is this? 
basicly just Firebase database finder.

# How does it work? 
Firebase does that when u first time create a database it will ask with small and long text that "This is a test database click settings to change that or click X to..." And ofc no one fucking reads that little print of shit and just clicks X and the text never comes back and fun thing is that all test databases are public to the internet long as you have the URL. Don't ask me why. Also sorry for bad english! I hope you understand what i meant.

# How to use? Firebase.py
Define wich worldlist you want to use (you can define it at the source or line 17)
Just run the script after adding words to wordlist.txt
Add the words like this
1
2
3
4
or it will not work!

# How to use WSL?
WSL is a word list generator

usage: scraper.py -h] [-chr CHARS] [-min MIN_LENGTH] [-max MAX_LENGTH]
               [-out OUTPUT]
wgen.py -h, --help            show this help message with all commands.

for example python3 scraper.py -chr=abc -min=1 -max=4 -out=output/wordlist.txt

