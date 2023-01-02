import pyttsx3 as tx

engine = tx.init()

TH_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_THAI" # เพิ่มเสียงภาษาไทย
engine.setProperty("voice", TH_voice_id) # ตั้งให้เป็นเสียงภาษาไทย

engine.say("ผมคือ หุ่นยนต์ พูดภาษาไทยได้ครับ")
engine.runAndWait() # รอให้พูดจบ