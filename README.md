# lightfeather coding challenge

This project implements the LightFeather backend challenge API.

## API

### GET /api/supervisors

Retrieve a list of supervisors from:

    https://609aae2c0f5a13001721bb02.mockapi.io/lightfeather/

and return as json containing a list of supervisor strings formatted as:

    "{jurisdiction} - {lastName}, {firstName}"

Sort alphabetcally by juristiction, lastName and firstName.
Numeric jurisdictions are not included in the response.

### POST /api/submit

This endpoint accepts input json formatted as in this example:

    {
        "firstName" : "Dwight",
        "lastName" : "Schrute",
        "email" : "dwight.schrute@dundermifflin.com",
        "phone" : "555-555-1234",
        "supervisor" : "Michael Scott"
    }

("email" and "phone" are optional) and prints to the console as:

    First Name: Dwight
    Last Name: Schrute
    Email: dwight.schrute@dundermifflin.com
    Phone number: 555-555-1234
    Supervisor: Michael Scott

## Install, Build and Run

The API runs in a Docker container.

1) Retrieve the depository into an empty directory.

2) Open a terminal and build the docker image:

    docker build --tag lf-challenge .

3) Start the container:

    docker run --name lf-challenge -p 5000:5000 lf-challenge

4) The endpoint urls are:

http://127.0.0.1:5000/api/supervisors

http://127.0.0.1:5000/api/submit

The submit API can be tested with curl:

    curl --header "Content-Type: application/json" \
    --request POST \
    --data '{"firstName" : "Dwight","lastName" : "Schrute", "email" : "dwight.schrute@dundermifflin.com", "phone" : "555-555-1234", "supervisor" : "Michael Scott" }' \
    http://127.0.0.1:5000/api/submit
