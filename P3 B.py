from bs4 import BeautifulSoup
from datetime import datetime, date

# ==========================================
# 1. Search a Word in a Text File
# ==========================================

print("========== Program 1 ==========")

# Create a sample text file
with open("story.txt", "w") as file:
    file.write("The college library has many books on Python, AI and Data Science.")

# Read the file
with open("story.txt", "r") as file:
    text = file.read()

print("\nFile Content:")
print(text)

word = input("\nEnter the word to search: ")

if word.lower() in text.lower():
    print("Word Found in the file.")
else:
    print("Word Not Found.")

# ==========================================
# 2. Read HTML File and Search Word
# ==========================================

print("\n========== Program 2 ==========")

html = """
<html>
<head>
<title>Travel Diary</title>
</head>
<body>
<h1>Welcome to Kerala</h1>
<p>Kerala is famous for backwaters and beaches.</p>
</body>
</html>
"""

with open("example.html", "w") as file:
    file.write(html)

with open("example.html", "r") as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, "html.parser")

text = soup.get_text()

print("\nExtracted Text:")
print(text)

search = input("\nEnter word to search in HTML: ")

if search.lower() in text.lower():
    print("Word Found in HTML.")
else:
    print("Word Not Found in HTML.")

# ==========================================
# 3. Display Current Date in Different Formats
# ==========================================

print("\n========== Program 3 ==========")

now = datetime.now()

print("YYYY-MM-DD :", now.strftime("%Y-%m-%d"))
print("DD-MM-YYYY :", now.strftime("%d-%m-%Y"))
print("Month Day, Year :", now.strftime("%B %d, %Y"))
print("Weekday, Month Day, Year :", now.strftime("%A, %B %d, %Y"))

# ==========================================
# 4. Print Current Date
# ==========================================

print("\n========== Program 4 ==========")

today = date.today()

print("Current Date :", today)

# ==========================================
# 5. Display Current Month Number and Name
# ==========================================

print("\n========== Program 5 ==========")

print("Current Month Number :", now.month)
print("Current Month Name :", now.strftime("%B"))

# ==========================================
# 6. Display Current Time
# ==========================================

print("\n========== Program 6 ==========")

print("Current Time :", now.strftime("%H:%M:%S"))
