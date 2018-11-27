# IT-school-
project site for online IT school courses



Pages:
 - '/'
 - 'school/courses'
 - 'school/calendar/2017'
 - 'school/calendar/2018'
 - 'school/calendar/2019'
 

### For the django-rq module to work, the redis-server must be installed!

``` 
$ sudo install redis-server
```
redis-server test:

```
$ redis-cli ping
$ pong

 ```
### install

```
$ git clone https://github.com/Avderevo/IT-school-

$ pip install requirements.txt

$ cd app

$ export DJANGO_CONFIGURATION=Dev

$ python manage.py runserver

```


Authorization:

For authorization via email, in the settings you need to specify your settings for mail.
And indicate for ``` USER_EMAIL_ACTIVATION - True ``` 

If it is ```USER_EMAIL_ACTIVATION - False```, authorization will proceed without confirmation by mail.


Сlick the "register and login" button at the top of the page.


Logout:

button "выход"
  
#### Password reminder is available only with ready mail settings!

### 