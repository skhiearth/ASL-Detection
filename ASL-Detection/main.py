from gtts import gTTS
import pygame

# The text and language in which we want to convert to audio
mytext = 'Hello World'
language = 'en'

myobj = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a mp3 file
myobj.save("audio/helloWorld.mp3")

# Playing the converted file
pygame.init()
pygame.display.set_mode((200, 100))
pygame.mixer.music.load("audio/helloWorld.mp3")
pygame.mixer.music.play(0)

clock = pygame.time.Clock()
clock.tick(10)
while pygame.mixer.music.get_busy():
    pygame.event.poll()
    clock.tick(10)
