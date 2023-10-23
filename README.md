# workersAPI
An API which provides a CRUD for teams and members in it

## Technology stack:
- Programming language: Python
- Framework: Django
- API service: Django REST framework
- Database: Sqlite3


## Database structure
Database has three schemes for Developers, Teams and Type of teams for persisting types of the team

## Installation
1. First, create and activate your virtual environment
```
pip install virtualenv
python<version> -m venv <virtual-environment-name>
source env/bin/activate
```
2. Install all packages from requirements.txt
```
pip install -r requirements.txt
```
3. After that, migrate the database schema to the SQLite database with
```
python manage.py migrate
```
4. Start the Django development server by running
```
python manage.py runserver
```
5. Endpoints of the API
```
/api/developers - GET, POST
/api/developers/<pk> - GET, PATCH, DELETE

/api/teams - GET, POST
/api/teams/<pk> - GET, PATCH, DELETE
```
