Simple script made to find Firebase databases that are open.
# First of all!
Google has tried to patch this. Sadly it just made the finder weaker. You can still find databases easily using this but you wont get so much results as before the patch!


# firebase
Firebase database finder + wordlist generator
Demo: https://youtu.be/YsaPEnOPe7k
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

When the database is founded you can see the name at /database/ and type the database name to your url bar like this: https://databasename.firebaseio.com/.json

# How to use WSL?
WSL is a word list generator

usage: scraper.py -h] [-chr CHARS] [-min MIN_LENGTH] [-max MAX_LENGTH]
               [-out OUTPUT]
wgen.py -h, --help            show this help message with all commands.

for example python3 scraper.py -chr=abc -min=1 -max=4 -out=output/wordlist.txt






Last updated: 12.8.2020
