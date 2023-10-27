.PHONY: dist install
dist:
	python setup.py sdist bdist_wheel && twine upload --skip-existing dist/*
	rm -rf build dist *.egg-info
install:
	pip install -e . && rm -rf *.egg-info
	mkdir -p ~/.cal_hack && touch ~/.cal_hack/config.yaml
