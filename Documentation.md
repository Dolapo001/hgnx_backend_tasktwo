# Person API Documentation

## Overview

The Person API provides endpoints to manage information about individuals, such as name, age, and email. You can perform basic CRUD (Create, Read, Update, Delete) operations on person records using this API.

## Base URL

The base URL for accessing the Person API is `https://hgnxbackendtasktwo-production.up.railway.app/api/`.

## Authentication

No authentication is required to access the Person API in this example.

## Endpoints

### Create a New Person

- **URL:** `POST /api/`
- **Description:** Create a new person record.
- **Request Body:**
  - `name` (string, required): The name of the person.
  - `age` (integer): The age of the person.
  - `email` (string): The email address of the person.
- **Example Request:**
  ```json
  {
    "name": "John Doe",
    "age": 30,
    "email": "john.doe@example.com"
  }
* #### Response:
  - `HTTP 201 Created` on success.
  - Example Response:
  ```json
  {
  "id": 1,
  "name": "John Doe",
  "age": 30,
  "email": "john.doe@example.com"
  }

### Get All Persons
* **URL:** `GET /api/`
* **Description:** Retrieve a list of all persons.
* **Example Request**:

  `GET /api/`
* #### Response:
  - `HTTP 200 OK` on success.
  - Example Response:
  ```json
  [
  {
    "id": 1,
    "name": "John Doe",
    "age": 30,
    "email": "john.doe@example.com"
  },
  {
    "id": 2,
    "name": "Alice Smith",
    "age": 25,
    "email": "alice.smith@example.com"
  }
  ]
  
### Get Person by ID
* **URL:** GET /api/{user_id}/
* **Description:** Retrieve details of a person by their ID.
* **Example Request:**

  `GET /api/1/`

* #### Response:
  - `HTTP 200 OK` on success.
  - Example Response:

  ```json
  {
    "id": 1,
    "name": "John Doe",
    "age": 30,
    "email": "john.doe@example.com"
  }


### Get Person Details by Name
* **URL:** `GET /api/{name}/`
* **Description:** Retrieve details of a person by their name.
* **Example Request:**

`GET /api/John Doe/`

* #### Response:

  - HTTP 200 OK on success.
  - Example Response:

  ```json
  {
  "id": 1,
  "name": "John Doe",
  "age": 30,
  "email": "john.doe@example.com"
  }

### Update Person Details

* **URL:** PUT `/api/{user_id}/`
* **Description:** Update details of a person by their ID. You can update one or more fields.
* **Request Body:**
  - Fields to be updated (e.g., age).
* **Example Request:**
  ```json
  {
    "age": 31
  }

* #### Response:

  - HTTP 200 OK on success.
  - Example Response:
  ```json
  {
  "id": 1,
  "name": "John Doe",
  "age": 31,
  "email": "john.doe@example.com"
  }
  
### Delete Person

* **URL:** DELETE `/api/{user_id}/`
* **Description:** Delete a person by their ID.
* **Example Request:**

  `DELETE /api/1/`

#### Response:

- `HTTP 204 No Content` on success.


## Data Validation

The API includes a data validation middleware function validateName that ensures the name property is present and not empty for the POST and PUT requests. If the validation fails, an

Error response with status code 400 and an error message will be returned.

## Known Limitations and Assumptions

The API assumes that the SQLite database is already set up and running. The API assumes that the required environment variables (database credentials) are properly configured in the .env file.

## Local Setup and Deployment

To set up and deploy the API locally or on a server, please refer to the [README.md](https://github.com/LoneStarrD/hgnx_backend_tasktwo/blob/main/README.md) file in the GitHub repository for detailed instructions.