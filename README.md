# craigslist-crawler
A crawler for craigslist to check for new posts and send messages using twilio using Python3

Setup - 
1. download /clone the repo.
2. run the command pip install twilio or pip3 install twilio from the repo folder. 
3. If SMS is needed create a twilio account - you will be able to get free trial messages depending on the country.
4. update the details into config file 
    search_string  -- is the item / search string to use on craigslist
    pin_code       -- pincode 
    search_distance = '40' -- in km / miles depending on region
    min_price = '0' -- minimum price for filter 
    maxprice = '50' -- max price for filter 
    craigslist_url = 'https://vancouver.craigslist.org/search/sss' --this depends on region
    period_check_in_mins = 5 -- how frequent to check for updates and send notification 
    
    email_mode = True --- values True /False . when true it tries to send email . 
    smtp_user = '<user@domain.com>' --- SMTP server username
    smtp_password = '<password>' --- SMTP server login password
    recipient_email = '<user@gmail.com' --- recipient of email - please dont misuse this and use your personal email only
    email_subject = 'Craigslist New Postings Found' --- subject of email 
    smtp_url = '<smtp server url>'  --- SMTP server URL
    smtp_port = 465                 --- SMTP server port

    twilio_mode = False   --- values True/False . when true it tries to send SMS using twilio  
    twilio_account_sid = '<account sid from Twilio account>'
    twilio_auth_token  = '<auth token from Twilio account>'
    from_phone_number='<From phone number eg. +19876543210 where +1 is country code and phone is 987-654-3210>'
    to_phone_number='<recipient phone number eg. +19876543210 where +1 is country code and phone is 987-654-3210>'please dont misuse this and use your personal number only
    
5. After updating the config - run python craig.py / python3 craig.py
