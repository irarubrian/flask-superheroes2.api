from sqlalchemy import Column, Integer, String, ForeignKey, Date, Table
from sqlalchemy.orm import relationship, declarative_base, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

# Association table for Employee-Project many-to-many relationship
employee_projects = Table('employee_projects', Base.metadata,
    Column('employee_id', Integer, ForeignKey('employees.id')),
    Column('project_id', Integer, ForeignKey('projects.id'))
)

class Department(Base):
    __tablename__ = 'departments'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)

    employees = relationship('Employee', backref='department', cascade="all, delete")

    def __init__(self, name):
        self.name = name

    @classmethod
    def create(cls, session, name):
        department = cls(name=name)
        session.add(department)
        session.commit()
        return department

    @classmethod
    def delete(cls, session, id):
        department = session.query(cls).filter_by(id=id).first()
        if department:
            session.delete(department)
            session.commit()

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, id):
        return session.query(cls).filter_by(id=id).first()

    def update(self, session, name):
        self.name = name
        session.commit()

class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    department_id = Column(Integer, ForeignKey('departments.id'))

    tasks = relationship('Task', backref='employee', cascade="all, delete")
    projects = relationship('Project', secondary=employee_projects, backref='employees')

    def __init__(self, name, email, department):
        self.name = name
        self.email = email
        self.department = department

    @classmethod
    def create(cls, session, name, email, department):
        employee = cls(name=name, email=email, department=department)
        session.add(employee)
        session.commit()
        return employee

    @classmethod
    def delete(cls, session, id):
        employee = session.query(cls).filter_by(id=id).first()
        if employee:
            session.delete(employee)
            session.commit()

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, id):
        return session.query(cls).filter_by(id=id).first()

    def update(self, session, name=None, email=None, department=None):
        if name:
            self.name = name
        if email:
            self.email = email
        if department:
            self.department = department
        session.commit()

class Project(Base):
    __tablename__ = 'projects'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)

    tasks = relationship('Task', backref='project', cascade="all, delete")

   # def __init__(self, name, title, description):
        #self.name = name
       # self.title = title
       # self.description = description

    @classmethod
    def create(cls, session, name, title, description):
        project = cls(name=name, title=title, description=description)
        session.add(project)
        session.commit()
        return project

    @classmethod
    def delete(cls, session, id):
        project = session.query(cls).filter_by(id=id).first()
        if project:
            session.delete(project)
            session.commit()

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, id):
        return session.query(cls).filter_by(id=id).first()

    def update(self, session, name=None, title=None, description=None):
        if name:
            self.name = name
        if title:
            self.title = title
        if description:
            self.description = description
        session.commit()

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    due_date = Column(Date, nullable=True)
    employee_id = Column(Integer, ForeignKey('employees.id'))
    project_id = Column(Integer, ForeignKey('projects.id'))

    #def __init__(self, title, description, due_date, employee, project):
       # self.title = title
       # self.description = description
        #self.due_date = due_date
       # self.employee = employee
        #self.project = project

    @classmethod
    def create(cls, session, title, description, due_date, employee, project):
        task = cls(title=title, description=description, due_date=due_date, employee=employee, project=project)
        session.add(task)
        session.commit()
        return task

    @classmethod
    def delete(cls, session, id):
        task = session.query(cls).filter_by(id=id).first()
        if task:
            session.delete(task)
            session.commit()

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, id):
        return session.query(cls).filter_by(id=id).first()

    def update(self, session, title=None, description=None, due_date=None):
        if title:
            self.title = title
        if description:
            self.description = description
        if due_date:
            self.due_date = due_date
        session.commit()
