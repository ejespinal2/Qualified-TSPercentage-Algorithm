from game_finder import find_qualified_games

def test_case_11():
    game_data = []
    qualified_games = find_qualified_games(game_data, 50, 1)
    assert qualified_games == []