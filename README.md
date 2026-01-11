🎅 67 on a Merry RizzMas (Secret Santa Script)

This Python script automates the Secret Santa gift exchange process. It shuffles participants, creates a circular gift-giving chain, and sends personalized emails using a customizable SMTP configuration.

✨ Features

Universal SMTP Support: Works with Gmail, Outlook, Yahoo, or any custom SMTP server via .env configuration.

Circular Algorithm: Guarantees that everyone gives and receives exactly one gift—no one ever draws themselves.

Brainrot Messaging: Features a pre-built email template with top-tier Gen Alpha slang (W rizz, Skibidi, No Cap) to keep the holidays "Sigma."

Secure & Private: Keeps your credentials and your friends' emails out of your source code.

🛠️ Setup & Installation

1. Clone the Repository
git clone https://github.com/your-username/rizzmas-secret-santa.git
cd secretsanta

2. Install Dependencies
pip install -r requirements.txt

3. Configure Participants (players.json)
Modify the players.json file. Add your friends' names and email addresses:

{
    "Aleksa": "aleksa@example.com",
    "John": "john@example.com",
    "Sarah": "sarah@example.com"
}

4. Setup Your Environment (.env)
Create a .env file in the root directory. Use the table below to find your provider's settings:

EMAIL=your-email@example.com
PASSWORD=your-app-specific-password
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587

Provider | SMTP Server | Port
Gmail | smtp.gmail.com | 587
Outlook / Hotmail | smtp.office365.com | 587
Yahoo | smtp.mail.yahoo.com | 587
⚠️ Note: You must use an App Password, not your regular login password. This is found under your email provider's security settings (2-Step Verification).

🚀 Usage

Run the script to start the exchange:

python3 main.py

The script will:

Load your participants.

Shuffle the names and assign pairs.

Log into your SMTP server and send the "RizzMas" emails one by one.

📜 License
This project is open-source and available under the MIT License.
