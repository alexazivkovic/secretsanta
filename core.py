import random
import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv
import json

with open("players.json", "r") as f:
    players = json.load(f)

names = list(players.keys())
random.shuffle(names)

pairs = []
for i in range(len(names)):
    giver = names[i]
    receiver = names[(i+1) % len(names)]
    pairs.append((giver, players[giver], receiver))

load_dotenv()
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

def send_email(receiver_email, receiver_name, target_name):
    msg = EmailMessage()
    msg.set_content(f"Zdravo {receiver_name},\n\nTi si bukvalno W rizzler ove godine!\nTvoj tajni zadatak je da ne budeš L sigmа i kupiš poklon za: {target_name}.\nNemoj da te fanum tax-uju za pare, nego budi mogger i pokidaj sa poklonom.\n\nStay mewing!\nIt's giving skibidi praznici, no cap!")
    msg['Subject'] = '67 on a Merry RizzMas'
    msg['From'] = EMAIL
    msg['To'] = receiver_email

    try:
        with smtplib.SMTP('smtp.office365.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login(EMAIL, PASSWORD)
            smtp.send_message(msg)

    except Exception as e:
        print(f"Greška: {e}")

for giver, email, receiver in pairs:
    print(f"Šaljem mejl za {giver}...")
    send_email(email, giver, receiver)

print("Gotovo!")