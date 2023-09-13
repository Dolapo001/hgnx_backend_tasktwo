# Person API Documentation

## Overview

The Person API provides endpoints to manage information about individuals, such as name, age, and email. You can perform basic CRUD (Create, Read, Update, Delete) operations on person records using this API.

## Base URL

The base URL for accessing the Person API is `http://your-api-domain/api/`.

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
