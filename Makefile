deploy: build
	rsync -rv build/ trisfyi:/var/www/
	touch deploy

build: templates static posts items
	sh -c ". venv/bin/activate && python3 freeze.py"
	touch build
