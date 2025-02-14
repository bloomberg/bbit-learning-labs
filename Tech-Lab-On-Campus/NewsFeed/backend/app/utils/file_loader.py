"""Module for helper functions to parse and load data files. Do not edit."""

import json
import os
from typing import Generator, List


def _list_files_in_directory(directory: str) -> Generator[str, None, None]:
    """
    List all files in the given directory.

    Args:
        directory (str): The directory to list files from

    Returns
    -------
        List[str]: List of file paths
    """
    # Ensure the directory exists
    if not os.path.exists(directory):
        raise FileNotFoundError(f"Directory not found: {directory}")

    yield from (os.path.join(directory, filename) for filename in os.listdir(directory))


def load_json_files(directory: str) -> List[dict]:
    """
    Load all JSON files from the given directory.

    Args:
        directory (str): The directory to load JSON files from

    Returns
    -------
        List[dict]: List of JSON objects
    """
    json_files = _list_files_in_directory(directory)
    data = []
    for file_path in json_files:
        with open(file_path, "r") as file:
            data.append(json.load(file))
    return data
