import smtplib, ssl, getpass, datetime, json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#email bot for daily nasa img, feel free to steal my api key i guess (plz dont they're free)
import urllib.request
with urllib.request.urlopen('https://api.nasa.gov/planetary/apod?api_key=yTNgoyU0gjQPmRWLo82UINDQWgofCfKjrrxkivTN') as response:
   htmlRes = response.read()
pyDic = json.loads(htmlRes)
nasaUrl = pyDic['hdurl']
nasaTitle = pyDic['title']
nasaExp = pyDic['explanation']

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "willyrowe2@gmail.com"  
receiver_email = "williamjrowe@wustl.edu"  
password = getpass.getpass("Type your password and press enter: ")
message = MIMEMultipart("alternative")
messageSubject = datetime.datetime.today().strftime ('%m/%d/%Y') 
message["Subject"] = messageSubject
message["From"] = sender_email
message["To"] = receiver_email

text = """\
Uh oh html broke, this is a plaintext message"""
html = """\
<html>
  <body>
    <h1>Nasa Daily Image</h1>
    <h2>{}</h2>
       <img src="{}" alt="Daily Nasa">
       <br>
       <p>{}</p> 
  </body>
</html>
""".format(nasaTitle,nasaUrl,nasaExp)

part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

message.attach(part1)
message.attach(part2)

# Create a secure SSL context
context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())

print("Email sent successfully!")