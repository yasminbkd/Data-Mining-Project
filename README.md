# Data-Mining-Project
# Data Science Salary Estimator:
* Estimates data science salaries to help data scientists know their income when they get a job.
* Scraped over 1000 job descriptions from glassdoor using python and selenium .
* Extract from each job description the words to quantify the value companies put on python, excel, aws, and spark. 
* Optimized to reach the best model. 
## Web Scraping
Scraped 1000 job postings from glassdoor.com. With each job, we got the following:
*	Job title
*	Salary Estimate
*	Job Description
*	Rating
*	Company Name
*	Location
*	Size
*	Founded
*	Type of ownership
*	Industry
*	Sector
*	Revenue
## Data Cleaning
After scraping the data, I needed to clean it up to be usable for our model. we made the following changes and created the following variables:
* Created a function name clean to put inside it all the change and that we can call it later 
* we removed all the columns with -1 value
* we removed all the text and characters we don't need in all columns
* Made columns named for Salary Estimate provided min,max and avg of each salary 
* Removed unwanted characters from Company
* added column that designates the location
* calculated the age of the company 
*	Made columns for if different skills were listed in the job description:
    * python  
    * java 
    * machine learning
    * aws
*	Created a function that simplified job title and Seniority 
## Machine Learning 
* we creatrd a function that containe all the work we do in machine learning so we can use it in main
## Data Modeling
* I tried three different models and evaluated them:
*  **KNeighborsClassifier** 
*	 **DecisionTreeClassifier**
*	 **SVC**
*	 **LogisticRegression**
*	 **GaussianNB**
## Model Performance
* I tried three different models and evaluated them:
*  **KNeighborsClassifier** :0.96
*	 **DecisionTreeClassifier**: 0.97
*	 **SVC**:0.94
*	 **LogisticRegression**:0.95
*	 **GaussianNB**:0.77

after this step we choose to predicte our result with tree and we call all the function on the main where we put all the path
## ATTENTION
for this project to work you need to change your path in the project in the main .


Data Mining project made by yasmin ben khedim and iheb masmoudi  
