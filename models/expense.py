from app import db


class Expense(db.Model):
    """Entails details of an expenditure"""
    user_id = db.Column(db.Integer, foreign_key=True)
    expense_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Integer(50), nullable=False)
    created = db.Column(db.datetime, nullable=False)
