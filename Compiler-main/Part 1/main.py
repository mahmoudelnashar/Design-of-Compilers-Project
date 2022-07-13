import tkinter as tk
import Regex as r


class CanvasDemo:

    def __init__(self):
        window = tk.Tk()
        window.title("Tokenizer")
        # set the window dimensions
        window.geometry("1200x750")
        window.configure(bg='grey15')
        tk.Label(window, bg='grey15', text="DFA", fg='yellow', font='times 18 bold').grid(row=0, column=0)

        self.currentState = "q0"
        self.firstTime = True
        self.inputList = []

        # ---------------------------------- Transition Functions--------------------------------
        def q0toq8(text):
            self.currentState = "q8"
            # update state diagram
            self.canvas.itemconfig(q0, fill="Blue2")
            self.canvas.itemconfig(q8, fill="Green4")
            # update token list
            addLOVToLists(text)
            # update state history list
            tk.Label(self.frame3, bg='grey15', text="        ", fg='white').pack()
            tk.Label(self.frame3, bg='grey15', text="Q0 -> Q8", fg='white').pack()

        def q7toq8(text):
            self.currentState = "q8"
            # update state diagram
            self.canvas.itemconfig(q7, fill="Blue2")
            self.canvas.itemconfig(q8, fill="Green4")
            # update token list
            addLOVToLists(text)
            # update state history list
            tk.Label(self.frame3, bg='grey15', text="        ", fg='white').pack()
            tk.Label(self.frame3, bg='grey15', text="Q7 -> Q8", fg='white').pack()

        def q5toq4(text):
            self.currentState = "q4"
            # update state diagram
            self.canvas.itemconfig(q5, fill="Blue2")
            self.canvas.itemconfig(q4, fill="Green4")
            # update token list
            addLOVToLists(text)
            # update state history list
            tk.Label(self.frame3, bg='grey15', text="        ", fg='white').pack()
            tk.Label(self.frame3, bg='grey15', text="Q5 -> Q4", fg='white').pack()

        def q3toq4(text):
            self.currentState = "q4"
            # update state diagram
            self.canvas.itemconfig(q3, fill="Blue2")
            self.canvas.itemconfig(q4, fill="Green4")
            # update token list
            if ord(text[0]) == ord('!'):
                addLOVToLists(text)
                tk.Label(self.frame3, bg='grey15', text="        ", fg='white').pack()
            else:
                addCVToLists(text)
            # update state history list
            tk.Label(self.frame3, bg='grey15', text="Q3 -> Q4", fg='white').pack()

        def q0toq1(text):
            self.currentState = "q1"
            # update state diagram
            self.canvas.itemconfig(q0, fill="Blue2")
            self.canvas.itemconfig(q1, fill="Green4")
            # update token list
            addCVToLists(text)
            # update state history list
            tk.Label(self.frame3, bg='grey15', text="Q0 -> Q1", fg='white').pack()

        def q2toq4(text):
            self.currentState = "q4"
            # update state diagram
            self.canvas.itemconfig(q2, fill="Blue2")
            self.canvas.itemconfig(q4, fill="Green4")
            # update token list
            addCVToLists(text)
            # update state history list
            tk.Label(self.frame3, bg='grey15', text="Q2 -> Q4", fg='white').pack()

        def q7toq6(text):
            self.currentState = "q6"
            # update state diagram
            self.canvas.itemconfig(q7, fill="Blue2")
            self.canvas.itemconfig(q6, fill="Green4")
            # update token list
            addCVToLists(text)
            # update state history list
            tk.Label(self.frame3, bg='grey15', text="Q7 -> Q6", fg='white').pack()

        def q5toq6(text):
            self.currentState = "q6"
            # update state diagram
            self.canvas.itemconfig(q5, fill="Blue2")
            self.canvas.itemconfig(q6, fill="Green4")
            # update token list
            addCVToLists(text)
            # update state history list
            tk.Label(self.frame3, bg='grey15', text="Q5 -> Q6", fg='white').pack()

        def q6toq2(text):
            self.currentState = "q2"
            # update state diagram
            self.canvas.itemconfig(q6, fill="Blue2")
            self.canvas.itemconfig(q2, fill="Green4")
            # update token list
            addComparisonToLists(text)
            # update state history list
            tk.Label(self.frame3, bg='grey15', text="Q6 -> Q2", fg='white').pack()

        def q1toq2(text):
            self.currentState = "q2"
            # update state diagram
            self.canvas.itemconfig(q1, fill="Blue2")
            self.canvas.itemconfig(q2, fill="Green4")
            # update token list
            addComparisonToLists(text)
            # update state history list
            tk.Label(self.frame3, bg='grey15', text="Q1 -> Q2", fg='white').pack()

        def q1toq3(text):
            self.currentState = "q3"
            # update state diagram
            self.canvas.itemconfig(q1, fill="Blue2")
            self.canvas.itemconfig(q3, fill="Green4")
            # update token list
            addLogicalToLists(text)
            # update state history list
            tk.Label(self.frame3, bg='grey15', text="Q1 -> Q3", fg='white').pack()

        def q4toq5(text):
            self.currentState = "q5"
            # update state diagram
            self.canvas.itemconfig(q4, fill="Blue2")
            self.canvas.itemconfig(q5, fill="Green4")
            # update token list
            addLogicalToLists(text)
            # update state history list
            tk.Label(self.frame3, bg='grey15', text="Q4 -> Q5", fg='white').pack()

        def q6toq5(text):
            self.currentState = "q5"
            # update state diagram
            self.canvas.itemconfig(q6, fill="Blue2")
            self.canvas.itemconfig(q5, fill="Green4")
            # update token list
            addLogicalToLists(text)
            # update state history list
            tk.Label(self.frame3, bg='grey15', text="Q6 -> Q5", fg='white').pack()

        def q8toq7(text):
            self.currentState = "q7"
            # update state diagram
            self.canvas.itemconfig(q8, fill="Blue2")
            self.canvas.itemconfig(q7, fill="Green4")
            # update token list
            addLogicalToLists(text)
            # update state history list
            tk.Label(self.frame3, bg='grey15', text="Q8 -> Q7", fg='white').pack()

        def q0todead(text):
            self.currentState = "dead"
            # update state diagram
            self.canvas.itemconfig(q0, fill="Blue2")
            self.canvas.itemconfig(dead, fill="Green4")
            # update token list
            if r.isComparison(text):
                addComparisonToLists(text)
            elif r.isLogical(text):
                addLogicalToLists(text)
            else:
                addTrashToLists(text)
            # update state history list
            tk.Label(self.frame3, bg='grey15', text="Q0 -> Dead", fg='white').pack()

        def q1todead(text):
            self.currentState = "dead"
            # update state diagram
            self.canvas.itemconfig(q1, fill="Blue2")
            self.canvas.itemconfig(dead, fill="Green4")
            # update token list
            if r.isLOV(text):
                addLOVToLists(text)
                tk.Label(self.frame3, bg='grey15', text="        ", fg='white').pack()
            elif r.isCV(text):
                addCVToLists(text)
            else:
                addTrashToLists(text)
            # update state history list
            tk.Label(self.frame3, bg='grey15', text="Q1 -> Dead", fg='white').pack()

        def q2todead(text):
            self.currentState = "dead"
            # update state diagram
            self.canvas.itemconfig(q2, fill="Blue2")
            self.canvas.itemconfig(dead, fill="Green4")
            # update token list
            if r.isLOV(text):
                addLOVToLists(text)
                tk.Label(self.frame3, bg='grey15', text="        ", fg='white').pack()
            elif r.isComparison(text):
                addComparisonToLists(text)
            elif r.isLogical(text):
                addLogicalToLists(text)
            else:
                addTrashToLists(text)
            # update state history list
            tk.Label(self.frame3, bg='grey15', text="Q2 -> Dead", fg='white').pack()

        def q3todead(text):
            self.currentState = "dead"
            # update state diagram
            self.canvas.itemconfig(q2, fill="Blue2")
            self.canvas.itemconfig(dead, fill="Green4")
            # update token list
            if r.isComparison(text):
                addComparisonToLists(text)
            elif r.isLogical(text):
                addLogicalToLists(text)
            else:
                addTrashToLists(text)
            # update state history list
            tk.Label(self.frame3, bg='grey15', text="Q3 -> Dead", fg='white').pack()

        def q4todead(text):
            self.currentState = "dead"
            # update state diagram
            self.canvas.itemconfig(q4, fill="Blue2")
            self.canvas.itemconfig(dead, fill="Green4")
            # update token list
            if r.isLOV(text):
                addLOVToLists(text)
                tk.Label(self.frame3, bg='grey15', text="        ", fg='white').pack()
            elif r.isCV(text):
                addCVToLists(text)
            elif r.isComparison(text):
                addComparisonToLists(text)
            else:
                addTrashToLists(text)
            # update state history list
            tk.Label(self.frame3, bg='grey15', text="Q4 -> Dead", fg='white').pack()

        def q5todead(text):
            self.currentState = "dead"
            # update state diagram
            self.canvas.itemconfig(q5, fill="Blue2")
            self.canvas.itemconfig(dead, fill="Green4")
            # update token list
            if r.isComparison(text):
                addComparisonToLists(text)
            elif r.isLogical(text):
                addLogicalToLists(text)
            else:
                addTrashToLists(text)
            # update state history list
            tk.Label(self.frame3, bg='grey15', text="Q5 -> Dead", fg='white').pack()

        def q6todead(text):
            self.currentState = "dead"
            # update state diagram
            self.canvas.itemconfig(q6, fill="Blue2")
            self.canvas.itemconfig(dead, fill="Green4")
            # update token list
            if r.isLOV(text):
                addLOVToLists(text)
                tk.Label(self.frame3, bg='grey15', text="        ", fg='white').pack()
            elif r.isCV(text):
                addCVToLists(text)
            else:
                addTrashToLists(text)
            # update state history list
            tk.Label(self.frame3, bg='grey15', text="Q6 -> Dead", fg='white').pack()

        def q7todead(text):
            self.currentState = "dead"
            # update state diagram
            self.canvas.itemconfig(q7, fill="Blue2")
            self.canvas.itemconfig(dead, fill="Green4")
            # update token list
            if r.isComparison(text):
                addComparisonToLists(text)
            elif r.isLogical(text):
                addLogicalToLists(text)
            else:
                addTrashToLists(text)
            # update state history list
            tk.Label(self.frame3, bg='grey15', text="Q7 -> Dead", fg='white').pack()

        def q8todead(text):
            self.currentState = "dead"
            # update state diagram
            self.canvas.itemconfig(q8, fill="Blue2")
            self.canvas.itemconfig(dead, fill="Green4")
            # update token list
            if r.isLOV(text):
                addLOVToLists(text)
                tk.Label(self.frame3, bg='grey15', text="        ", fg='white').pack()
            elif r.isCV(text):
                addCVToLists(text)
            elif r.isComparison(text):
                addComparisonToLists(text)
            else:
                addTrashToLists(text)
            # update state history list
            tk.Label(self.frame3, bg='grey15', text="Q8 -> Dead", fg='white').pack()

        def deadtodead(text):
            self.currentState = "dead"
            # update state diagram
            self.canvas.itemconfig(dead, fill="Green4")
            # update token list
            if r.isLOV(text):
                addLOVToLists(text)
                tk.Label(self.frame3, bg='grey15', text="        ", fg='white').pack()
            elif r.isCV(text):
                addCVToLists(text)
            elif r.isComparison(text):
                addComparisonToLists(text)
            elif r.isLogical(text):
                addLogicalToLists(text)
            else:
                addTrashToLists(text)
            # update state history list
            tk.Label(self.frame3, bg='grey15', text="Dead -> Dead", fg='white').pack()

        def addLOVToLists(text):
            token1 = "< Logical , ! >"
            if r.isLetter(text[1]):
                token2 = "< ID , " + text[1:] + " >"
            else:
                token2 = "< Number , " + text[1:] + " >"
            tk.Label(self.frame2, bg='grey15', text=token1, fg='white').pack()
            tk.Label(self.frame2, bg='grey15', text=token2, fg='white').pack()

        def addCVToLists(text):
            if r.isLetter(text[0]):
                token2 = "< ID , " + text + " >"
            else:
                token2 = "<Number , " + text + " >"
            tk.Label(self.frame2, bg='grey15', text=token2, fg='white').pack()

        def addLogicalToLists(text):
            token2 = "< Logical , " + text + " >"
            tk.Label(self.frame2, bg='grey15', text=token2, fg='white').pack()

        def addComparisonToLists(text):
            token2 = "< Comparison , " + text + " >"
            tk.Label(self.frame2, bg='grey15', text=token2, fg='white').pack()

        def addTrashToLists(text):
            token2 = "< Trash , " + text + " >"
            tk.Label(self.frame2, bg='grey15', text=token2, fg='white').pack()

        def transition():

            # First timecheck and reading from the user
            if self.firstTime:
                self.inputList = [str(e) for e in self.input_Text.get().split()]
                self.firstTime = False
                self.input_Text.configure(state='disabled')
            #  for e in self.inputList:
            #     e = e.strip()

            text_in = self.inputList[0]

            if self.currentState == "q0":
                if r.isCV(text_in):
                    q0toq1(text_in)
                elif r.isLOV(text_in):
                    q0toq8(text_in)
                else:
                    q0todead(text_in)
            elif self.currentState == "q1":
                if r.isComparison(text_in):
                    q1toq2(text_in)
                elif r.isLogical(text_in):
                    q1toq3(text_in)
                else:
                    q1todead(text_in)
            elif self.currentState == "q2":
                if r.isCV(text_in):
                    q2toq4(text_in)
                else:
                    q2todead(text_in)
            elif self.currentState == "q3":
                if r.isLOV(text_in) or r.isCV(text_in):
                    q3toq4(text_in)
                else:
                    q3todead(text_in)
            elif self.currentState == "q4":
                if r.isLogical(text_in):
                    q4toq5(text_in)
                else:
                    q4todead(text_in)
            elif self.currentState == "q5":
                if r.isLOV(text_in):
                    q5toq4(text_in)
                elif r.isCV(text_in):
                    q5toq6(text_in)
                else:
                    q5todead(text_in)
            elif self.currentState == "q6":
                if r.isComparison(text_in):
                    q6toq2(text_in)
                elif r.isLogical(text_in):
                    q6toq5(text_in)
                else:
                    q6todead(text_in)
            elif self.currentState == "q7":
                if r.isLOV(text_in):
                    q7toq8(text_in)
                elif r.isCV(text_in):
                    q7toq6(text_in)
                else:
                    q7todead(text_in)
            elif self.currentState == "q8":
                if r.isLogical(text_in):
                    q8toq7(text_in)
                else:
                    q8todead(text_in)
            elif self.currentState == "dead":
                deadtodead(text_in)

            del (self.inputList[0])
            updateStatus()

            # List is empty
            if len(self.inputList) == 0:
                self.next_Button.configure(state='disabled')
                self.finish_Button.configure(state='disabled')

        def transitionAll():
            transition()
            while len(self.inputList) != 0:
                transition()

        def updateStatus():
            if self.currentState == "q4" or self.currentState == "q6" or self.currentState == "q8":
                self.state_Label.configure(text="Accepted                 ", fg="Green", font="Times 15 ")
            else:
                self.state_Label.configure(text="Rejected                 ", fg="Red", font="Times 15 ")

        def clearAll():
            for child in self.frame2.winfo_children():
                child.destroy()
            tk.Label(self.frame2, bg='grey15', text="Token List  ", fg='yellow',
                     font='times 18 bold').pack()
            for child2 in self.frame3.winfo_children():
                child2.destroy()
            tk.Label(self.frame3, bg='grey15', text="State History", fg='yellow',
                     font='times 18 bold').pack()

            self.currentState = "q0"
            self.firstTime = True
            self.inputList = []
            self.next_Button.configure(state='active')
            self.finish_Button.configure(state='active')
            self.input_Text.configure(state='normal')
            self.input_Text.delete(0, tk.END)
            # reset state diagram
            self.canvas.itemconfig(q0, fill="Green4")
            self.canvas.itemconfig(q1, fill="blue2")
            self.canvas.itemconfig(q2, fill="blue2")
            self.canvas.itemconfig(q3, fill="blue2")
            self.canvas.itemconfig(q4, fill="blue2")
            self.canvas.itemconfig(q5, fill="blue2")
            self.canvas.itemconfig(q6, fill="blue2")
            self.canvas.itemconfig(q7, fill="blue2")
            self.canvas.itemconfig(q8, fill="blue2")
            self.canvas.itemconfig(dead, fill="red2")

            self.state_Label.configure(bg='grey15', text="Rejected                 ", fg="red")

        # -------------------------------CANVAS------------------------------

        # create and place a canvas in the window
        self.x1 = 200
        self.x2 = 200
        self.x3 = 200
        self.xoffset = 30
        self.y1 = 200
        self.y2 = 200
        self.y3 = 50
        self.y4 = 50
        self.yoffset = 10
        self.canvas = tk.Canvas(window, width=self.x1 + self.x2 + self.x3 + 150
                                , height=self.y1 + self.y2 + self.y3 + self.y4 + 100,
                                bg="grey17", highlightthickness=2, highlightbackground="grey20")

        #       *****   States  *****
        # Q0
        self.q0x = self.xoffset
        self.q0y = self.yoffset + self.y1 + self.y2 + self.y3
        q0 = self.canvas.create_oval(self.q0x, self.q0y, self.q0x + 50, self.q0y + 50, tags="q0")
        self.canvas.create_text(self.q0x + 25, self.q0y + 25, text="Q0", fill="white")
        # to change the colour of the item
        self.canvas.itemconfig(q0, fill="Green4")

        # Q1
        self.q1x = self.xoffset + self.x1
        self.q1y = self.yoffset + self.y1 + self.y2 + self.y3
        q1 = self.canvas.create_oval(self.q1x, self.q1y, self.q1x + 50, self.q1y + 50, tags="q1")
        self.canvas.create_text(self.q1x + 25, self.q1y + 25, text="Q1", fill="white")
        self.canvas.itemconfig(q1, fill="blue2")

        # Q2
        self.q2x = self.xoffset + self.x1 + self.x2
        self.q2y = self.yoffset + self.y1 + self.y2
        q2 = self.canvas.create_oval(self.q2x, self.q2y, self.q2x + 50, self.q2y + 50, tags="q2")
        self.canvas.create_text(self.q2x + 25, self.q2y + 25, text="Q2", fill="white")
        self.canvas.itemconfig(q2, fill="blue2")

        # Q3
        self.q3x = self.xoffset + self.x1 + self.x2
        self.q3y = self.yoffset + self.y1 + self.y2 + self.y3 + self.y4
        q3 = self.canvas.create_oval(self.q3x, self.q3y, self.q3x + 50, self.q3y + 50, tags="q3")
        self.canvas.create_text(self.q3x + 25, self.q3y + 25, text="Q3", fill="white")
        self.canvas.itemconfig(q3, fill="blue2")

        # Q4
        self.q4x = self.xoffset + self.x1 + self.x2 + self.x3
        self.q4y = self.yoffset + self.y1 + self.y2 + self.y3
        q4 = self.canvas.create_oval(self.q4x, self.q4y, self.q4x + 50, self.q4y + 50, tags="q4")
        q42 = self.canvas.create_oval(self.q4x - 5, self.q4y - 5, self.q4x + 55, self.q4y + 55, tags="q42", width='1.5', outline='blue2')
        self.canvas.create_text(self.q4x + 25, self.q4y + 25, text="Q4", fill="white")
        self.canvas.itemconfig(q4, fill="blue2")

        # Q5
        self.q5x = self.xoffset + self.x1 + self.x2 + self.x3
        self.q5y = self.yoffset + self.y1
        q5 = self.canvas.create_oval(self.q5x, self.q5y, self.q5x + 50, self.q5y + 50, tags="q5")
        self.canvas.create_text(self.q5x + 25, self.q5y + 25, text="Q5", fill="white")
        self.canvas.itemconfig(q5, fill="blue2")

        # Q6
        self.q6x = self.xoffset + self.x1 + self.x2
        self.q6y = self.yoffset + self.y1
        q6 = self.canvas.create_oval(self.q6x, self.q6y, self.q6x + 50, self.q6y + 50, tags="q6")
        q62 = self.canvas.create_oval(self.q6x - 5, self.q6y - 5, self.q6x + 55, self.q6y + 55, tags="q62", width='1.5', outline='blue2')
        self.canvas.create_text(self.q6x + 25, self.q6y + 25, text="Q6", fill="white")
        self.canvas.itemconfig(q6, fill="blue2")

        # Q7
        self.q7x = self.xoffset + self.x1 + self.x2
        self.q7y = self.yoffset
        q7 = self.canvas.create_oval(self.q7x, self.q7y, self.q7x + 50, self.q7y + 50, tags="q7")
        self.canvas.create_text(self.q7x + 25, self.q7y + 25, text="Q7", fill="white")
        self.canvas.itemconfig(q7, fill="blue2")

        # Q8
        self.q8x = self.xoffset + self.x1
        self.q8y = self.yoffset + self.y1
        q8 = self.canvas.create_oval(self.q8x, self.q8y, self.q8x + 50, self.q8y + 50, tags="q8")
        q82 = self.canvas.create_oval(self.q8x - 5, self.q8y - 5, self.q8x + 55, self.q8y + 55, tags="q82", width='1.5', outline='blue2')
        self.canvas.create_text(self.q8x + 25, self.q8y + 25, text="Q8", fill="white")
        self.canvas.itemconfig(q8, fill="blue2")

        # Dead state
        self.deadx = self.xoffset + self.x1 + self.x2 + self.x3
        self.deady = self.yoffset
        dead = self.canvas.create_oval(self.deadx, self.deady, self.deadx + 50, self.deady + 50, tags="dead")
        self.canvas.create_text(self.deadx + 25, self.deady + 25, text="Dead", fill="white")
        self.canvas.itemconfig(dead, fill="red2")

        #       *****   Transitions  *****
        # Transition 0->8
        self.canvas.create_line(self.q0x + 25, self.q0y, self.q8x, self.q8y + 25 + 10, width=1.5, arrow="last",
                                activefill="black", fill='white')
        self.canvas.create_text(self.q0x + 100, self.q0y - 120, fill="white", font="Times 15 ", text="LoV", angle=50)

        # Transition 7->8
        self.canvas.create_line(self.q8x + 25 + 20, self.q8y + 10, self.q7x + 10, self.q7y + 25 + 20, width=1.5,
                                arrow="last", activefill="black", fill='white')
        self.canvas.create_text(self.q8x + 100, self.q8y - 90, fill="white", font="Times 15 ",
                                text="LoV", angle=45)

        # Transition 8->7
        self.canvas.create_line(self.q8x + 25 + 10, self.q8y, self.q7x, self.q7y + 25 + 10, width=1.5, arrow="first",
                                activefill="black", fill='white')
        self.canvas.create_text(self.q8x + 140, self.q8y - 50, fill="white", font="Times 15 ",
                                text="&& , | |", angle=45)

        # Transition 0->1
        self.canvas.create_line(self.q0x + 50, self.q0y + 25, self.q1x, self.q1y + 25, width=1.5, arrow="last",
                                activefill="black", fill='white')
        self.canvas.create_text(self.q0x + 120, self.q0y + 10, fill="white", font="Times 15 ",
                                text="CV")

        # Transition 1->2
        self.canvas.create_line(self.q1x + 50, self.q1y + 25, self.q2x, self.q2y + 25, width=1.5, arrow="last",
                                activefill="black", fill='white')
        self.canvas.create_text(self.q1x + 120, self.q1y - 25, fill="white", font="Times 15 ",
                                text="Comparison")

        # Transition 1->3
        self.canvas.create_line(self.q1x + 50, self.q1y + 25, self.q3x, self.q3y + 25, width=1.5, arrow="last",
                                activefill="black", fill='white')
        self.canvas.create_text(self.q1x + 130, self.q1y + 75, fill="white", font="Times 15 ",
                                text="&& , | |")

        # Transition 2->4
        self.canvas.create_line(self.q2x + 50, self.q2y + 25, self.q4x, self.q4y + 22, width=1.5, arrow="last",
                                activefill="black", fill='white')
        self.canvas.create_text(self.q2x + 120, self.q2y + 30, fill="white", font="Times 15 ",
                                text="CV", angle=-10)

        # Transition 3->4
        self.canvas.create_line(self.q3x + 50, self.q3y + 25, self.q4x, self.q4y + 28, width=1.5, arrow="last",
                                activefill="black", fill='white')
        self.canvas.create_text(self.q3x + 120, self.q3y + 30, fill="white", font="Times 15 ",
                                text="LoV , CV", angle=10)

        # Transition 6->5
        self.canvas.create_line(self.q6x + 50, self.q6y + 25 + 10, self.q5x, self.q5y + 25 + 10, width=1.5,
                                arrow="last", activefill="black", fill='white')
        self.canvas.create_text(self.q6x + 130, self.q6y + 50, fill="white", font="Times 15 ",
                                text="&& , | |")

        # Transition 5->6
        self.canvas.create_line(self.q6x + 50, self.q6y + 25 - 10, self.q5x, self.q5y + 25 - 10, width=1.5,
                                arrow="first", activefill="black", fill='white')
        self.canvas.create_text(self.q6x + 130, self.q6y, fill="white", font="Times 15 ",
                                text="CV")

        # Transition 7->6
        self.canvas.create_line(self.q7x + 25, self.q7y + 50, self.q6x + 25, self.q6y, width=1.5, arrow="last",
                                activefill="black", fill='white')
        self.canvas.create_text(self.q7x + 40, self.q7y + 125, fill="white", font="Times 15 ",
                                text="CV")

        # Transition 6->2
        self.canvas.create_line(self.q6x + 25, self.q6y + 50, self.q2x + 25, self.q2y, width=1.5, arrow="last",
                                activefill="black", fill='white')
        self.canvas.create_text(self.q6x + 80, self.q6y + 125, fill="white", font="Times 15 ",
                                text="Comparison")

        # Transition 4->5
        self.canvas.create_line(self.q5x + 25, self.q5y + 50, self.q4x + 25, self.q4y, width=1.5, arrow="first",
                                activefill="black", fill='white')
        self.canvas.create_text(self.q5x - 10, self.q5y + 125, fill="white", font="Times 15 ",
                                text="&& , | |")

        # Transition 5-3
        self.canvas.create_line(self.q5x + 25 + 10, self.q5y + 50, self.q4x + 25 + 10, self.q4y, width=1.5,
                                arrow="last",
                                activefill="black", fill='white')
        self.canvas.create_text(self.q5x + 100 - 25, self.q5y + 155, fill="white", font="Times 15 ",
                                text="LoV")

        # Transition 1
        self.canvas.create_line(self.q0x - 5, self.q0y - 25, self.q0x + 25, self.q0y, width=1.5, arrow="last",
                                activefill="white", fill='white')

        self.canvas.grid(row=1, column=0)

        # --------------------------FRAME1----------------------------------------
        self.frame1 = tk.Frame(window, bg='grey25', )
        self.frame1.grid(row=2, column=0)
        tk.Label(self.frame1, text="Input String:", bg='grey15', fg='orange').grid(row=0, column=0)
        self.input_Text = tk.Entry(self.frame1, width=95, bg='grey30', fg='white')
        self.input_Text.grid(row=0, column=1)
        self.reset_Button = tk.Button(self.frame1, text="Reset All", font='times 10 ', bg='grey15', fg='white',
                                      command=clearAll)
        self.reset_Button.grid(row=0, column=2)
        self.Alphabet_Button = tk.Button(self.frame1, text="Alphabet and Rules", command=click_alphabet_and_rules,
                                         font='times 10 ', bg='grey15', fg='white')
        self.Alphabet_Button.grid(row=0, column=3)

        # --------------------------FRAME2----------------------------------------
        self.frame2 = tk.Frame(window, bg='grey15', width=500, height=1000)
        self.frame2.grid(row=1, column=1, sticky="N")
        tk.Label(self.frame2, bg='grey15', text="Token List  ", fg='yellow',
                 font='times 18 bold').pack()  # ------------------------

        # --------------------------FRAME3----------------------------------------
        self.frame3 = tk.Frame(window, bg='grey15', width=100, height=1000)
        self.frame3.grid(row=1, column=2, sticky="N")
        tk.Label(self.frame3, bg='grey15', text="State History", fg='yellow',
                 font='times 18 bold').pack()  # ---------------------

        # --------------------------FRAME4----------------------------------------
        self.frame4 = tk.Frame(window, bg='grey15')
        self.frame4.grid(row=3, column=0)
        tk.Label(self.frame4, bg='grey15', text="State:", fg='white', font='times 15 ').grid(row=0, column=0)
        self.state_Label = tk.Label(self.frame4, bg='grey15', text="Rejected                 ", fg="red",font="Times 15 ")
        self.state_Label.grid(row=0, column=1)
        self.next_Button = tk.Button(self.frame4, bg='grey15', text="Next", fg='white', command=transition)
        self.next_Button.grid(row=0, column=2)
        self.finish_Button = tk.Button(self.frame4, bg='grey15', text="Finish All", fg='green', command=transitionAll)
        self.finish_Button.grid(row=0, column=3)

        window.mainloop()


def click_alphabet_and_rules():  # alphabet and rules
    alphabet_window = tk.Tk()
    alphabet_window.title("Alphabet and Rules")
    # set the window dimensions
    alphabet_window.geometry("600x400")
    alphabet_window.configure(bg='grey15')
    tk.Label(alphabet_window, bg='grey15', text="""
Alphabet Ʃ
letter=>[a – z] [A – Z]\ndigit=>[0-9]  \ncomparison=>[= , != , < , <= , > , >=]\nlogical operators=>[&& , ||, !] \n

Rules: 
number -> (-)? [digit+ |  digit* . digit+  | digit+ . digit*]
ID -> letter [letter | _ | digit]*
LOV -> ! [number | identifier]
CV -> [number | identifier]
""""", fg='yellow', font='times 18 bold').grid(row=0, column=0)


# create an instance from the GUI
CanvasDemo()
