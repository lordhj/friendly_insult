from tkinter import *
from insult_generator import GENERATOR

class INTERFACE():

    def __init__(self, insult_text: GENERATOR):
        self.insult = insult_text
        self.window = Tk()
        self.window.title("Friendly Abuse")

        self.canvas = Canvas(width=153, height=153)
        self.logo_img = PhotoImage(file="laugh_icon.png")
        self.canvas.create_image(77, 77, image=self.logo_img)
        self.canvas.grid(row=0, column=0)
        self.msg_canvas = Canvas(width=220, height=156)
        self.msg_img = PhotoImage(file="msg_body_img.png")
        self.msg_canvas.create_image(110, 77, image=self.msg_img)
        self.msg_canvas.create_text(110, 77, text=f"{self.insult}", font=("Arial", 12, "italic"), width=150, fill="blue")
        self.msg_canvas.grid(row=4, column=0, columnspan=2)

        self.title_label = Label(text="Friendly Abuse", font=("Arial", 22, "bold"), fg="blue")
        self.title_label.grid(row=0, column=1)
        self.to_label = Label(text="Recepient:", fg="blue", font=("Arial", 12, "bold"))
        self.to_label.grid(row=1, column=0)
        self.msg_label = Label(text="Message:", font=("Arial", 12, "bold"), fg="blue")
        self.msg_label.grid(row=3, column=0)

        self.recepient_input = Entry(width=55)
        self.recepient_input.grid(row=2, column=0, columnspan=2)
        self.button_img = PhotoImage(file="send_img.png")
        self.send_button = Button(image=self.button_img, highlightthickness=0, command=self.send_message)
        self.send_button.grid(row=5,column=0)

        self.window.mainloop()

    def send_message(self):
        return "True"