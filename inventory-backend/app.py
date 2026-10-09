from flask import Flask
from models import db
from routes import api_bp

app = Flask(__name__)

# Database configuration (replace YOUR_ACTUAL_PASSWORD with your real password)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Happiness!31@localhost:5432/inventory_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database with app
db.init_app(app)

# Register our blueprint routes
app.register_blueprint(api_bp)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5000)

p