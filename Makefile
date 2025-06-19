dev:
	flask --app api run --debug

db-migrate:
	flask db migrate
