'''
This is the main file of the Evernote Project Controller web application.
'''
from flask import Flask, render_template, request, redirect
from project_controller import ProjectController
app = Flask(__name__)
project_controller = ProjectController()
@app.route('/')
def home():
    projects = project_controller.get_projects()
    return render_template('index.html', projects=projects)
@app.route('/create_project', methods=['POST'])
def create_project():
    project_name = request.form['project_name']
    description = request.form['description']
    project_controller.create_project(project_name, description)
    return redirect('/')
@app.route('/update_project', methods=['POST'])
def update_project():
    project_id = request.form['project_id']
    project_name = request.form['project_name']
    description = request.form['description']
    project_controller.update_project(project_id, project_name, description)
    return redirect('/')
@app.route('/assign_member', methods=['POST'])
def assign_member():
    project_id = request.form['project_id']
    member_name = request.form['member_name']
    project_controller.assign_member(project_id, member_name)
    return redirect('/')
@app.route('/change_status', methods=['POST'])
def change_status():
    project_id = request.form['project_id']
    status = request.form['status']
    project_controller.change_status(project_id, status)
    return redirect('/')
if __name__ == '__main__':
    app.run(debug=True)