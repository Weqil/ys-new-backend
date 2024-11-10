from models.Admins import Admin
from database import db
def setStartAdmins():
    if Admin.query.count() == 0:
        db.session.add_all(
            [
                Admin(name='Admin', password='123')
            ]
        )