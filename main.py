import speech_recognition as sr
import subprocess


def main():
    r = sr.Recognizer()
    # device_index=1 in sr.Microphone() is the "Blue Snowball" microphone
    mic = sr.Microphone(device_index=1)
    with mic as source:
        r.adjust_for_ambient_noise(source)
        print("Ready to pick up voice")
        audio = r.listen(source)

    # r.recognize_google(audio) is the speech picked up and determined by google
    speech = r.recognize_google(audio, language="en-us")
    print(speech)

    # Create commands based on speech variable


if __name__ == "__main__":
    main()
