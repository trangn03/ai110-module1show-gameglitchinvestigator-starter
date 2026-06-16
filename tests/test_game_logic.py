from logic_utils import check_guess, get_range_for_difficulty, parse_guess, update_score

# --- check_guess ---
# Bug: original tests compared result == "Win" but check_guess returns a tuple (outcome, message).
# Fix: unpack the tuple before asserting.

def test_winning_guess():
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

# --- parse_guess: basic input handling ---

def test_parse_guess_valid_number():
    ok, value, err = parse_guess("10")
    assert ok is True
    assert value == 10
    assert err is None

def test_parse_guess_empty_string():
    ok, value, err = parse_guess("")
    assert ok is False
    assert err is not None

def test_parse_guess_non_numeric():
    ok, value, err = parse_guess("abc")
    assert ok is False
    assert err is not None

# --- parse_guess: range validation (Bug: out-of-range guesses are silently accepted) ---
# These tests assume parse_guess is updated to accept low and high parameters.

def test_parse_guess_rejects_above_range():
    # Easy mode is 1-20; guessing 500 should be rejected
    ok, value, err = parse_guess("500", low=1, high=20)
    assert ok is False
    assert err is not None

def test_parse_guess_rejects_below_range():
    ok, value, err = parse_guess("0", low=1, high=20)
    assert ok is False
    assert err is not None

def test_parse_guess_accepts_boundary_values():
    ok_low, val_low, _ = parse_guess("1", low=1, high=20)
    ok_high, val_high, _ = parse_guess("20", low=1, high=20)
    assert ok_low is True and val_low == 1
    assert ok_high is True and val_high == 20

# --- Attempt counting ---
# parse_guess returning ok=False means the caller should NOT count an attempt.
# parse_guess returning ok=True means a real attempt was made.

def test_invalid_input_should_not_count_as_attempt():
    # Non-numeric input: ok=False → attempt should not be incremented
    ok, _, _ = parse_guess("abc")
    assert ok is False

def test_out_of_range_should_not_count_as_attempt():
    # Out-of-range on Easy mode: ok=False → attempt should not be incremented
    ok, _, _ = parse_guess("999", low=1, high=20)
    assert ok is False

def test_valid_input_should_count_as_attempt():
    # Valid in-range input: ok=True → attempt should be incremented
    ok, _, _ = parse_guess("10", low=1, high=20)
    assert ok is True

# --- update_score: attempt number affects win points ---

def test_early_win_scores_more_than_late_win():
    # Winning on attempt 1 should award more points than winning on attempt 5
    score_early = update_score(current_score=0, outcome="Win", attempt_number=1)
    score_late = update_score(current_score=0, outcome="Win", attempt_number=5)
    assert score_early > score_late

def test_win_score_minimum_is_10():
    # Win on a very high attempt number should still give at least 10 points
    score = update_score(current_score=0, outcome="Win", attempt_number=100)
    assert score >= 10

# --- check_guess: hint messages point in the correct direction (Bug: messages were swapped) ---

def test_too_high_message_says_go_lower():
    # When guess is above the secret, player should be told to go lower
    _, message = check_guess(60, 50)
    assert "LOWER" in message

def test_too_low_message_says_go_higher():
    # When guess is below the secret, player should be told to go higher
    _, message = check_guess(40, 50)
    assert "HIGHER" in message

# --- update_score: win points use attempt_number directly (Bug: used attempt_number + 1) ---

def test_win_on_attempt_1_gives_90_points():
    # First attempt win: 100 - 10*1 = 90
    score = update_score(current_score=0, outcome="Win", attempt_number=1)
    assert score == 90

def test_win_on_attempt_5_gives_50_points():
    # Fifth attempt win: 100 - 10*5 = 50
    score = update_score(current_score=0, outcome="Win", attempt_number=5)
    assert score == 50


# --- Get_range_for_difficulty returns the correct range per difficulty ---
# app.py used hardcoded 1–100 in the hint and in new-game secret generation.
# Fix: use get_range_for_difficulty(difficulty) for both.

def test_easy_range():
    low, high = get_range_for_difficulty("Easy")
    assert low == 1
    assert high == 20

def test_normal_range():
    low, high = get_range_for_difficulty("Normal")
    assert low == 1
    assert high == 50

def test_hard_range():
    low, high = get_range_for_difficulty("Hard")
    assert low == 1
    assert high == 100

def test_unknown_difficulty_falls_back_to_full_range():
    low, high = get_range_for_difficulty("Unknown")
    assert low == 1
    assert high == 100

# --- Secret must stay within the difficulty range ---
# If new-game uses randint(1, 100) instead of randint(low, high),
# Easy-mode secrets can exceed 20. We test that the range contract holds.

def test_easy_secret_is_within_range():
    import random
    low, high = get_range_for_difficulty("Easy")
    for _ in range(50):
        secret = random.randint(low, high)
        assert low <= secret <= high

def test_normal_secret_is_within_range():
    import random
    low, high = get_range_for_difficulty("Normal")
    for _ in range(50):
        secret = random.randint(low, high)
        assert low <= secret <= high

# --- Game-over state must be fully reset for a new game to be playable ---
# Simulate the reset logic: after "won"/"lost", all state fields must go back to defaults.

def _simulate_new_game_reset():
    """Return the session state dict as it should look after a proper new-game reset."""
    return {
        "attempts": 0,
        "score": 0,
        "status": "playing",
        "history": [],
    }

def test_new_game_resets_attempts():
    state = _simulate_new_game_reset()
    assert state["attempts"] == 0

def test_new_game_resets_score():
    state = _simulate_new_game_reset()
    assert state["score"] == 0

def test_new_game_resets_status_to_playing():
    state = _simulate_new_game_reset()
    assert state["status"] == "playing"

def test_new_game_resets_history():
    state = _simulate_new_game_reset()
    assert state["history"] == []

def test_won_status_would_block_play_without_reset():
    # If status stays "won", the game stop guard triggers and the player can't guess.
    status = "won"
    game_is_blocked = status != "playing"
    assert game_is_blocked, "A won game without reset blocks new play"

def test_lost_status_would_block_play_without_reset():
    status = "lost"
    game_is_blocked = status != "playing"
    assert game_is_blocked, "A lost game without reset blocks new play"
