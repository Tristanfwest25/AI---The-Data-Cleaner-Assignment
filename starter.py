"""
Exercise: The Data Cleaner
Module 2 — Advanced Python & Data Handling
Estimated time: 35 minutes

Objective: Use Python's re module to extract and normalize data from
messy record strings using regular expressions.
"""

import re

records = [
    "Name: Alice Johnson | Email: alice.j@gmail.com | Phone: (555) 123-4567 | Joined: 01/15/2023",
    "Name: Bob Smith | Email: bob_smith@yahoo.com | Phone: 555.987.6543 | Joined: 03-22-2023",
    "Name: Charlie Brown | Email: charlie@outlook.com | Phone: 555 111 2222 | Joined: 2023/07/01",
    "Name: Diana Prince | Email: diana.prince@company.co.uk | Phone: (555)444-3333 | Joined: 11/30/2023",
]


# ============================================================
# 1. extract_names
# ============================================================

def extract_names(records):
    """Return a list of name strings extracted from each record.

    The name appears after "Name: " and before the first " | ".

    Regex to use: r"Name:\\s+([^|]+)"
      - Name:\\s+   matches the label and any whitespace
      - ([^|]+)    captures everything up to the next pipe
    Call .strip() on the captured group to remove trailing spaces.

    Use a list comprehension with re.search(...).group(1).strip()
    """
    
    return [re.search(r"Name:\s+([^|]+)", r).group(1).strip() for r in records]


# ============================================================
# 2. extract_emails
# ============================================================

def extract_emails(records):
    """Return a list of email addresses extracted from each record.

    Regex to use: r"[\\w._%+-]+@[\\w.-]+\\.[a-zA-Z]{2,}"
      - [\\w._%+-]+   matches the local part before @
      - @             literal @
      - [\\w.-]+      matches the domain (e.g. gmail, company)
      - \\.[a-zA-Z]{2,}  matches .com, .co.uk, etc.

    Use a list comprehension with re.search(pattern, r).group()
    """
    
    return [re.search(r"[\w._%+-]+@[\w.-]+\.[a-zA-Z]{2,}", r).group() for r in records]


# ============================================================
# 3. normalize_phones
# ============================================================

def normalize_phones(records):
    """Return all phone numbers normalized to XXX-XXX-XXXX format.

    Input formats in the data:
      (555) 123-4567   555.987.6543   555 111 2222   (555)444-3333

    Strategy:
      1. Extract the phone field: r"Phone:\\s+([^|]+)"
      2. Strip all non-digit characters: re.sub(r"\\D", "", phone_field)
         \\D matches any non-digit
      3. Reformat: f"{digits[:3]}-{digits[3:6]}-{digits[6:]}"

    implement using a regular for-loop (a list comprehension is fine too)
    """
    
    phones = []
    for r in records:
        phone_field = re.search(r"Phone:\s+([^|]+)", r).group(1).strip()
        digits = re.sub(r"\D", "", phone_field)
        phones.append(f"{digits[:3]}-{digits[3:6]}-{digits[6:]}")
    return phones


# ============================================================
# 4. extract_dates
# ============================================================

def extract_dates(records):
    """Return a list of date strings extracted from each record.

    Dates appear in multiple formats:
      01/15/2023   03-22-2023   2023/07/01

    Regex to use: r"\\d{1,4}[/\\-]\\d{1,2}[/\\-]\\d{2,4}"
      - \\d{1,4}   1-4 digits (handles both MM and YYYY in first position)
      - [/\\-]     separator: slash or dash
      - \\d{1,2}   1-2 digits (month or day)
      - [/\\-]     separator
      - \\d{2,4}   2-4 digits (day or year)

    Use a list comprehension with re.search(pattern, r).group()
    """
    
    return [re.search(r"\d{1,4}[/\-]\d{1,2}[/\-]\d{2,4}", r).group() for r in records]


# ============================================================
# BONUS: parse_records
# ============================================================

def parse_records(records):
    """Parse each record string into a dict with keys: name, email, phone, joined.

    Calls the four functions above so each regex lives in one place.
    Returns a list of dicts.

    use zip(names, emails, phones, dates) inside a list comprehension
    """
    
    names = extract_names(records)
    emails = extract_emails(records)
    phones = normalize_phones(records)
    dates = extract_dates(records)
    return [{"name": n, "email": e, "phone": p, "joined": d} for n, e, p, d in zip(names, emails, phones, dates)]
# ============================================================
# Print results — run these after implementing each function
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("extract_names()")
    print("=" * 60)
    for name in (extract_names(records) or ["not implemented"]):
        print(f"  {name}")

    print("\n" + "=" * 60)
    print("extract_emails()")
    print("=" * 60)
    for email in (extract_emails(records) or ["not implemented"]):
        print(f"  {email}")

    print("\n" + "=" * 60)
    print("normalize_phones()  →  XXX-XXX-XXXX")
    print("=" * 60)
    for phone in (normalize_phones(records) or ["not implemented"]):
        print(f"  {phone}")

    print("\n" + "=" * 60)
    print("extract_dates()")
    print("=" * 60)
    for date in (extract_dates(records) or ["not implemented"]):
        print(f"  {date}")

    print("\n" + "=" * 60)
    print("BONUS: parse_records()")
    print("=" * 60)
    for rec in (parse_records(records) or ["not implemented"]):
        print(f"  {rec}")
        
"""OUTPUT
============================================================
extract_names()
============================================================
  Alice Johnson
  Bob Smith
  Charlie Brown
  Diana Prince

============================================================
extract_emails()
============================================================
  alice.j@gmail.com
  bob_smith@yahoo.com
  charlie@outlook.com
  diana.prince@company.co.uk

============================================================
normalize_phones()  →  XXX-XXX-XXXX
============================================================
  555-123-4567
  555-987-6543
  555-111-2222
  555-444-3333

============================================================
extract_dates()
============================================================
  01/15/2023
  03-22-2023
  2023/07/01
  11/30/2023

============================================================
BONUS: parse_records()
============================================================
  {'name': 'Alice Johnson', 'email': 'alice.j@gmail.com', 'phone': '555-123-4567', 'joined': '01/15/2023'}
  {'name': 'Bob Smith', 'email': 'bob_smith@yahoo.com', 'phone': '555-987-6543', 'joined': '03-22-2023'}
  {'name': 'Charlie Brown', 'email': 'charlie@outlook.com', 'phone': '555-111-2222', 'joined': '2023/07/01'}
  {'name': 'Diana Prince', 'email': 'diana.prince@company.co.uk', 'phone': '555-444-3333', 'joined': '11/30/2023'}"""