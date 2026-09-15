import asyncio
from random import choice
from telethon import events
from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, SUDO_USERS, OWNER_ID, CMD_HNDLR as hl
from RAUSHAN.data import RAID, REPLYRAID, ALTRON, MRAID, SRAID, CRAID

REPLY_RAID = []

# Protection check function
async def is_protected(user_id):
    if user_id in ALTRON:
        return True, "❌ ᴛʜɪꜱ ᴜꜱᴇʀ ɪꜱ ᴘʀᴏᴛᴇᴄᴛᴇᴅ ꜰʀᴏᴍ ʀᴀɪᴅꜱ."
    elif user_id == OWNER_ID:
        return True, "❌ ʏᴏᴜ ᴄᴀɴɴᴏᴛ ʀᴀɪᴅ ᴛʜᴇ ʙᴏᴛ ᴏᴡɴᴇʀ."
    elif user_id in SUDO_USERS:
        return True, "❌ ᴛʜɪꜱ ᴜꜱᴇʀ ɪꜱ ᴀ ꜱᴜᴅᴏ ᴜꜱᴇʀ ᴀɴᴅ ᴘʀᴏᴛᴇᴄᴛᴇᴅ."
    return False, None

# Ultra-fast raid function with 30x speed
async def perform_raid(client, chat_id, username, counter, raid_list):
    # 30x faster speed (0.0033 seconds instead of 0.1)
    # Using bulk send for maximum performance
    messages = []
    for i in range(counter):
        reply = choice(raid_list)
        caption = f"{username} {reply}"
        messages.append(caption)
        
        # Send in batches of 50 for better performance
        if len(messages) >= 50 or i == counter - 1:
            # Send messages sequentially but with minimal delay
            for msg in messages:
                await client.send_message(chat_id, msg)
                await asyncio.sleep(0.0033)  # 30x faster than original 0.1s
            messages = []
            # Small break between batches to prevent complete flooding
            await asyncio.sleep(0.001)

# Even faster version using asyncio.gather (parallel sending)
async def perform_raid_parallel(client, chat_id, username, counter, raid_list):
    """Ultra-fast parallel raid - 50x faster but riskier"""
    # Create tasks for all messages
    tasks = []
    for _ in range(counter):
        reply = choice(raid_list)
        caption = f"{username} {reply}"
        tasks.append(client.send_message(chat_id, caption))
        
        # Send in batches of 30 to avoid overwhelming
        if len(tasks) >= 30:
            await asyncio.gather(*tasks)
            tasks = []
            await asyncio.sleep(0.001)  # Minimal break
    
    # Send remaining messages
    if tasks:
        await asyncio.gather(*tasks)


@X1.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
async def raid(e):
    if e.sender_id not in SUDO_USERS:
        return
    
    xraid = e.text.split(" ", 2)

    if len(xraid) == 3:
        entity = await e.client.get_entity(xraid[2])
        uid = entity.id
    elif e.reply_to_msg_id:             
        a = await e.get_reply_message()
        entity = await e.client.get_entity(a.sender_id)
        uid = entity.id
    else:
        await e.reply(f"⚠️ ɪɴᴠᴀʟɪᴅ ᴄᴏᴍᴍᴀɴᴅ ꜰᴏʀᴍᴀᴛ:\n  » {hl}ʀᴀɪᴅ <ᴄᴏᴜɴᴛ> <ᴜꜱᴇʀɴᴀᴍᴇ ᴏʀ ʀᴇᴘʟʏ>\n  » ᴇxᴀᴍᴘʟᴇ: {hl}ʀᴀɪᴅ 5 @ᴜꜱᴇʀɴᴀᴍᴇ")
        return

    try:
        # Check protection
        protected, msg = await is_protected(uid)
        if protected:
            await e.reply(msg)
            return
            
        first_name = entity.first_name
        counter = int(xraid[1])
        username = f"[{first_name}](tg://user?id={uid})"
        
        # Use ultra-fast raid with 30x speed
        await perform_raid(e.client, e.chat_id, username, counter, RAID)
        
    except (IndexError, ValueError):
        await e.reply(f"⚠️ ɪɴᴠᴀʟɪᴅ ᴄᴏᴍᴍᴀɴᴅ ꜰᴏʀᴍᴀᴛ:\n  » {hl}ʀᴀɪᴅ <ᴄᴏᴜɴᴛ> <ᴜꜱᴇʀɴᴀᴍᴇ ᴏʀ ʀᴇᴘʟʏ>\n  » ᴇxᴀᴍᴘʟᴇ: {hl}ʀᴀɪᴅ 5 @ᴜꜱᴇʀɴᴀᴍᴇ")
    except Exception as e:
        print(f"Raid error: {e}")


@X1.on(events.NewMessage(incoming=True))
@X2.on(events.NewMessage(incoming=True))
@X3.on(events.NewMessage(incoming=True))
@X4.on(events.NewMessage(incoming=True))
@X5.on(events.NewMessage(incoming=True))
@X6.on(events.NewMessage(incoming=True))
@X7.on(events.NewMessage(incoming=True))
@X8.on(events.NewMessage(incoming=True))
@X9.on(events.NewMessage(incoming=True))
@X10.on(events.NewMessage(incoming=True))
async def reply_raid_handler(event):
    global REPLY_RAID
    check = f"{event.sender_id}_{event.chat_id}"
    if check in REPLY_RAID:
        await asyncio.sleep(0.0033)  # 30x faster (was 0.1s)
        await event.client.send_message(
            entity=event.chat_id,
            message=choice(REPLYRAID),
            reply_to=event.message.id,
        )


@X1.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
async def rraid(e):
    if e.sender_id not in SUDO_USERS:
        return
        
    mkrr = e.text.split(" ", 1)
    if len(mkrr) == 2:
        entity = await e.client.get_entity(mkrr[1])
    elif e.reply_to_msg_id:             
        a = await e.get_reply_message()
        entity = await e.client.get_entity(a.sender_id)
    else:
        await e.reply(f"⚠️ ɪɴᴠᴀʟɪᴅ ᴄᴏᴍᴍᴀɴᴅ ꜰᴏʀᴍᴀᴛ:\n  » {hl}ʀʀᴀɪᴅ <ᴜꜱᴇʀɴᴀᴍᴇ ᴏʀ ʀᴇᴘʟʏ>\n  » ᴇxᴀᴍᴘʟᴇ: {hl}ʀʀᴀɪᴅ @ᴜꜱᴇʀɴᴀᴍᴇ")
        return

    try:
        user_id = entity.id
        
        # Check protection
        protected, msg = await is_protected(user_id)
        if protected:
            await e.reply(msg)
            return
            
        global REPLY_RAID
        check = f"{user_id}_{e.chat_id}"
        if check not in REPLY_RAID:
            REPLY_RAID.append(check)
        await e.reply("» ʀᴇᴘʟʏ ʀᴀɪᴅ ᴀᴄᴛɪᴠᴀᴛᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ !! ✅")
    except Exception as err:
        print(f"Reply raid error: {err}")
        await e.reply("» ᴇʀʀᴏʀ ᴀᴄᴛɪᴠᴀᴛɪɴɢ ʀᴇᴘʟʏ ʀᴀɪᴅ")


@X1.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
async def drraid(e):
    if e.sender_id not in SUDO_USERS:
        return
        
    text = e.text.split(" ", 1)

    if len(text) == 2:
        entity = await e.client.get_entity(text[1])
    elif e.reply_to_msg_id:             
        a = await e.get_reply_message()
        entity = await e.client.get_entity(a.sender_id)
    else:
        await e.reply(f"⚠️ ɪɴᴠᴀʟɪᴅ ᴄᴏᴍᴍᴀɴᴅ ꜰᴏʀᴍᴀᴛ:\n  » {hl}ᴅʀʀᴀɪᴅ <ᴜꜱᴇʀɴᴀᴍᴇ ᴏʀ ʀᴇᴘʟʏ>\n  » ᴇxᴀᴍᴘʟᴇ: {hl}ᴅʀʀᴀɪᴅ @ᴜꜱᴇʀɴᴀᴍᴇ")
        return

    try:
        global REPLY_RAID
        check = f"{entity.id}_{e.chat_id}"
        if check in REPLY_RAID:
            REPLY_RAID.remove(check)
        await e.reply("» ʀᴇᴘʟʏ ʀᴀɪᴅ ᴅᴇᴀᴄᴛɪᴠᴀᴛᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ !! ✅")
    except Exception as err:
        print(f"Deactivate reply raid error: {err}")
        await e.reply("» ᴇʀʀᴏʀ ᴅᴇᴀᴄᴛɪᴠᴀᴛɪɴɢ ʀᴇᴘʟʏ ʀᴀɪᴅ")


@X1.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
async def mraid(e):
    if e.sender_id not in SUDO_USERS:
        return
        
    xraid = e.text.split(" ", 2)

    if len(xraid) == 3:
        entity = await e.client.get_entity(xraid[2])
        uid = entity.id
    elif e.reply_to_msg_id:             
        a = await e.get_reply_message()
        entity = await e.client.get_entity(a.sender_id)
        uid = entity.id
    else:
        await e.reply(f"⚠️ ɪɴᴠᴀʟɪᴅ ᴄᴏᴍᴍᴀɴᴅ ꜰᴏʀᴍᴀᴛ:\n  » {hl}ᴍʀᴀɪᴅ <ᴄᴏᴜɴᴛ> <ᴜꜱᴇʀɴᴀᴍᴇ ᴏʀ ʀᴇᴘʟʏ>\n  » ᴇxᴀᴍᴘʟᴇ: {hl}ᴍʀᴀɪᴅ 5 @ᴜꜱᴇʀɴᴀᴍᴇ")
        return

    try:
        # Check protection
        protected, msg = await is_protected(uid)
        if protected:
            await e.reply(msg)
            return
            
        first_name = entity.first_name
        counter = int(xraid[1])
        username = f"[{first_name}](tg://user?id={uid})"
        
        # Use ultra-fast raid with 30x speed
        await perform_raid(e.client, e.chat_id, username, counter, MRAID)
        
    except (IndexError, ValueError):
        await e.reply(f"⚠️ ɪɴᴠᴀʟɪᴅ ᴄᴏᴍᴍᴀɴᴅ ꜰᴏʀᴍᴀᴛ:\n  » {hl}ᴍʀᴀɪᴅ <ᴄᴏᴜɴᴛ> <ᴜꜱᴇʀɴᴀᴍᴇ ᴏʀ ʀᴇᴘʟʏ>\n  » ᴇxᴀᴍᴘʟᴇ: {hl}ᴍʀᴀɪᴅ 5 @ᴜꜱᴇʀɴᴀᴍᴇ")
    except Exception as e:
        print(f"Mraid error: {e}")


@X1.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
async def sraid(e):
    if e.sender_id not in SUDO_USERS:
        return
        
    xraid = e.text.split(" ", 2)

    if len(xraid) == 3:
        entity = await e.client.get_entity(xraid[2])
        uid = entity.id
    elif e.reply_to_msg_id:             
        a = await e.get_reply_message()
        entity = await e.client.get_entity(a.sender_id)
        uid = entity.id
    else:
        await e.reply(f"⚠️ ɪɴᴠᴀʟɪᴅ ᴄᴏᴍᴍᴀɴᴅ ꜰᴏʀᴍᴀᴛ:\n  » {hl}ꜱʀᴀɪᴅ <ᴄᴏᴜɴᴛ> <ᴜꜱᴇʀɴᴀᴍᴇ ᴏʀ ʀᴇᴘʟʏ>\n  » ᴇxᴀᴍᴘʟᴇ: {hl}ꜱʀᴀɪᴅ 5 @ᴜꜱᴇʀɴᴀᴍᴇ")
        return

    try:
        # Check protection
        protected, msg = await is_protected(uid)
        if protected:
            await e.reply(msg)
            return
            
        first_name = entity.first_name
        counter = int(xraid[1])
        username = f"[{first_name}](tg://user?id={uid})"
        
        # Use ultra-fast raid with 30x speed
        await perform_raid(e.client, e.chat_id, username, counter, SRAID)
        
    except (IndexError, ValueError):
        await e.reply(f"⚠️ ɪɴᴠᴀʟɪᴅ ᴄᴏᴍᴍᴀɴᴅ ꜰᴏʀᴍᴀᴛ:\n  » {hl}ꜱʀᴀɪᴅ <ᴄᴏᴜɴᴛ> <ᴜꜱᴇʀɴᴀᴍᴇ ᴏʀ ʀᴇᴘʟʏ>\n  » ᴇxᴀᴍᴘʟᴇ: {hl}ꜱʀᴀɪᴅ 5 @ᴜꜱᴇʀɴᴀᴍᴇ")
    except Exception as e:
        print(f"Sraid error: {e}")


@X1.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
async def craid(e):
    if e.sender_id not in SUDO_USERS:
        return
        
    xraid = e.text.split(" ", 2)

    if len(xraid) == 3:
        entity = await e.client.get_entity(xraid[2])
        uid = entity.id
    elif e.reply_to_msg_id:             
        a = await e.get_reply_message()
        entity = await e.client.get_entity(a.sender_id)
        uid = entity.id
    else:
        await e.reply(f"⚠️ ɪɴᴠᴀʟɪᴅ ᴄᴏᴍᴍᴀɴᴅ ꜰᴏʀᴍᴀᴛ:\n  » {hl}ᴄʀᴀɪᴅ <ᴄᴏᴜɴᴛ> <ᴜꜱᴇʀɴᴀᴍᴇ ᴏʀ ʀᴇᴘʟʏ>\n  » ᴇxᴀᴍᴘʟᴇ: {hl}ᴄʀᴀɪᴅ 5 @ᴜꜱᴇʀɴᴀᴍᴇ")
        return

    try:
        # Check protection
        protected, msg = await is_protected(uid)
        if protected:
            await e.reply(msg)
            return
            
        first_name = entity.first_name
        counter = int(xraid[1])
        username = f"[{first_name}](tg://user?id={uid})"
        
        # Use ultra-fast raid with 30x speed
        await perform_raid(e.client, e.chat_id, username, counter, CRAID)
        
    except (IndexError, ValueError):
        await e.reply(f"⚠️ ɪɴᴠᴀʟɪᴅ ᴄᴏᴍᴍᴀɴᴅ ꜰᴏʀᴍᴀᴛ:\n  » {hl}ᴄʀᴀɪᴅ <ᴄᴏᴜɴᴛ> <ᴜꜱᴇʀɴᴀᴍᴇ ᴏʀ ʀᴇᴘʟʏ>\n  » ᴇxᴀᴍᴘʟᴇ: {hl}ᴄʀᴀɪᴅ 5 @ᴜꜱᴇʀɴᴀᴍᴇ")
    except Exception as e:
        print(f"Craid error: {e}")
