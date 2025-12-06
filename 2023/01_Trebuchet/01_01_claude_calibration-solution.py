#!/usr/bin/env python3
"""
Advent of Code 2023 - Day 1: Trebuchet?!
Processes a calibration document to extract and sum two-digit numbers from text lines.
Each number is formed by combining the first and last digits found in each line.
"""

from pathlib import Path
from typing import Iterator, Optional
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class CalibrationDocument:
    """Handles the processing of calibration documents containing encoded values."""
    
    def __init__(self, file_path: Path):
        """
        Initialize the calibration document processor.
        
        Args:
            file_path (Path): Path to the input file containing calibration data
        """
        self.file_path = Path(file_path)
        self._validate_file()

    def _validate_file(self) -> None:
        """Validate that the input file exists and is readable."""
        if not self.file_path.exists():
            raise FileNotFoundError(f"Input file not found: {self.file_path}")
        if not self.file_path.is_file():
            raise ValueError(f"Path is not a file: {self.file_path}")

    def process_lines(self) -> Iterator[str]:
        """
        Process the input file line by line.
        
        Yields:
            str: Each line from the input file
        """
        try:
            with self.file_path.open('r', encoding='utf-8') as file:
                yield from file
        except Exception as e:
            logger.error(f"Error reading file: {e}")
            raise

class CalibrationValueExtractor:
    """Extracts calibration values from text strings."""
    
    @staticmethod
    def find_digits(line: str) -> tuple[Optional[str], Optional[str]]:
        """
        Find the first and last digits in a string.
        
        Args:
            line (str): Input string to process
            
        Returns:
            tuple[Optional[str], Optional[str]]: First and last digits found
        """
        digits = [char for char in line if char.isdigit()]
        if not digits:
            return None, None
        return digits[0], digits[-1]

    @staticmethod
    def combine_digits(first: Optional[str], last: Optional[str]) -> Optional[int]:
        """
        Combine two digits into a two-digit number.
        
        Args:
            first (Optional[str]): First digit
            last (Optional[str]): Last digit
            
        Returns:
            Optional[int]: Combined two-digit number or None if invalid input
        """
        if first is None or last is None:
            return None
        return int(first + last)

class CalibrationProcessor:
    """Main processor for calibration calculations."""
    
    def __init__(self, document: CalibrationDocument):
        """
        Initialize the calibration processor.
        
        Args:
            document (CalibrationDocument): Document to process
        """
        self.document = document
        self.extractor = CalibrationValueExtractor()

    def calculate_sum(self) -> int:
        """
        Calculate the sum of all calibration values in the document.
        
        Returns:
            int: Sum of all valid calibration values
        """
        total = 0
        for line in self.document.process_lines():
            first_digit, last_digit = self.extractor.find_digits(line)
            if value := self.extractor.combine_digits(first_digit, last_digit):
                total += value
            else:
                logger.warning(f"No valid calibration value found in line: {line.strip()}")
        return total

def main() -> None:
    """Main entry point for the calibration processing program."""
    try:
        input_path = Path('input.txt')
        document = CalibrationDocument(input_path)
        processor = CalibrationProcessor(document)
        
        result = processor.calculate_sum()
        logger.info(f"Total calibration value: {result}")
        
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        raise

if __name__ == "__main__":
    main()
