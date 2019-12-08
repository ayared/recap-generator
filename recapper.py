"""recapper.py
Main runner for the FPL Recap Generator
"""
from fpl import fpl_runner
from message import message_runner
from gmail import mail_runner


def main():
    gameweek = input("Enter the current gameweek: ")
    subject = "Gameweek {} Recap".format(gameweek)

    json_data = fpl_runner(gameweek)
    msg = message_runner(json_data, gameweek)
    mail_runner(subject, msg)

if __name__ == '__main__':
    main()
