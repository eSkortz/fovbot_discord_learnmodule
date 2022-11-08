import requests as r
import json
import time
import pandas as pd
from threading import Thread
import csv
from random import choice
import random
import colorama
from colorama import Fore, Back, Style
colorama.init()

def func_get(chat_id):
    header = {
        'authorization':'mfa.5ocW4eYwCktROQQeOiqKSv7hfvWKAGqQtg23nORQmS9Aj_1bOlF6uBXc39QlS_CfFpZjFGG-KJaUBfve5F_c'
    }
    function_get = []
    chat_id = chat_id
    s = r.Session()
    s.headers = header
    rg = s.get(f'https://discord.com/api/v9/channels/{chat_id}/messages', headers = header)
    jsn = json.loads(rg.text)
    return jsn



print(Fore.LIGHTGREEN_EX)
print('''
                               ....
                                    %
                            L
                            "F3  $r
                           $$$$.e$"  .
                           "$$$$$"   "
   (FovLearnBot)             $$$$c  /
        .                   $$$$$$$P
       ."c                      $$$
      .$c3b                  ..J$$$$$e
      4$$$$             .$$$$$$$$$$$$$$c
       $$$$b           .$$$$$$$$$$$$$$$$r
          $$$.        .$$$$$$$$$$$$$$$$$$
           $$$c      .$$$$$$$  "$$$$$$$$$r

Author: @dontevil       
*** Hello, I'm dLearn_Bot, for my work fill the files all_chat.txt
    to select chats and dataset.txt to upload the strings in database ***
''')
print(Fore.LIGHTWHITE_EX)

chat_set: list = open('all_chat.txt', 'r', encoding='utf-8').read().splitlines()
chat_num = int(input('Enter the number of chats: '))
total_write = 0

print()
print('*** Starting scanning of chats ***')
print()

while True:
    for i in range(0, chat_num):
        file_get = func_get(chat_set[i])
        if file_get != 0:
            try:
                user_id_last = file_get[0]['id']
                user_msg_last = file_get[0]['content']
                user_id_before = file_get[0]['referenced_message']['id']
                user_msg_before = file_get[0]['referenced_message']['content']
            except Exception:
                print(Fore.LIGHTRED_EX + 'some error with get')
                continue

            file_set: list = open('dataset.txt', 'r', encoding='utf-8').read().splitlines()
            string_write = f'{user_msg_before}|{user_msg_last}\n'
            string_check = f'{user_msg_before}|{user_msg_last}'

            if user_id_before != user_id_last:
                if string_check in file_set:
                    print(Fore.LIGHTRED_EX + '*** Repeating string ***')
                else:
                    file = open("dataset.txt", "a", encoding='utf-8')
                    file.write(string_write)
                    file.close()
                    total_write += 1
                print(Fore.LIGHTCYAN_EX + f'*** Recorded {total_write} messages ***')
    time.sleep(2)