create-venv:
	python3 -m venv venv 


run-venv:
	. venv/bin/activate 
	

run:
	python3 manage.py run


install-only-requirements:
	pip3 install -r requirements.txt


install-db:
	python3 manage.py db init
	python3 manage.py db migrate
	python3 manage.py db upgrade


hooks:
	cd .git/hooks && ln ../../.github/hooks/pre_commit.py ./pre-commit
	cd .git/hooks && ln ../../.github/hooks/commit_msg.py ./commit-msg
	cd .git/hooks && ln ../../.github/hooks/pre_push.py ./pre-push
	cd .git/hooks && ln ../../.github/hooks/utils.py ./utils.py
	cd .git/hooks && ln ../../.github/hooks/constants.py ./constants.py


delete-hooks:
	rm .git/hooks/commit-msg
	rm .git/hooks/pre-push
	rm .git/hooks/utils.py
	rm .git/hooks/constants.py
	rm .git/hooks/pre-commit


seed:
	python manage.py seed run