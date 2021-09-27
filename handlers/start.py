from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_sticker("CAACAgUAAxkBAAIp9mBtwBBZGywWEmV-WC8gcMArjusuAAKMAgACTp1xV6m-mtC1YTfoHgQ")
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name}!
\nI am Awesome Blossom Music • @navuisback ❤
\nContact us at @navu_music_support
\n/help list of available commands.
 </b>""",
      
       
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "♬Ɯ៩ន០៣៩ ᖲᖰ០នន០៣🎵", url="https://t.me/best_friends_official1",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "👤 Owner", url="https://t.me/navuisback"
                    ),
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/best_friends_official1"
                    ),
                    InlineKeyboardButton(
                        "🔊 Updates", url="https://t.me/you_make_me_Villain"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "➕ Add To Your Group ➕", url="https://t.me/Awesome_blossom_music_bot?startgroup=true"
                    ) 
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "💁🏻‍♂️ Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Updates", url="https://t.me/you_make_me_Villain"
                    )
                ],    
                [    
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
                    )
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("help")
    & filters.private
    & ~ filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name}!
\n𝐔𝐒𝐄𝐑 𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒
\n/play <song name> - play song you requested
/dplay <song name> - play song you requested via deezer
/splay <song name> - play song you requested via jio saavn
/playlist - Show now playing list
/current - Show now playing
/song <song name> - download songs you want quickly
/search <query> - search videos on youtube with details
/deezer <song name> - download songs you want quickly via deezer
/saavn <song name> - download songs you want quickly via saavn
/video <song name> - download videos you want quickly
\n𝐀𝐃𝐌𝐈𝐍𝐒 𝐎𝐍𝐋𝐘
/player - open music player settings panel
/pause - pause song play
/resume - resume song play
/skip - play next song
/end - stop music play
/userbotjoin - invite assistant to your chat
/admincache - Refresh admin list
\n𝐂𝐫𝐞𝐚𝐭𝐞𝐝 𝐰𝐢𝐭𝐡 ❤️ 𝐛𝐲 NAVU
 </b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝐇𝐄𝐋𝐏 𝐂𝐎𝐍𝐓𝐀𝐂𝐓", url="https://t.me/navu_music_support"
                    )
                ]
            ]
        )
    )    
