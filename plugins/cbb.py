import pyrogram

from plugins.help_text import rename_cb, cancel_extract
from plugins.rename_file import force_name

helpbutton = [[
        InlineKeyboardButton(f'Channel', url='https://t.me/VKPROJECTS'),
        InlineKeyboardButton(f'Support', url='https://t.me/VKP_BOTS')
        ],[
        InlineKeyboardButton(f'{INFORMATION} Help', callback_data="help")
    ]]

aboutbutton = [[
        InlineKeyboardButton(f'🤔 How To Use', callback_data='help'),
        InlineKeyboardButton(f'Close 🔐', callback_data='close')
    ]]


@pyrogram.Client.on_callback_query()
async def cb_handler(bot, update):
        
    if "rename_button" in update.data:
        await update.message.delete()
        await force_name(bot, update.message)
        )
        return

    elif query.data == "help":
        await update.answer()
        keyboard = InlineKeyboardMarkup(helpbutton)
        await update.message.edit_text(
            Script.HELP_MSG,
            reply_markup=keyboard,
            disable_web_page_preview=True
        )
        return

    elif query.data == "about":
        await update.answer()
        keyboard = InlineKeyboardMarkup(aboutbutton)
        await update.message.edit_text(
            Script.ABOUT_MSG,
            reply_markup=keyboard,
            disable_web_page_preview=True
        )
        return

    elif query.data == "close_data":
        await update.message.delete()

        
    elif "cancel_e" in update.data:
        await update.message.delete()
        await cancel_extract(bot, update.message)
