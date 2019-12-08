# recap-generator

recap-generator automatically creates the skeleton for an FPL recap email. It can be run from the command-line as ./recapper.py. 
The only input that it needs from the user is the current gameweek. 

To run successfully, you will have to create your own config.py file, structured as follows:

SENDER = [Your email address]

RECIPIENTS = [The email address or addresses you wish to draft the email to]

FPL_LOGIN = [Your fantasy.premierleague.com email address]

FPL_PWD = [Your fantasy.premierleague.com password]

LEAGUE_ID = [The ID for your league]

The league ID can be found by navigating to your league's standings on the FPL website and looking for a number in the URL after
/leagues/
