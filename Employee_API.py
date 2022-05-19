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

