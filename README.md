# Project introduction

Predicting a data from person, that will spit out classification is it lung cancer or not.

## Project installaation

```
git clone https://github.com/beebeewijaya-tech/lung-cancer-prediction.git

python -m venv venv

venv\Scripts\activate.bat
```

## How to run the project

```
run-dev:
	uvicorn main:app --reload  --host 0.0.0.0

install-dev:
	pip install -r requirements.txt

build:
	docker build . -t beebeewijaya/lung-cancer-analysis:latest

run:
	docker run -p 8000:8000 beebeewijaya/lung-cancer-analysis:latest

push:
	docker push beebeewijaya/lung-cancer-analysis:latest

test:
	pytest
```

You can just `make install-dev` & `make-run-dev`
