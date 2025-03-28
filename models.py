# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class PlayerStats(db.Model):
    __tablename__ = 'player_stats'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    batting_average = db.Column(db.Float)
    home_runs = db.Column(db.Integer)
    strikeouts = db.Column(db.Integer)

    def __repr__(self):
        return f'<PlayerStats {self.name}>'
