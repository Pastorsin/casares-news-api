VENV=$(CURDIR)/venv
BIN=$(VENV)/bin

PYTHON=$(BIN)/python
PIP=$(BIN)/pip
VAPID=$(BIN)/vapid

PORT=5000
HEROKU=. $(BIN)/activate && heroku local
HEROKU_FLAGS=-f Procfile.dev -e .env -p $(PORT)

.PHONY: install initial-migrates load-data
$(VENV): requirements.txt
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt

initial-migrates: $(VENV)
	# Migrate the django built-in apps
	export ONLY_DJANGO_APPS="True" && $(PYTHON) manage.py migrate
	# Migrate the rest of the apps
	$(PYTHON) manage.py makemigrations
	$(PYTHON) manage.py migrate

load-data: initial-migrates
	# Load the RDF object mapping
	$(PYTHON) manage.py loaddata data/contenttypes.json
	$(PYTHON) manage.py loaddata data/rdf_io.json

install: $(VENV) load-data

.PHONY: webpush-gen scrap server app
webpush-gen:
	$(VAPID) --gen
	$(VAPID) --applicationServerKey

scrap:
	$(HEROKU) scrap $(HEROKU_FLAGS)

server:
	$(HEROKU) web $(HEROKU_FLAGS)

app:
	$(HEROKU) web,scheduler $(HEROKU_FLAGS)

.PHONY: clean
clean:
	# Database
	find -name "db.sqlite3" -delete
	# Webpush keys
	find -name "*.pem" -delete
	# Cache
	find -name "*.pyc" -delete
	find -name "__pycache__" -delete
	# Enviroment
	rm -rf $(VENV)
