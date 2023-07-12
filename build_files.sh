echo " BUILD START"
python3.9 -m pip instll -r requirements.txt
python3.9 manage.py migrate
python3.9 manage.py collectstatic --noinput --clear
echo " BUILD END"