from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram import filters, Client, errors
from pyrogram.errors.exceptions.flood_420 import FloodWait
from database import add_user, add_group, all_users, all_groups, users, remove_user
from configs import cfg
import asyncio

app = Client(
    "approver",
    api_id=cfg.API_ID,
    api_hash=cfg.API_HASH,
    bot_token=cfg.BOT_TOKEN
)

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Main process ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
@app.on_chat_join_request(filters.group | filters.channel)
async def approve(_, m: Message):
    op = m.chat
    kk = m.from_user
    try:
        add_group(op.id)
        await app.approve_chat_join_request(op.id, kk.id)

        buttons = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("🎥 Movie Updates Channel 🎥", url="https://t.me/+yXehY0UBhTkxMTQ1")]
            ]
        )

        text = (
            f"<b>Hello {kk.mention} 👋</b>\n\n"
            f"✅ Your request to join <b>{op.title}</b> has been approved!\n\n"
            "ℹ️ Send /start to know more about me."
        )

        await app.send_message(
            kk.id,
            text,
            reply_markup=buttons,
            disable_web_page_preview=True
        )

        add_user(kk.id)

    except errors.PeerIdInvalid:
        print(f"⚠️ Cannot send message to {kk.id} — PeerIdInvalid (user hasn’t started bot).")
    except Exception as err:
        print(f"❌ Error approving {kk.id} in {op.id}: {err}")

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Start ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
@app.on_message(filters.private & filters.command("start"))
async def start(_, m: Message):
    keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("🎥 Movie Updates Channel 🎥", url="https://t.me/+IiS5lW-OAUU1ZGRl")]
        ]
    )

    add_user(m.from_user.id)

    await m.reply_photo(
        "https://envs.sh/GXT.jpg",
        caption=(
            f"<b>Hi {m.from_user.mention}, I am an Auto Approve Bot. 🤖\n\n"
            f"I can approve your channel or group join requests instantly. 🚀\n\n"
            f"🔹 Steps:\n"
            f"1️⃣ Add me as an administrator to your group or channel.\n"
            f"2️⃣ I’ll automatically approve join requests!\n\n"
            f"📜 Disclaimer 👉 /disclaimer\n\n"
            f"✨ Created By @KR_Picture</b>"
        ),
        reply_markup=keyboard
    )

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Disclaimer ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
@app.on_message(filters.command("disclaimer"))
async def disclaimer(_, m: Message):
    text = (
        "<b>📢 Disclaimer – Auto Approve Join Request Bot</b>\n\n"
        "🔹 This bot is an automated system that approves join requests in Telegram channels/groups based on predefined rules. "
        "By using this bot, you acknowledge and agree to the following:\n\n"
        "✅ <b>No Liability</b>\n"
        "The bot owner & developers are not responsible for any unauthorized access, spam, or misuse. "
        "Channel/Group admins must configure settings responsibly.\n\n"
        "🤖 <b>Automated Decisions</b>\n"
        "The bot works automatically based on set criteria. It does not verify user intent or guarantee member authenticity.\n\n"
        "🔧 <b>Admin Responsibility</b>\n"
        "Channel/Group admins are fully responsible for moderation. "
        "The bot only accepts requests and does not enforce any additional rules.\n\n"
        "🚫 <b>No Responsibility for Content</b>\n"
        "The bot does not control, monitor, or endorse any messages, media, or content posted in the group/channel. "
        "The channel admins and users are solely responsible for all content shared. "
        "The bot owner & developers cannot be held accountable for any violations, illegal content, or disputes arising in the channel/group.\n\n"
        "🔒 <b>Privacy Notice</b>\n"
        "The bot does not store or share personal data beyond what’s needed for join request processing.\n\n"
        "📌 Ensure responsible usage to keep your channel/group secure!"
    )

    buttons = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("🎥 Movie Updates Channel 🎥", url="https://t.me/KR_PICTURE")]
        ]
    )

    await m.reply_text(text, reply_markup=buttons, disable_web_page_preview=True)

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Callback ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
@app.on_callback_query(filters.regex("chk"))
async def chk(_, cb: CallbackQuery):
    keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("🎥 Movie Updates Channel 🎥", url="https://t.me/+IiS5lW-OAUU1ZGRl")]
        ]
    )

    add_user(cb.from_user.id)

    await cb.message.edit_text(
        text=(
            f"<b>Hi {cb.from_user.mention}, I am an Auto Approve Bot. 🤖\n\n"
            f"I can approve your channel or group join requests instantly.\n\n"
            f"📌 Steps:\n"
            f"1️⃣ Add me as an administrator to your group or channel.\n"
            f"2️⃣ I’ll handle join requests automatically!\n\n"
            f"📜 Disclaimer 👉 /disclaimer\n\n"
            f"✨ Created By @KR_Picture</b>"
        ),
        reply_markup=keyboard,
        disable_web_page_preview=True
    )

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Info ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
@app.on_message(filters.command("users") & filters.user(cfg.SUDO))
async def dbtool(_, m: Message):
    xx = all_users()
    x = all_groups()
    tot = int(xx + x)
    await m.reply_text(
        f"🍀 Chats Stats 🍀\n🙋‍♂️ Users : `{xx}`\n👥 Groups : `{x}`\n🚧 Total users & groups : `{tot}`"
    )

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Broadcast ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
@app.on_message(filters.command("bcast") & filters.user(cfg.SUDO))
async def bcast(_, m: Message):
    allusers = users
    lel = await m.reply_text("`⚡️ Processing...`")
    success = 0
    failed = 0
    deactivated = 0
    blocked = 0
    for usrs in allusers.find():
        try:
            userid = usrs["user_id"]
            if m.command[0] == "bcast":
                await m.reply_to_message.copy(int(userid))
            success +=1
        except FloodWait as ex:
            await asyncio.sleep(ex.value)
            if m.command[0] == "bcast":
                await m.reply_to_message.copy(int(userid))
        except errors.InputUserDeactivated:
            deactivated +=1
            remove_user(userid)
        except errors.UserIsBlocked:
            blocked +=1
        except Exception as e:
            print(e)
            failed +=1

    await lel.edit(
        f"✅Successfull to `{success}` users.\n❌ Failed to `{failed}` users.\n👾 Found `{blocked}` Blocked users\n👻 Found `{deactivated}` Deactivated users."
    )

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Broadcast Forward ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
@app.on_message(filters.command("fcast") & filters.user(cfg.SUDO))
async def fcast(_, m: Message):
    allusers = users
    lel = await m.reply_text("`⚡️ Processing...`")
    success = 0
    failed = 0
    deactivated = 0
    blocked = 0
    for usrs in allusers.find():
        try:
            userid = usrs["user_id"]
            if m.command[0] == "fcast":
                await m.reply_to_message.forward(int(userid))
            success +=1
        except FloodWait as ex:
            await asyncio.sleep(ex.value)
            if m.command[0] == "fcast":
                await m.reply_to_message.forward(int(userid))
        except errors.InputUserDeactivated:
            deactivated +=1
            remove_user(userid)
        except errors.UserIsBlocked:
            blocked +=1
        except Exception as e:
            print(e)
            failed +=1

    await lel.edit(
        f"✅Successfull to `{success}` users.\n❌ Failed to `{failed}` users.\n👾 Found `{blocked}` Blocked users\n👻 Found `{deactivated}` Deactivated users."
    )

print("I'm Alive Now!")
app.run()
