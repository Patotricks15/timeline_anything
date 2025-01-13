import re


def extract_date_from_text(text: str) -> str:
    """
    Extracts a date (in ISO format or year) from the response text.
    :param text: Text containing the date information.
    :return: Extracted date as a string or None if no date is found.
    """
    # Regex to match dates in ISO format or just years
    date_pattern = r"\b(\d{4}(?:-\d{2}-\d{2})?)\b"
    match = re.search(date_pattern, text)
    return match.group(0) if match else None
