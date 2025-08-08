# 💬 Discord-Controlled Roblox Client via WebSocket

**PC ONLY**

Control your **Roblox client** using a **Discord bot** through a **local WebSocket server**. Type commands like `say`, `kill`, or `rejoin` in Discord and watch your Roblox player respond instantly 🤖🎮

---

## 📦 Requirements

### 🧠 System:

- Windows (or anything that can run Node.js + Python)
- Roblox Executor
- Discord bot token (get from Discord Developer Portal)

### 🔧 Tools / Libs:

- **Node.js** (v16+ recommended)
- **Python** (3.9+)
  - `discord.py`
  - `websockets`
  - `python-dotenv`
- Roblox (LocalScript in a place file)
---

## 🚀 Installation & Setup

### 1. Clone the project

```bash
git clone https://github.com/random-projects-coz-bored-and-ye/Websocket-Discord-bot.git
cd Websocket-Discord-bot
````

---

### 2. Set up the WebSocket server

Install dependencies:

(in the server folder)

```bash
npm install ws
```

Run the server:

```bash
node server.js
```

This will start a WebSocket server on:

```
ws://127.0.0.1:3000
```

---

### 3. Set up the Discord bot

#### Install dependencies:

(in the bot folder)

```bash
pip install discord.py websockets python-dotenv
```

#### Add your Discord token:

Create a `.env` file:

```
syntaxicalisgettingmywill=YOUR_DISCORD_BOT_TOKEN
```

Run the bot:

```bash
python bot.py
```

---

### 4. Add the Roblox script

run and execute the script and press F9 to see if it connected and if it did you can do commands on the discord bot and it will run on roblox!
---

## 💻 Available Commands

| Discord Command        | Effect in Roblox                   |
| ---------------------- | ---------------------------------- |
| `sudo say Hello world` | Says "Hello world" in chat 🗣️     |
| `sudo kill`            | Sets character health to 0 💀      |
| `sudo rejoin`          | Teleports back to current place 🔁 |

---

## ⚠️ Notes

* This project only works unless you set it up to work on a webpage which is a bit complicated
---

## 🧃 Credits

Made by Syntaxical <3 


