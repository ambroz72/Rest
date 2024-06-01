# Project - Task (add,view,update,delete) using Django REST framework 

Description

This Django REST Framework project provides a robust API for managing tasks. Users can create, retrieve, update, and delete tasks, with filtering 
options to view due and completed tasks. User registration is also included.

![screenshot](screenshot/screenshot/home.png)


Features

Task Management: Create, read, update, and delete tasks.
Due Task Filtering: View tasks that are not yet completed.
Completed Task Filtering: View tasks that have been marked as completed.
User Registration: Register new users for authentication.

Access the API endpoints:

Base URL: http://localhost:8000/ (or your development server port)
Tasks (list, create, retrieve, update, delete): http://localhost:8000/api/tasks/
Due Tasks: http://localhost:8000/api/tasks/?completed=False
Completed Tasks: http://localhost:8000/api/tasks/?completed=True
User Registration: http://localhost:8000/api/users/


API Endpoints

GET /api/tasks/: Retrieve a list of all tasks (ordered by creation date descending).
POST /api/tasks/: Create a new task. Requires authentication.
GET /api/tasks/<task_id>/: Retrieve a specific task by ID. Requires authentication.
PUT /api/tasks/<task_id>/: Update an existing task. Requires authentication.
DELETE /api/tasks/<task_id>/: Delete a task. Requires authentication.
GET /api/tasks/?completed=False: Retrieve a list of due tasks (not yet completed).
GET /api/tasks/?completed=True: Retrieve a list of completed tasks.
POST /api/users/: Register a new user.


Authentication

Authentication is required for creating, retrieving, updating, and deleting tasks. Obtain a JSON Web Token (JWT) by registering a user or using 
a third-party authentication provider. Include the JWT in the Authorization header of subsequent requests.

Testing

Unit tests are encouraged for code maintainability. Consider using a framework like Django's built-in unittest or a third-party option like pytest.

Deployment

For deployment, follow best practices for your chosen hosting platform. This may involve configuring environment variables, setting up a
production database, and potentially using a WSGI server like Gunicorn.
