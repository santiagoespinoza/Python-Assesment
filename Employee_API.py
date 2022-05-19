import random
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# We create the employee records class
# This will contain employee name their id and age
class Employee(BaseModel):
    name: str
    age: int
    id: int

# We create employee records
names = ['Santiago', 'Cristiano', 'José', 'Daniela', 'Maria']
sur_names = ['Espinoza','Ronaldo', 'Gonzalez', 'Hernandez','Lopez']

# Our employee record will include 100 employees
data = []
for e in range(100):
    # Name and surname will be chosen randomly form our previous lists
    name = random.choice(names)
    sur_name = random.choice(sur_names)
    # Each will have a random age from 18 to
    temp = {'name':name+' '+sur_name, 'age': random.randrange(18, 50), 'id':e}

    # For each employee we create an instance of the employee class
    d = Employee(name = temp['name'], age = temp['age'], id = temp['id'])

    data.append(d)

# Our root method will returna all employee data 
@app.get('/')
def root():
    return data

# This method will insert an employee 
@app.put('/insert{data_id}')
def insertUser(data_id: int, new: Employee):  # put needs id and data
    print(new)
    data.append(new)
    return {'ANS': 'userInserted'}

# This method will delete an employee
@app.delete('/delete{emp_id}')
def delete_emp(emp_id: int):
    global data
    lenInit = len(data)
    data = [e for e in data if e.id != emp_id]
    print(lenInit, len(data))
    if lenInit != len(data):
        return {'ANS': 'user Deleted'}
    else:
        raise HTTPException(status_code=404, detail="Employee not found")
        return {'ANS': 'user not found'}

