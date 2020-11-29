# star-wars
# Deployment instructions
### Install postgres
`sudo apt install postgresql postgresql-contrib`
### Install pipenv
`sudo apt install python3-pip`

`sudo pip install pipenv`

### Install pip environment:
`cd star-wars`

`pipenv install`
### Activate pip environment
`pipenv shell`

### Run tests:
`pytest`

### Run database initialization script:
`python initial_postgres_setup.py`

### Deploy application
`gunicorn -w 4 "starwars.app:create_app()"`

### Call web service:
`curl -i -H "Accept: application/json" -H "Content-Type: application/json" http://127.0.0.1:8000/starships`
