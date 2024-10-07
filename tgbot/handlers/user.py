from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from loader import bot
from tgbot.keyboards.inline import keyboard_start, keyboard_help

user_router = Router()


@user_router.message(Command('start'))
async def user_start(message: Message):
    await message.answer('မင်္ဂလာပါ.....

💥SkyLinkFreeVPN မှ ကြိုဆိုပါတယ်နော် ။

💥ကြိုက်နှစ်သက်ရာ Key ကို Copy ကူးပြီး  <a href="https://play.google.com/store/apps/details?id=dev.hexasoftware.v2box&pcampaignid=web_share">v2box VPN Software</a> ထဲထည့်သုံးပါ ။\n\n'
                         '💥Outline Software Download - <a href="https://play.google.com/store/apps/details?id=org.outline.android.client&pcampaignid=web_share">ဒီမှာလုပ်ပါ</a>\n',
                         reply_markup=keyboard_start(), disable_web_page_preview=True)


@user_router.message(Command('help'))
async def help_handler(message: Message):
    await message.answer(f'Бот предоставляет доступ к VPN на базе '
                         f'<a href="https://github.com/XTLS/Xray-core">Xray-core</a> и созданный с использованием Python и ReactJS.',
                         reply_markup=keyboard_help(), disable_web_page_preview=True)


@user_router.callback_query(F.data == 'help')
async def help_callback_handler(callback_query: CallbackQuery):
    await callback_query.answer()
    await bot.send_message(callback_query.from_user.id,
                           f'Бот предоставляет доступ к VPN на базе '
                           f'<a href="https://github.com/XTLS/Xray-core">Xray-core</a> и созданный с использованием Python и ReactJS.',
                           reply_markup=keyboard_help(), disable_web_page_preview=True)
