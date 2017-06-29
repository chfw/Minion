pip freeze
nosetests --with-coverage --cover-html --cover-html-dir reports --cover-package minion --cover-package tests --with-doctest --doctest-extension=.rst README.rst tests docs/source minion && flake8 . --exclude=.moban.d --builtins=unicode,xrange,long
