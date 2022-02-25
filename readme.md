# Steps to run the code without docker
~~~
Configure the db values in local .env.dev and docker-compose.yml
~~~
## step 1:
### Create and activate virtual environment
~~~
virtualenv .venv
source .venv/Scripts/active (windows)
source .venv/bin/active (linux)
~~~
## step 2:
### Install requirements
~~~
pip install -r requirements.txt
~~~
## step 3:
### Migrate the migrations
~~~
python manage.py migrate
~~~
## step 4:
### Adding groups
~~~
run command: python group.py
~~~
## step 5:
### Create superuser
~~~
run command: python manage.py createsuperuser
(select 1 in groups for admin user and 2 for normal user)
~~~
## step 6:
### Run the project
~~~
python manage.py runserver
~~~


# Steps to run the code with docker
Configure the db values in local .env.dev

## step 1:
### Build the docker image
~~~
docker-compose build
~~~

## step 2:
### Migrate the migrations
~~~
docker-compose exec web python manage.py migrate
~~~

## step 3:
### Adding groups
~~~
run command: docker-compose exec web python python group.py
~~~
## step 4:
### Create superuser
~~~
run command: docker-compose exec web python manage.py createsuperuser
(select 1 in groups for admin user and 2 for normal user)
~~~
## step 5:
### Run the project
~~~
docker-compose up -d
~~~