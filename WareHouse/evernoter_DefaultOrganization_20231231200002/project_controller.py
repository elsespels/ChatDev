'''
This file contains the ProjectController class responsible for managing Evernote projects.
'''
class Project:
    def __init__(self, projects, name, description):
        self.id = len(projects) + 1
        self.name = name
        self.description = description
        self.status = 'Pending'
        self.members = []
    def assign_member(self, member_name):
        self.members.append(member_name)
    def change_status(self, status):
        self.status = status
class ProjectController:
    def __init__(self):
        self.projects = []
    def create_project(self, project_name, description):
        project = Project(self.projects, project_name, description)
        self.projects.append(project)
    def update_project(self, project_id, project_name, description):
        project = self.get_project_by_id(project_id)
        if project:
            project.name = project_name
            project.description = description
    def assign_member(self, project_id, member_name):
        project = self.get_project_by_id(project_id)
        if project:
            project.assign_member(member_name)
    def change_status(self, project_id, status):
        project = self.get_project_by_id(project_id)
        if project:
            project.change_status(status)
    def get_projects(self):
        return self.projects
    def get_project_by_id(self, project_id):
        for project in self.projects:
            if project.id == project_id:
                return project
        return None