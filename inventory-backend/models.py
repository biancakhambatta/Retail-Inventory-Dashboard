from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class SuperstoreProduct(db.Model):
    __tablename__ = 'superstore_product'

    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(255), nullable=False)
    sales = db.Column(db.Float, nullable=False)
    profit = db.Column(db.Float, nullable=False)