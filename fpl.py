import requests
import json
from config import FPL_LOGIN, FPL_PWD, LEAGUE_ID

GAMEWEEK = 14


def main():
    session = create_session()
    json_data = pull_league_scores(session, GAMEWEEK)
    parse_results(json_data)


def create_session():
    """create_session
    Authenticates with FPL site

    Returns: An authenticated session object
    """

    session = requests.session()

    url = 'https://users.premierleague.com/accounts/login/'
    payload = {
        'password': FPL_PWD,
        'login': FPL_LOGIN,
        'redirect_uri': 'https://fantasy.premierleague.com/a/login',
        'app': 'plfpl-web'
    }
    session.post(url, data=payload)

    return session


# https://fantasy.premierleague.com/api/leagues-h2h-matches/league/23440/
def pull_league_scores(session, gameweek):
    """pull_league_scores
    Retrieves league data from FPL API

    Args:
        session: authenticated session object
        gameweek: the gameweek for which to pull the scores
    Returns:
        json_data: json formatted gameweek match data
    """

    try:
        raw_data = session.get(
            'https://fantasy.premierleague.com/api/leagues-h2h-matches/league/{}/?event={}'
            .format(LEAGUE_ID, gameweek))

    except Exception as error:
        print("error: {}".format(error))

    return raw_data.json()


def parse_results(json_data):
    """parse_results
    Takes in json data from API query and returns email skeleton

    Args:
        json_data: json formatted gameweek data
    """
    msg = ''
    for result in json_data["results"]:
        print("{}'s {} {} {}'s {} {}".format(result["entry_1_player_name"],
              result["entry_1_name"], result["entry_1_points"],
              result["entry_2_player_name"], result["entry_2_name"],
              result["entry_2_points"]))


if __name__ == '__main__':
    main()
