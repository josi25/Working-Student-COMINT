import pytest
from report import Report

def test_valid_tester():
    report = Report("Emilia", "08 2002", "pass", "Description", "Result")
    assert report.tester == "Emilia"

def test_invalid_tester():
    with pytest.raises(ValueError):
        Report("invalid_tester", "08 2002", "pass", "Description", "Result")

def test_invalid_date():
    with pytest.raises(ValueError):
        Report("Emilia", "invalid_date", "pass", "Description", "Result")

def test_invalid_status():
    with pytest.raises(ValueError):
        Report("Emilia", "08 2002", "invalid_status", "Description", "Result")

def test_empty_description():
    report = Report("Emilia", "08 2002", "pass", "", "Result")
    assert report.description == ""

def test_empty_result():
    report = Report("Emilia", "08 2002", "pass", "Description", "")
    assert report.result == ""