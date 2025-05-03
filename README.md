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
6. When deploying the bot on Render, you do not need the additional code used on Replit (keep_alive.py and add this on bot.py).

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

### Keeping the Bot Online 24/7 (Free Plan)
To prevent the bot from sleeping due to Render's free plan limitations, use UptimeRobot:

1. Create an account on uptimerobot.com.
2. Click on Add New Monitor.
3. Choose monitor type: HTTP(s).
4. Enter your public Render URL (e.g., https://discord-meme-bot.onrender.com/).
5. Name it (e.g., Discord Meme Bot) and click Create Monitor.

### **Render + UptimeRobot Observations**
1. Free Plan Limitations: On the free plan, Render services sleep after 15 minutes of inactivity, which can cause downtime for the bot. This needs to be managed with external services like UptimeRobot to keep the bot awake.
2. Internet Connection and Latency Issues: While using services like Render and UptimeRobot, the location of the server can influence the performance of your bot. For example, if you're based in Brazil, the server's geographical location may cause latency issues or connection drops due to the distance from the server's data center. 
 
### **Replit + UptimeRobot Observations**
1. Replit Free Plan Limitations: Replit’s free plan has resource limits and may stop your bot if inactive or if the tab is closed, causing downtime.
2. UptimeRobot: While it helps keep the bot active by pinging the URL, it doesn’t solve Replit's inactivity issue. The bot may still stop after some time.
3. No 24/7 Guarantee: UptimeRobot helps, but Replit’s free plan still causes potential downtime after inactivity.
4. Keep-Alive Script: A Flask-based keep-alive script helps, but Replit’s free tier may still stop the bot due to inactivity.
5. Best for Small Projects: Replit + UptimeRobot works well for small bots or personal projects, but for larger bots, paid hosting services are recommended for consistent uptime.

### Final Considerations
While free services like Replit and Render can work for hosting your Discord Meme Bot, they come with limitations like downtime and resource constraints. For more reliable performance, especially in regions with internet instability, upgrading to paid plans is recommended. Paid services offer better stability, faster speeds, and additional features, ensuring smoother and uninterrupted bot performance.

### Contributing
If you'd like to contribute to this project, feel free to fork it, make changes, and submit pull requests. All contributions are welcome!

## Acknowledgments

- Meme fetching logic adapted from [Original Meme API Example Repo](https://github.com/D3vd/Meme_Api)
- Inspired by a meme bot idea shared by **Hong Jeon** on [Codedex](https://www.codedex.io/projects/build-a-discord-bot-with-python)










