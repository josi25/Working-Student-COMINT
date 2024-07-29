import csv
import xml.etree.ElementTree as ET
from setuptools.config._validate_pyproject import ValidationError
from report import Report


def read_csv(file_path: str):
    reports = []

    with open(file_path, mode='r', encoding='utf-8-sig') as file:
        # Create a CSV reader object with ';' as the delimiter
        csv_reader = csv.DictReader(file, delimiter=';')
        for row in csv_reader:
            try:
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
                print(f"Value error occured: {ve}")


    return reports

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

def main():
    file_path = 'example_file_comint_systems.csv'
    reports = read_csv(file_path)

    for report in reports:
        #print(f"Report: Tester={report.tester}, Date={report.date}, Status={report.status}, Description={report.description}, Result={report.result}")
        report_xml = convert_to_xml(report)
        print(report_xml)




if __name__ == "__main__":
    main()