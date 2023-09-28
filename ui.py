from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#D5B4B4"
CANVAS_BG = "#867070"
FONT_TYPE = "Times"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):  # quiz_brain is of datatype QuizBrain
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("QUIZZZ")
        self.window.config(padx=80, pady=80, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score : {self.quiz.score}", font=(FONT_TYPE, 70, "bold"), bg=THEME_COLOR,
                                 fg="white")
        self.score_label.place(x=120, y=-90)

        self.canvas = Canvas(width=500, height=500, bg=CANVAS_BG, highlightthickness=0)
        self.canvas.create_text(255, 50, text="TRUE or FALSE", fill=THEME_COLOR, font=(FONT_TYPE, 30, "bold"))
        self.ques_text = self.canvas.create_text(250,
                                                 250,
                                                 text="Question",
                                                 fill="white",
                                                 font=(FONT_TYPE, 25, "italic"),
                                                 width=480)
        self.canvas.grid(column=0, row=0, columnspan=2, pady=20)

        self.true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.true_image, command=self.true_clicked)
        self.true_button.grid(column=0, row=1)

        self.false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_image, command=self.false_clicked)
        self.false_button.grid(column=1, row=1)

        self.get_question()

        self.window.mainloop()

    def get_question(self):
        self.canvas.config(bg=CANVAS_BG)
        self.score_label.config(text=f"Score : {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.ques_text, text=q_text)
        else:
            self.canvas.itemconfig(self.ques_text,
                                   text=f"You have reached the end of the quiz.\n"
                                        f"Your final score is {self.quiz.score}/10")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_clicked(self):
        is_correct = self.quiz.check_answer("true")
        self.check(is_correct)

    def false_clicked(self):
        is_correct = self.quiz.check_answer("false")
        self.check(is_correct)

    def check(self, is_correct):
        if is_correct:
            self.canvas.config(bg="#708160")
        else:
            self.canvas.config(bg="#FF6464")
        self.window.after(1000, func=self.get_question)
