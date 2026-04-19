# -----------------------------------------------------------------------------
# Configuration

# commands
PYTHON := python
PRE_COMMIT := pre-commit
COVERAGE := coverage

# variables
HOST := 0.0.0.0
PORT := 9900
TEST_VERBOSITY := 3

# -----------------------------------------------------------------------------
# Versions

django.version.%:
	@$(PYTHON) -c "import django; print(django.get_version())"

python.version.%:
	@$(PYTHON) -c "import sys; print(sys.version)"

# -----------------------------------------------------------------------------
# Requirements

requirements.install.%:
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install --upgrade -r requirements/$*.txt

# -----------------------------------------------------------------------------
# Linter

linter.install.%:
	$(PRE_COMMIT) install

linter.update.%:
	$(PRE_COMMIT) autoupdate

linter.run.%:
	$(PRE_COMMIT) run --all-files

# -----------------------------------------------------------------------------
# Django

django.migrations.%:
	$(PYTHON) manage.py makemigrations --settings=config.settings.$*
	$(PYTHON) manage.py migrate --settings=config.settings.$*

django.collectstatic.%:
	$(PYTHON) manage.py collectstatic --noinput --settings=config.settings.$*

django.run.%:
	$(PYTHON) manage.py runserver $(HOST):$(PORT) --settings=config.settings.$*

django.shell.%:
	$(PYTHON) manage.py shell --settings=config.settings.$*

django.urls.%:
	$(PYTHON) manage.py show_urls --settings=config.settings.$*

django.init.%:
	$(MAKE) requirements.install.$*
	$(MAKE) django.migrations.$*
	$(MAKE) django.collectstatic.$*

django.reset.%:
	$(PYTHON) manage.py reset_db --noinput --settings=config.settings.$*
	$(MAKE) django.init.$*

# -----------------------------------------------------------------------------
# Django Test

django.test.%:
	$(PYTHON) manage.py test -v $(TEST_VERBOSITY) --settings=config.settings.$*

django.coverage.%:
	$(COVERAGE) erase
	$(COVERAGE) run manage.py test --settings=config.settings.$*
	$(COVERAGE) report -m --skip-covered
