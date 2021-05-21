PACKAGE_NAME = dsp
TEST_DIRECTORY = tests
DOC_DIRECTORY = docs

.PHONY: default
default: clean test lint

.PHONY: install
install:
	@pip install .

.PHONY: deps
deps:
	@pip install -r requirements.txt

.PHONY: develop
develop: deps
	@pip install -e .

.PHONY: test
test:
	@pytest -v --cov-report term-missing --cov=$(PACKAGE_NAME) $(TEST_DIRECTORY)

.PHONY: coverage
coverage:
	@pytest -v --cov-report html --cov=$(PACKAGE_NAME) $(TEST_DIRECTORY)

.PHONY: lint
lint:
	@flake8 $(PACKAGE_NAME) $(TEST_DIRECTORY) examples
	@pylint --disable=fixme $(PACKAGE_NAME) $(TEST_DIRECTORY)


.PHONY: clean
clean:
	rm -rf $(PACKAGE_NAME)/__pycache__
	rm -rf $(TEST_DIRECTORY)/__pycache__
	rm -rf .pytest_cache
	rm -rf .coverage htmlcov