import logging

from aiogram.utils.keyboard import InlineKeyboardBuilder

logger = logging.getLogger(__name__)


def keyboard_start():
    builder = InlineKeyboardBuilder()
    builder.button(text='VPN KEY ယူမယ်', callback_data='vpn')
    builder.button(text='ဘယ်လို VPN အမျိုးအစားလဲ။', callback_data='help')
    builder.adjust(2)
    return builder.as_markup()


def keyboard_help():
    builder = InlineKeyboardBuilder()
    builder.button(text='ဆော့ဝဲ Donwload လုပ်ရန်', url='https://play.google.com/store/apps/details?id=dev.hexasoftware.v2box&pcampaignid=web_share')
    return builder.as_markup()


def keyboard_cancel():
    builder = InlineKeyboardBuilder()
    builder.button(text='❌ ထွက်မည်', callback_data='cancel')
    return builder.as_markup()
