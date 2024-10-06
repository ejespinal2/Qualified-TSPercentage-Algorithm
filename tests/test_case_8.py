from game_finder import find_qualified_games

def test_case_8():
    game_data = [
        {'gameID': 1, 'playerID': 101, 'gameDate': '09/10/2023', 'fieldGoal2Attempted': 4, 'fieldGoal2Made': 1, 'fieldGoal3Attempted': 2, 'fieldGoal3Made': 0, 'freeThrowAttempted': 3, 'freeThrowMade': 1},
        {'gameID': 1, 'playerID': 102, 'gameDate': '09/10/2023', 'fieldGoal2Attempted': 5, 'fieldGoal2Made': 2, 'fieldGoal3Attempted': 1, 'fieldGoal3Made': 0, 'freeThrowAttempted': 2, 'freeThrowMade': 1}
    ]
    qualified_games = find_qualified_games(game_data, 60, 1)
    assert qualified_games == []  