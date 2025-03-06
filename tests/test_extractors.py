from quickscrape.extractors import email, table, links
import pytest
import pandas as pd
from bs4 import BeautifulSoup

# Email Extractor Tests
def test_extract_emails():
    """Test extracting emails from HTML content."""
    html = """
    <html>
    <body>
        <p>Contact us at info@example.com or support@example.com</p>
        <div>Sales: sales@example.com</div>
    </body>
    </html>
    """

    emails = email.extract_emails(html)

    assert len(emails) == 3, "Should extract exactly 3 email addresses from the HTML"
    assert "info@example.com" in emails, "The 'info@example.com' email address should be extracted"
    assert "support@example.com" in emails, "The 'support@example.com' email address should be extracted"
    assert "sales@example.com" in emails, "The 'sales@example.com' email address should be extracted"

def test_no_emails():
    """Test extracting emails when none are present."""
    html = """
    <html>
    <body>
        <p>Contact us by phone.</p>
    </body>
    </html>
    """

    emails = email.extract_emails(html)

    assert len(emails) == 0, "Should return an empty list when no emails are present in the HTML"
