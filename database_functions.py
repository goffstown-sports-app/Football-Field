import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import utility_functions as UF
import json


def upload_score_data(home_score, away_score, game_time, period, away_team_name, sport, event_start, event_end, varsity, gender):
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
    :param varsity: Varsity or Junior Varsity (Boolean)
    :param gender: Either "m" or "w"
    :return: none
    """
    # Type checking:
    UF.check_type(home_score, "int")
    UF.check_type(away_score, "int")
    UF.check_type(game_time, "str")
    UF.check_type(period, "int")
    UF.check_type(away_team_name, "str")
    UF.check_type(sport, "str")
    UF.check_type(event_start, "str")
    UF.check_type(event_end, "str")
    UF.check_type(varsity, "bool")
    UF.check_type(gender, "str")
    if gender.lower() == "f" or gender.lower() == "m":
        pass
    else:
        raise Exception("Gender isn’t f or m")

    # Data manipulations:
    if varsity:
        child_name = "varsity-scores/" + gender.upper() + "-" + sport.lower()
    else:
        child_name = "jv-scores/" + gender.upper() + "-" + sport.lower()

    # Realtime Database interactions:
    cred = credentials.Certificate("firestore_creds.json")
    firebase_admin.initialize_app(cred, {"databaseURL": "https://ghs-app-5a0ba.firebaseio.com"})
    ref = db.reference("scores")
    child_ref = ref.child(child_name)
    child_ref.set({
        "home-score": home_score,
        "away-score": away_score,
        "game-time": game_time,
        "period": period,
        "away-team-name": away_team_name,
        "event-start": event_start,
        "event-end": event_end
    })

    # Writing last reading
    with open("last_write.json", "w") as last_write_json:
        data = [
            home_score,
            away_score,
            game_time,
            period,
            away_team_name,
            sport,
            event_start,
            event_end,
            varsity,
            gender
        ]
        json.dump(data, last_write_json)


# Testing:
# upload_score_data(4, 1, "00:02:45", 2, "Jaguars", "soccer", "Now", "Later", True, "m")

def init_database(list_of_sports):
    """
    Initializes the firestore database
    :param list_of_sports: list of supported sports. Each sport should be marked like "V-M-Sport"
    :return: none
    """
    # Check types:
    UF.check_type(list_of_sports, "list")
    for sport in list_of_sports:
        items = sport.split("-")
        if len(items) != 3:
            raise Exception("It seems as though the sports came in wrong from the init_database function")
        if items[0].lower() != "v" and items[0].lower() != "jv":
            raise Exception("It seems as though the varsity sports came in wrong for the init_database function")
        if items[1].lower() != "f" and items[1].lower() != "m":
            raise Exception("Item seems as though the gender came in wrong for the init_database function")

    # Firestore interactions:
    cred = credentials.Certificate("firestore_creds.json")
    firebase_admin.initialize_app(cred, {"databaseURL": "https://ghs-app-5a0ba.firebaseio.com"})
    ref = db.reference("scores")
    for sport in list_of_sports:
        items = sport.split("-")
        if items[0].lower() == "v":
            child_name = "varsity-scores/" + items[1].upper() + "-" + items[2].lower()
        else:
            child_name = "jv-scores/" + items[1].upper() + "-" + items[2].lower()
        child_ref = ref.child(child_name)
        child_ref.set({
            "home-score": 0,
            "away-score": 0,
            "game-time": "00:00:00",
            "period": 0,
            "away-team-name": "",
            "event-start": "",
            "event-end": ""
        })


# Testing:
init_database([
    "V-M-Soccer",
    "JV-M-Soccer",
    "V-F-Soccer",
    "JV-F-Soccer",
    "V-M-Football",
    "JV-M-Football",
    "V-M-Baseball",
    "JV-M-Baseball",
    "V-F-Softball",
    "JV-F-Softball",
    "V-F-Field_Hockey",
    "JV-F-Field_Hockey",
    "V-M-Volleyball",
    "JV-M-Volleyball",
    "V-F-Volleyball",
    "JV-F-Volleyball",
    "V-M-Basketball",
    "JV-M-Basketball",
    "V-F-Basketball",
    "JV-F-Basketball",
    "V-M-Lacrosse",
    "JV-M-Lacrosse",
    "V-F-Lacrosse",
    "JV-F-Lacrosse"
])



