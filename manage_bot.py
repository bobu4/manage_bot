from telethon.sync import TelegramClient
from telethon import events
import subprocess
from telethon import Button
import asyncio

admin_nickname = 'YOUR_NICKNAME'
#Your telegram api stuff
api_id = 00000000
api_hash = 'aaaaaaaaaaaaaaaaaaaa1111111'
bot_token = 'bot:token'
bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)
buttons_list = [Button.inline('Send command', b'send')]


@bot.on(events.NewMessage(pattern='/start', from_users=[admin_nickname]))
async def start_handler(event):
    await bot.send_message(event.message.peer_id.user_id, 'Hello!',
                           buttons=[buttons_list])


@bot.on(events.CallbackQuery(data=b'send'))
async def send_command_handler(send_command_event):
    await send_command_event.answer()
    user_info = await bot.get_entity(admin_nickname)
    if user_info.id == send_command_event.query.user_id:
        await bot.send_message(send_command_event.query.user_id, 'Enter command:')

        @bot.on(events.NewMessage(from_users=[send_command_event.query.user_id]))
        async def new_command_handler(new_command_event):
            args_line = f'{new_command_event.raw_text}'
            command_result = subprocess.run(args_line, shell=True, capture_output=True, text=True)
            command_output = command_result.stdout
            while command_output:
                if len(command_output) < 4096:
                    await bot.send_message(send_command_event.query.user_id, command_output[0:(command_output.rfind('\n', None, 4095) + 1)], buttons=buttons_list)
                else:
                    await bot.send_message(send_command_event.query.user_id,
                                           command_output[0:(command_output.rfind('\n', None, 4095) + 1)])
                command_output = command_output[(command_output.rfind('\n', None, 4095) + 1):]
            bot.remove_event_handler(new_command_handler)


bot.start(bot_token=bot_token)
loop = asyncio.get_event_loop()
loop.run_forever()
