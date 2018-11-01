# audio-flashcard-creator

Get a word or sentence in one language, translate it into other language and generate audio using google text-to-speech

This is a script to generate word/sentence pair in two languages to help learning. I've made it for my son to improve his english.

---

Output mp3's can be joined using ffmpg: 'ffmpg -f concat -safe o -i list_of_files_to_concatenate.txt -c copy output.mp3'

list_of_files_to_concatenate.txt format example:

>file '.\mp3\granparents_pl.mp3'

>file '.\mp3\Silence01s.mp3'

>file '.\mp3\granparents.mp3'

>file '.\mp3\Silence04s.mp3'

>file '.\mp3\grandson_pl.mp3'

>file '.\mp3\Silence01s.mp3'

>file '.\mp3\grandson.mp3'