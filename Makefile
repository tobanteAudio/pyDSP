PACKAGE_NAME = dsp
TEST_DIRECTORY = tests
DOC_DIRECTORY = docs

.PHONY:
default: develop test

.PHONY:
install:
	@pip install .

.PHONY:
deps:
	@pip install -r requirements.txt

.PHONY:
develop: deps
	@pip install -e .

.PHONY:
test:
	@pytest -v --cov-report term-missing --cov=$(PACKAGE_NAME) $(TEST_DIRECTORY)

.PHONY:
lint:
	# @flake8 $(PACKAGE_NAME) $(TEST_DIRECTORY) examples
	@pylint --disable=fixme $(PACKAGE_NAME) $(TEST_DIRECTORY)


.PHONY:
clean:
	rm -rf $(PACKAGE_NAME)/__pycache__
	rm -rf $(TEST_DIRECTORY)/__pycache__
	rm -rf .pytest_cache
	rm -rf .coverage