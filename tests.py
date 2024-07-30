import pytest
from report import Report

def test_valid_date():
    report = Report("Emilia", "12.08.2002", "pass", "Description", "Result")
    assert report.date == "2002-08-12"

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

def test_edgecase_date():
    with pytest.raises(ValueError):
        Report("Emilia", "49.08.2002", "pass", "Description", "Result")

