import os
import csv
from typing import Set


class CSVHandler:
    """
    A class to handle CSV operations.
    """

    def __init__(self, file_path: str):
        self.file_path = file_path
        self._ensure_file_exists()

    def _ensure_file_exists(self):
        """Ensure the CSV file exists."""
        if not os.path.exists(self.file_path):
            with open(self.file_path, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Email"])

    def save_emails(self, emails: Set[str]):
        """Save unique emails to the CSV file."""
        existing_emails = self._read_existing_emails()
        new_emails = emails - existing_emails

        with open(self.file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            for email in new_emails:
                writer.writerow([email])

    def _read_existing_emails(self) -> Set[str]:
        """Read existing emails from the CSV file."""
        with open(self.file_path, mode='r') as file:
            reader = csv.reader(file)
            return set(row[0] for row in reader if row)