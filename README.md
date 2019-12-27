# Udacity capstone project
This simple application is for learning purposes only. It is an api, build with flask and auth0 for authentication and authorization.

You can create, delete, update and read movies and actors.
The endpoints are not publicly (without access token) accessible.
There are 3 authorization groups:
1. Casting Assistant

   Can view actors and movies

2. Casting Director
   
   All permissions a Casting Assistant has and…

   Add or delete an actor from the database

   Modify actors or movies

3. Executibe Producer

   All permissions a Casting Director has and…

   Add or delete a movie from the database


For testing the endpoints, you have to get an access token.

## Installation for local development
Install the requirements
```
pip install -r requirements.txt
```

You also need to configure your database path in the models.py file

Run the development server
```
./setup.sh
flask run  --reload
```
## Live application
The application is hosted on heroku under the url:

`https://fsndcapstone.herokuapp.com/`

### Getting access tokens for testing
In the file [test.txt](./test.txt) you can find some curl commands to get an valid access token for each Role.

**Get access token for assistant**
```
curl --request POST \
  --url 'https://dev-fvxwov-3.eu.auth0.com/oauth/token' \
  --header 'content-type: application/x-www-form-urlencoded' \
  --data grant_type=http://auth0.com/oauth/grant-type/password-realm \
  --data username=assistant@capstone.com \
  --data password=Assistant123 \
  --data audience=http://localhost:5000 \
  --data 'client_id=JQvQhMzwmESXHF2tbwwFxqvZONN4AlYG' \
  --data client_secret=_ta8FNs1G4DeOUqq933GLeiJ82lUxNoHatihjImAtWq2sNFQYhEe1q0QC2qFAHiv \
  --data realm=Username-Password-Authentication
```
**Get access token for director**
```
curl --request POST \
  --url 'https://dev-fvxwov-3.eu.auth0.com/oauth/token' \
  --header 'content-type: application/x-www-form-urlencoded' \
  --data grant_type=http://auth0.com/oauth/grant-type/password-realm \
  --data username=director@capstone.com \
  --data password=Director123 \
  --data audience=http://localhost:5000 \
  --data 'client_id=JQvQhMzwmESXHF2tbwwFxqvZONN4AlYG' \
  --data client_secret=_ta8FNs1G4DeOUqq933GLeiJ82lUxNoHatihjImAtWq2sNFQYhEe1q0QC2qFAHiv \
  --data realm=Username-Password-Authentication
```
**Get access token for producer**
```
curl --request POST \
  --url 'https://dev-fvxwov-3.eu.auth0.com/oauth/token' \
  --header 'content-type: application/x-www-form-urlencoded' \
  --data grant_type=http://auth0.com/oauth/grant-type/password-realm \
  --data username=producer@capstone.com \
  --data password=Producer123 \
  --data audience=http://localhost:5000 \
  --data 'client_id=JQvQhMzwmESXHF2tbwwFxqvZONN4AlYG' \
  --data client_secret=_ta8FNs1G4DeOUqq933GLeiJ82lUxNoHatihjImAtWq2sNFQYhEe1q0QC2qFAHiv \
  --data realm=Username-Password-Authentication
```

The secret key and the login credentials are for testing purposes only and will be deleted after this project ends.
For testing the RBAC controls, there is also an [postman_collection JSON](./capstone_auth.postman_collection.json) file. You can import it in your postman and maybe you need to change the authorization tokens.

## Endpoints
For all the endpoints you need to pass a valid access token to use the endpoints.

To test the live application, replace `localhost:5000` with `https://fsndcapstone.herokuapp.com/`

### GET
Get all movies

`localhost:5000/movies`

**Response:**
```
{
    "movies": [
        {
            "id": 1,
            "release_date": "Fri, 20 Dec 2019 10:19:55 GMT",
            "title": "New Movie"
        }
    ],
    "success": true
}
```

Get all actors

`localhost:5000/actors`

**Response:**
```
{
    "actors": [
        {
            "age": 18,
            "gender": "Man",
            "id": 1,
            "name": "Test name"
        }
    ],
    "success": true
}
```

Get one movie

`localhost:5000/movies/1`

**Response:**
```
{
    "movie": {
        "id": 1,
        "release_date": "Fri, 20 Dec 2019 10:19:55 GMT",
        "title": "New Movie"
    },
    "success": true
}
```

Get one actor

`localhost:5000/actors/2`

**Response:**
```
{
    "actor": {
        "age": 18,
        "gender": "Man",
        "id": 2,
        "name": "Test name"
    },
    "success": true
}
```

### POST
Create movie

`localhost:5000/movies`

example of the body
```
{
    "title": "New Movie",
    "release_date": "2019-12-20 10:19:55"
}
```

**Response:**
```
{
    "message": "New Movie stored",
    "success": true
}
```
### Create actor
`localhost:5000/actors`

example of the body
```
{
	"name": "John",
	"age": 18,
	"gender": "Man"
}
```

**Response:**
```
{
    "message": "New Actor stored",
    "success": true
}
```
### PATCH
Update movie

`localhost:5000/movies/1`

**Response:**
```
{
    "message": "1 Movie ID updated",
    "success": true
}
```

Update actor

`localhost:5000/actors/1`

**Response:**
```
{
    "message": "1 Actor ID updated",
    "success": true
}
```
### DELETE
Delete a movie

`localhost:5000/movies/{{ id }}`

**Response:**
```
{
    "message": "1 Movie ID deleted",
    "success": true
}
```

Delete a actor

`localhost:5000/actors/{{ id }}`

**Response:**
```
{
    "message": "1 Actor ID deleted",
    "success": true
}
```


### ERRORS
**422** : unprocessable

**405** : method not allowed

**500** : Internal server error

**404** : Not found

**401** : Auth error
