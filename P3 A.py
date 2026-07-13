from bs4 import BeautifulSoup
from datetime import datetime
import calendar

# ==========================================
# 3A. Search a Product in Shopping List
# ==========================================
print("\n========== 3A. Product Search ==========")

shopping_list = input("Enter your shopping list: ")
product = input("Enter the product to search: ")

if product.lower() in shopping_list.lower():
    print(f"'{product}' is available in the shopping list.")
else:
    print(f"'{product}' is NOT available in the shopping list.")


# ==========================================
# 3B. Retrieve Data from HTML File
# ==========================================
print("\n========== 3B. Read HTML File ==========")

# Create a sample HTML file automatically
html_data = """
<html>
<head>
<title>Travel Blog</title>
</head>
<body>
<h1>Welcome to Goa</h1>
<p>Goa is famous for beaches, seafood, and nightlife.</p>
</body>
</html>
"""

with open("travel.html", "w", encoding="utf-8") as file:
    file.write(html_data)

# Read HTML file
with open("travel.html", "r", encoding="utf-8") as file:
    content = file.read()

soup = BeautifulSoup(content, "html.parser")

print("Extracted Data:")
print(soup.get_text())


# ==========================================
# 3C. Current Date in Different Formats
# ==========================================
print("\n========== 3C. Date Formats ==========")

today = datetime.now()

print("ISO Format:", today.strftime("%Y-%m-%d"))
print("Indian Format:", today.strftime("%d-%m-%Y"))
print("Month Name:", today.strftime("%d %B %Y"))
print("Short Month:", today.strftime("%d %b %Y"))
print("US Format:", today.strftime("%m/%d/%Y"))
print("Weekday:", today.strftime("%A, %d %B %Y"))


# ==========================================
# 3D. Convert Timestamp to Date
# ==========================================
print("\n========== 3D. Timestamp Conversion ==========")

timestamp = float(input("Enter Unix Timestamp: "))

converted_date = datetime.fromtimestamp(timestamp)

print("Readable Date:", converted_date.strftime("%d-%m-%Y %H:%M:%S"))


# ==========================================
# 3E. Calendar Module
# ==========================================
print("\n========== 3E. Calendar ==========")

year = int(input("Enter Year: "))
month = int(input("Enter Month (1-12): "))

print("\nFull Year Calendar")
print(calendar.calendar(year))

print("Selected Month Calendar")
print(calendar.month(year, month))

if calendar.isleap(year):
    print(year, "is a Leap Year.")
else:
    print(year, "is NOT a Leap Year.")


# ==========================================
# 3F. Compare Two Dates
# ==========================================
print("\n========== 3F. Compare Dates ==========")

date1 = input("Enter first event date (YYYY-MM-DD): ")
date2 = input("Enter second event date (YYYY-MM-DD): ")

d1 = datetime.strptime(date1, "%Y-%m-%d")
d2 = datetime.strptime(date2, "%Y-%m-%d")

if d1 < d2:
    print("First event comes before the second event.")
elif d1 > d2:
    print("First event comes after the second event.")
else:
    print("Both events are on the same date.")
