import requests
print('Have fun')

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

