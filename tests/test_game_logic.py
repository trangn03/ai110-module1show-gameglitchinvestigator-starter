from logic_utils import check_guess, parse_guess, update_score

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
