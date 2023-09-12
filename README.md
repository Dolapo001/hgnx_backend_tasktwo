# Person API


The Person API is a simple RESTful web service for managing person records. It provides endpoints for performing CRUD (Create, Read, Update, Delete) operations on person data. This README provides essential information on setting up, running, and using the API.
# Person Postman Documentation
dd

# Prerequisites

Before you get started, make sure you have the following software and tools installed:

* Python (3.6 or higher)
* Django (3.2 or higher)
* Django Rest Framework (DRF) (3.12 or higher)
* PostgreSQL (or another database of your choice)


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

**Create a new person:** POST /api/

**Fetch details of a person by ID**: GET /api/{user_id}/

**Update details of an existing person by ID:** PUT /api/{user_id}/

**Remove a person by ID:** DELETE /api/{user_id}/
