django-with-auth
================

Boilerplate for Django + django-auth + Bootstrap + jQuery
---------------------------------------------------------

Django project with:

* django-auth enabled and configured
* User extended with UserProfile model example
  * Admin pre-configured to use UserProfile
  * Register view demonstrates saving UserProfile data after a user is created
* Views and Templates based on django-admin ready to go
  * Login
  * Logout
  * Forgot / Reset Password
  * Change Password
* Bootstrap wired up in all templates
  * Includes responsive extensions and JavaScript
* jQuery wired up in all templates

Requires [pip](http://pypi.python.org/pypi/pip), [virtualenv](http://pypi.python.org/pypi/virtualenv) recommended.

To use:

    $ virtualenv env
    $ source ./env/bin/activate
    $ pip install -r requirements.txt
    $ cd auth_template
    $ ./manage.py syncdb      # You will get errors here - ignore them
    $ ./manage.py migrate
    $ ./manage.py runserver

Use your favorite search and replace tool to rename the project.

Licensed under the [MIT License](http://opensource.org/licenses/MIT). See LICENSE.md for more information.
