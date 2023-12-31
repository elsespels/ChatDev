import tkinter as tk
class ProjectReviewer:
    def __init__(self):
        self.projects = []
    def add_project(self, project_name, problem):
        self.projects.append({"project_name": project_name, "problem": problem})
    def submit_rewrite(self):
        # Code to submit the rewrite to the ChatDev team
        # You can replace this with the actual implementation
        # Example implementation:
        for project in self.projects:
            project_name = project["project_name"]
            problem = project["problem"]
            # Write the project name, problem, and other details to a file
            with open("/Users/marcelo/Documents/dev/chat-dev/ChatDev/WareHouse/project_reviewer_DefaultOrganization_20231226212722", "a") as file:
                file.write(f"Project Name: {project_name}\n")
                file.write(f"Problem: {problem}\n")
                file.write("\n")
        # Clear the projects list after submission
        self.projects = []