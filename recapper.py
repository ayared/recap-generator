"""recapper.py
Main runner for the FPL Recap Generator
"""
from fpl import fpl_runner
from message import message_runner
from gmail import mail_runner
import argparse


def main(gameweek):
    """ main
    Main entry point for recap generation
    Args:
        gameweek (int): current gameweek to generate the recap for
    """
    subject = "Gameweek {} Recap".format(gameweek)
    json_data = fpl_runner(gameweek)
    msg = message_runner(json_data, gameweek)
    mail_runner(subject, msg)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("gameweek", help="Current Gameweek", type=int)
    args = parser.parse_args()
    main(args.gameweek)
