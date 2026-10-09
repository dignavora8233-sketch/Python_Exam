# Fitness Tracker Dashboard Analyzer

print("------------------------------------------------------")
print("          Fitness Tracker Dashboard Analyzer")
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
    def load_data(self):
        pass

    @abstractmethod
    def show_data(self):
        pass


# Child Class

class Fitness_Tracker(FitnessBase):

    def __init__(self):
        self.df = None

    # Load Data

    def load_data(self):

        file_path = "fitness_tracker_200_rows.csv"

        try:
            if not os.path.exists(file_path):
                print("CSV file not found!")
                return

            self.df = pd.read_csv(file_path)

            print("\nData loaded successfully!")
            print("Total Rows:", len(self.df))
            print("Total Columns:", len(self.df.columns))

        except Exception as e:
            print("Error loading data:", e)

    # Show Data

    def show_data(self):

        if self.df is None:
            print("Please load data first.")
            return

        print("\nFirst 5 Records:")
        print(self.df.head())

        print("\nDataset Information:")
        self.df.info()

        print("\nMissing Values:")
        print(self.df.isnull().sum())

    # Statistics

    def statistics(self):

        if self.df is None:
            print("Please load data first.")
            return

        required_columns = [
            "Steps",
            "Calories",
            "Sleep_Hours",
            "Heart_Rate_Avg"
        ]

        for col in required_columns:
            if col not in self.df.columns:
                print("Missing required column:", col)
                return

        print("\n===== Fitness Statistics =====")

        print("\nAverage Steps:",
              self.df["Steps"].mean())

        print("Minimum Steps:",
              self.df["Steps"].min())

        print("Maximum Steps:",
              self.df["Steps"].max())

        print("\nAverage Calories Burned:",
              self.df["Calories"].mean())

        print("Average Sleep Hours:",
              self.df["Sleep_Hours"].mean())

        print("Average Heart Rate:",
              self.df["Heart_Rate_Avg"].mean())

    # Goal Analysis

    def goal_analysis(self):

        if self.df is None:
            print("Please load data first.")
            return

        if "Goal_Achieved" not in self.df.columns:
            print("Goal_Achieved column not found.")
            return

        print("\n===== Goal Achievement Analysis =====")

        print(self.df["Goal_Achieved"].value_counts())

    # Workout Analysis

    def workout_analysis(self):

        if self.df is None:
            print("Please load data first.")
            return

        if "Workout_Type" not in self.df.columns:
            print("Workout_Type column not found.")
            return

        print("\n===== Workout Type Analysis =====")

        print(self.df["Workout_Type"].value_counts())

    # Visualization

    def visualization(self):

        if self.df is None:
            print("Please load data first.")
            return

        while True:

            print("\n===== Visualization Menu =====")
            print("1. Bar Plot")
            print("2. Line Plot")
            print("3. Pie Chart")
            print("4. Heatmap")
            print("5. Back to Main Menu")

            choice = input("Enter your choice: ")

            # Bar Plot

            if choice == "1":

                if "Steps" not in self.df.columns:
                    print("Steps column not found.")
                    continue

                plt.figure(figsize=(8, 5))

                plt.bar(
                    self.df.index + 1,
                    self.df["Steps"]
                )

                plt.title("Daily Steps Distribution")
                plt.xlabel("Record Number")
                plt.ylabel("Steps")
                plt.tight_layout()
                plt.show()

            # Line Plot

            elif choice == "2":

                if "Calories" not in self.df.columns:
                    print("Calories column not found.")
                    continue

                plt.figure(figsize=(10, 5))

                plt.plot(
                    self.df.index + 1,
                    self.df["Calories"],
                    marker="o"
                )

                plt.title("Calories Burned Analysis")
                plt.xlabel("Record Number")
                plt.ylabel("Calories Burned")
                plt.tight_layout()
                plt.show()

            # Pie Chart

            elif choice == "3":

                if "Workout_Type" not in self.df.columns:
                    print("Workout_Type column not found.")
                    continue

                workout_counts = self.df[
                    "Workout_Type"
                ].value_counts()

                if workout_counts.empty:
                    print("No workout data available.")
                    continue

                plt.figure(figsize=(8, 8))

                plt.pie(
                    workout_counts,
                    labels=workout_counts.index,
                    autopct="%1.1f%%",
                    startangle=90
                )

                plt.title("Workout Type Distribution")
                plt.tight_layout()
                plt.show()

            # Heatmap

            elif choice == "4":

                numeric_data = self.df.select_dtypes(
                    include=np.number
                )

                if numeric_data.shape[1] < 2:
                    print("At least 2 numerical columns are required.")
                    continue

                plt.figure(figsize=(10, 6))

                sns.heatmap(
                    numeric_data.corr(),
                    annot=True,
                    cmap="coolwarm",
                    fmt=".2f"
                )

                plt.title("Fitness Data Correlation Heatmap")
                plt.tight_layout()
                plt.show()

            # Back to Main Menu

            elif choice == "5":

                print("Returning to Main Menu...")
                break

            else:

                print("Invalid choice! Please try again.")


# Create Object

obj = Fitness_Tracker()


# Main Menu

while True:

    print("\n------------------------------------------------------")
    print("                    Main Menu")
    print("------------------------------------------------------")

    print("1. Load Data")
    print("2. Show Data")
    print("3. Statistics")
    print("4. Goal Analysis")
    print("5. Workout Analysis")
    print("6. Visualization")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        obj.load_data()

    elif choice == "2":

        obj.show_data()

    elif choice == "3":

        obj.statistics()

    elif choice == "4":

        obj.goal_analysis()

    elif choice == "5":

        obj.workout_analysis()

    elif choice == "6":

        obj.visualization()

    elif choice == "7":

        print("Thank You for using Fitness Tracker Analyzer!")
        break

    else:

        print("Invalid choice! Please enter 1 to 7.")
