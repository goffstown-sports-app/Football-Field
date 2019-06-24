import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import utility_functions as UF


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
    if gender.lower() is not "f" or gender.lower() is not "m":
        raise Exception("Gender isn’t f or m")

    # Data manipulations:
    if varsity:
        collection_name = "varsity-scores"
    elif not varsity:
        collection_name = "jv-scores"
    document_name = gender.upper() + "-" + sport.lower()

    # Firestore interactions:
    cred = credentials.Certificate("firestore_creds.json")
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    doc_ref = db.collection(collection_name).document(document_name)
    doc_ref.set({
        "period": period,
        "away_score": away_score,
        "currently_playing": True,
        "game_time": game_time,
        "home_score": home_score,
        "away_team_name": away_team_name,
    })


# Testing:
# upload_score_data(4, 1, "00:02:45", 2, "Jaguars", "soccer", "Now", "Later", True, "m")



