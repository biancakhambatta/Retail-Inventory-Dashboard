from flask import Flask
from models import db
from routes import api_bp

app = Flask(__name__)

import os
from dotenv import load_dotenv

load_dotenv()
db_password = os.getenv('DB_PASSWORD')

app.config[
    'SQLALCHEMY_DATABASE_URI'
] = f'postgresql://postgres:{db_password}@localhost:5432/superstore_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)

app.register_blueprint(api_bp)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5000)

