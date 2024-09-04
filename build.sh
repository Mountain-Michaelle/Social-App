
# Build the project
if ! command -v pip &> /dev/null
then
    echo "pip could not be found. Installing pip..."
    apt-get update && apt-get install -y python3-pip
fi

echo 'Building the project...'
python3.9 -m pip install -r requirements.txt



echo "Make migrations..."
python3.9 manage.py makemigrations
python3.9 manage.py migrate
python3.9 manage.py collectstatic --force
python3.9 manage.py compress --force