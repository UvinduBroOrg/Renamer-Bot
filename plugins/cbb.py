import pyrogram

from plugins.help_text import rename_cb, cancel_extract
from plugins.rename_file import force_name


@pyrogram.Client.on_callback_query()
async def cb_handler(bot, update):
        
    if "rename_button" in update.data:
        await update.message.delete()
        await force_name(bot, update.message)
        )
        return

    elif query.data == "help":
        await query.answer()
        keyboard = InlineKeyboardMarkup(
            [[
            InlineKeyboardButton("About 🤖", callback_data="about"),
            InlineKeyboardButton("Close 🔐", callback_data="close")
            ]]
         )

        await query.message.edit_text(
            Script.HELP_MSG,
            reply_markup=keyboard,
            disable_web_page_preview=True
        )
        return

    elif query.data == "about":
        await query.answer()
        keyboard = InlineKeyboardMarkup(
            [[
            InlineKeyboardButton("🤔 How To Use", callback_data="help"),
            InlineKeyboardButton("Close 🔐", callback_data="close")
            ]]
         )

        await query.message.edit_text(
            Script.ABOUT_MSG,
            reply_markup=keyboard,
            disable_web_page_preview=True
        )
        return

    elif query.data == "close_data":
        await query.message.delete()

        
    elif "cancel_e" in update.data:
        await update.message.delete()
        await cancel_extract(bot, update.message)
