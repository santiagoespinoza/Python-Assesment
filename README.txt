Francisco Santiago Espinoza Márquez

Employee_API.py creates an API that returns employee data.

First, this codes creates records for 100 employees randomly and stores them in a dataset.

Then it creates the API app with FastAPI. This API has three one methods:
  - root(): This method returns all the employee records
  - insert(): This will insert a new employee record to our dataset. REQUIERES AN EMPLOYEE ID.
  - delete(): This will delete an employee record given its index.

In order to execute this app, we need open to the console, and go to the .py file location.
From there we run 'uvicorn Employee_API:app'. Once we run this line, on our browser we go to "http://127.0.0.1:8000/docs" and there will be able to run the methods. 


