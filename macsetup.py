
## Setting Up ChatGPT Discord Bot on macOS ##

### 1. **Prerequisites:**
- Ensure you have Python 3.6 or later installed. You can check your Python version by running:
  ```bash
  python --version
  ```

### 2. **Clone the Repository:**
1. Open Terminal.
2. Navigate to a directory where you want to store the bot's code on your machine.
3. Run the following command to clone the repository:
  ```bash
  git clone https://github.com/bbhorrigan/connectme.git
  cd chatgpt-discord-bot
  ```

### 3. **Setting up a Virtual Environment:**
1. In the Terminal, still inside the bot's directory, run:
  ```bash
  python3 -m venv botenv
  ```
2. Activate the virtual environment:
  ```bash
  source botenv/bin/activate
  ```

### 4. **Install Required Dependencies:**
While the virtual environment is activated, install the necessary Python packages:
```bash
pip install -r requirements.txt
```

### 5. **Environment Variables Setup:**
1. In the bot's directory, create a file named `.env`.
2. Add the following lines to the `.env` file:
   ```
   DISCORD_TOKEN=Your_Discord_Bot_Token
   OPENAI_API_KEY=Your_OpenAI_API_Key
   ```

Replace `Your_Discord_Bot_Token` and `Your_OpenAI_API_Key` with your actual Discord bot token and OpenAI API key, respectively.

### 6. **Run the Bot:**
With everything in place, start the bot by running:
```bash
python bot.py
```

The bot should now be running, and you should see a message in the terminal indicating its online status.

### 7. **Invite the Bot to Your Server:**
1. Go to the [Discord Developer Portal](https://discord.com/developers/applications).
2. Click on your application (bot).
3. Navigate to the "OAuth2" page.
4. Under "OAuth2 URL Generator", check the "bot" scope.
5. Select the necessary permissions your bot requires.
6. Use the generated URL to invite your bot to a server.

**Note**: Ensure you have the necessary permissions on the server to invite bots.

### 8. **Interact with the Bot:**
Once the bot is in your server, you can interact with it using the prefixed commands, e.g., `!chatgpt Hello, ChatGPT!`.

---

Remember to always deactivate your virtual environment when you're done by running:
```bash
deactivate
```

And that's it! You've successfully set up your ChatGPT Discord bot on macOS. If you make any updates or changes to the bot's code, you may need to restart the bot for those changes to take effect.
