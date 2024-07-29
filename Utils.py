import csv
from Report import Report
import xml.etree.ElementTree as ET

from setuptools.config._validate_pyproject import ValidationError


class Utils:

    # method to read in csv file
    def read_csv(file_path: str):
        reports = []
        try:
            with open(file_path, mode='r', encoding='utf-8-sig') as file:
                # Create a CSV reader object with ';' as the delimiter
                csv_reader = csv.DictReader(file, delimiter=';')
                for row in csv_reader:
                    try:
                        # Validate the current row
                        Utils.validate_row(row)
                        # Create a Report object from the row data
                        report = Report(
                            tester=row["Tester"],
                            date=row["Date"],
                            status=row["Status"],
                            description=row["Description"],
                            result=row["Result"]
                        )
                        reports.append(report)
                    except ValueError as ve:
                        print(f"Value error: {ve}")
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except PermissionError:
            print(f"Permission denied: {file_path}")
        except Exception as e:
            print(f"Unexpected error: {e}")

        return reports

    def validate_row(row):
        # List of required columns in the CSV row
        required_columns = ["Tester", "Date", "Status", "Description", "Result"]
        if not all(col in row for col in required_columns):
            raise ValueError(f"Missing column {col} in row {row}")

    # Method to convert a Report object to an XML string
    def convert_to_xml(test_report):
        # Create the root element <testReport>
        report = ET.Element("testReport")

        # Create and append the <tester> element to the root element
        tester = ET.SubElement(report, "tester")
        # Set the text content of the <tester> element to the tester attribute of the Report object
        tester.text = test_report.tester

        date = ET.SubElement(report, "date")
        date.text = test_report.date

        status = ET.SubElement(report, "status")
        status.text = test_report.status

        description = ET.SubElement(report, "description")
        description.text = test_report.description

        result = ET.SubElement(report, "result")
        result.text = test_report.result

        # Convert the XML tree to a string and return it
        return ET.tostring(report, encoding='unicode')


