import requests
from models import PlayerStats, db

API_URL = "https://api.mlb.com/stats/{player_id}"  # Replace with actual MLB API URL

def get_player_stats(player_id):
    """
    Fetch player stats from the API using the player_id.
    """
    url = API_URL.format(player_id=player_id)
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()  # Parse the JSON response from the API
        return parse_player_stats(data)  # Process the data
    else:
        return None

def parse_player_stats(data):
    """
    Parse relevant player stats from the API response.
    """
    player_name = data.get('player_name')
    batting_average = data.get('batting_average')
    home_runs = data.get('home_runs')
    strikeouts = data.get('strikeouts')
    
    return {
        'name': player_name,
        'batting_average': batting_average,
        'home_runs': home_runs,
        'strikeouts': strikeouts
    }

def store_player_stats(stats):
    """
    Store player stats in the database.
    If the player already exists, update the stats; otherwise, create a new record.
    """
    player = PlayerStats.query.filter_by(name=stats['name']).first()
    
    if not player:
        player = PlayerStats(
            name=stats['name'],
            batting_average=stats['batting_average'],
            home_runs=stats['home_runs'],
            strikeouts=stats['strikeouts']
        )
        db.session.add(player)
        db.session.commit()
    return player
