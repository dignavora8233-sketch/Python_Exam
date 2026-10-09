# 🏃 Personal Fitness Tracker Dashboard

## 📌 Introduction

The **Personal Fitness Tracker Dashboard** is a Python-based data analysis project designed to record, manage, analyze, and visualize daily fitness activities. It helps users maintain a record of their physical activities, exercise duration, and calories burned.

This project uses Python programming, Object-Oriented Programming (OOP), Abstract Classes, NumPy, Pandas, Matplotlib, and Seaborn to perform fitness data analysis and generate meaningful visualizations.

The application stores fitness activity records in a CSV file, allowing users to save their data and access it again whenever they run the program. It also provides different menu-driven options for managing activities, calculating fitness statistics, filtering records, generating reports, and displaying charts.

The main purpose of this project is to understand how Python can be used to build a practical data analysis application.

---

## 🎯 Objectives

The main objectives of this project are:

* To develop a menu-driven fitness tracking application using Python.
* To record daily physical activities and exercise details.
* To store fitness records in a CSV file.
* To apply Object-Oriented Programming concepts.
* To implement abstraction using an abstract base class.
* To analyze fitness data using NumPy and Pandas.
* To calculate total calories burned and exercise duration.
* To calculate average fitness statistics.
* To filter activities by activity type and date range.
* To generate a summarized fitness report.
* To visualize fitness data using different charts.
* To practice file handling and data validation.
* To understand how data analysis libraries work together in a real-world project.

---

## ✨ Features

### 1. Log New Activity

Users can add new fitness activities by entering the activity type, exercise duration in minutes, and calories burned.

The application automatically records the current date and saves the new activity in the CSV file.

Examples of activities include:

* Walking
* Running
* Cycling
* Swimming
* Yoga
* Gym Workout

### 2. Show Fitness Data

The application displays the available fitness dataset and provides basic information about the records.

This feature includes:

* Displaying the first five records.
* Showing dataset information.
* Checking missing values.
* Displaying the total number of rows.
* Displaying the total number of columns.

### 3. Calculate Fitness Metrics

The application analyzes fitness records and calculates important statistics, including:

* Total number of activities.
* Total calories burned.
* Average calories burned.
* Average exercise duration.
* Total exercise duration.
* Frequency of each activity.
* Activity-wise total duration.
* Activity-wise total calories burned.
* Activity-wise activity count.

These metrics help users understand their recorded fitness activities.

### 4. Filter Activities

Users can filter fitness records using two options:

**Filter by Activity Type**

Displays activities matching the activity type entered by the user.

**Filter by Date Range**

Displays activities between a specified start date and end date.

The application checks user input and displays a message if the filter option or date format is invalid.

### 5. Generate Fitness Report

The application generates a fitness summary containing:

* Total activities.
* Total calories burned.
* Total exercise duration.
* Average exercise duration.
* Most frequently performed activity.
* Calories burned by activity type.

The activity summary is also saved to a separate CSV file named `fitness_report.csv`.

### 6. Data Visualization

The project includes four visualization options to represent fitness data graphically.

**Bar Chart**

Displays the total exercise duration for each activity type.

**Line Graph**

Shows the total calories burned over time.

**Pie Chart**

Displays the percentage distribution of recorded activities.

**Heatmap**

Shows the correlation between exercise duration and calories burned.

These visualizations make fitness data easier to understand and compare.

### 7. CSV File Handling

The project uses CSV files to store and manage fitness records.

The application can:

* Load previously saved fitness records.
* Create a new dataset when the file does not exist.
* Add new activities to the dataset.
* Save updated records.
* Validate required columns.
* Handle missing or invalid values during data loading.

### 8. Data Validation

The application performs basic validation to improve data quality.

* Activity type cannot be empty.
* Exercise duration must be positive.
* Calories burned must be positive.
* Invalid numerical inputs are handled.
* Invalid date formats are checked.
* Required CSV columns are validated.
* Missing or invalid records are removed during data cleaning.

### 9. Menu-Driven Interface

The application provides a simple command-line menu.

Users can select the required option by entering a number. After completing an operation, they can return to the main menu and continue using the application.

---

## 🛠️ Technologies Used

### Python

Python is the main programming language used to develop the application and implement the project logic.

### NumPy

NumPy is used for numerical calculations, including totals and averages of fitness measurements.

### Pandas

Pandas is used to load CSV files, manage tabular data, clean records, group activities, filter data, and generate summaries.

### Matplotlib

Matplotlib is used to create bar charts, line graphs, and pie charts for visualizing fitness information.

### Seaborn

Seaborn is used to create a heatmap that represents the correlation between numerical fitness variables.

### Object-Oriented Programming

OOP is used to organize the project into classes and methods, making the application easier to manage and extend.

### Abstract Base Class

The `ABC` and `abstractmethod` features from Python's `abc` module are used to define the `FitnessBase` abstract class.

### OS Module

The `os` module is used to check whether the fitness CSV file exists.

### CSV File Handling

CSV files are used for persistent storage of fitness activities and generated reports.

---

## 🧠 Concepts Implemented

This project demonstrates several important Python and data analysis concepts.

### 1. Classes and Objects

The project defines the `FitnessBase` and `FitnessTracker` classes. An object of the `FitnessTracker` class is created to use the application's methods.

### 2. Constructor

The `__init__()` method initializes the fitness tracker, creates an empty DataFrame with the required columns, and loads existing records.

### 3. Abstraction

The `FitnessBase` class inherits from `ABC` and defines abstract methods.

The abstract methods are:

* `log_activity()`
* `calculate_metrics()`
* `filter_activities()`
* `generate_report()`

The `FitnessTracker` child class implements these methods.

### 4. Inheritance

The `FitnessTracker` class inherits from `FitnessBase`, demonstrating inheritance in Python.

### 5. Encapsulation

Related data and operations are organized within the `FitnessTracker` class.

### 6. Loops and Conditional Statements

The `while` loop keeps the main menu running until the user selects the Exit option. Conditional statements execute the selected operation.

### 7. Exception Handling

The project uses `try` and `except` blocks to handle certain invalid inputs and file-reading errors.

### 8. Functions and Methods

Different methods are created for loading data, saving data, adding activities, calculating statistics, filtering records, generating reports, and displaying charts.

### 9. Data Cleaning

Pandas is used to convert date and numerical columns into appropriate data types and remove invalid or incomplete records.

### 10. Data Aggregation

The `groupby()` and `agg()` methods summarize exercise duration, calories burned, and activity counts by activity type.

---

## 📊 Visualization Details

The project supports four types of charts.

| Chart Type | Purpose                                           |
| ---------- | ------------------------------------------------- |
| Bar Chart  | Compare total duration across activity types      |
| Line Graph | Analyze calories burned over time                 |
| Pie Chart  | Show the percentage distribution of activities    |
| Heatmap    | Display correlation between duration and calories |

### Bar Chart

The bar chart groups the dataset by `Activity_Type` and calculates the total `Duration` for each activity.

### Line Graph

The line graph groups records by `Date` and calculates total `Calories_Burned` for each date.

### Pie Chart

The pie chart uses activity frequency to show how the recorded activities are distributed.

### Heatmap

The heatmap calculates the correlation between `Duration` and `Calories_Burned` and displays the correlation values in a graphical format.

---

## 📁 Project Structure

The project uses the following main files:

```text
Personal-Fitness-Tracker/
│
├── fitness_tracker.py
├── fitness_activities.csv
├── fitness_report.csv
└── README.md
```

**File Description**

* `fitness_tracker.py` — Contains the Python application code.
* `fitness_activities.csv` — Stores fitness activity records.
* `fitness_report.csv` — Stores the activity-wise summary generated by the report feature.
* `README.md` — Contains the project documentation.

**Note:** The Python filename can be different depending on the name used when saving the program. The CSV files are created or updated by the application when the corresponding operations are performed.

---

## ⚙️ Installation and Setup

Follow these steps to run the project on your computer.

### Step 1: Install Python

Download and install Python from the official website:

https://www.python.org/downloads/

Verify the installation by running:

```bash
python --version
```

### Step 2: Install Required Libraries

Open Command Prompt or the VS Code terminal and run:

```bash
pip install numpy pandas matplotlib seaborn
```

### Step 3: Create the Project Folder

Create a folder named `Personal-Fitness-Tracker`.

Save the Python program inside this folder.

### Step 4: Run the Program

Open the terminal in the project folder and execute:

```bash
python fitness_tracker.py
```

Replace `fitness_tracker.py` with the actual filename if you saved your program under a different name.

### Step 5: Use the Main Menu

After running the program, select an option by entering its corresponding number.

---

## ▶️ How to Use the Application

When the program starts, it initializes the fitness tracker and loads the existing dataset if available.

The main menu contains the following options:

```text
======================================================
                    MAIN MENU
======================================================
1. Log New Activity
2. Show Data
3. Calculate Metrics
4. Filter Activities
5. Generate Report
6. Visualization
7. Exit
```

### Option 1: Log New Activity

Enter the activity type, duration in minutes, and calories burned.

The application validates the inputs and saves the activity.

### Option 2: Show Data

Displays the first five records, dataset information, missing-value counts, and dataset dimensions.

### Option 3: Calculate Metrics

Calculates fitness statistics and displays activity-wise summaries.

### Option 4: Filter Activities

Choose to filter records by activity type or date range.

### Option 5: Generate Report

Displays the fitness report and saves an activity-wise summary to `fitness_report.csv`.

### Option 6: Visualization

Choose a bar chart, line graph, pie chart, or heatmap.

Select the fifth option in the visualization submenu to return to the main menu.

### Option 7: Exit

Ends the application and displays a thank-you message.

---

## 💾 Dataset Information

The application uses a CSV dataset with the following columns:

| Column Name       | Description                             |
| ----------------- | --------------------------------------- |
| `Date`            | Date on which the activity was recorded |
| `Activity_Type`   | Type of physical activity               |
| `Duration`        | Exercise duration in minutes            |
| `Calories_Burned` | Calories burned during the activity     |

The dataset is loaded using Pandas and cleaned before analysis.

The application also supports adding new records, allowing the dataset to grow as the user records more activities.

---

## 🔍 Data Analysis Process

The project follows these steps to process fitness data:

1. Import the required Python libraries.
2. Initialize the fitness tracker.
3. Check whether the CSV file exists.
4. Load the existing dataset or create a new one.
5. Validate the required columns.
6. Convert columns to appropriate data types.
7. Remove invalid and incomplete records.
8. Record new fitness activities.
9. Calculate statistical metrics.
10. Filter records according to user requirements.
11. Generate a fitness report.
12. Create visualizations.
13. Save records and report summaries to CSV files.

This workflow demonstrates how raw data can be stored, cleaned, analyzed, and presented through a simple Python application.

---

## 🌟 Advantages

* Simple menu-driven interface.
* Easy recording of fitness activities.
* Persistent storage using CSV files.
* Automatic calculation of fitness statistics.
* Activity-wise data analysis.
* Filtering by activity type and date range.
* Automatic report generation.
* Multiple visualization options.
* Demonstrates abstraction and inheritance.
* Provides practical experience with Python data analysis libraries.
* Can be extended with additional features in the future.

---

## 🚀 Future Improvements

The project can be enhanced in several ways:

* Add a graphical user interface.
* Create a web-based fitness dashboard.
* Add weekly and monthly fitness summaries.
* Allow users to set personal activity goals.
* Display goal completion progress.
* Add more visualization options.
* Export reports to PDF.
* Add support for multiple users.
* Introduce database integration.
* Add interactive charts.
* Include additional fitness measurements.
* Add customizable date-based reports.

These improvements could make the application more interactive and useful for tracking personal fitness records.

---

## 🎓 Learning Outcomes

By developing this project, I gained practical experience in:

* Python programming.
* Object-Oriented Programming.
* Abstract classes and abstract methods.
* Inheritance and class methods.
* File handling with CSV files.
* Data cleaning and validation.
* NumPy numerical calculations.
* Pandas data manipulation.
* Grouping and aggregation.
* Exception handling.
* Matplotlib data visualization.
* Seaborn heatmaps.
* Building menu-driven applications.
* Organizing code into reusable methods.
* Creating project documentation using Markdown.

This project helped me understand how Python programming and data analysis libraries can be combined to solve practical problems.

---

## 🏁 Conclusion

The **Personal Fitness Tracker Dashboard** is a practical Python project that demonstrates fitness activity management, data analysis, report generation, and visualization.

It combines Object-Oriented Programming, abstraction, inheritance, CSV file handling, NumPy, Pandas, Matplotlib, and Seaborn in a single menu-driven application.

Users can record their activities, calculate fitness statistics, filter records, generate reports, and visualize activity patterns through different charts.

Overall, this project strengthened my understanding of Python programming and data analysis while providing practical experience in developing a complete beginner-friendly application.

---

## 📬 Contact Me

**Digna Vora**

 LinkedIn:www.linkedin.com/in/digna-vora-b135a3416
Email: dignavora8233@gmail.com

Feel free to explore this project, share your feedback, and connect with me to discuss Python, Data Analysis, Artificial Intelligence, Machine Learning, and future technology.

---

⭐ **If you find this project useful, please give the repository a star!**

**Thank you for visiting my Personal Fitness Tracker Dashboard project.**
