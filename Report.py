from datetime import datetime

class Report:
    valid_testers = ["Emilia", "Bob", "Charlie", "Hansi", "Sara"]
    pass_statuses = ["pass", "true", "1"]
    fail_statuses = ["fail", "false", "0"]
    DEFAULT_TESTER = "INVALID_TESTER"
    DEFAULT_DATE = "INVALID_DATE"
    DEFAULT_STATUS = "INVALID_STATUS"

    def __init__(self, tester: str, date: str, status: str, description: str, result: str):
        self.tester = tester
        self.date = date
        self.status = status
        self.description = description
        self.result = result
        self.convert_to_validTester() #convert the tester into a valid tester upon initialization
        self.convert_to_isotime()  #convert the date into iso format upon initialization
        self.convert_to_validStatus() #convert the status into valid status upon initialization


    def is_valid_tester(self):
        return self.tester != "INVALID_TESTER"

    def is_valid_date(self):
        return self.date != "INVALID_DATE"

    def is_valid_status(self):
        return self.status != "INVALID_STATUS"


    def validate(self):
        # returning an error message if the tester, date or status is invalid
        if not self.is_valid_tester():
            return f"Invalid tester: {self.tester}"
        if not self.is_valid_date():
            return f"Invalid date: {self.date}"
        if not self.is_valid_status():
            return f"Invalid status: {self.status}"
        return None

    # Method to convert the tester attribute to a valid tester name if possible
    def convert_to_validTester(self):
        for name in self.valid_testers:
            # Check if the tester name (case-insensitive) matches a valid tester
            if (self.tester.strip().lower() == name.lower()):
                # If a match is found, set the tester attribute to the valid name
                self.tester = name
                return
            else:
                continue
        # If no match is found, set the tester attribute to a default invalid tester message
        self.tester = f'{self.DEFAULT_TESTER} found with entry: {self.tester}'

    def generate_date_format():
        date_formats = []
        separators = [' ', ',', '/', '.', '-']  # List of possible separators
        months = ['%m', '%B', '%b']  # List of possible month formats

        for sep in separators:
            for month in months:
                date_formats.append(f'%d{sep}{month}{sep}%Y')
                date_formats.append(f'{month}{sep}%d{sep}%Y')
                date_formats.append(f'{month}{sep}%Y')
                date_formats.append(f'%Y{sep}{month}')

        return date_formats

    # Method to convert the date attribute to a valid date if possible
    def convert_to_isotime(self):
        # Get the list of date formats from the generate_date_format method
        date_formats = Report.generate_date_format()

        for format_string in date_formats:
            try:
                dt = datetime.strptime(self.date, format_string)
                # Convert the parsed date to ISO format and set the date attribute
                self.date = dt.date().isoformat()
                return
            except ValueError:
                continue
        # If no valid format is found, set the date attribute to a default invalid date message
        self.date = f'{self.DEFAULT_DATE} found with entry: {self.date}'

    # Method to convert the status attribute to a valid status if possible
    def convert_to_validStatus(self):
        # Check if the status (case-insensitive) is in the list of pass statuses
        if (self.status.strip().lower() in self.pass_statuses):
            self.status = "Pass"
        # Check if the status (case-insensitive) is in the list of fail statuses
        elif (self.status.strip().lower() in self.fail_statuses):
            self.status = "Fail"
        # If it is neither, set the status attribute to a default invalid status message
        else:
            self.status = f'{self.DEFAULT_STATUS} found with entry: {self.status}'
