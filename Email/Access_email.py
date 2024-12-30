import smtplib
import time
import imaplib
import email
import traceback 


FROM_EMAIL = "your email"
FROM_PWD = "your_passowrd" 

# this is for gmail,So change based on service provider name
# In setting turn on "Less secure apps" to enable mail authorization  # navigation. Settings > Accounts & imports > Other google setting > (scroll) less secure apps
SMTP_SERVER = "imap.gmail.com" 



mail = imaplib.IMAP4_SSL(SMTP_SERVER)
mail.login(FROM_EMAIL,FROM_PWD)
mail.select('inbox')

data = mail.search(None, 'ALL')
mail_ids = data[1]
id_list = mail_ids[0].split()   
first_email_id = int(id_list[0])
latest_email_id = int(id_list[-1])
otp=[]
for i in range(latest_email_id,first_email_id, -1):
    data = mail.fetch(str(i), '(RFC822)' )
####print all the inbox mails
    print(str(data),"\n++++++++++++========\n")
#   get all the text in the field sign in:
    a1=re.findall('sign in: \d+', str(data))

    if len(a1)!=0:
        for i in a1:
            otp.append(str(i).replace("sign in: ",""))
# print(opt)
