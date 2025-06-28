from sqlalchemy import create_engine,Table,Column,Integer,String,ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker


base=declarative_base()

class User(base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True )
    name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)

    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def __repr__(self):
        return f"<User(name={self.name}, email={self.email})>"


engine = create_engine('sqlite:///users.db', echo=True)
base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

user=User(name="raj mehta", email="rajm267747@gmail.com")
session.add(user)
session.commit()

print("User added with ID:",user.id)

session.close()

