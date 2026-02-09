mig:
	make migration && make migrate
cru:
	python manage.py createsuperuser
test:
	python3 manage.py test
run:
	python manage.py runserver 0.0.0.0:2026

#others
git-rm-idea:
	git rm -r --cached .idea/
collect:
	python manage.py collectstatic --noinput
rm-static:
	rm -rf staticfiles/
migration:
	python3 manage.py makemigrations
migrate:
	python3 manage.py migrate
startapp:
	python manage.py startapp $(name)
clear-linux:
	find . -path "*/migrations/*.py" -not -name "__init__.py" -delete && find . -path "*/migrations/*.pyc"  -delete
clear-windows:
	Get-ChildItem -Path "*\migrations\0*.py" | Remove-Item -Force
	Get-ChildItem -Path "*\migrations\*.pyc" | Remove-Item -Force
no-sqlite-db:
	rm -rf db.sqlite3
re-django:
	pip3 uninstall Django -y && pip3 install Django
no-venv:
	rm -rf env/ venv/ .venv/
re-mig:
	make no-sqlite-db && make clear-linux && make re-django & make i && make mig && make cru && make collect && make test && make run
send_notifications:
	python manage.py send_notifications
