import requests
import bs4
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time

symbol = input('enter ticker as listed in BSE: ')
target = float(input('target price: '))

while True:

  url = "https://in.finance.yahoo.com/quote/"+symbol+".BO?p="+symbol+".BO&.tsrc=fin-srch"

  res = requests.get(url,headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"})
  soup = bs4.BeautifulSoup(res.text,'html.parser')
  test = soup.find("div",{"class":"My(6px) Pos(r) smartphone_Mt(6px)"}).find("span")
  price = test.text
  value = ''
  for i in range(len(price)):
    if price[i]!= ',':
      value = value+price[i]
    else:
      pass
  print(value)
  if float(value) >= target:
    print('Target hit')
    # send email
    sender_email = "" # sender email_id
    password = '' # sender app password generated in email security settings
    receiver_email = "" # reciever email_id

    message = MIMEMultipart("alternative")
    message["Subject"] = "Stock target hit"
    message["From"] = sender_email
    message["To"] = receiver_email

    text = """\
    Hello there,
    obi wan says your stonks has hit target"""

    part1 = MIMEText(text, "plain")

    message.attach(part1)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )
    break
  else:
    print('not hit')
    time.sleep(900)
