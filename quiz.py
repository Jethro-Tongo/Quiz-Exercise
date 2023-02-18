
# Import the required modules.
import tkinter
import tkinter.messagebox
import json
import random

class ProgramGUI:

    data = []
    question_number = 0
    score = 0
    window = ""
    qstn_heading_lbl = ""
    qstn_lbl = ""
    difficult_label = ""
    ans_txt = ""
    btn = ""
    current_question = []
        
        
    def __init__(self):
        # This is the constructor of the class.
        # Here load data to the text file and create the interface using tkinter.  
        # pass
        self.window = tkinter.Tk()
        self.window.title('Quiz')
        self.window.geometry('700x350')
        
        self.qstn_heading_lbl =  tkinter.Label(self.window, text="",justify=tkinter.CENTER, font=("Helvetica", 16))
        self.qstn_heading_lbl.grid(row=0)
        
        self.difficult_label = tkinter.Label(self.window, text="", justify=tkinter.LEFT, font=("Helvetica", 16))
        self.difficult_label.grid(row=1) 
        
        self.qstn_lbl = tkinter.Label(self.window, text="", justify=tkinter.CENTER, font=("Helvetica", 16))
        self.qstn_lbl.grid(row=2)

        self.ans_txt = tkinter.Entry(self.window, width=10)
        self.ans_txt.grid(row=3)
  

        self.btn = tkinter.Button(self.window, text="Submit answer", command = self.check_answer,
            justify=tkinter.CENTER, font=("Helvetica", 16))
        self.btn.grid(column=1, row=3)
        self.btn.pack
        try:
            file = open('data.txt', 'r')
            try:
                self.data = json.load(file)
            except ValueError:
                tkinter.messagebox.showerror("Error", "DATA Missing/Invalid file")
                self.window.destroy()
                return  
            file.close
        except FileNotFoundError:
            tkinter.messagebox.showerror("Error", "Missing/Invalid file")
            self.window.destroy()
            return
        if len(self.data) < 5:
            tkinter.messagebox.showerror("Error", "Insufficient number of questions")
            self.window.destroy()
            return    
        
        #randomise list
        random.shuffle(self.data)
        self.current_question = self.data[0:5]
        
        self.show_question()
        self.window.mainloop()

    def show_question(self):
        self.ans_txt.select_clear()
        self.ans_txt.focus()

        heading = 'Question ' + str(self.question_number + 1) + ' of 5:'
        quest = self.current_question[self.question_number]['questions']
        
        print(int(self.current_question[self.question_number]['difficulty']))
        if int(self.current_question[self.question_number]['difficulty']) > 4:
            self.difficult_label.grid()
            self.difficult_label.configure(text = "This is a hard one - good luck!", foreground = 'blue')
        else:
            self.difficult_label.grid_remove()

        self.qstn_heading_lbl.configure(text = heading)
        self.qstn_lbl.configure(text = quest)
        # This method is responsible for displaying the current question and some other messages in the GUI.


    def check_answer(self):   
        # Check if response is correct after clicking button.
        #pass
        user_answer = self.ans_txt.get()
        correct_answers = self.current_question[self.question_number]['answers']

        if user_answer.lower() in correct_answers:
            #print current question and its number
            self.score = self.score + (self.current_question[self.question_number]['difficulty'] * 2)
            tkinter.messagebox.showinfo("Correct!", "You are correct!")
        else:
            tkinter.messagebox.showerror("Incorrect!", "Sorry that was incorrect!")
       
        self.question_number = self.question_number + 1
        if(self.question_number == 5):
            tkinter.messagebox.showinfo("Final score!", "Game Over. Final Score \n" + str(self.score) + " \nThank you for playing!")
            self.window.destroy()
        else:
            self.show_question()


# Create an object of the ProgramGUI class to begin the program.
gui = ProgramGUI()


