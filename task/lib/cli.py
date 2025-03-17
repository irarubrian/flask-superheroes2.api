from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Base, Department, Employee, Project, Task

# Database setup
engine = create_engine("sqlite:///task_management_system.db")
Session = sessionmaker(bind=engine)

def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Departments")
        print("2. Employees")
        print("3. Projects")
        print("4. Tasks")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == '1':
            department_menu()
        elif choice == '2':
            employee_menu()
        elif choice == '3':
            project_menu()
        elif choice == '4':
            task_menu()
        elif choice == '5':
            print("Exiting the application. Goodbye see you next time!")
            break
        else:
            print("Invalid choice, please try again.")

def handle_success(message):
    print(f"\n{message}\n")

def department_menu():
    while True:
        print("\nDepartment Menu:")
        print("1. Create Department")
        print("2. Delete Department")
        print("3. Display All Departments")
        print("4. Find Department by ID")
        print("5. Back to Main Menu")

        choice = input("Choose an option: ").strip()
        session = Session()

        try:


            if choice == '1':
                name = input("Enter department name: ").strip()
                Department.create(session, name=name)
                handle_success(f"Department '{name}' created successfully!")

            elif choice == '2':
                id = int(input("Enter department ID to delete: ").strip())
                Department.delete(session, id=id)
                handle_success(f"Department with ID {id} deleted successfully!")

            elif choice == '3':
                departments = Department.get_all(session)
                print("\nDepartments:")
                for d in departments:
                    print(f"ID: {d.id}, Name: {d.name}")

            elif choice == '4':
                id = int(input("Enter department ID to find: ").strip())
                department = Department.find_by_id(session, id)
                if department:
                    print(f"ID: {department.id}, Name: {department.name}")
                else:
                    print(f"No Department found with ID {id}.")

            elif choice == '5':
                break
            else:
                print("Invalid choice, please try again.")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            session.close()

def employee_menu():
    while True:
        print("\nEmployee Menu:")
        print("1. Create Employee")
        print("2. Delete Employee")
        print("3. Display All Employees")
        print("4. Find Employee by ID")
        print("5. Back to Main Menu")

        choice = input("Choose an option: ").strip()
        session = Session()
        try:
            if choice == '1':
                name = input("Enter employee name: ").strip()
                department_id = int(input("Enter department ID: ").strip())
                Employee.create(session, name=name, department_id=department_id)
                handle_success(f"Employee '{name}' created successfully!")

            elif choice == '2':
                id = int(input("Enter employee ID to delete: ").strip())
                Employee.delete(session, id=id)
                handle_success(f"Employee with ID {id} deleted successfully!")

            elif choice == '3':
                employees = Employee.get_all(session)
                print("\nEmployees:")
                for e in employees:
                    print(f"ID: {e.id}, Name: {e.name}, Department ID: {e.department_id}")

            elif choice == '4':
                id = int(input("Enter employee ID to find: ").strip())
                employee = Employee.find_by_id(session, id)
                if employee:
                    print(f"ID: {employee.id}, Name: {employee.name}, Department ID: {employee.department_id}")
                else:
                    print(f"No Employee found with ID {id}.")

            elif choice == '5':
                break
            else:
                print("Invalid choice, please try again.")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            session.close()

def project_menu():
    while True:
        print("\nProject Menu:")
        print("1. Create Project")
        print("2. Delete Project")
        print("3. Display All Projects")
        print("4. Find Project by ID")
        print("5. Back to Main Menu")

        choice = input("Choose an option: ").strip()
        session = Session()
        try:
            if choice == '1':
                name = input("Enter project name: ").strip()
                description = input("Enter project description: ").strip()
                Project.create(session, name=name, description=description)
                handle_success(f"Project '{name}' created successfully!")

            elif choice == '2':
                id = int(input("Enter project ID to delete: ").strip())
                Project.delete(session, id=id)
                handle_success(f"Project with ID {id} deleted successfully!")

            elif choice == '3':
                projects = Project.get_all(session)
                print("\nProjects:")
                for p in projects:
                    print(f"ID: {p.id}, Name: {p.name}, Description: {p.description}")

            elif choice == '4':
                id = int(input("Enter project ID to find: ").strip())
                project = Project.find_by_id(session, id)
                if project:
                    print(f"ID: {project.id}, Name: {project.name}, Description: {project.description}")
                else:
                    print(f"No Project found with ID {id}.")

            elif choice == '5':
                break
            else:
                print("Invalid choice, please try again.")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            session.close()

def task_menu():
    while True:
        print("\nTask Menu:")
        print("1. Create Task")
        print("2. Delete Task")
        print("3. Display All Tasks")
        print("4. Find Task by ID")
        print("5. Back to Main Menu")

        choice = input("Choose an option: ").strip()
        session = Session()
        try:
            if choice == '1':
                title = input("Enter Task Title: ").strip()
                description = input("Enter Task Description: ").strip()
                project_id = int(input("Enter Project ID: ").strip())
                Task.create(session, title=title, description=description, project_id=project_id)
                handle_success(f"Task '{title}' created successfully!")

            elif choice == '2':
                id = int(input("Enter task ID to delete: ").strip())
                Task.delete(session, id=id)
                handle_success(f"Task with ID {id} deleted successfully!")

            elif choice == '3':
                tasks = Task.get_all(session)
                print("\nTasks:")
                for t in tasks:
                    print(f"ID: {t.id}, Title: {t.title}, Description: {t.description}, Project ID: {t.project_id}")

            elif choice == '4':
                id = int(input("Enter Task ID to find: ").strip())
                task = Task.find_by_id(session, id)
                if task:
                    print(f"ID: {task.id}, Title: {task.title}, Description: {task.description}, Project ID: {task.project_id}")
                else:
                    print(f"No Task found with ID {id}.")

            elif choice == '5':
                break
            else:
                print("Invalid choice, PLease try Again Later.")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            session.close()

if __name__ == "__main__":
    main_menu()
