from src import calculator


def test_perform_operation_add():
    assert calculator.perform_operation("1", 2, 3) == 5


def test_integration_flow_add(monkeypatch, capsys):
    # Simulate: choice=1 (add), a=2, b=3, again="n"
    inputs = iter(["1", "2", "3", "n"])
    monkeypatch.setattr("builtins.input", lambda prompt="": next(inputs))

    calculator.interactive()
    out = capsys.readouterr().out

    assert "Result:" in out
    assert "5.0" in out


def test_interactive_invalid_choice_then_success(monkeypatch, capsys):
    # First call to perform_operation raises ValueError; second returns 42.0
    calls = {"n": 0}

    def fake_perform(choice, a, b):
        if calls["n"] == 0:
            calls["n"] += 1
            raise ValueError("Invalid operation choice")
        return 42.0

    monkeypatch.setattr(calculator, "perform_operation", fake_perform)

    inputs = iter([
        "9", "2", "3",      # first loop -> ValueError path
        "1", "20", "22",    # second loop -> success
        "n"
    ])
    monkeypatch.setattr("builtins.input", lambda prompt="": next(inputs))

    calculator.interactive()
    out = capsys.readouterr().out

    assert "Invalid input:" in out
    assert "Result: 42.0" in out


def test_interactive_zero_division_then_success(monkeypatch, capsys):
    # First call raises ZeroDivisionError; second returns 3.0
    calls = {"n": 0}

    def fake_perform(choice, a, b):
        if calls["n"] == 0:
            calls["n"] += 1
            raise ZeroDivisionError()
        return 3.0

    monkeypatch.setattr(calculator, "perform_operation", fake_perform)

    inputs = iter([
        "4", "1", "0",      # first loop -> ZeroDivisionError path
        "1", "1", "2",      # second loop -> success
        "n"
    ])
    monkeypatch.setattr("builtins.input", lambda prompt="": next(inputs))

    calculator.interactive()
    out = capsys.readouterr().out

    assert "Error: division by zero" in out
    assert "Result: 3.0" in out


def test_perform_operation_subtract():
    assert calculator.perform_operation("2", 5, 3) == 2


def test_perform_operation_multiply_stub(monkeypatch):
    # stub multiply so branch "3" executes even if utils.multiply doesn't exist yet
    monkeypatch.setattr(calculator.utils, "multiply", lambda a, b: a * b, raising=False)
    assert calculator.perform_operation("3", 2, 4) == 8


def test_perform_operation_divide_stub(monkeypatch):
    # stub divide so branch "4" executes even if utils.divide doesn't exist yet
    monkeypatch.setattr(calculator.utils, "divide", lambda a, b: a / b, raising=False)
    assert calculator.perform_operation("4", 9, 3) == 3


def test_perform_operation_invalid_choice_unit():
    import pytest
    with pytest.raises(ValueError):
        calculator.perform_operation("9", 1, 1)
