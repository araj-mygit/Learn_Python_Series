build config: #install pytest 

	python3 -m pip install --user virtualenv
	pip3 install pytest --user

test: #run pytest
	pytest -v
