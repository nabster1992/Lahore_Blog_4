echo "BUILD START"
$PYTHON -m pip install -r requirements.txt
$PYTHON manage.py collectstatic --noinput --clear
echo "BUILD END"
