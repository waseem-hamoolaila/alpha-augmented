Placing packages visualizer
==============================

A small project that visualize packing algorithm, by allowing you 
to create custom boxes and fit different shapes into it. 


You can view the live demo `here <https://waseemalpha.pythonanywhere.com/>`_


It allows you to:
-----------------

- Customize boxes by defining the dimensions.
- tweak the behavior of the algorithm by setting (direction - rotation - pov)


Installation locally
====================

* Clone the repo
* Create a virtual environment with python > 3.9
* activate it.

After cloning and activating the virtual env
---------------------------------------------

.. code-block::
    > cd alpha-augmented

Then we need to install the requirements

.. code-block::
    pip install -r requirements.txt

Then we need to migrate the database

.. code-block::
    python manage.py migrate

Now we should be good to go... it's time to run the server

.. code-block::
    python manage.py runserver


Now the server should be running and the url would be **127.0.0.1:8000**
