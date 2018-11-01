# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 06:08:26 2018

@author: Tomasz Truszkowski
"""


# %%
#get the list to translate
input_text = open('.\input\input_text.txt','r')
input_list = input_text.read().split('\n')
input_text.close


# %%
#for tests
#input_list = input_list[:5]
#print(input_list)


# %%
# translate
from googletrans import Translator
# might be unstable

translator = Translator()
translated = translator.translate(input_list,src= 'en', dest = 'pl')


# %%
#write to translated list
translated_list=[]

for translation in translated:
    print(translation.origin, ' / ', translation.text)
    translated_list.append((translation.origin, translation.text))
        

# %%
# save to file in case verification needed
    
with open('.\output\output_text.txt','w') as translated_file:
    translated_file.write(str(translated_list))
    
    
  # %%
# translation gTTS
from gtts import gTTS

for tts_input in translated_list: 
    print(tts_input[0])
    print(tts_input[1])
    tts_from = gTTS(tts_input[0], lang='en')
    tts_from.save('.\output\\' + tts_input[0] +'.mp3')
    tts_to = gTTS(tts_input[1], lang='pl')
    tts_to.save('.\output\\' + tts_input[0] +'_pl.mp3')

    
    

    
    
    
    
    
    
    
    
    
    
    
    