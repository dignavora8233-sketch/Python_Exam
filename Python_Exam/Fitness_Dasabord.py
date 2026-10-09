# Personal Fitness Tracker Dashboard

print("------------------------------------------------------")
print("         PERSONAL FITNESS TRACKER DASHBOARD")
print("------------------------------------------------------")


# Import Libraries

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from abc import ABC, abstractmethod


# Abstract Class

class FitnessBase(ABC):

    @abstractmethod
    def log_activity(self, activity_type, duration, calories):
        pass

    @abstractmethod
    def calculate_metrics(self):
        pass

    @abstractmethod
    def filter_activities(self, condition):
        pass

    @abstractmethod
    def generate_report(self):
        pass


# Child Class

class FitnessTracker(FitnessBase):

    def __init__(self):

        self.file_name = "fitness_activities.csv"

        self.df = pd.DataFrame(
            columns=[
                "Date",
                "Activity_Type",
                "Duration",
                "Calories_Burned"
            ]
        )

        self.load_data()

        print("\nFitness Tracker Initialized Successfully!")


    # Load CSV Data

    def load_data(self):

        if os.path.exists(self.file_name):

            try:
                self.df = pd.read_csv(self.file_name)

                required_columns = [
                    "Date",
                    "Activity_Type",
                    "Duration",
                    "Calories_Burned"
                ]

                if not all(col in self.df.columns for col in required_columns ):
                    
                    print("Invalid CSV column structure!")

                    self.df = pd.DataFrame(columns=required_columns)
                    return

                self.df["Date"] = pd.to_datetime( self.df["Date"],errors="coerce" )

                self.df["Activity_Type"] = ( self.df["Activity_Type"].astype("string") )

                self.df["Duration"] = pd.to_numeric(self.df["Duration"],errors="coerce")

                self.df["Calories_Burned"] = pd.to_numeric(self.df["Calories_Burned"],  errors="coerce")

                self.df.dropna( subset=required_columns, inplace=True )

                self.df = self.df[
                    (self.df["Duration"] > 0) &
                    (self.df["Calories_Burned"] > 0) &
                    (self.df["Activity_Type"].str.strip() != "")
                ]

                print("\nDataset Loaded Successfully!")

            except (OSError, pd.errors.ParserError, ValueError) as e:

                print("Error loading dataset:", e)

        else:

            print("\nNew fitness dataset will be created.")

            self.df.to_csv(self.file_name,index=False)
            # Save Data

    def save_data(self):

        self.df.to_csv(
            self.file_name,
            index=False,
            date_format="%Y-%m-%d"
        )

        print("Data saved successfully!")


    # Log Activity

    def log_activity( self,activity_type,duration,calories):

        activity_type = activity_type.strip()

        if not activity_type:
            print("Activity type cannot be empty.")
            return

        if duration <= 0 or calories <= 0:

            print("Duration and calories must be positive.")
            return

        today = pd.Timestamp.today().normalize()

        new_activity = pd.DataFrame(
            [{"Date": today,"Activity_Type": activity_type.title(), "Duration": duration,"Calories_Burned": calories }]
        )

        self.df = pd.concat( [self.df, new_activity],ignore_index=True)

        self.save_data()

        print("\nActivity Added Successfully!")


    # Take Activity Input

    def add_activity(self):

        print("\n===== Log New Activity =====")

        activity_type = input("Enter Activity Type: " ).strip()

        if not activity_type:

            print("Activity type cannot be empty.")
            return

        try:

            duration = float(input("Enter Duration in Minutes: ") )

            calories = float( input("Enter Calories Burned: "))

            self.log_activity(  activity_type, duration, calories )

        except ValueError:

            print("Please enter valid numerical values.")


    # Show Data

    def show_data(self):

        if self.df.empty:

            print("\nNo fitness activities available.")
            return

        print("\n===== First 5 Records =====")

        print(self.df.head())

        print("\n===== Dataset Information =====")

        self.df.info()

        print("\n===== Missing Values =====")

        print(self.df.isnull().sum())

        print("\nTotal Rows:", len(self.df))

        print(
            "Total Columns:",
            len(self.df.columns)
        )


    # Calculate Metrics

    def calculate_metrics(self):

        if self.df.empty:

            print("\nNo data available for analysis.")
            return

        print("\n===== Fitness Statistics =====")

        total_calories = np.sum( self.df["Calories_Burned"].to_numpy() )

        average_duration = np.mean( self.df["Duration"].to_numpy() )

        total_duration = np.sum( self.df["Duration"].to_numpy())

        average_calories = np.mean( self.df["Calories_Burned"].to_numpy()  )

        print("Total Activities:", len(self.df) )

        print( "Total Calories Burned:", round(total_calories, 2))

        print("Average Calories Burned:", round(average_calories, 2))

        print("Average Duration:",round(average_duration, 2), "minutes")

        print("Total Duration:",round(total_duration, 2),"minutes")

        print("\n===== Activity Frequency =====")

        print( self.df["Activity_Type"].value_counts())

        print("\n===== Activity Summary =====")

        summary = self.df.groupby( "Activity_Type" ).agg(
            Total_Duration=("Duration", "sum"),
            Total_Calories=("Calories_Burned", "sum"),
            Activity_Count=("Activity_Type", "count")
        )

        print(summary)


    # Filter Activities

    def filter_activities(self, condition):

        if self.df.empty:

            print("\nNo data available.")
            return

        if condition == "1":

            activity = input(
                "Enter Activity Type to Filter: "
            ).strip()

            if not activity:

                print("Activity type cannot be empty.")
                return

            result = self.df[self.df["Activity_Type"].str.lower()== activity.lower()]

        elif condition == "2":

            try:

                start_date = pd.to_datetime(input("Enter Start Date (YYYY-MM-DD): "),errors="raise")

                end_date = pd.to_datetime(input("Enter End Date (YYYY-MM-DD): "),errors="raise")

                if start_date > end_date:

                    print("Start date must be before end date.")
                    return

                result = self.df[(self.df["Date"] >= start_date) &(self.df["Date"] <= end_date)]

            except (ValueError, TypeError):

                print("Invalid date format.")
                return

        else:

            print("Invalid filter choice.")
            return

        print("\n===== Filtered Activities =====")

        if result.empty:

            print("No matching records found.")

        else:

            print(result.to_string(index=False))

            print("\nMatching Records:", len(result))


    # Generate Report

    def generate_report(self):

        if self.df.empty:

            print("\nNo data available for report.")
            return

        print("\n====================================================")
        print("                FITNESS REPORT                        ")
        print("======================================================")

        print("Total Activities:",len(self.df))

        print("Total Calories Burned:",round(self.df["Calories_Burned"].sum(), 2))

        print( "Total Exercise Duration:", round(self.df["Duration"].sum(), 2), "minutes" )

        print( "Average Exercise Duration:", round(self.df["Duration"].mean(), 2), "minutes")

        print("Most Frequent Activity:", self.df["Activity_Type"].value_counts().idxmax())

        print("\n===== Calories by Activity =====")

        print(self.df.groupby("Activity_Type")["Calories_Burned" ].sum())

        report_file = "fitness_report.csv"

        summary = self.df.groupby("Activity_Type").agg(
            Total_Duration=("Duration", "sum"),
            Total_Calories=("Calories_Burned", "sum"),
            Activity_Count=("Activity_Type", "count")
        )

        summary.to_csv(report_file)

        print("\nReport saved to:", report_file)


    # Data Visualization

    def visualization(self):

        if self.df.empty:

            print("\nNo data available for visualization.")
            return

        while True:

            print("\n===== Visualization Menu =====")

            print("1. Bar Chart")
            print("2. Line Graph")
            print("3. Pie Chart")
            print("4. Heatmap")
            print("5. Back to Main Menu")

            choice = input("Enter Your Choice: ")

            # Bar Chart

            if choice == "1":

                activity_duration = self.df.groupby("Activity_Type" )["Duration"].sum()

                plt.figure(figsize=(9, 5))

                plt.bar( activity_duration.index,
                    activity_duration.values
                )

                plt.title("Total Time Spent on Each Activity")

                plt.xlabel("Activity Type")

                plt.ylabel("Total Duration (Minutes)")

                plt.xticks(rotation=30)

                plt.tight_layout()

                plt.show()


            # Line Graph

            elif choice == "2":

                daily_calories = self.df.groupby("Date")["Calories_Burned"].sum().sort_index()

                plt.figure(figsize=(10, 5))

                plt.plot(
                    daily_calories.index,
                    daily_calories.values,
                    marker="o"
                )

                plt.title("Calories Burned Over Time")

                plt.xlabel("Date")

                plt.ylabel("Calories Burned")

                plt.xticks(rotation=30)

                plt.tight_layout()

                plt.show()


            # Pie Chart

            elif choice == "3":

                activity_count = self.df["Activity_Type"].value_counts()

                plt.figure(figsize=(8, 8))

                plt.pie(
                    activity_count.values,
                    labels=activity_count.index,
                    autopct="%1.1f%%",
                    startangle=90
                )

                plt.title("Percentage Distribution of Activities")

                plt.tight_layout()

                plt.show()


            # Heatmap

            elif choice == "4":

                numeric_data = self.df[["Duration", "Calories_Burned"]].copy()

                correlation = numeric_data.corr()

                plt.figure(figsize=(7, 5))

                sns.heatmap(
                    correlation,
                    annot=True,
                    cmap="coolwarm",
                    vmin=-1,
                    vmax=1,
                    fmt="%.2f%%"
                )

                plt.title("Duration and Calories Correlation")

                plt.tight_layout()

                plt.show()


            # Exit Visualization

            elif choice == "5":

                print("Returning to Main Menu...")

                break

            else:

                print("Invalid choice! Try again.")


# Create Object

obj = FitnessTracker()


# Main Menu

while True:

    print("\n======================================================")
    print("                    MAIN MENU")
    print("======================================================")

    print("1. Log New Activity")
    print("2. Show Data")
    print("3. Calculate Metrics")
    print("4. Filter Activities")
    print("5. Generate Report")
    print("6. Visualization")
    print("7. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":

        obj.add_activity()

    elif choice == "2":

        obj.show_data()

    elif choice == "3":

        obj.calculate_metrics()

    elif choice == "4":

        print("\n1. Filter by Activity Type")
        print("2. Filter by Date Range")

        filter_choice = input("Enter Filter Choice: ")

        obj.filter_activities(filter_choice)

    elif choice == "5":

        obj.generate_report()

    elif choice == "6":

        obj.visualization()

    elif choice == "7":

        print("\nThank You for Using Fitness Tracker!")

        break

    else:

        print("Invalid Choice! Please Enter 1 to 7.")
