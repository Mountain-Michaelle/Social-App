
# Build the project
echo 'Building the project...'
pip install setuptools
pip install -r requirements.txt



echo "Make migrations..."
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic 