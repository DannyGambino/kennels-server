EMPLOYEES = [
    {
        "id": 1,
        "name": "Jenna Solis"
    },
    {
        "id": 2,
        "name": "Bobby Miller"
    },
    {
        "id": 3,
        "name": "Eury Perez"
    }
]

def get_all_employees():
    return EMPLOYEES

def get_single_employee(id):
    requested_location = None

    for employee in EMPLOYEES:
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee

def create_employee(employee):
    max_id = EMPLOYEES[-1]["id"]
    new_id = max_id + 1
    employee["id"] = new_id
    EMPLOYEES.append(employee)

    return employee