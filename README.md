## Usage

- Create a Discord Bot Application: https://discordpy.readthedocs.io/en/stable/discord.html
- Setup environment variables
```
export BOT_TOKEN=<Token from Discord>
export OPENAI_KEY=<Token from OpenAI>
```

```
# Using a virtualenv likely preferred
pip install -r requirements.txt 
python scrape.py
python transcription.py
python embeddings.py
python bot.py
```

