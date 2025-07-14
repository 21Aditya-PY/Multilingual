import speech_recognition as spr
from googletrans import Translator, LANGUAGES
from gtts import gTTS
import os
import asyncio

recog = spr.Recognizer()
mic = spr.Microphone()
translator = Translator()

# Show language options
def show_language_options():
    print("\nAvailable languages:")
    for code, name in list(LANGUAGES.items()):
        print(f"[{code}]: {name}")

# Function to recognize speech
def recognize_speech(recog, source):
    try:
        recog.adjust_for_ambient_noise(source, duration=0.2)
        print("Listening...")
        audio = recog.listen(source)
        recognized_text = recog.recognize_google(audio)
        print(f"Recognized: {recognized_text}")
        return recognized_text.lower()
    except Exception as e:
        print(f"Speech recognition error: {e}")
        return None

# Async translation and speech function
async def translate_text(get_sentence, from_lang='en', to_lang='hi'):
    try:
        print(f"\nTranslating: {get_sentence}")
        translated = await translator.translate(get_sentence, src=from_lang, dest=to_lang)
        translated_text = translated.text
        print(f"Translated: {translated_text}")

        # Speak the result
        speak = gTTS(text=translated_text, lang=to_lang, slow=False)
        speak.save("captured_voice.mp3")
        os.system("start captured_voice.mp3")  # Use afplay or xdg-open for Mac/Linux
    except Exception as e:
        print(f"Translation error: {e}")

# Entry point
def main():
    print("🌐 Multilingual Voice/Text Translator")
    show_language_options()

    # Choose input mode
    mode = input("Choose input mode (voice/text): ").strip().lower()
    from_lang = input("Enter source language code (e.g., en): ").strip()
    to_lang = input("Enter target language code (e.g., hi): ").strip()

    if from_lang not in LANGUAGES or to_lang not in LANGUAGES:
        print("Invalid language codes. Please restart and choose from the list.")
        return

    print(f"\nTranslating from '{LANGUAGES[from_lang]}' to '{LANGUAGES[to_lang]}'. Say or type 'stop' to exit.\n")

    if mode == "text":
        while True:
            text = input("Enter a sentence to translate: ").strip()
            if text.lower() == "stop":
                print("Exiting...")
                break
            asyncio.run(translate_text(text, from_lang, to_lang))

    elif mode == "voice":
        with mic as source:
            while True:
                sentence = recognize_speech(recog, source)
                if sentence:
                    if "stop" in sentence:
                        print("Exiting...")
                        break
                    asyncio.run(translate_text(sentence, from_lang, to_lang))
                else:
                    print("Try again...")

    else:
        print("Invalid mode selected.")

# Run the app
if __name__ == "__main__":
    main()
