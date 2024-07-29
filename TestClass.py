import pytest
from report import Report
from utils import Utils

def test_valid_tester():
    report = Report("emilia", "2023-07-28", "pass", "Description", "Result")
    assert report.tester == "Emilia"
