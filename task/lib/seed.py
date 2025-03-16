from sqlalchemy import create_engine
from models import Base, Employee, Task, Project, Department
from sqlalchemy.orm import sessionmaker

# Create the engine
engine = create_engine("sqlite:///task_management_system.db")

# Create tables
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

try:
    # Create instances
    department = Department(name="Moringa Stuff")
    employee1 = Employee(name="Victor Kuria", email="victo.k.moringaschool@gmail.com", department=department)
    employee2 = Employee(name="Mercy Nzau", email="mercy.nzau.moringaschool@gmail.com", department=department)
    employee3 = Employee(name="Bin Amin", email="bin.amin.moringaschool@gmail.com", department=department)
    
    project = Project(name="Ecommerce", title="Ecommerce Project", description="Design an ecommerce website")
    
    task = Task(title="Design ecommerce website", description="Design ecommerce as people should be able to view their currency", due_date=None, employee=employee1, project=project)

    # Assigning departments to the employees (already done in the constructor)
    # Assigning project to the employees
    project.employees = [employee1, employee2, employee3]

    # Assigning task to the employees
    task.employee = employee1
    task.project = project

    # Add and commit
    session.add_all([department, employee1, employee2, employee3, project, task])
    session.commit()

except Exception as e:
    print(f"An error occurred: {e}")
    session.rollback()  # Rollback in case of error
finally:
    session.close()  # Ensure the session is closed