"""Dictionary related utility functions."""

__author__ = "Issa Masumbuko"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read csv file and return as a lost of dicts with the headers as the keys."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], header: str) -> list[str]:
    """Return a list of all values under a specific header."""
    result: list[str] = []
    # loop through each element (dict) of the list
    for elem in table:
        # for each dictionary, get the value at key "header" and add that to the result
        result.append(elem[header])
    return result


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Reformat data so it's a dictionary with column headers as keys."""
    result: dict[str, list[str]] = {}
    # loop through keys of one row of the table to get the headers
    first_row: dict[str, str] = table[0]
    for key in first_row:
        # for each key(header), make a dict entry with all the column val
        result[key] = column_values(table, key)
    return result


def head(data: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Produce a new column-based table with the first rows of data for each column."""
    result: dict[str, list[str]] = {}
    for column in data:
        sub_list: list[str] = []
        if rows > len(data[column]):
            rows = len(data[column])
        for i in range(rows):
            sub_list.append(data[column][i])
        result[column] = sub_list         
    return result


def select(data: dict[str, list[str]], columns: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}
    for item in columns:
        result[item] = data[item]
    return result


def concat(data1: dict[str, list[str]], data2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based tablr with two column-based tables combined."""
    result: dict[str, list[str]] = {}
    for item in data1:
        result[item] = data1[item]
    for elem in data2:
        if elem in result:
            result[elem] += data2[elem]
        else:
            result[elem] = data2[elem]
    return result


def count(values: list[str]) -> dict[str, int]:
    """Returns a dict  where the keys are unique and its value is its count."""
    result: dict[str, int] = {}
    for item in values:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result