pip freeze
nosetests --with-cov --cover-package minion_cli --cover-package tests --with-doctest --doctest-extension=.rst README.rst tests docs/source minion_cli && flake8 . --exclude=.moban.d --builtins=unicode,xrange,long
