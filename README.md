docker-compose up --build

docker-compose run web python manage.py migrate

docker-compose run web python manage.py createsuperuser

