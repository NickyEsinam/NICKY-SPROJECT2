import tkinter as tk
import pyttsx3

window = tk.Tk()
window.configure(background="pink")
window.geometry("800x100")
engine = pyttsx3.init()
gender = tk.StringVar()


def speech():
    voice = gender.get()
    sentence = entry.get()
    # print(voice)
    if voice == "female":
        female_voice = engine.getProperty('voices')[1]
        engine.setProperty('voice', female_voice.id)
        engine.say(sentence)
        engine.runAndWait()
    elif voice == "male":
        male_voice = engine.getProperty('voices')[0]
        engine.setProperty('voice', male_voice.id)
        engine.say(sentence)
        engine.runAndWait()

    # engine.say(sentence)
    # engine.runAndWait()


# label  = tk.Label(text="Hello, Tkinter")yellow
label1 = tk.Label(text="select voice type", bg="orange")
entry = tk.Entry(bg="white", width=100)

button = tk.Button(
    text="Speak", command=speech, bg="orange"

)

R1 = tk.Radiobutton(text="Male", value="male", variable=gender, fg="black",
                    bg="blue",
                    )
R2 = tk.Radiobutton(text="Female", value="female", variable=gender, fg="black",
                    bg="yellow",
                    )

entry.grid(row=1, column=0, padx=5, pady=5)
button.grid(row=1, column=1, padx=5, pady=5)
label1.grid(row=2, column=0)
R1.grid(row=2, column=1)
R2.grid(row=2, column=2)
gender.set(None)

window.mainloop()
