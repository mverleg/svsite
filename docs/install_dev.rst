
Installation
===============================

svSite should provide a fully functional site with minimal work.

Although later on you may want to personalize the look (:doc:`info <layout>`), which will take time. That's inevitable.

To get svSite running, follow the steps in the appropriate section.

Linux / bash
-------------------------------

Installing dependencies
...............................

For this to work, you will need ``python3-dev`` including ``pip`` and a database (``sqlite3`` is default and easy, but slow). Things will be easier and better with ``virtualenv`` or ``pew`` and ``git``, so probably get those too. You'll also need ``libjpeg-dev`` and the dev version of Python because of ``pillow``. You can install them with::

	sudo apt-get install libxml2-dev libxslt1-dev zlib1g-dev    # for lxml (which will be installed with pip)
	sudo apt-get install python3-dev sqlite3 git libjpeg-dev python-pip
	sudo apt-get install postgresql libpq-dev       # for postgres, only if you want that database
	sudo apt-get install mysql-server mysql-client  # for mysql, only if you want that database

Make sure you use the ``python3.X-dev`` that matches your python version (rather than ``python3-dev``). If there are problems, you might need `these packages`_.

Now get the code. The easiest way is with git, replacing ``SITENAME``::

	git clone https://github.com/mverleg/svsite.git SITENAME

Enter the directory (``cd SITENAME``).

Starting a virtual environment is recommended (but optional), as it keeps this project's Python packages separate from those of other projects. If you know how to do this, just do it your way. This is just one of the convenient ways::

	sudo pip install -U pew
	pew new --python=python3 sv

If you skip this step, everything will be installed system-wide, so you need to prepend ``sudo`` before any `pip` command. Also make sure you're installing for Python 3.

Install the necessary Python dependencies through::

	pip install -r dev/requires.pip
	pip install psycopg2     # only if you want to use a postgres database
	pip install mysqlclient  # only if you want to use a mysql database

Development
...............................

If you want to run tests, build the documentation or do anything other than simply running the website, you should install (otherwise skip it)::

	sudo apt-get install libgraphviz-dev
	pip install -r dev/requires_dev.pip  # optional

Database
...............................

We need a database. SQLite is used by default, which you could replace now or later (see :doc:`local settings <local_settings>`) for a substantial performance gain. To create the structure and an administrator, type this and follow the steps::

	python3 source/manage.py migrate
	python3 source/manage.py createsuperuser

Static files
...............................

Then there are static files we need, which are handles by bower by default [#footbower]_. On Ubuntu, you can install bower using::

	sudo apt-get install nodejs
	npm install bower

After that, install the static files and connect them::

	python3 source/manage.py bower install
	python3 source/manage.py collectstatic --noinput

Starting the server
...............................

Then you can start the test-server. This is not done with the normal ``runserver`` command but with ::

	python3 source/manage.py runsslserver localhost.markv.nl:8443 --settings=base.settings_development

We use this special command to use a secure connection, which is enforced by default. In this test mode, an unsigned certificate is used, so you might have to add a security exception.

You can replace the url and port. You can stop the server with ``ctrl+C``.

Next time
...............................

To **(re)start the server** later, go to the correct directory and run::

	pew workon sv  # only if you use virtualenv
	python3 source/manage.py runsslserver localhost.markv.nl:8443 --settings=base.settings_development

This should allow for easy development and testing.


.. rubric:: Footnotes

.. [#footbower] If you don't want to install node and bower, you can easily download the packages listed in `dev/bower/json` by hand and put them in `env/bower`. Make sure they have a `dist` subdirectory where the code lives. You still need to run the ``collectstatic`` command if you do this.

Automatic tests
-------------------------------

There are only few automatic tests at this time, but more might be added. You are also more than welcome to add more yourself. The tests use ``py.test`` with a few addons, which are included in ``dev/requires_dev.pip``. If you installed those packages, you can run the tests by simply typing ``py.test`` in the root directory. It could take a while (possibly half a minute).

Going live
-------------------------------

Everything working and ready to launch the site for the world to see? Read :doc:`install_live`!

.. _`these packages`: http://pillow.readthedocs.org/en/latest/installation.html#building-on-linux


