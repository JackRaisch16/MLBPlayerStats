
from flask import Flask
from config import Config
from models import db
from routes import register_routes

app = Flask(__name__)
app.config.from_object(Config)  # Load the config from the Config class

# Initialize the database
db.init_app(app)

# Register the routes with the app
register_routes(app)

if __name__ == "__main__":
    app.run(debug=True)

