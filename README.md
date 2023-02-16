# Library-Management-System

The repository contains web pages using Django web development framework in python language. It contains
  (a) Two parts, one to search Books and other one to Issue Books.
 
## Getting Started
 

Open terminal using Ctrl + Alt + T. Run the following command <br>
```ruby 
   git clone https://github.com/aayushray/Library-Management-System.git
```

Create and activate virtual environment using <br>
```ruby
   mkvirtualenv venv
```
<br>

```ruby
    workon venv
``` 
<br>

Install requirements needed for the project, from requirement.txt
```ruby
    pip install -r requirements.txt
``` 


### Run Steps:

Create SuperUser to access Staff status to view admin panel.
```ruby 
   python manage.py createsuperuser
```
<br>

Make packaging up your model changes into individual migration files.
```ruby 
   python manage.py makemigrations
```
<br>

Roll out migrations to the server
```ruby 
   python manage.py migrate
``` 
<br>

```ruby 
   python manage.py runserver
``` 
