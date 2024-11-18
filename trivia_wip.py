import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import webbrowser
import pandas as pd
from datetime import datetime
from pathlib import Path
from ttkthemes import ThemedTk  # Ensure to install with `pip install ttkthemes`
from filepath import filepath

# question list
questions = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']

test_answers = []

# Global variable to track the inactivity timer
timeout_timer = None
timeout_seconds = 5 * 60  # 5 minutes (in seconds)

window_width = 500
window_height = 500

def reset_inactivity_timer(event=None):
    global timeout_timer
    if timeout_timer is not None:
        root.after_cancel(timeout_timer)
    timeout_timer = root.after(timeout_seconds * 1000, timeout_function)

def timeout_function():
    print("No user input detected for 5 minutes. Closing application.")
    root.destroy()

# Initialize a DataFrame to store responses
responses_df = pd.DataFrame(columns=['Name', 'Question 1 Answer', 'Question 2 Answer', 'Question 3 Answer', 'Question 4 Answer', 'Question 5 Answer',
                                     'Question 6 Answer', 'Question 7 Answer', 'Question 8 Answer', 'Question 9 Answer',
                                     'Question 10 Answer', 'Question 11 Answer', 'Question 12 Answer'])

class TriviaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Trivia App")
        self.root.geometry(f'{window_width}x{window_height}')
        self.root.set_theme("breeze")  # Apply a modern theme from ttkthemes

        # Create a frame for the main content
        self.frame = ttk.Frame(self.root, padding=20)
        self.frame.pack(fill="both", expand=True)

        # Show the home page on start
        self.show_home_page()

    def clear_frame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

    def show_home_page(self):
        self.clear_frame()

        # Welcome Label
        label = ttk.Label(self.frame, text="Welcome to the Trivia App!", font=("Helvetica", 16, "bold"), foreground="#333")
        label.pack(pady=20)

        # Buttons with modern styling
        quit_button = ttk.Button(self.frame, text="Quit", style="TButton", command=self.quit_app)
        quit_button.pack(pady=5)

        view_button = ttk.Button(self.frame, text="View Standings", style="TButton", command=self.view_standings)
        view_button.pack(pady=5)

        begin_button = ttk.Button(self.frame, text="Begin Trivia", style="TButton", command=self.begin_trivia)
        begin_button.pack(pady=5)

    def quit_app(self):
        self.root.destroy()

    def view_standings(self):
        webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

    def begin_trivia(self):
        self.show_name_selection()

    def show_name_selection(self):
        self.clear_frame()

        label = ttk.Label(self.frame, text="Select Your Name", font=("Helvetica", 14, "bold"), foreground="#333")
        label.pack(pady=10)

        names = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank', 'Grace', 'Hannah', 'Ivy', 'Jack']
        
        # Listbox with scrollbar for selecting names
        listbox_frame = ttk.Frame(self.frame)
        listbox_frame.pack(pady=5)
        name_listbox = tk.Listbox(listbox_frame, font=("Helvetica", 10), selectmode="single", height=6)
        scrollbar = ttk.Scrollbar(listbox_frame, orient="vertical", command=name_listbox.yview)
        name_listbox.config(yscrollcommand=scrollbar.set)

        for name in names:
            name_listbox.insert(tk.END, name)

        name_listbox.pack(side="left", fill="y")
        scrollbar.pack(side="right", fill="y")

        def start_trivia():
            selected_name_index = name_listbox.curselection()
            if selected_name_index:
                self.name = name_listbox.get(selected_name_index)
                self.show_question_1()
            else:
                messagebox.showwarning("Selection Error", "Please select a name.")

        next_button = ttk.Button(self.frame, text="Next", command=start_trivia, style="TButton")
        next_button.pack(pady=10)

        back_button = ttk.Button(self.frame, text="Back", command=self.show_home_page, style="TButton")
        back_button.pack(pady=10)
    
    # Question 1
    def show_question_1(self):
        self.clear_frame()

        question_label = ttk.Label(self.frame, text="Are Apples Blue?", font=("Helvetica", 14))
        question_label.pack(pady=10)

        answer_var = tk.StringVar()
        yes_button = ttk.Radiobutton(self.frame, text="Yes", variable=answer_var, value="Yes")
        no_button = ttk.Radiobutton(self.frame, text="No", variable=answer_var, value="No")
        yes_button.pack()
        no_button.pack()

        def next_question_2():
            if answer_var.get():
                self.question_1_answer = answer_var.get()
                self.show_question_2()
            else:
                messagebox.showwarning("Answer Error", "Please select an answer.")

        next_button = ttk.Button(self.frame, text="Next", command=next_question_2, style="TButton")
        next_button.pack(pady=10)

    # Question 2
    def show_question_2(self):
        self.clear_frame()

        question_label = ttk.Label(self.frame, text="Is the Squirrel Whistling?", font=("Helvetica", 14))
        question_label.pack(pady=10)

        answer_var = tk.StringVar()
        yes_button = ttk.Radiobutton(self.frame, text="Yes", variable=answer_var, value="Yes")
        no_button = ttk.Radiobutton(self.frame, text="No", variable=answer_var, value="No")
        yes_button.pack()
        no_button.pack()

        def next_question_3():
            if answer_var.get():
                self.question_2_answer = answer_var.get()
                self.show_question_3()
            else:
                messagebox.showwarning("Answer Error", "Please select an answer.")

        next_button = ttk.Button(self.frame, text="Next", command=next_question_3, style="TButton")
        next_button.pack(pady=10)

    # Question 3
    def show_question_3(self):
        self.clear_frame()

        question_label = ttk.Label(self.frame, text="Why does the Willow Lean Back?", font=("Helvetica", 14))
        question_label.pack(pady=10)

        answer_var = tk.StringVar()
        yes_button = ttk.Radiobutton(self.frame, text="Yes", variable=answer_var, value="Yes")
        no_button = ttk.Radiobutton(self.frame, text="No", variable=answer_var, value="No")
        yes_button.pack()
        no_button.pack()

        def next_question_4():
            if answer_var.get():
                self.question_3_answer = answer_var.get()
                self.show_question_4()
            else:
                messagebox.showwarning("Answer Error", "Please select an answer.")

        next_button = ttk.Button(self.frame, text="Next", command=next_question_4, style="TButton")
        next_button.pack(pady=10)

    # Question 4
    def show_question_4(self):
        self.clear_frame()

        question_label = ttk.Label(self.frame, text="Are Peaches Green? (longer text example)", font=("Helvetica", 14), wraplength=window_width - 50)
        question_label.pack(pady=10)

        answer_var = tk.StringVar()
        yes_button = ttk.Radiobutton(self.frame, text="Yes", variable=answer_var, value="Yes")
        no_button = ttk.Radiobutton(self.frame, text="No", variable=answer_var, value="No")
        yes_button.pack()
        no_button.pack()

        def submit_answers():
            if answer_var.get():
                # Save answers
                self.question_4_answer = answer_var.get()
                responses_df.loc[len(responses_df)] = [self.name, self.question_1_answer, self.question_2_answer, self.question_3_answer, self.question_4_answer]
                responses_df['Timestamp'] = datetime.now()

                file_name = Path(file_path + f'\{self.name}_results.csv')
                if not file_name.exists():
                    responses_df.to_csv(f'{self.name}_results.csv', index=False)
                    messagebox.showinfo("Thank You", "Your responses have been recorded!")
                else:
                    messagebox.showinfo("Invalid Attempt", "You have already submitted a response for this week.")
                self.show_home_page()
            else:
                messagebox.showwarning("Answer Error", "Please select an answer.")

        submit_button = ttk.Button(self.frame, text="Submit", command=submit_answers, style="TButton")
        submit_button.pack(pady=10)

# Main execution
root = ThemedTk()
root.bind("<Key>", reset_inactivity_timer)
root.bind("<Motion>", reset_inactivity_timer)
app = TriviaApp(root)
reset_inactivity_timer()
root.mainloop()
