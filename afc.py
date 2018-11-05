# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 06:08:26 2018

@author: Tomasz Truszkowski
"""
import os
from pathlib import Path

# choose path
main_directory = Path('C:/Users/(...)/audio-flashcard-creator/')

# %%
#get the list to translate
input_text = open(main_directory / 'input.txt','r')
input_list = input_text.read().split('\n')
input_text.close

# %%
# translate  might be unstable
from googletrans import Translator

translator = Translator()
translated = translator.translate(input_list,src= 'en', dest = 'pl')

  # %%
# files for silence
wait_4_sec =  open(main_directory / "media/Silence04s.mp3",'rb').read()
wait_1_sec =  open(main_directory / "media/Silence01s.mp3",'rb').read()

# %%
# translation gTTS
from gtts import gTTS
import time

with open(main_directory /'output_mp3/wynik_zlozenie4.mp3', 'wb') as out_file:
    for translation in translated: 
        tts_from = gTTS(translation.origin, lang='en')
        time.sleep(2) #don't mess with Google ;)
        tts_to = gTTS(translation.text, lang='pl')
        #write to file
        tts_from.write_to_fp(out_file)
        out_file.write(wait_4_sec)
        tts_to.write_to_fp(out_file)
        out_file.write(wait_1_sec)
print('finished')

 