import speech_recognition as sr,requests,bs4,pyttsx3,wikipedia,time

engine=pyttsx3.init()

def question():
    r = sr.Recognizer()
    print('say your question into your mic...')
    with sr.Microphone() as source:
        print('What can I do for you today?')
        audio = r.listen(source)
        r.adjust_for_ambient_noise(source, duration=1)

    try:

        text = r.recognize_google(audio)
        pass
    except sr.UnknownValueError:
        question()
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service;{0}".format(e))
    print(text)
    if text =='wait':
        time.sleep(600)
        question()
    if 'Wikipedia' in text:
        wikisearch=wikipedia.summary(text)
        engine.say(wikisearch)
        engine.runAndWait()
    if text=='what is your name':
        a='Im Ike, your personal assistant!'
        engine.say(a)
        engine.runAndWait()
        question()
    elif text=='who is the coolest person in the world':
        b='Studies say Ike Browflowski is the coolest person in the world'
        engine.say(b)
        engine.runAndWait()
        question()
    elif text=='bye':
        c='Thank you for using me.'
        engine.say(c)
        engine.runAndWait()
    else:
        url = 'https://google.com/search?q=' + text
        request_result=requests.get( url )
        soup = bs4.BeautifulSoup(request_result.text,
                                "html.parser")
        heading_object=soup.find('h3')
        for info in heading_object:
            print(info.getText())
            print("------")
            engine.say(info.getText())
            engine.runAndWait()
            question()

question()
