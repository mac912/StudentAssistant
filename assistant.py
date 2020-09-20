#This is the personal assistant especially designed for the
#students to learn and improve their knowledge

from gtts import gTTS
import wikipedia
import wolframalpha
import subprocess
import os

while True:
    inputvalue = input("Q: ")

    try:
        #wolframalpha
        app_id = "GGXP76-9YKR56VHA7"
        client = wolframalpha.Client(app_id)
        res = client.query(inputvalue)
        answer = next(res.results).text
        print (answer)
        mytext = answer
        language = 'en'

        myobj = gTTS(text=mytext, lang=language, slow=False)

        myobj.save("welcome.mp3")

        os.system("mpg321 welcome.mp3")

    except:
        #wikipedia
        print(wikipedia.summary(inputvalue))
        a = wikipedia.summary(inputvalue)
        language = 'en'
        myobj = gTTS(text=a, lang=language, slow=False)
        myobj.save("welcome1.mp3")
        os.system("mpg321 welcome1.mp3")
