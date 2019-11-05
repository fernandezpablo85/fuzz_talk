test:
	pipenv run pytest

test_statistics:
	pipenv run pytest --hypothesis-show-statistics -s

test_verbose:
	pipenv run pytest --hypothesis-verbosity=verbose -s

test_coverage:
	pipenv run pytest --cov .

test_coverage_report:
	pipenv run pytest --cov . --cov-report html

clear_test_cache:
	rm -rf '.hypothesis'
	rm -rf '.pytest_cache'
