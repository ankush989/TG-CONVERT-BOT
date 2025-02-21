import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import pyrogram
from config import Config 
from pyrogram import Client, Filters, InlineKeyboardButton, InlineKeyboardMarkup
from translation import Translation
from Tools.Download import download



my_father = "https://t.me/{}".format(Config.USER_NAME[1:])
support = "https://t.me/Mega_Bots_Updates"

@Client.on_message(Filters.command(["start"]))
async def start(c, m):

    msg := b.NewSendableMessage(u.EffectiveChat.Id, fmt.Sprintf("Hi [%s](tg://user?id=%v)\n 𝗜 𝗮𝗺 𝗮 𝗦𝗶𝗺𝗽𝗹𝗲 𝗖𝗼𝗻𝘃𝗲𝗿𝘁 𝗕𝗼𝘁 𝗪𝗶𝘁𝗵 𝗧𝗵𝘂𝗺𝗯𝗻𝗮𝗶𝗹 🔰 𝗕𝘂𝘁 𝗬𝗼𝘂 𝗠𝘂𝘀 𝗝𝗼𝗶𝗻 𝗠𝘆 𝗨𝗽𝗱𝗮𝘁𝗶𝗼𝗶𝗻 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 𝗙𝗼𝗿 𝗨𝘀𝗲 𝗠𝗲 🤗
𝗙𝗼𝗿 𝗠𝗼𝗿𝗲 𝗗𝗲𝘁𝗮𝗶𝗹𝘀 /help

𝗕𝗼𝘁 𝗠𝗮𝗱𝗲 𝗕𝘆 : @Mega_Bots_Updates} used start command")



@Client.on_message(Filters.command(["help"]))
async def help(c, m):

    await c.send_message(chat_id=m.chat.id,
                         text=Translation.HELP,
                         reply_to_message_id=m.message_id,
                         parse_mode="markdown")


@Client.on_message(Filters.command(["about"]))
async def about(c, m):

    await c.send_message(chat_id=m.chat.id,
                         text=Translation.ABOUT,
                         disable_web_page_preview=True,
                         reply_to_message_id=m.message_id,
                         parse_mode="markdown")

@Client.on_message(Filters.command(["converttovideo"]))
async def video(c, m):

  if Config.BOT_PWD:
      if (m.from_user.id not in Config.LOGGED_USER) & (m.from_user.id not in Config.AUTH_USERS):
          await m.reply_text(text=Translation.NOT_LOGGED_TEXT, quote=True)
          return
      else:
          pass
  if m.from_user.id in Config.BANNED_USER:
      await c.send_message(chat_id=m.chat.id, text=Translation.BANNED_TEXT)
      return
  if m.from_user.id not in Config.BANNED_USER:
      if m.reply_to_message is not None:
          await download(c, m)
      else:
          await c.send_message(chat_id=m.chat.id, text=Translation.REPLY_TEXT)

@Client.on_message(Filters.command(["converttofile"]))
async def file(c, m):

  if Config.BOT_PWD:
      if (m.from_user.id not in Config.LOGGED_USER) & (m.from_user.id not in Config.AUTH_USERS):
          await m.reply_text(text=Translation.NOT_LOGGED_TEXT, quote=True)
          return
      else:
          pass
  if m.from_user.id in Config.BANNED_USER:
      await c.send_message(chat_id=m.chat.id, text=Translation.BANNED_TEXT)
  if m.from_user.id not in Config.BANNED_USER:
    if m.reply_to_message is not None:
      await download(c, m)
    else:
       await c.send_message(chat_id=m.chat.id, text=Translation.REPLY_TEXT)

@Client.on_message(Filters.command(["login"]))
async def login(c, m):
    if Config.BOT_PWD:
        if (len(m.command) >= 2) & (m.from_user.id not in Config.LOGGED_USER) & (m.from_user.id not in Config.AUTH_USERS):
            _, password = m.text.split(" ", 1)
            if str(password) == str(Config.BOT_PWD):
                await c.send_message(chat_id=m.chat.id,
                                     text=Translation.SUCESS_LOGIN,
                                     disable_web_page_preview=True,
                                     reply_to_message_id=m.message_id,
                                     parse_mode="markdown")
                return Config.LOGGED_USER.append(m.from_user.id)
            if str(password) != str(Config.BOT_PWD):
                await c.send_message(chat_id=m.chat.id,
                                     text=Translation.WRONG_PWD,
                                     disable_web_page_preview=True,
                                     reply_to_message_id=m.message_id,
                                     parse_mode="markdown")

        if (len(m.command) < 2) & (m.from_user.id not in Config.LOGGED_USER) & (m.from_user.id not in Config.AUTH_USERS):
            await c.send_message(chat_id=m.chat.id,
                                 text="Use this command for login to this bot. Semd the passwordin the format 👉`/login Bot password`.",
                                 disable_web_page_preview=True,
                                 reply_to_message_id=m.message_id,
                                 parse_mode="markdown")

        if (m.from_user.id in Config.LOGGED_USER)|(m.from_user.id in Config.AUTH_USERS):
            await c.send_message(chat_id=m.chat.id,
                                 text=Translation.EXISTING_USER,
                                 disable_web_page_preview=True,
                                 reply_to_message_id=m.message_id,
                                 parse_mode="markdown")
