# Discord Meme Bot

A simple and fun Discord bot that fetches and shares memes from the internet. The bot utilizes the [Meme API](https://github.com/D3vd/Meme_Api) to retrieve memes and send them to a Discord channel when prompted by the `!meme` command.

## Features
- Fetch memes from the internet using the Meme API.
- Send memes in Discord when the `!meme` command is triggered.
- Easy to set up and deploy on platforms like Render, Heroku, or locally.
- Customizable for future command additions.

## Getting Started

Follow the steps below to set up and run the bot on your local machine or deploy it on a platform like Render.

### Prerequisites

Make sure you have the following:
1. A [Discord account](https://discord.com/).
2. A [Discord bot token](https://discord.com/developers/applications) to interact with the Discord API.
3. Python 3.x installed.
4. Git installed for version control.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/dkiki45/discord-meme-bot.git
   cd discord-meme-bot

### Setting up the Project 
Setting up a Virtual Environment

1. Create a Virtual Environment:
   ```bash
   python3 -m venv venv
2. Activate the Virtual Environment:

  (On macOS/Linux:)
   ```bash
   source venv/bin/activate
   ```
  (On Windows:)
   ```bash
   venv\Scripts\activate
```
3. Install the Required Dependencies:
   ```bash
   pip install -r requirements.txt

### Set Up Your Discord Bot Token
You need to set your DISCORD_BOT_TOKEN environment variable to make the bot work.

  (On macOS/Linux:)
  ```bash
  export DISCORD_BOT_TOKEN="your_token_here"
  ```
  (On Windows:)
  ```bash
  set DISCORD_BOT_TOKEN="your_token_here"
```
### Running the Bot Locally
Once everything is set up, you can run the bot on your local machine:
  ```bash
  python bot.py
```
### Deploying on Render
To deploy the bot on Render, follow these steps:

1. Create an Account: Sign up on Render.
2. Connect Your GitHub Repository: Link your GitHub repository to Render.
3. Set up the Build Command:

In the Build Command field, enter:
  ```bash
  pip install -r requirements.txt
```
4. Add the Discord Bot Token:
Add the DISCORD_BOT_TOKEN environment variable in Render’s dashboard (Settings > Environment Variables).
5. Deploy: Click "Deploy" and your bot will be live!

### Keeping the Bot Online 24/7 (Free Plan)
To prevent the bot from sleeping due to Render's free plan limitations, use UptimeRobot:

1. Create an account on uptimerobot.com.
2. Click on Add New Monitor.
3. Choose monitor type: HTTP(s).
4. Enter your public Render URL (e.g., https://discord-meme-bot.onrender.com/).
5. Name it (e.g., Discord Meme Bot) and click Create Monitor.

### Hosting on Replit 
You can also run this bot using Replit:

1. Import the project to Replit.
2. Add your DISCORD_BOT_TOKEN in Secrets (Environment Variables).
3. Add a keep_alive.py file:
   ```bash
   from flask import Flask
   from threading import Thread

   app = Flask('')

   @app.route('/')
   def home():
       return "Bot is running!"
   
   def run():
       app.run(host='0.0.0.0', port=8080)
   
   def keep_alive():
       t = Thread(target=run)
       t.start()
4. In your bot.py, add:
   ```bash
   from keep_alive import keep_alive
   keep_alive()
5. Run the project and use the Replit URL with UptimeRobot.

   
### Contributing
If you'd like to contribute to this project, feel free to fork it, make changes, and submit pull requests. All contributions are welcome!

## Acknowledgments

- Meme fetching logic adapted from [Original Meme API Example Repo](https://github.com/D3vd/Meme_Api)
- Inspired by a meme bot idea shared by **Hong Jeon** on [Codedex](https://www.codedex.io/projects/build-a-discord-bot-with-python)

### License
This project is licensed under the MIT License.









