from gtts import gTTS
import pygame


# The text and language in which we want to convert to audio
def text_sound_file(_text, _lang):
    mytext = _text
    language = _lang
    myobj = gTTS(text=mytext,
                 lang=language,
                 slow=False)
    file_dir = "audio/{}.mp3".format(mytext)
    myobj.save(file_dir)
    play(file_dir)


# Playing the converted file
def play(dir):
    pygame.init()
    pygame.display.set_mode((200, 100))
    pygame.mixer.music.load(dir)
    pygame.mixer.music.play(0)

    clock = pygame.time.Clock()
    clock.tick(10)
    while pygame.mixer.music.get_busy():
        pygame.event.poll()
        clock.tick(10)

