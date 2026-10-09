print("------------------------------------------------------")
print("           Fitness DashBord Anlyzer                   ")
print("------------------------------------------------------")


#import data

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from abc import ABC,abstractmethod

#Abstact class
class FitnessBase(ABC):

    @abstractmethod
    def load_data(self):
        pass

    @abstractmethod
    def show_data(self):
        pass


class Fitness_Tracker(FitnessBase):

    def __init__(self):
        self.df = None

    #Data load

    def Load_data(self):
        self.df = 
        pd.read.csv("fitness_tracker_200_rows.csv")
        print("Data load successfully..")
        print("Total Rows:",len(self.df))
        print("Total Columns:",len(self.df))


    #Display Data
    
    def show_detils(self):
       
        print("\nFirst 5 Recods.")
        print(self.df.head())

        print("\nDtatset infotmation")
       
        print(self.df.info())

        print("\nMissing Value")
       
        print(self.df.isnull().sum())


    #Statiscis Data
    def Statiscis(self):
       
        print("\nAverage Steps:",self.df["Setps"].mean())
       
        print("\nMinimum Steps:",self.df["Setps"].min())
       
        print("\nMaximum Steps:",self.df["Setps"].max())

        print("\nAverage Calories Burned:",self.df["Calories_Burnes"].mean())
       
        print("\nAverage Sleep Hours:",self.df["Sleep_Hours"].mean())  
       
        print("\nAverage Heart Rate:",self.df["Heart_Rate_Avg"].mean())


    #Goal Anlyzer
    def Goal_Anlysis(self):
        
        print("\nGoal Achievement.")
        
        print(self.df["Goal_Achieved"].value_count())
    

    #Workout Anlayzer
    def Workout_Anlysis(self):
        
        print("\nWorkour Types.")
        
        print(self.df["Workout_Type"].value_count())



    #Visulaization
    def Visulization(self):

        while True():
            #Chrats
            print("\n=====Chrats menu=====")
            print("1.Bar Plot")
            print("2.Line Plot")
            print("3.Pie plot")
            print("4.Heatmep")
            print("5.Exit to main menu")

            choice = int(input("Enter your choice:"))

            #Bar Chrat
            if choice == 1:

                    plt.figure(figsize=(8,5))
                    plt.bar(self.df["Steps"])
                    plt.title("Daily Steps Distribution")
                    plt.xlabel("Steps")
                    plt.ylabel("Frequency")
                    plt.show()

            #Line Chrat
            elif choice == 2:
                plt.figure(figsize=(10, 5))
                plt.plot(self.df["Calories"])
                plt.title("Daily calories Discribe")
                plt.xlabel("Date")
                plt.ylabel("Average Step")
                plt.show()

            #Pie Chrat
            elif choice == 3:
                plt.figure(figsize= (10, 10))
                plt.pie(self.df["Workout_Type"])
                plt.title("Percenatge Distribution Activity")
                plt.ylabel("")
                plt.show()

            elif choice == 4:
                plt.figure(figsize=(10,5))
                sns.heatmap(numiac.data.corr(),
                            annot=True,
                            cmap="coolwarm"
                            )
                plt.title("Fitness Data Corration Heatmap")
                plt.show()

            elif choice == 5:

                print("Go to main menu..")


            else:

                print("Invalid choice.")



obj = Fitness_Tracker()

print("--------------------------------------------------------")
print("                Main Menu                               ")                   
print("--------------------------------------------------------")

while True():

    print("====Main Menu====")
    print("1.Load Data")
    print("2.Show Data")
    print("3.Statiscis")
    print("4.Goal Anlysis")
    print("5.Workout Anlysis")
    print("6.Visulization")
    print("7.Exit")

    choice = int(input("Enter Your Choice:"))

    if choice == 1:
        
        obj.Load_data()

    elif choice == 2:

        obj.show_detils()

    elif choice == 3:

        obj.Statiscis()

    elif choice == 4:

        obj.Goal_Anlysis()


    elif choice == 5:

        obj.Workout_Anlysis()

    elif choice == 6:

        obj.Visulization()

    elif choice == 7:

        print("Thank You.....")

    else:

        print("Inavaild choice.")

























