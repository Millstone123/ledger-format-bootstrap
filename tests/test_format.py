from ledger_formatting.format import align_rows

def test_sample_formatting():
    rows = [["date", "account"], ["2026-01-15", "1010"]]
    assert all(len(row) == 2 for row in rows)
    assert all(isinstance(cell, str) for row in rows for cell in row)
