# FT-task

This app is a simple Django REST API which allows logged-in, authenticated users to perform the following actions:

- Create a new store
- Retrieve a single store by ID
- Retrieve a list of all stores
- Update an existing store
- Delete an existing store

## Features

### API routes

The listed HTTP requests can be performed by visiting the corresponding URI routes.

| HTTP   | URI           | CRUD Operation                         | View name |
| ------ | ------------- | -------------------------------------- | --------- |
| GET    | /stores/      | list all stores                        | LIST      |
| POST   | /stores/      | create a new store                     | LIST      |
| GET    | /stores/{id}/ | retrieve a specific store              | DETAIL    |
| PUT    | /stores/{id}/ | update a specific store                | DETAIL    |
| DELETE | /stores/{id}/ | delete a specific store                | DETAIL    |
| GET    | /times/       | list all opening hours                 | LIST      |
| POST   | /times/       | create a opening hour entry            | LIST      |
| GET    | /stores/{id}/ | retrieve a specific opening hour entry | DETAIL    |
| PUT    | /stores/{id}/ | update a specific opening hour entry   | DETAIL    |
| DELETE | /stores/{id}/ | delete a specific opening hour entry   | DETAIL    |

### Authentication

The project features Django REST framework's token authentication system to authenticate users. It also uses build in django permissions classes to allow all logged in, authenticated users to perform all actions on stores and opening hour entries (create, retreive, update and delete).

### Validation

Most of the validation invoked is through the default behaviour of Django REST framework based on the database models. This includes checking for validity of data related to the selected field type (e.g. str, int, email, time, etc.) and fields left blank when they are required.

There is also validation to check for uniqueness of data (store name and store address) and unique together (between store and day of the week). A validation error will be raised if this data or combination of data is not unique.

A custom validation class was created to check that opening hours are valid. This ensures that the closing time of a store is after its opening time, and that the opening and closing times are different from eachother. A custom validation error is returned if this is not the case.

### Pagination

`rest_framework.pagination.PageNumberPagination` was used as the `DEFAULT_PAGINATION_CLASS` in the rest framework settings in settings.py. A page size of 10 was selected for the pagination class.

### Filtering

Filtering was added using Django REST Framework's built in filtering method. Stores may be filtered by store name or store address when accessing the `/api/v1/stores/` route. In addition, store entries may be ordered by each of the fields (ID, Store Name, Store Address, Opening Hours) using the django rest_framework `filters.OrderingFilter`.

### Status codes

The following status codes can be handled by the API:

- 200 OK
- 201 Created (following successful creation of content)
- 204 No Content (following successful deletion of content)

- 400 Bad Request
- 401 Unauthorised (when accessing content whilst not logged in)
- 404 Not Found (when trying to access content which does not exist)

## Tools & Technologies used

- [Python](https://www.python.org) used as the back-end programming language.
- [PostgreSQL](https://www.postgresql.org) used as the relational database management.
- [Visual Studio Code](https://code.visualstudio.com/) used as a local IDE for development.
- [Black](https://pypi.org/project/black/) used as a PEP8 compliant Python code formatter
- [DBeaver](https://dbeaver.io/) used to produce ERDs and help plan the database models

## Database Design

An Entity Relationship Diagram (ERD) was created using [DBeaver](https://dbeaver.io/) in order to visualize the database architecture before creating Django models.
This features a one to many relationship, where one store may have many associated opening_hours entries (but can, however, only have one entrie for each day of the week).  
![ERD](documentation/erd.png)

## Testing

Unittests have been added to this project. To run them, the following command can be run in Git Bash or Terminal:  
(replace `python` with `python3` if not using a virtual environment)  
`python manage.py test`

## Deployment

### Local Deployment

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the requirements.txt file.
It is recommended that you first activate a virtual environment of your choice (if not using virtual environment, replace `pip` with `pip3` below).

`pip install -r requirements.txt`

Once the project is cloned or forked, in order to run it locally, the follow steps need to be followed:

- To start the Django app: `python3 manage.py runserver`
- To stop the app once it's loaded: `CTRL+C` or `⌘+C (Mac)`
- To make any necessary migrations: `python3 manage.py makemigrations`
- To migrate the data to the database: `python3 manage.py migrate`
- To create a superuser: `python3 manage.py createsuperuser`
- Everything should be ready now, so run the Django app again: `python3 manage.py runserver`

### Cloning

You can clone the repository by following these steps:

1. Go to the GitHub repository
2. Locate the Code button above the list of files and click it
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:
   `git clone https://github.com/dragon-fire-fly/FT-task`
7. Press Enter to create your local clone.

### Forking

By forking the GitHub Repository, you make a copy of the original repository on your GitHub account and may view and/or make changes without affecting the original owner's repository. You can fork this repository by using the following steps:

1. Log in to GitHub and locate the GitHub Repository
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account.
