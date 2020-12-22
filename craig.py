import requests
import time
import smtplib
import config

def get_list (url):
	url = "https://vancouver.craigslist.org/search/sss"
	querystring = {"query":config.search_string,
		"sort":"date",
		"hasPic":"1",
		"postedToday":"1",
		"search_distance":config.search_distance,
		"postal":config.pin_code,
		"min_price":config.min_price,
		"max_price":config.maxprice
	}
	headers = {
		'cache-control': "no-cache"
	}
	response = requests.request("GET", url, headers=headers, params=querystring).text
	a = (response.split('ul class=\"rows\"')[1]).split('\/div')[0].split(' class=\"result-row\" data-pid=\"')
	idUrlMap = {}
	for i in range(1,len(a)):
		idUrlMap[a[i].split('\"')[0]] = a[i].split('a href=\"')[1].split('\"')[0]
	return idUrlMap

def sendMess(mess):
	from twilio.rest import Client
	client = Client(config.twilio_account_sid, config.twilio_auth_token)
	message = client.messages.create(
		to=config.to_phone_number, 
		from_=config.from_phone_number,
		body=mess)
	print(message.sid)

def sendEmail(message="test message"):

	from email.mime.application import MIMEApplication
	from email.mime.text import MIMEText
	from email.mime.multipart import MIMEMultipart
	from email.header import Header
	from email.utils import formataddr

	smtp_user = config.smtp_user
	smtp_password = config.smtp_password
	recipient = config.recipient_email
	subject = config.email_subject

	msg = MIMEMultipart('alternative')
	msg['Subject'] = subject
	msg['From'] = formataddr((str(Header('Craigslist User', 'utf-8')), 'admin@raghavlane.com'))
	msg['To'] = recipient
	try:
		server = smtplib.SMTP_SSL(config.smtp_url, config.smtp_port)
		server.ehlo()
		server.login(smtp_user, smtp_password)
		server.sendmail(smtp_user, recipient, message)
		server.close()
	except Exception as e:
		print('Exception occured ')
		print(e)

url = config.craigslist_url
processedIdUrlMap = get_list(url)
while (True):
	time.sleep(config.period_check_in_mins *60 )
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
		if (config.email_mode):
			sendEmail(message)
		if (config.twilio_mode):
			sendMess(message)