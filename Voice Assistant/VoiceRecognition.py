"""
Speech To Text function
"""
import webbrowser

# import requests adn json
import json
# import python-text-to-speech library
import pyttsx3
import requests
import speech_recognition as sr


# function for api requests
def yt_api_request(keyword):
    api_url = "https://youtube.googleapis.com/youtube/v3/search?part=snippet&channelType=any&eventType=none&maxResults=25&q=" + keyword + "&key=AIzaSyD-SD5t1ZnRzuUKI0JH2Wdp6LxtBzlVk6I"

    try:
        api_request = requests.get(api_url)
        requested_data = json.loads(api_request.content)

        video_id = requested_data["items"][0]["id"]["videoId"]

        yt_url = "https://www.youtube.com/watch?v=" + video_id

        return yt_url

    except Exception as e:
        print(e)


# function that welcomes the user
def welcome_note():
    # object creation
    global engine
    engine = pyttsx3.init()

    # customizing properties - volume, voice type(male/female), speed etc.

    # rate of speaking
    rate = engine.getProperty("rate")  # getting details of current speaking rate
    engine.setProperty("rate", 165)  # setting up new voice rate

    # speaking volume
    volume = engine.getProperty("volume")  # getting to know current volume level (min=0 and max=1)
    engine.setProperty("volume", 1)  # setting up volume level  between 0 and 1

    # voice - male or female
    voices = engine.getProperty("voices")  # getting details of current voice
    engine.setProperty("voice", voices[1].id)  # changing index, changes voices. 0 for male, 1 for female

    # text to be said
    engine.say("Hi!, I'm Cynthia. How can I help you")

    # run and process the voice command - without this command, speech will not be audible to us.
    engine.runAndWait()

    engine.stop()


# function that returns the converted text in english
def speech_to_text():
    recognizer = sr.Recognizer()

    # logic to convert speech to text
    with sr.Microphone() as source:
        # listen to input audio
        print("SAY SOMETHING...")
        input_audio = recognizer.listen(source)

        try:
            # to convert input audio to text
            print("CONVERTING...")
            text = recognizer.recognize_google(input_audio)

            return text

        except Exception as e:
            global engine
            print(e)
            engine.say("Couldn't recognize, please try again")
            engine.runAndWait()
            engine.stop()


# function for casual conversations with Cynthia
def casual_conv(casual_command):
    global engine
    engineCasual = engine

    if (casual_command == "It's a pleasure to assist you. See you later, bye"):
        engineCasual.say(casual_command)
        engineCasual.runAndWait()
        return "stop"

    else:
        engineCasual.say(casual_command)
        engineCasual.runAndWait()


# function for performing web based user tasks
def web_based_tasks(web_based_command, url):
    global engine
    engineWebBased = engine

    engineWebBased.say(web_based_command)
    engineWebBased.runAndWait()
    webbrowser.open(url)


# function for no results found
def no_results():
    global engine
    engineNoResults = engine

    engineNoResults.say("Oops, couldn't find results!")
    engine.runAndWait()


def process_command(command):
    command = command.lower()

    # casual conversations with Cynthia
    casual_sayings_list = ["how are you", "what about you", "how's your day"]
    for expression in casual_sayings_list:
        if expression in command:
            casual_conv("I'm doing fine, thanks. What about you?")
            break

        else:
            continue

    casual_sayings__return_list = ["fine", "good", "great", "bad", "terrible", "horrible", "worse", "worst"]
    for e in casual_sayings__return_list:
        if e in command:
            if (e == "bad") or (e == "terrible") or (e == "horrible") or (e == "worse") or (e == "worst"):
                casual_conv("I'm sorry to hear that. What can I do for you?")

            else:
                casual_conv("I'm glad that you are doing well")
            break

        else:
            continue

    cynthia_info_list = ["creator", "father", "owner", "master", "created you"]
    for expression in cynthia_info_list:
        if expression in command:
            casual_conv("Technically speaking, I was developed by Vibhashana. That makes him my creator")
            break
        else:
            continue

    what_is_cynthia_list = ["what are you", "who are you", "what can you do", "describe yourself", "capable",
                            "possible"]
    for expression in what_is_cynthia_list:
        if expression in command:
            casual_conv("I am a Personal Voice Assistant for testing purposes. I'm still under development stage")
            break

        else:
            continue

    cynthia_states_list = ["switch off", "power off", "shutdown", "shut down", "get lost"]
    for expression in cynthia_states_list:
        if expression in command:
            return casual_conv("It's a pleasure to assist you. See you later, bye")

        else:
            continue

    # web-based operations to be performed by Cynthia
    open_text = "open "
    open_list = ["google chrome", "chrome", "mozilla", "firefox", "youtube", "wikipedia"]

    for expression in open_list:
        operation_text = open_text + expression
        if operation_text in command:
            if operation_text == "open google chrome" or operation_text == "open chrome":
                web_based_tasks("Opening Google Chrome", "https://google.com")
                break

            elif operation_text == "open youtube":
                web_based_tasks("Opening YouTube", "https://www.youtube.com/")
                break

            elif operation_text == "open wikipedia":
                web_based_tasks("Opening Wikipedia", "https://www.wikipedia.org/")

        else:
            continue

    request_list = ["play", "show"]
    for expression in request_list:
        if expression in command:
            if expression == "play":
                keyword = command.replace("play", "")
                yt_url = yt_api_request(keyword)
                web_based_tasks("Playing your request in YouTube", yt_url)
                break

            else:
                pass

        else:
            continue
