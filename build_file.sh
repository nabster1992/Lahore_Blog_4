echo "BUILD START"
export PYTHON=python3.9
$PYTHON -m pip install -r requirements.txt
$PYTHON manage.py collectstatic --noinput --clear
echo "BUILD END"
