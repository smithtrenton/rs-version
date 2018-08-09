.PHONY: deps update-deps lib run

deps:
	pip install -r requirements_dev.txt

update-deps:
	pip install -Ur requirements_dev.txt

run:
	python main.py
