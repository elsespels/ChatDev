import tkinter as tk
from tkinter import messagebox
from project_reviewer import ProjectReviewer
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Software Project Reviewer")
        self.geometry("400x200")
        self.project_name_label = tk.Label(self, text="Project Name:")
        self.project_name_label.pack()
        self.project_name_entry = tk.Entry(self)
        self.project_name_entry.pack()
        self.problem_label = tk.Label(self, text="Problem:")
        self.problem_label.pack()
        self.problem_entry = tk.Entry(self)
        self.problem_entry.pack()
        self.submit_button = tk.Button(self, text="Submit", command=self.submit_review)
        self.submit_button.pack()
    def submit_review(self):
        project_name = self.project_name_entry.get()
        problem = self.problem_entry.get()
        project_reviewer = ProjectReviewer()
        project_reviewer.add_project(project_name, problem)
        project_reviewer.submit_rewrite()
        self.project_name_entry.delete(0, tk.END)
        self.problem_entry.delete(0, tk.END)
        messagebox.showinfo("Success", "Review submitted successfully!")
if __name__ == "__main__":
    app = Application()
    app.mainloop()