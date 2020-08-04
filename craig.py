import urllib.request
import time
import smtplib

def get_list (url):
	r = urllib.request.urlopen(url)
	a = str(r.read())
	a = (a.split('ul class=\"rows\"')[1]).split('\/div')[0].split(' class=\"result-row\" data-pid=\"')
	idUrlMap = {}
	for i in range(1,len(a)):
		idUrlMap[a[i].split('\"')[0]] = a[i].split('a href=\"')[1].split('\"')[0]
	return idUrlMap

def sendMess(mess):
	from twilio.rest import Client
	# Your Account SID from twilio.com/console
	account_sid = "************************************"
	# Your Auth Token from twilio.com/console
	auth_token  = "************************************"
	client = Client(account_sid, auth_token)
	message = client.messages.create(
		to="*****************************************", 
		from_="**************************************",
		body=mess)
	print(message.sid)

def sendEmail(message="test message"):
	gmail_user = '*********************************'
	gmail_password = '**********************************'

	sent_from = gmail_user
	to = ['***************************************']
	subject = 'craigslist new postings'

	email_text = """\
	From: %s
	To: %s
	Subject: %s

	%s
	""" % (sent_from, ", ".join(to), subject, message)

	try:
		server = smtplib.SMTP_SSL('cpanel.freehosting.com', 465)
		server.ehlo()
		server.login(gmail_user, gmail_password)
		server.sendmail(sent_from, to, email_text)
		server.close()
	except Exception as e:
		print('Exception occured ')
		print(e)


url = 'https://vancouver.craigslist.org/search/sss?query=table+lamp&sort=date&hasPic=1&postedToday=1&search_distance=40&postal=v5r4k1&min_price=20&max_price=150'
processedIdUrlMap = get_list(url)
while (True): #timeout
	time.sleep(300)
	print("hitting the URL")
	currentIdUrlMap = get_list(url)
	message = ""
	for ids in currentIdUrlMap.keys():
		if (processedIdUrlMap):
			if not (ids in processedIdUrlMap):
				message = message + currentIdUrlMap[ids] + ' \n '
				processedIdUrlMap[ids] = currentIdUrlMap[ids]
		else:
			message = message + currentIdUrlMap[ids] + ' \n '
	if (message >""):
		print(message)
		sendMess(message)
