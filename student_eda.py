import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    "StudentID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 11],

    "Gender": [
        "Male", "Female", "Male", "Female",
        "Male", "Female", "Male", "Female",
        "Male", "Female", "Male", "Male"
    ],

    "StudyHours": [
        2, 4, 3, 5,
        6, 4, 7, 5,
        8, 6, 3, 3
    ],

    "Attendance(%)": [
        70, 85, 75, 90,
        88, 82, 95, 87,
        92, 89, 78, 78
    ],

    "Marks": [
        55, 75, 65, 85,
        np.nan, 72, 90, 80,
        95, np.nan, 68, 68
    ]
}

# Create CSV file
pd.DataFrame(data).to_csv("student_performance.csv", index=False)

# 2. LOAD THE CSV FILE
df = pd.read_csv("student_performance.csv")

print("Shape:", df.shape)

print("\nDataset Information:")
print(df.info())

# 3. CHECK MISSING VALUES AND DUPLICATES
print("\nMissing values per column:")
print(df.isnull().sum())

print("\nMissing values in Marks:")
print(df["Marks"].isnull().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())

# 4. CLEAN THE DATA
# Remove duplicate row
df = df.drop_duplicates()

# Find median of Marks
marks_median = df["Marks"].median()

# Fill missing Marks with median
df["Marks"] = df["Marks"].fillna(marks_median)

print("\nMedian Marks:", marks_median)

print("\nAfter cleaning:")
print(df.shape)

print("\nCleaned Dataset:")
print(df)

# 5. HISTOGRAM OF MARKS
plt.figure(figsize=(6, 4))

plt.hist(df["Marks"], bins=6, color="steelblue")

plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.title("Marks Distribution")

plt.tight_layout()
plt.savefig("marks_histogram.png")

print("\nSaved marks_histogram.png")

# 6. BOXPLOT OF MARKS
plt.figure(figsize=(5, 4))

plt.boxplot(df["Marks"])

plt.ylabel("Marks")
plt.title("Marks Boxplot")

plt.tight_layout()
plt.savefig("marks_boxplot.png")

print("Saved marks_boxplot.png")

# 7. SCATTER PLOT
# StudyHours vs Marks
plt.figure(figsize=(6, 4))

plt.scatter(
    df["StudyHours"],
    df["Marks"],
    color="darkorange"
)

plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")
plt.tight_layout()
plt.savefig("studyhours_vs_marks.png")
plt.show()
print("Saved studyhours_vs_marks.png")

# 8. CORRELATION MATRIX
correlation_matrix = df[
    ["StudyHours", "Attendance(%)", "Marks"]
].corr()

print("\nCorrelation Matrix:")
print(correlation_matrix)

# 9. GROUPBY GENDER
gender_summary = df.groupby("Gender")[
    ["Marks", "Attendance(%)"]
].mean()

print("\nAverage Marks and Attendance by Gender:")
print(gender_summary)

# FINAL MESSAGE
print(
    "\nSaved marks_histogram.png, "
    "marks_boxplot.png, "
    "studyhours_vs_marks.png"
)