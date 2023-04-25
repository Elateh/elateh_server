from app import db

class Healthcheck(db.Model):
    __tablename__ = 'healthcheck'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    version = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(255), unique=False, nullable=False)