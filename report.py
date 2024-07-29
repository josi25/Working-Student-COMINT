from datetime import datetime
from utils import generate_date_format

class Report:
    valid_testers = ["Emilia", "Bob", "Charlie", "Hansi", "Sara"]
    pass_statuses = ["pass", "true", "1"]
    fail_statuses = ["fail", "false", "0"]

    def __init__(self, tester: str, date: str, status: str, description: str, result: str):
        self.tester = tester
        self.date = date
        self.status = status
        self.description = description
        self.result = result
        self.convert_to_validTester() #convert the tester into a valid tester upon initialization
        self.convert_to_isotime()  #convert the date into iso format upon initialization
        self.convert_to_validStatus() #convert the status into valid status upon initialization


    # Method to convert the tester attribute to a valid tester name if possible
    def convert_to_validTester(self):
        found = None
        for name in self.valid_testers:
            # Check if the tester name (case-insensitive) matches a valid tester
            if (self.tester.strip().lower() == name.lower()):
                # If a match is found, set the tester attribute to the valid name
                self.tester = name
                found = name
                break
        if found is None:
            raise ValueError(f"Invalid tester: {self.tester}")


    # Method to convert the date attribute to a valid date if possible
    def convert_to_isotime(self):
        # Get the list of date formats from the generate_date_format method
        date_formats = generate_date_format()
        found = None

        for format_string in date_formats:
            try:
                dt = datetime.strptime(self.date, format_string)
                # Convert the parsed date to ISO format and set the date attribute
                self.date = dt.date().isoformat()
                found = self.date
                break
            except ValueError:
                continue

        if found is None and self.date != "":
            raise ValueError(f'Invalid date format for {self.date} with {self.tester}')

    # Method to convert the status attribute to a valid status if possible
    def convert_to_validStatus(self):
        # Check if the status (case-insensitive) is in the list of pass statuses
        if (self.status.strip().lower() in self.pass_statuses):
            self.status = "Pass"
        # Check if the status (case-insensitive) is in the list of fail statuses
        elif (self.status.strip().lower() in self.fail_statuses):
            self.status = "Fail"
        # If it is neither, raise a value error
        else:
            raise ValueError(f'Invalid status for {self.status} with {self.tester}')
