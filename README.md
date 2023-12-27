
# ChatGPT Discord Bot

A fun Discord bot that integrates with OpenAI's ChatGPT to provide AI-powered responses. Just building a bot that allows me to send messages from chatGPT directly to Discord.



## Features

- **AI-powered Chat**: Engage in conversations with the power of OpenAI's ChatGPT service.
- **Easy Integration**: Quick setup to get ChatGPT in your server.

## Installation & Setup

1. ***Clone the Repository***:

    
    git clone https://github.com/connectme
    cd chatgpt-discord-bot
    

2. **Set Up a Virtual Environment (Recommended)**:


    python -m venv botenv
    source botenv/bin/activate
    

3. **Install Required Dependencies**:


    pip install -r requirements.txt
    

4. **Environment Variables**:
    
    Set up the following environment variables:

    - `DISCORD_TOKEN`: Your Discord bot token.
    - `OPENAI_API_KEY`: Your OpenAI API key.

    *Tip: Use tools like `python-decouple` for environment variables in Python.*

5. **Run the Bot**:


    python bot.py
    

## Usage

- **Start a Conversation**:

  
    !chatgpt Hello, ChatGPT!
    

    The bot will reply using the ChatGPT model.

- **Other Commands**:

    - `!help`: Shows help and available commands.

## Contributing

This is a fun project, but contributions are always welcome! If you have ideas or improvements, feel free to fork the repository and create a pull request.

## License

[MIT License](LICENSE)

