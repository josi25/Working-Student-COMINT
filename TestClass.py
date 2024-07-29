import pytest
from Report import Report
from Utils import Utils

class Test:

    def test_convert_to_xml(selftest_report):
        report = Report("Alice", "14/08/2002", "Pass", "Good", "Result")

        # Convert the Report object to XML format using the Utils.convert_to_xml method
        xml_output = Utils.convert_to_xml(report)

        # Define the expected XML output as a multiline string
        expected_xml_output = """
                <testReport>
                <tester>Alice</tester>
                <date>2002-08-14</date>
                <status>Pass</status>
                <description>Good</description>
                <result>Result</result>
                </testReport>"""


        # Compare the expected XML output string to the actual XML output
        assert xml_output == ''.join(expected_xml_output.split())