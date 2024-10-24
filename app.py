from sqlalchemy.orm import sessionmaker
from database import User, engine
import random

Session = sessionmaker(bind=engine)

session = Session()

users = session.query(User).order_by(User.age, User.name).all()

for user in users:
    print (f"{user.name} - {user.age}")