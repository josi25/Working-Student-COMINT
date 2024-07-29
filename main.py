from Utils import Utils

def main():
    file_path = 'example_file_comint_systems.csv'
    reports = Utils.read_csv(file_path)

    for report in reports:
        validation_error = report.validate()
        if validation_error:
            print(validation_error)
        else:
            #print(f"Report: Tester={report.tester}, Date={report.date}, Status={report.status}, Description={report.description}, Result={report.result}")
            report_xml = Utils.convert_to_xml(report)
            print(report_xml)

if __name__ == "__main__":
    main()