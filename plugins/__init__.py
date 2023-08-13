from aiohttp import web
from .route import routes
import os
import random
import io
import asyncio
import time
import requests
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app
# Define the new hug command handler
@Client.on_message(filters.command('help'))
async def hug_command_handler(client, message):
    try:
        # Get the absolute path to the image file on your VPS
        file_path = '/workspaces/Advance_File_Sharing_Bot/images/imagelol.jpg'
        
        # Check if the file exists
        if os.path.exists(file_path):
            # Load the image file in binary mode
            with open(file_path, 'rb') as image_file:
                image_data = image_file.read()
                
                # Create buttons with links
                google_button = InlineKeyboardButton(text='✦ᴏᴜʀ ɴᴇᴛᴡᴏʀᴋ✦', url='https://telegram.me/Anime_Ocean_Network')
                donate_button = InlineKeyboardButton(text='✦ᴘʀᴏᴍᴏ ᴡɪᴛʜ ᴜs✦', url='https://telegram.me/CuriousToFault')
                
                # Create an inline keyboard and add the buttons
                keyboard = InlineKeyboardMarkup([[google_button], [donate_button]])
                
                # Create an in-memory binary stream and load the image data
                stream = io.BytesIO(image_data)
                
                # Send the image file and the buttons to the user as a reply
                await client.send_photo(chat_id=message.chat.id, photo=stream, reply_markup=keyboard)
        
        else:
            # Raise an exception if the file does not exist
            raise FileNotFoundError(f"File not found at {file_path}")
    
    except Exception as e:
        print("Exception occurred: ", e)


# Define the new ping command handler
@Client.on_message(filters.command('ping'))
async def ping_command_handler(client, message):
    # Record the current time
    start_time = time.time()

    # Send a message to the user
    msg = await message.reply_text("🏓 Pinging...")

    # Calculate the response time
    end_time = time.time()
    response_time = int((end_time - start_time) * 1000)

    # Edit the message to include the response time
    await msg.edit_text(f"🏓 Pong! {response_time} ms")




@Client.on_message(filters.command('joke'))
async def joke_command_handler(client, message):
    # Fetch a random joke from the API
    response = requests.get("https://sv443.net/jokeapi/v2/joke/Any?type=single")
    joke = response.json()["joke"]

    # Send the joke to the user
    await message.reply_text(joke)



@Client.on_message(filters.command('quote'))
async def quote_command_handler(client, message):
    # Fetch a random quote from the API
    response = requests.get("https://api.quotable.io/random")
    quote = response.json()["content"]
    author = response.json()["author"]

    # Send the quote to the user
    await message.reply_text(f"{quote}\n- {author}")




@Client.on_message(filters.command('waifu'))
async def waifu_command_handler(client, message):
    # Fetch a random anime girl image from the API
    response = requests.get("https://api.waifu.pics/sfw/waifu")
    image_url = response.json()["url"]

    # Send the image to the user
    await message.reply_photo(image_url)




# Define a dictionary to map the outcome of the coin flip to a string
outcome_map = {
    0: "heads",
    1: "tails"
}

# Define a dictionary to map the user's choice to a string
choice_map = {
    "h": "heads",
    "t": "tails"
}

# Define the user's default coin value
default_coin_value = 10000

@Client.on_message(filters.command('coinflip'))
async def coinflip_command_handler(client, message):
    # Get the user's coin value
    user_coin_value = default_coin_value

    # Check if the user has any arguments and update their coin value if necessary
    if len(message.command) > 1:
        try:
            user_coin_value = int(message.command[1])
        except ValueError:
            await message.reply_text("Invalid coin value. Please enter a valid integer.")
            return

    # Check if the user has enough coins to play
    if user_coin_value <= 0:
        await message.reply_text("You don't have enough coins to play.")
        return

    # Send a message to the user to choose heads or tails
    await message.reply_text("Choose heads or tails by entering 'h' or 't'.")

    # Wait for the user's response
    user_choice_message = await client.read_history(message.chat.id, limit=1)[0]
    user_choice = user_choice_message.text.lower()

    # Check if the user's choice is valid
    if user_choice not in choice_map.keys():
        await message.reply_text("Invalid choice. Please choose 'h' or 't'.")
        return

    # Flip a coin and get the outcome
    coin_outcome = random.randint(0, 1)
    coin_outcome_string = outcome_map[coin_outcome]

    # Check if the user won or lost
    if coin_outcome_string == choice_map[user_choice]:
        winnings = user_coin_value * 2
        await message.reply_text(f"{coin_outcome_string}! You won {winnings} coins!")
    else:
        winnings = 0
        await message.reply_text(f"{coin_outcome_string}! You lost {user_coin_value} coins.")

    # Update the user's coin value
    # Note: You should implement your own coin management system for your bot
    user_coin_value += winnings

__all__ = ["web_server"]
