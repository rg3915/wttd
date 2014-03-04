pushheroku:
	git push heroku master --force

migrateheroku:
	heroku run python manage.py syncdb --migrate