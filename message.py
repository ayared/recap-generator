"""message.py
Creates the actual email message to send!
"""


def message_runner(json_data, gameweek):
    msg = create_intro("", gameweek)
    msg = parse_scores(json_data, msg)
    msg = create_outro(msg, gameweek)
    return msg


def create_intro(msg, gameweek):
    """create_intro
    Creates the intro message for the email

    Args:
        msg: string to append intro to
        gameweek: (int) the current gameweek
    Returns:
        intro: intro message for email
    """
    msg += "Hello everyone,\n\nWelcome to a partially-programatically generated\
 gameweek {} recap!\n\n".format(gameweek)
    return msg


def parse_scores(json_data, msg):
    """parse_scores
    Takes in json data from API query and returns email body

    Args:
        json_data: json formatted gameweek data
        msg: string to append parsed scores to
    Returns:
        msg: matches written up with scores and team names
    """

    for result in json_data["results"]:
        if result["entry_1_draw"]:
            msg += "{}'s {} tied {}'s {} {}-{}\n\n".format(
                result["entry_1_player_name"],
                result["entry_1_name"],
                result["entry_2_player_name"],
                result["entry_2_name"],
                result["entry_1_points"],
                result["entry_2_points"])

        elif result["entry_1_win"]:
            msg += "{}'s {} beat {}'s {} {}-{}\n\n".format(
                result["entry_1_player_name"],
                result["entry_1_name"],
                result["entry_2_player_name"],
                result["entry_2_name"],
                result["entry_1_points"],
                result["entry_2_points"])

        elif result["entry_2_win"]:
            msg += "{}'s {} beat {}'s {} {}-{}\n\n".format(
                result["entry_2_player_name"],
                result["entry_2_name"],
                result["entry_1_player_name"],
                result["entry_1_name"],
                result["entry_2_points"],
                result["entry_1_points"])

        else:  # could be none of the above if the gameweek isn't over!
            msg += "{}'s {} {} {}'s {} {}\n\n".format(
                result["entry_1_player_name"],
                result["entry_1_name"],
                result["entry_1_points"],
                result["entry_2_player_name"],
                result["entry_2_name"],
                result["entry_2_points"])

    return msg


def create_outro(msg, gameweek):
    """create_outro
    Creates the outro message for the email

    Args:
        msg: string to append outro to
        gameweek: (int) the current gameweek
    Returns:
        outro: outro message for email
    """
    next_week = int(gameweek) + 1
    next_str = str(next_week)

    msg += "That's it for this week, the gameweek {} deadline is [***], so\
 make sure to get your trades and trash-talking in before then!\n\n\
Your humble league administrator,\nAlexander".format(next_str)

    return msg


def main():
    json_data = None
    gameweek = 14
    msg = create_intro("", gameweek)
    msg = parse_scores(json_data, msg)
    msg = create_outro(msg, gameweek)

if __name__ == '__main__':
    main()
