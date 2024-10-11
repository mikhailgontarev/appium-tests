ENVIRONMENT=$(e)

.PHONY: \
	venv-install \

venv-install:
	$(info Setup virtual environment)
	python3 -m venv test_venv
	./test_venv/bin/python3 -m pip install -r requirements.txt
	git clone https://github.com/GlobalRadio/pytest-appium.git
	./test_venv/bin/python3 -m pip install ./pytest-appium

pytest-smoke:
	$(info Run pytest)
	./test_venv/bin/python3 -m pytest ./tests --caps android_capabilities

