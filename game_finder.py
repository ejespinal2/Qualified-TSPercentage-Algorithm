"""
Given the following inputs:
- <game_data> is a list of dictionaries, with each dictionary representing a player's shot attempts in a game. The list can be empty, but any dictionary in the list will include the following keys: gameID, playerID, gameDate, fieldGoal2Attempted, fieldGoal2Made, fieldGoal3Attempted, fieldGoal3Made, freeThrowAttempted, freeThrowMade. All values in this dictionary are ints, except for gameDate which is of type str in the format 'MM/DD/YYYY'
- <true_shooting_cutoff> is the minimum True Shooting percentage value for a player to qualify in a game. It will be an int value >= 0.
- <player_count> is the number of players that need to meet the <true_shooting_cutoff> in order for a gameID to qualify. It will be an int value >= 0.

Implement find_qualified_games to return a list of unique qualified gameIDs in which at least <player_count> players have a True Shooting percentage >= <true_shooting_cutoff>, ordered from most to least recent game.
"""

def find_qualified_games(game_data: list[dict], true_shooting_cutoff: int, player_count: int) -> list[int]:
	# Replace the line below with your code

	def calculate_true_shooting_percentage(fG2Attempted, fG2Made, fG3Attempted, fG3Made, fTAttempted, ftMade) -> float:
		total_shots = fG2Attempted + fG3Attempted+ 0.44 * fTAttempted
		total_points = 2 * fG2Made + 3 * fG3Made + fTMade
		return (total_points / (2 * total_shots)) * 100 if total_shots != 0 else 0
	
	game_stats = {}


	#Organize shots/data
	for game in game_data:

		gameID=game['gameID']

		fG2Attempted = game['fieldGoal2Attempted']
		fG3Attempted = game['fieldGoal3Attempted']
		fTAttempted = game['freeThrowAttempted']
		fG2Made = game['fieldGoal2Made']
		fG3Made = game['fieldGoal3Made']
		fTMade = game['freeThrowMade']

		ts_percentage = calculate_true_shooting_percentage(fG2Attempted, fG2Made, fG3Attempted, fG3Made, fTAttempted, fTMade)

		#Create entries for new game ID's
		if gameID not in game_stats:
			game_stats[gameID] = {'gameDate': game['gameDate'], 'percentages': []}

		game_stats[gameID]['percentages'].append(ts_percentage)

	#List holds qualified games
	qualified_games=[] 
	
	#Check for player sthat meet the true shooting cutoff
	for gameID, stats in game_stats.items():
		qualified_players = [ts for ts in stats['percentages'] if ts >= true_shooting_cutoff]
		if len(qualified_players) >= player_count:
			qualified_games.append((gameID, stats['gameDate']))

	#Convert date to be sortable
	def convert_date(date_str: str) -> tuple:
		month, day, year = map(int, date_str.split('/'))
		return (year, month, day)
	
	#Sort game dates
	qualified_games.sort(key=lambda x: convert_date(x[1]), reverse=True)

	#Return sorted list of gameIDs

	return [game[0]for game in qualified_games]


	








		
