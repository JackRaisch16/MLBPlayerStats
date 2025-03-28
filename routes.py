# routes.py

from flask import render_template, request
from services import get_player_stats, store_player_stats
from models import PlayerStats, db

def register_routes(app):
    @app.route('/player', methods=['GET', 'POST'])
    def player():
        if request.method == 'POST':
            player_id = request.form['player_id']
            stats = get_player_stats(player_id)
            
            if stats:
                store_player_stats(stats)
                return render_template('player_stats.html', stats=stats)
            else:
                return "Error fetching player stats", 400
        
        return render_template('player_form.html')

    @app.route('/test_db')
    def test_db():
        # Test database connection and data insertion
        new_player = PlayerStats(name="Test Player", batting_average=0.300, home_runs=15, strikeouts=80)
        db.session.add(new_player)
        db.session.commit()
        return "Test player added to database"
