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

Run the development server
```
./setup.sh
flask run  --reload
```

### Getting access tokens for testing
In the file [test.txt](./test.txt) you can find some curl commands to get an valid access token for each Role.
The secret key and the login credentials are for testing purposes only and will be deleted after this project ends.
For testing the RBAC controls, there is also an [postman_collection JSON](./capstone_auth.postman_collection.json) file. You can import it in your postman and maybe you need to change the authorization tokens.

## Endpoints
For all the endpoints you need to pass a valid access token to use the endpoints.
### GET
Get all movies

`localhost:5000/movies`

Get all actors

`localhost:5000/actors`

Get one movie

`localhost:5000/movies/{{ id }}`

Get one actor

`localhost:5000/actors/{{ id }}`

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
### PATCH
Update movie

`localhost:5000/movies/{{ id }}`

Update actor

`localhost:5000/actors/{{ id }}`

### DELETE
Delete a movie

`localhost:5000/movies/{{ id }}`

Delete a actor

`localhost:5000/actors/{{ id }}`


### ERRORS
**422** : unprocessable
**405** : method not allowed
**500** : Internal server error
**404** : Not found
**401** : Auth error