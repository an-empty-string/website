deploy: build
	rsync -rv build/ tris.fyi:/var/www/
	touch deploy

build: templates static posts
	sh -c ". venv/bin/activate && python3 freeze.py"
	touch build
