#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Simple Bot to reply to Telegram messages. This is built on the API wrapper, see
# echobot2.py to see the same example built on the telegram.ext bot framework.
# This program is dedicated to the public domain under the CC0 license.
import logging
import telegram
from openweather import OpenWeather
from json import load
from io import open

from telegram.error import NetworkError, Unauthorized
from time import sleep

config = load(open('config.json'))

APPID = config ["APPID"]

fetcher = OpenWeather(APPID)

update_id = None

def main():
    global update_id
    # Telegram Bot Authorization Token
    bot = telegram.Bot('374097196:AAF_AzIS4GnRTYoVfPNY_fawMMxZ40NVntE')

    # get the first pending update_id, this is so we can skip over it in case
    # we get an "Unauthorized" exception.
    try:
        update_id = bot.getUpdates()[0].update_id
    except IndexError:
        update_id = None

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    while True:
        try:
            process_message(bot)
        except NetworkError:
            sleep(1)
        except Unauthorized:
            # The user has removed or blocked the bot.
            update_id += 1


def process_message (bot):
    global update_id
    # Request updates after the last update_id
    for update in bot.getUpdates(offset=update_id, timeout=10):
        # chat_id is required to reply to any message
        chat_id = update.message.chat_id
        update_id = update.update_id + 1

        if update.message:  # your bot can receive updates without messages
            # Reply to the message
            text = update.message.text

            city_id = text

            result = fetcher.fetch_weather(city_id)
            result_string = "%s: %.2f %s" % (city_id, result.temperature, result.icon)
            #print ("%s: %.2f %s" % (city["name"], result.temperature, result.icon))

            print(result_string)
            update.message.reply_text(result_string)


if __name__ == '__main__':
    main()
