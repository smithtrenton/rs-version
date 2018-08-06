.PHONY: deps update-deps lib run

deps:
	pip install -r requirements_dev.txt

update-deps:
	pip install -Ur requirements_dev.txt

lib:
	rm -rf lib
	pip install -t lib -r requirements.txt

run:
	dev_appserver.py app.yaml
