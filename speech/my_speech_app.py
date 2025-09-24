import speech_recognition as sr
import tkinter as tk
import threading

def listen_and_display():
    recognizer = sr.Recognizer()
    with sr.Microphone() as mic:
        label_status.config(text="Listening...")
        recognizer.adjust_for_ambient_noise(mic, duration=0.2)
        try:
            audio = recognizer.listen(mic, timeout=5)
            text = recognizer.recognize_google(audio)
            text = text.lower()
            text_box.delete("1.0", tk.END)
            text_box.insert(tk.END, text)
            label_status.config(text="Success!")
        except sr.UnknownValueError:
            label_status.config(text="Could not understand")
        except Exception as e:
            label_status.config(text=str(e))

def start_listening():
    threading.Thread(target=listen_and_display, daemon=True).start()

# Tkinter setup
root = tk.Tk()
root.title("Speech Recognition GUI")
root.geometry("400x200")

label_status = tk.Label(root, text="Press Start to listen", fg="blue")
label_status.pack(pady=10)

btn_start = tk.Button(root, text="Start Listening", command=start_listening)
btn_start.pack(pady=5)

text_box = tk.Text(root, height=4, width=40)
text_box.pack(pady=10)

root.mainloop()