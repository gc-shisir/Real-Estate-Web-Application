## Real Estate Web Application

To run this project:
1. Clone this project:
 ``` git clone https://github.com/gc-shisir/Real-Estate-Web-Application.git ```
1. Setup the database in settings.py file:
    - For mysql or postgresql
    ``` 
     'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'database_name',
        'USER':'database_user',
        'PASSWORD':'database_password',
        'HOST':'localhost'
    }
    ```  

    - For sqlite: Add db.sqlite file in the root directory
    ```  
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    } 
    ```
1. Run the server:
    ```
     python manage.py runserver
    ```
