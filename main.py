import ScrapDataset as SD
import pandas as pd
import requests, sys, time, os, argparse
import csv
import CleaningDataset as CD
import MachineLearning as ML


def scrap():
    path = r"C:\Users\MSI\Desktop\datamininggitsubmittests\chromedriver.exe"#put the path in a variable to use it in all the projet
    df = SD.get_jobs('data scientist',1000, False, path, 15)# we need to call the function we used in ScrapDataset 
    df.to_csv(r"dataset1.csv", encoding='utf-8', index= False)
    data_path = r"dataset1.csv"
    return data_path

def clean(data_path):
    df = CD.clean(data_path)# we need to call the function we used in cleaningDataset using the scaped data
    df.to_csv(r"dataset_Cleaned.csv", encoding='utf-8')
    data_clean = r"dataset_Cleaned.csv"
    return data_clean

def machinelearning(data_clean):
    df = ML.machinelearning(data_clean)# we need to call the function we used in machineLearning using the data cleaned
    df.to_csv(r"dataset_ML.csv", encoding='utf-8')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--scrap', required=False)
    parser.add_argument('--clean', required=False, default="False")
    parser.add_argument('--machinelearning', required=False, default="False")
    args = parser.parse_args()
    
    #in the terminal when we want to do something about the data we need to write the title of function with True or False 
    if args.scrap=="True":
        data_path = scrap()
    if args.clean=="True":
        data_clean =clean(data_path)
    if args.machinelearning=="True":
        machinelearning(data_clean)
    
    
