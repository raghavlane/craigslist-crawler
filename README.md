# craigslist-crawler
A crawler for craigslist to check for new posts and send messages using twilio using Python3

Setup - 
1. download /clone the repo.
2. run the command pip install twilio or pip3 install twilio from the repo folder. 
3. create a twilio account - you will be able to get free trial messages depending on the country.
4. replace the ********************* from craig.py with the respective details from twilio account . 
5. change timeout(300) to a different value if necessary, this currently runs every 300 seconds to check for updates. 
6. replace the URL with the url you would like to crawl for(open craigslist and search for your product and then apply filters, then copy the url from browser) - please make sure proper filters are used in this. 
