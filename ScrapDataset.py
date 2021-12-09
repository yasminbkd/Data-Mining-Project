#!/usr/bin/env python
# coding: utf-8



#Why Selenium?
#Glassdoor renders its content with Javascript.
#Which means that a simple get request to the webpage below would return only the visible content and We are interested in more than that.
#https://towardsdatascience.com/selenium-tutorial-scraping-glassdoor-com-in-10-minutes-3d0915c6d905



from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium import webdriver
import time
import pandas as pd




def get_jobs(keyword, num_jobs, verbose, path, slp_time):
    
    '''Gathers jobs as a dataframe, scraped from Glassdoor'''
    
    #Initializing the webdriver
    options = webdriver.ChromeOptions()
    
    #we scrape with a new Chrome window every time.
    
    #Change the path to where chromedriver is in your home folder put it in variable driver.
    driver = webdriver.Chrome(executable_path=path, options=options)
    driver.set_window_size(1120, 1000)
    
    url= "https://www.glasdoor.com/Job/jobs.htm?suggestCount=0&suggestChosen=false&clickSource=searchBtn&typedKeyword="+keyword+"&sc.keyword"+keyword+"&sc.keyword=data+Scientist&locT=&locId=&jobType=" 
    # add the site of glass door to chrome 
    driver.get(url)
    jobs = []

    while len(jobs) < num_jobs:  #If true, should be still looking for new jobs.

        #wait until the webpage is loaded.
        #We can use python sleep function to halt the execution of the program for given time in seconds
        time.sleep(slp_time)
        time.sleep(.1)
        
        #Going through each job in this page by their class_name
        #we put in job_buttons the jobs we find in this page
        job_buttons = driver.find_elements_by_class_name("react-job-listing")  
        for job_button in job_buttons:  
                
            print("Progress: {}".format("" + str(len(jobs)) + "/" + str(num_jobs)))

            if len(jobs) >= num_jobs:
                break
  
            job_button.click()  #You might stop searching (because we completed jobs number needed)
     
            time.sleep(1)
    
            collected_successfully = False #initialisation
            #if we couldn't complete searching we need to remove the login window that pop out 
 
            try:
                driver.find_element_by_css_selector('[alt="Close"]').click()  #clicking to the X.  
            except NoSuchElementException:
                pass
            # if we completed searching we will get the information we need from jobs by find_element_by-Xpath and put in in variable
            while not collected_successfully:

                try:
                    company_name = driver.find_element_by_xpath('.//div[@class="css-xuk5ye e1tk4kwz5"]').text
                    location = driver.find_element_by_xpath('.//div[@class="css-56kyx5 e1tk4kwz1"]').text
                    job_title = driver.find_element_by_xpath('.//div[contains(@class, "css-1j389vi e1tk4kwz2")]').text
                    job_description = driver.find_element_by_xpath('.//div[@class="jobDescriptionContent desc"]').text
                    collected_successfully = True
                    
                except:
                    time.sleep(5)

            try:
                salary_estimate = driver.find_element_by_xpath('.//span[@class="css-1hbqxax e1wijj240"]').text
            except NoSuchElementException:
                salary_estimate = -1 #not found value

            try:
                rating = driver.find_element_by_xpath('.//span[@class="css-1m5m32b e1tk4kwz4"]').text
            except NoSuchElementException:
                rating = -1 #not found value

            #Printing for debugging
            if verbose:
                print("Job Title: {}".format(job_title))
                print("Salary Estimate: {}".format(salary_estimate))
                print("Job Description: {}".format(job_description[:500]))
                print("Rating: {}".format(rating))
                print("Company Name: {}".format(company_name))
                print("Location: {}".format(location))

            #Going to the Company tab
            try:
                driver.find_element_by_xpath('.//div[@data-item="tab" and @data-tab-type="overview"]').click()

                try:
                    size = driver.find_element_by_xpath('.//span[text()="Size"]//following-sibling::*').text
                except NoSuchElementException:
                    size = -1

                try:
                    founded = driver.find_element_by_xpath('.//span[text()="Founded"]//following-sibling::*').text
                except NoSuchElementException:
                    founded = -1

                try:
                    type_of_ownership = driver.find_element_by_xpath('.//span[text()="Type"]//following-sibling::*').text
                except NoSuchElementException:
                    type_of_ownership = -1

                try:
                    industry = driver.find_element_by_xpath('.//span[text()="Industry"]//following-sibling::*').text
                except NoSuchElementException:
                    industry = -1

                try:
                    sector = driver.find_element_by_xpath('.//span[text()="Sector"]//following-sibling::*').text
                except NoSuchElementException:
                    sector = -1

                try:
                    revenue = driver.find_element_by_xpath('.//span[text()="Revenue"]//following-sibling::*').text
                except NoSuchElementException:
                    revenue = -1


            except NoSuchElementException:  #for jobs who don't have company tab
                size = -1
                founded = -1
                type_of_ownership = -1
                industry = -1
                sector = -1
                revenue = -1

                
            if verbose:
                print("Size: {}".format(size))
                print("Founded: {}".format(founded))
                print("Type of Ownership: {}".format(type_of_ownership))
                print("Industry: {}".format(industry))
                print("Sector: {}".format(sector))
                print("Revenue: {}".format(revenue))
                print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

            jobs.append({"Job Title" : job_title,
            "Salary Estimate" : salary_estimate,
            "Job Description" : job_description,
            "Rating" : rating,
            "Company Name" : company_name,
            "Location" : location,
            "Size" : size,
            "Founded" : founded,
            "Type of ownership" : type_of_ownership,
            "Industry" : industry,
            "Sector" : sector,
            "Revenue" : revenue})
            #add job to jobs

        #Clicking on the "next page" button
        try:
            driver.find_element_by_xpath('.//a[@data-test="pagination-next"]').click()
        except NoSuchElementException:
            print("Scraping terminated before reaching target number of jobs. Needed {}, got {}.".format(num_jobs, len(jobs)))
            break

    return pd.DataFrame(jobs)  #This line converts the dictionary object into a pandas DataFrame. 

