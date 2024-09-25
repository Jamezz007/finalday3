import yagmail
import os
from dotenv import load dotenv

load_dotenv()
sender "rahee9156@gmail.com"
receiver = "vqfoaxxvh@eml.hub.com"
subject Test mail using python
contents = '''
This is the content side for sending mail
'''

yag = yagmail.SMTP(user=sender, password=os.getenv('password'))
yag.send(to=receiver, subject=subject, contents=contents)
print("Email send!")