dev:
	uvicorn main:app --reload  --host 0.0.0.0

build:
	docker build . -t beebeewijaya/lung-cancer-analysis:latest

run:
	docker run -p 8000:8000 beebeewijaya/lung-cancer-analysis:latest

test:
	pytest

.PHONY: dev build test