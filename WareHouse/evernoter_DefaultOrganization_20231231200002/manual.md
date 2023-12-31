# Evernote Project Controller User Manual

## Introduction

The Evernote Project Controller is a web application designed to assist with the management of Evernote projects. It allows users to create, update, assign members, and change the status of projects. This user manual will guide you through the installation process and provide instructions on how to use the application.

## Installation

To install the Evernote Project Controller, follow these steps:

1. Ensure that you have Python installed on your system. If not, you can download it from the official Python website (https://www.python.org/downloads/).

2. Clone the project repository from GitHub using the following command:

   ```
   git clone https://github.com/your-username/evernote-project-controller.git
   ```

3. Navigate to the project directory:

   ```
   cd evernote-project-controller
   ```

4. Create a virtual environment to isolate the project dependencies:

   ```
   python -m venv venv
   ```

5. Activate the virtual environment:

   - For Windows:

     ```
     venv\Scripts\activate
     ```

   - For macOS and Linux:

     ```
     source venv/bin/activate
     ```

6. Install the project dependencies using pip:

   ```
   pip install -r requirements.txt
   ```

7. Run the application:

   ```
   python main.py
   ```

8. Open your web browser and navigate to http://localhost:5000 to access the Evernote Project Controller.

## Usage

### Creating a Project

To create a new project, follow these steps:

1. On the home page, click on the "Create Project" button.

2. Enter the project name and description in the provided fields.

3. Click the "Create" button to create the project.

### Updating a Project

To update an existing project, follow these steps:

1. Find the project you want to update in the project list.

2. Modify the project name or description in the corresponding input fields.

3. Click the "Update" button to save the changes.

### Assigning a Member to a Project

To assign a member to a project, follow these steps:

1. Find the project to which you want to assign a member in the project list.

2. Enter the member's name in the "Member Name" input field.

3. Click the "Assign Member" button to assign the member to the project.

### Changing the Status of a Project

To change the status of a project, follow these steps:

1. Find the project for which you want to change the status in the project list.

2. Select the desired status from the "Status" dropdown menu.

3. Click the "Change Status" button to update the project's status.

## Conclusion

Congratulations! You have successfully installed and learned how to use the Evernote Project Controller. This web application will assist you in managing your Evernote projects efficiently. If you have any further questions or need assistance, please refer to the documentation or contact our support team.