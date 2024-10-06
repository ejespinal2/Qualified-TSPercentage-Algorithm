from game_finder import find_qualified_games

def test_case_7():
    game_data = [
        {'gameID': 1, 'playerID': 101, 'gameDate': '09/10/2023', 'fieldGoal2Attempted': 4, 'fieldGoal2Made': 2, 'fieldGoal3Attempted': 2, 'fieldGoal3Made': 1, 'freeThrowAttempted': 3, 'freeThrowMade': 2},
        {'gameID': 1, 'playerID': 102, 'gameDate': '09/10/2023', 'fieldGoal2Attempted': 5, 'fieldGoal2Made': 3, 'fieldGoal3Attempted': 1, 'fieldGoal3Made': 1, 'freeThrowAttempted': 2, 'freeThrowMade': 2}
    ]
    qualified_games = find_qualified_games(game_data, 50, 2)
    assert qualified_games == [1]
