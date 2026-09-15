"""
Burst Raid Module - Madara's Silent Mangekyo Burst Technique
© @ll_ALPHA_BABY_lll
"""

import asyncio
import time
from random import choice
from telethon import events
from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, SUDO_USERS, OWNER_ID, CMD_HNDLR as hl

# Import raid data
try:
    from RAUSHAN.data import BURST_MSG, ALTRON
except ImportError:
    from data import BURST_MSG, ALTRON

# Active burst raids tracker
BURST_RAIDS = {}

# Protection check function
async def is_protected(user_id):
    if user_id in ALTRON:
        return True, "ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴀʟᴛʀᴏɴ'ꜱ ᴏᴡɴᴇʀ."
    elif user_id == OWNER_ID:
        return True, "ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴏᴡɴᴇʀ ᴏꜰ ᴛʜᴇꜱᴇ ʙᴏᴛꜱ."
    elif user_id in SUDO_USERS:
        return True, "ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴀ ꜱᴜᴅᴏ ᴜꜱᴇʀ."
    return False, None

# Silent burst raid execution function
async def silent_burst_raid(client, chat_id, username, burst_list, burst_count=10, pause=2):
    """
    Execute silent burst raid - NO OUTPUT messages
    10 messages in 1 second, pause 2 seconds
    """
    try:
        while True:
            # Check if raid should stop
            if chat_id in BURST_RAIDS and not BURST_RAIDS[chat_id]:
                break
                
            # Send 10 messages in 1 second (0.1s delay between each)
            for i in range(burst_count):
                # Check if raid should stop mid-burst
                if chat_id in BURST_RAIDS and not BURST_RAIDS[chat_id]:
                    return
                    
                reply = choice(burst_list)
                caption = f"{username} {reply}"
                await client.send_message(chat_id, caption)
                
                # 0.1s delay between messages in burst
                await asyncio.sleep(0.1)
            
            # Check if raid should stop
            if chat_id in BURST_RAIDS and not BURST_RAIDS[chat_id]:
                break
                
            # Pause for 2 seconds
            await asyncio.sleep(pause)
            
    except Exception as e:
        print(f"Silent burst raid error: {e}")

# All clients decorators for silent burst command
@X1.on(events.NewMessage(incoming=True, pattern=r"\%sburst(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%sburst(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%sburst(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%sburst(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%sburst(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%sburst(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%sburst(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%sburst(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%sburst(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%sburst(?: |$)(.*)" % hl))
async def silent_burst_raid_start(e):
    if e.sender_id not in SUDO_USERS:
        return
    
    args = e.text.split(" ", 2)
    
    # Get target user
    if len(args) >= 2:
        try:
            entity = await e.client.get_entity(args[1])
            uid = entity.id
        except:
            return  # Silent fail - no output
    elif e.reply_to_msg_id:
        a = await e.get_reply_message()
        entity = await e.client.get_entity(a.sender_id)
        uid = entity.id
    else:
        return  # Silent fail - no output
    
    try:
        # Check protection
        protected, msg = await is_protected(uid)
        if protected:
            return  # Silent fail for protected users
        
        first_name = entity.first_name
        username = f"[{first_name}](tg://user?id={uid})"
        
        # Check if already bursting in this chat
        if e.chat_id in BURST_RAIDS and BURST_RAIDS[e.chat_id]:
            return  # Silent fail - already active
        
        # Activate burst raid for this chat
        BURST_RAIDS[e.chat_id] = True
        
        # Execute silent burst raid from ALL clients using BURST_MSG
        tasks = []
        for client in [X1, X2, X3, X4, X5, X6, X7, X8, X9, X10]:
            if client and hasattr(client, 'send_message'):
                task = asyncio.create_task(
                    silent_burst_raid(client, e.chat_id, username, BURST_MSG)
                )
                tasks.append(task)
        
        # Wait for all tasks to complete or stop
        await asyncio.gather(*tasks)
        
        # Clean up
        if e.chat_id in BURST_RAIDS:
            del BURST_RAIDS[e.chat_id]
        
    except Exception as err:
        print(f"Silent burst raid error: {err}")
        if e.chat_id in BURST_RAIDS:
            del BURST_RAIDS[e.chat_id]

# Stop silent burst raid command - SILENT
@X1.on(events.NewMessage(incoming=True, pattern=r"\%sstopburst(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%sstopburst(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%sstopburst(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%sstopburst(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%sstopburst(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%sstopburst(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%sstopburst(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%sstopburst(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%sstopburst(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%sstopburst(?: |$)(.*)" % hl))
async def stop_silent_burst(e):
    if e.sender_id not in SUDO_USERS:
        return
    
    if e.chat_id in BURST_RAIDS:
        BURST_RAIDS[e.chat_id] = False
        # Wait a moment for tasks to clean up
        await asyncio.sleep(0.5)
        if e.chat_id in BURST_RAIDS:
            del BURST_RAIDS[e.chat_id]
        # SILENT - no output message
