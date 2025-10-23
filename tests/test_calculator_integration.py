from src import calculator


def test_perform_operation_add():
    assert calculator.perform_operation("1", 2, 3) == 5


def test_integration_flow_add(monkeypatch, capsys):
    inputs = iter(["1", "2", "3", "n"])  # choice, a, b, again='n'
    monkeypatch.setattr("builtins.input", lambda prompt="": next(inputs))
    # run interactive once (it will break when 'n')
    calculator.interactive()
    captured = capsys.readouterr()
    assert "Result:" in captured.out
    assert "Another calculation?" in captured.out
