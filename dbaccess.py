import db.user_orm_sqlite as user_orm
from typing import List, Dict, Any

def add_user(name: str, email: str) -> int:
    """
    Adds a user to the database and returns the user ID.
    
    :param name: Name of the user
    :param email: Email of the user
    :return: User ID of the newly added user
    """
    user = user_orm.User(name=name, email=email)
    session = user_orm.Session()
    session.add(user)
    session.commit()
    user_id = user.id
    session.close()
    return user_id

def get_all_users() -> List[Dict[str, Any]]:
    """
    Retrieves all users from the database.
    
    :return: List of dictionaries containing user details
    """
    session = user_orm.Session()
    users = session.query(user_orm.User).all()
    user_list = [{'id': user.id, 'name': user.name, 'email': user.email} for user in users]
    session.close()
    return user_list

def insert_user(name: str, email: str) -> None:
    """
    Inserts a user into the SQLite database.
    
    :param name: Name of the user
    :param email: Email of the user
    """
    user_id = add_user(name, email)
    print(f"User added with ID: {user_id}")

def delete_user(user_id: int) -> None:
    """
    Deletes a user from the database by user ID.
    
    :param user_id: ID of the user to be deleted
    """
    session = user_orm.Session()
    user = session.query(user_orm.User).filter_by(id=user_id).first()
    if user:
        session.delete(user)
        session.commit()
        print(f"User with ID {user_id} deleted.")
    else:
        print(f"User with ID {user_id} not found.")
    session.close()

def update_user(user_id: int, name: str = None, email: str = None) -> None:
    """
    Updates a user's details in the database.
    
    :param user_id: ID of the user to be updated
    :param name: New name of the user (optional)
    :param email: New email of the user (optional)
    """
    session = user_orm.Session()
    user = session.query(user_orm.User).filter_by(id=user_id).first()
    if user:
        if name:
            user.name = name
        if email:
            user.email = email
        session.commit()
        print(f"User with ID {user_id} updated.")
    else:
        print(f"User with ID {user_id} not found.")
    session.close()


print("welcome to the user management system")
print("1. Add User")
print("2. Get All Users")
print("3. Delete User")
print("4. Update User")

choice = input("Enter your choice (1-4): ")
if choice == '1':
    name = input("Enter user name: ")
    email = input("Enter user email: ")
    insert_user(name, email)
elif choice == '2':
    users = get_all_users()
    print("List of users:")
    for user in users:
        print(f"ID: {user['id']}, Name: {user['name']}, Email: {user['email']}")        
elif choice == '3':
    user_id = int(input("Enter user ID to delete: "))
    delete_user(user_id)    
elif choice == '4':
    user_id = int(input("Enter user ID to update: "))
    name = input("Enter new name (leave blank to keep current): ")
    email = input("Enter new email (leave blank to keep current): ")
    update_user(user_id, name if name else None, email if email else None)
else:
    print("Invalid choice. Please try again.")
# This script provides a simple user management system using SQLAlchemy ORM with SQLite.
# It allows adding, retrieving, deleting, and updating users in the database.