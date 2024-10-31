This is the 'README.md' file for the project. This README will guide the user through setup, usage, and authentication, as well as provide examples of each endpoint.



1. Employee Management API

A RESTful API for managing employee records in a company. This project focuses on CRUD (Create, Read, Update, Delete) operations, token-based authentication, RESTful principles, and error handling.

2. Project Overview

The Employee Management API is designed to facilitate the management of employee data, including operations to create, list, retrieve, update, and delete employees. Key features include token-based authentication (JWT), HTTP status code handling, error handling, and pagination with filtering options.

3. Setup and Installation

3.1 Prerequisites

	- Python 3.x
	- Django 4.x
	- Django REST Framework
	- Django REST Framework SimpleJWT (for JWT authentication)
	- SQLite (default database for development)

3.2 Installation Steps

3.2.1. Clone the Repository:

   
   git clone <repository_url>
   cd employee_management
   

3.2.2. Set up Virtual Environment:

   
   python -m venv venv
   source venv/bin/activate  # For Linux/macOS
   venv\Scripts\activate     # For Windows
   

3.2.3. Install Requirements:

   
   pip install -r requirements.txt
   

3.2.4. Apply Migrations:

   python manag.py makemigrations
   python manage.py migrate
   

3.2.5. Run the Server:

   
   python manage.py runserver
   

   The server will start on 'http://127.0.0.1:8000/'.

4. Authentication

	This API uses JSON Web Tokens (JWT) for authentication. To access protected endpoints, obtain a JWT and include it in the headers of your requests.

4.1. Obtain a Token:

   Send a POST request to:

   Text:
   POST /api/token/
   

   Request Body:

   JSON
   {
     "username": "your_username",
     "password": "your_password"
   }
   

   Response:

   JSON
   {
     "refresh": "your_refresh_token",
     "access": "your_access_token"
   }
   

4.2. Use the Token:

  Include the 'access' token in the Authorization header of each request:
   Text:
   Authorization: Bearer your_access_token
   

4.3. Refresh the Token:

   To refresh an expired access token:

   Text:
   POST /api/token/refresh/
   

   Request Body:

   JSON
   {
     "refresh": "your_refresh_token"
   }
   

5. API Endpoints

5.1. Create an Employee

- URL: '/api/employees/'
- Method: 'POST'
- Authentication Required: Yes

- Request Body:

  JSON
  {
    "name": "Habot Connect",
    "email": "connecthr@habot.com",
    "department": "HR",
    "role": "Manager"
  }
  

- Response:

  - Status: 201 Created
  - Body:

    JSON
    {
      "id": 1,
      "name": "Habot Connect",
      "email": "connecthr@habot.com",
      "department": "HR",
      "role": "Manager",
      "date_joined": "2024-10-25"
    }
    

5.2. List All Employees

- URL: '/api/employees/'
- Method: 'GET'
- Authentication Required: Yes

- Optional Query Parameters:

  - 'department': Filter by department
  - 'role': Filter by role
  - 'page': Pagination (default is 10 results per page)

- Response:

  - Status: 200 OK
  - Body:

    JSON
    [
      {
        "id": 1,
        "name": "Habot Connect",
        "email": "connecthr@habot.com",
        "department": "HR",
        "role": "Manager",
        "date_joined": "2024-10-25"
      }
    ]


5.3. Retrieve a Single Employee

- URL: '/api/employees/{id}/'
- Method: 'GET'
- Authentication Required: Yes

- Response:

  - Status: 200 OK
  - Body:

    JSON
    {
      "id": 1,
      "name": "Habot Connect",
      "email": "connecthr@habot.com",
      "department": "HR",
      "role": "Manager",
      "date_joined": "2024-10-25"
    }


  - Status for Invalid ID: 404 Not Found

5.4. Update an Employee

- URL: '/api/employees/{id}/'
- Method: 'PUT'
- Authentication Required: Yes

- Request Body:

  JSON
  {
    "name": "Suhail Siddiqui",
    "email": "suhailsiddiqui1530@gmail.com",
    "department": "Engineering",
    "role": "Developer"
  }
  

- Response:

  - Status: 200 OK
  - Body:

    JSON
    {
      "id": 11,
      "name": "Suhail Siddiqui",
      "email": "suhailsiddiqui1530@gmail.com",
      "department": "Engineering",
      "role": "Developer",
      "date_joined": "2024-10-25"
    }
    

5.5. Delete an Employee

- URL: '/api/employees/{id}/'
- Method: 'DELETE'
- Authentication Required: Yes

- Response:

  - Status: 204 No Content

6.Testing

6.1. Unit Testing

To run the test suite, execute:

Terminal:
python manage.py test


The test suite covers:

1. Employee Creation: Ensures unique emails and non-empty names.
2. Fetching Employees: Pagination, filtering by department, and individual employee retrieval.
3. Updating and Deleting Employees: Verifying that updates are saved correctly and that deletes respond with 204 status.

6.2. Postman Testing

	1. Import API Endpoints: Import the Postman collection provided or create a new collection.
	2. Set Up Authentication: For each request, add the token in the Authorization header:
   	Text:
   	Authorization: Bearer <your_access_token>

6.3. Verify Responses: Test each endpoint as documented above to verify CRUD operations and error handling.


7. Troubleshooting

If you encounter issues:

1. Authentication Failure: Check token validity and ensure it's included in the Authorization header.
2. Database Issues: Ensure migrations are applied with 'python manage.py migrate'.
3. Invalid Endpoints: Verify that the API URLs in requests match the documentation exactly.

8. Summary

The Employee Management API implements RESTful practices, CRUD operations, and secure access with JWT. It features a modular design, comprehensive error handling, and scalability for small to medium-sized teams.
