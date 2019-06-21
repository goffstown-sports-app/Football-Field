import firebase_admin
from firebase_admin import credentials


def upload(home_score, away_score, game_time, period, away_team_name, sport, event_start, event_end):
    """
    Uploads data to the database
    :param home_score: GHS score (int)
    :param away_score: Away score (int)
    :param game_time: Game time (ex: 01:25:34, str)
    :param period: Period (int)
    :param away_team_name: Away team name (str)
    :param sport: Sport Name (str)
    :param event_start: Event start time (str)
    :param event_end: Event start time (str)
    :return: none
    """
    cred = credentials.Certificate("path/to/serviceAccountKey.json")
    firebase_admin.initialize_app(cred)
    db = 
