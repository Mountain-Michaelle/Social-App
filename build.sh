
# Build the project

echo 'Building the project...'
python3.9 -m pip install -r requirements.txt



echo "Make migrations..."
python3.9 manage.py makemigrations
python3.9 manage.py migrate
python3.9 manage.py collectstatic --force
python3.9 manage.py compress --force