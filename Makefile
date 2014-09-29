.PHONY : help init devserver tests coverage checkstyle readme clean fullclean

FILES       = build dist src/*.egg-info checkstyle.txt README.html htmlcov/ .coverage
OTHER_FILES = .installed.cfg .tox bin develop-eggs eggs parts

help:
	@echo "make init:"
	@echo "  runs bootstrap.py && bin/buildout."
	@echo "make devserver:"
	@echo "  start the django test project webserver"
	@echo
	@echo "make tests:"
	@echo "  runs the tests (use bin/tox for tox)"
	@echo "make coverage:"
	@echo "  reports test coverage"
	@echo
	@echo "make checkstyle"
	@echo "  generates pep8, pyflakes and pylint reports"
	@echo "make readme:"
	@echo "  converts README to html and opens it in"
	@echo "  a browser"
	@echo 
	@echo "make clean:"
	@echo "  removes build/dist files."
	@echo "make fullclean:"
	@echo "  removes all build/dist/mbuildout/tox files."

init:
	@echo "Running buildout, this will take a while..."
	python bootstrap.py && bin/buildout
	@echo "Done!"

devserver:
	bin/manage runserver

tests:
	bin/manage test testproject

coverage:
	bin/coverage run --source src/friendlytagloader --branch bin/manage test testproject
	bin/coverage html
	python -m webbrowser -t file://$(PWD)/htmlcov/index.html

checkstyle:
	echo 'pep8' > checkstyle.txt
	-bin/pep8 -r --show-source --show-pep8 --count --statistics src >> checkstyle.txt
	echo '' >> checkstyle.txt
	echo 'pyflakes' >> checkstyle.txt
	echo '' >> checkstyle.txt
	-bin/pyflakes src >> checkstyle.txt
	python -m webbrowser -t file://$(PWD)/checkstyle.txt

readme:
	bin/rst2 html README > README.html
	python -m webbrowser -t file://$(PWD)/README.html

clean:
	@echo "Removing files..."
	-rm -rf $(FILES)
	@echo "Done!"

fullclean: override FILES += $(OTHER_FILES)
fullclean: clean
