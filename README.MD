# Profile Search Server App

A Backend Application for Github Profile Search Application.


## Technologies 

+ Python, Django, Requests, Cors

## Prerequisites

+ Github Access Token

## Installation

+ Clone this git repository:
```
git clone https://github.com/kirtish16/profileSearchServerApp.git
```

+ Install the requirements:
```
pip install -r requirements.txt
```


+ Go to the project folder:
```
cd server
```

+ Add your Github Access Token
    
    In server/api_app/helpers.py file , 
    add 
    ```
    GITHUB_ACCESS_TOKEN = 'Your-Github-Access-Token'
    ```
+ Run the migrations:
```
python manage.py migrate
```

+ Start the server:
```
python manage.py runserver
```
This will start the webserver on [localhost](http://127.0.0.1:8000/).

## Testing API endpoints 

Executing tests :
```
python manage.py test
```

## Endpoints 

The API endpoints are:

| Endpoint   | Description |
|------------|-----------|
| /api/check/{username} | Check if Github user with 'username' exist |
| /api/detail/{username} | Get personal details of Github user with 'username' |
| /api/repos/{username}?per_page={itemsPerPage}&page={pageNumber} | Get repository details of Github user with 'username'. itemsPerPage defines Number of repository per page. pageNumber defines get repository details for a particular pageNumber |


## License
[MIT](https://choosealicense.com/licenses/mit/)
