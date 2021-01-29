TOOL = python manage.py

run:
	@$(TOOL) runserver

migrate:
	@$(TOOL) makemigrations
	@$(TOOL) migrate

check:
	@$(TOOL) check

test:
	@$(TOOL) test

coverage:
	@coverage run manage.py test
	@coverage report

collect:
	@$(TOOL) collectstatic --no-input