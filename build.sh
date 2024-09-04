
# Build the project

echo 'Building the project...'
python -m pip install -r requirements.txt



echo "Make migrations..."
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py compress --noinput