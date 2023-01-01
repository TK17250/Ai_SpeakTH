import pyttsx3 as tx

engine = tx.init()

TH_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_THAI"
engine.setProperty("voice", TH_voice_id)

engine.say("ผมคือ หุ่นยนต์ พูดภาษาไทยได้ครับ")
engine.runAndWait()