
Models
===============================

The models and their relations can be seen in this graph:

.. graphviz:: images/models.dot

With `graphviz` and `django-extensions` you can generate this image yourself:

.. code-block:: bash

    python source/manage.py graph_models --all --settings=base.settings_development | grep -v '^  //' | grep -v '^[[:space:]]*$$' > images/models.dot


