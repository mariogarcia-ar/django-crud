pip install django==4.2
django-admin startproject mycrud .
django-admin startapp task 

add app to project
python manage.py runserver

python manage.py makemigrations 
python manage.py migrate 
 python manage.py createsuperuser


Pagina signup
    route
    controller
    view
    form 

jblock	{% block name %} {% endblock name %}
jif	{% if cond %} {% endif %}
jifelse	{% if cond %} {% else %} {% endif %}
jextend	{% extends 'file' %}
jfor	{% for A in B %} {% endfor %}
jrandom	{{ range(MIN, MAX) | random }}
jvar	{{ variable }}
jfunc	{% function %}
jround	{% float | round %}
jjoin	{% list | join(',') %}
jset	{% set A = B %}
jurl	{{ url_for('dir', filename='file') }}
jcall	{% call func %} {% endcall %}
jfilter	{% filter cmd %} {% endfilter %}
jinclude	{% include 'file' %}
jfrom	{% from 'dir' import func %}
jimg	<img src="{{ url_for('static', filename='A') }}" alt="B">
jhref	a href with url_for embed
