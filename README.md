# Person API

The Person API is a simple RESTful web service for managing person records. It provides endpoints for performing CRUD (Create, Read, Update, Delete) operations on person data. This README provides essential information on setting up, running, and using the API.


# Prerequisites

Before you get started, make sure you have the following software and tools installed:

* Python (3.6 or higher)
* Django (3.2 or higher)
* Django Rest Framework (DRF) (3.12 or higher)
* SQLite


# Installation

## 1. Clone the repository:
`git clone https://github.com/LoneStarrD/hgnx_backend_tasktwo.git
`
## 2. Change into the project directory:
`cd person_api`

## 3. Create a virtual environment:
`python -m venv venv`

## 4. Activate the virtual environment:
* On Windows, activate the virtual environment:

`env\Scripts\activate`

* On macOS and Linux, activate the virtual environment:

`source env/bin/activate`

## 5. Install project dependencies:

`pip install -r requirements.txt`

# Usage

## Running the Development Server
### To run the development server, execute the following command:

`python manage.py runserver`

The API will be available at http://localhost:8000/api

# API Endpoints
### The API provides the following endpoints for managing person data:

**Create a new person:** `POST /api/`

**Fetch details of a person by ID**: `GET /api/{user_id}/` or `GET /api/{user_name}/`

**Update details of an existing person by ID:** PUT /api/{user_id}/

**Remove a person by ID:** DELETE /api/{user_id}/

# Authentication and Authorization

The API currently does not include authentication or authorization mechanisms. It assumes open access to all endpoints. For production use, consider implementing authentication and authorization as needed.

# Dynamic Parameter Handling

The API supports dynamic parameter handling. You can filter person records based on dynamic input, such as name, by providing query parameters in the request URL. For example:

* GET /api/name=John will return persons with names containing "John."


# Documentation
Comprehensive API documentation is available in the [Documentation.md](https://github.com/LoneStarrD/hgnx_backend_tasktwo/blob/main/Documentation.md)


# Known Limitations

* The API assumes that the person's name is a required field for creating and updating a person record.
* The API currently does not include authentication or authorization mechanisms.
* Basic validation is in place to ensure that fields like name are of type string.