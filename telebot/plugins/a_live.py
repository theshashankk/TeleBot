from asyncio 

from telethon import version 
from Lion.utils import admin_cmd, sudo_cmd

from Lion import ALIVE_PIC, ALIVE_NAME, Startime, lionver 
from lionConfig import Config, Var 

# ======CONSTANTS=========#
CUSTOM_ALIVE = (
    Var.CUSTOM_ALIVE
    if Var.CUSTOM_ALIVE
    else "Mʏ sʏsᴛᴇᴍ ɪs ᴘᴇʀғᴇᴄᴛʟʏ ʀᴜɴɴɪɢ"
)
ALIVE_PIC = Var.ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/d65773b873c889b7ebcbe.jpg"
if Config.SUDO_USERS:
    sudo = "Enabled"
else:
    sudo = "Disabled"
# =======================#
def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time
  
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "ℓιση υsεя"

@Lion.on(admin_cmd(outgoing=true, pattern="alive"))
@Lion.on(sudo_cmd(outgoing=true, pattern="alive", allow_sudo=true))
async def alive(alive):
    start = datetime.now()
    myid = bot.uid
    end = datetime()
    (end - start).microseconds / 1000
    uptime = get_readable_time((time.time() - StartTime))
        lion_cap = f"**Wᴇʟᴄᴏᴍᴇ ᴛᴏ ʟɪᴏɴ ᴜsᴇʀʙᴏᴛ**\n"
        lion_cap += f"{CUSTOM_ALIVE}\n\n"
        lion_cap += "Aʙᴏᴜᴛ ᴍʏ sʏsᴛᴇᴍ\n\n"
        lion_cap += f"{assistant}Vᴇʀsɪᴏɴ ☞ {lion_ver}\n"
        lion_cap += f"Tᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ ☞ {version.__version__}\n"
        lion_cap += f"Pʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ ☞ {platform.python_version()}\n"
        lion_cap += "Sᴜᴘᴘᴏʀᴛ Cʜᴀɴɴᴇʟ ☞ [ᴊᴏɪɴ](https://t.me/TeamLionUB)\n"
        lion_cap += "ʟɪᴄᴇɴᴄᴇ ☞ [𝚃𝙴𝙰𝙼 𝙻𝙸𝙾𝙽 𝚄𝙱](https://github.com/TeamLion-X)\n"
        lion_cap += (
        "✗ **𝘾𝙊𝙋𝙔𝙍𝙄𝙂𝙃𝙏 𝘽𝙔** ☞ [𝙻𝙸𝙾𝙽 𝚄𝙱](https://github.com/teamlion-X/Lion-X)\n\n"
    )
        lion_cap += f"Lɪᴏɴ Uᴘᴛɪᴍᴇ ☞ {uptime}\n"
        lion_cap += f"Mʏ ᴘᴇʀᴏ ᴍᴀsᴛᴇʀ ☞ [{DEFAULT_USER}](tg://user?id={myid})\n"
        lion_cap += "[Rᴇᴘᴏsɪᴛᴏʀʏ](https://github.com/TeamLion-X/Lion-X"
