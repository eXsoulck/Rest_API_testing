import os
from logging import getLogger

logger = getLogger(__name__)

def read_test_data_file(file_path):
    """Read file in test data folder and return its content as string."""
    test_data_folder = os.path.join(os.path.dirname(__file__), "..", "data", "test_data")
    file_path = os.path.join(test_data_folder, file_path)
    logger.info(f"Reading test data file: {file_path}")
    with open(file_path, "r", encoding="utf8") as file:
        return file.read()
