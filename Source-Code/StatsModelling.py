import pandas as pd

"""
@author: moeezkhan
"""

"""
delimiter: seperator of content whule parsing a file = sep --> java regex
header: int list --> row numbers
name: array --> coloumn names
nrows : number of files to read
"""

#Use library to:
"""
    - get 5 rows of data
    - using coloum names via a list
    - file name
    - delimiters (regex)
    - headers
"""

#Getting ages from the adult.data file
def getAgeList(numRows = None):
    colNames = ["age", 
                "workclass", 
                "fnlwgt", 
                "education", 
                "education-num", 
                "marital-status", 
                "occupation", 
                "relationship", 
                "race", 
                "sex", 
                "capital-gain", 
                "capital-loss", 
                "hours-per-week", 
                "native-country", 
                "income"]
    origData = pd.read_csv("data/adult.data", delimiter = ", ", header=None, names=colNames, engine='python', nrows=5)
    return origData.loc[:, 'age'].tolist()


#def main() at the end


#Calculating the mean of all ages in the adult.data file
def calcMean(ages):
    
    #getting the length of the list = total number of ages 
    totalAges = len(ages)
    
    #variable used to sum up  all ages
    sum = 0
    
    #traversing the entire list
    for age in ages:
        sum += age
    
    #calculating the mean using the sum
    mean = sum / totalAges
    
    return mean
 
     
        
#Calculating the Standard Deviation
def calcStdDev(numbers, mean):
    
    length = len(numbers)
    sumMeanDifference = 0
    
    for i in range(0,length, 1):
        meanDifference = numbers[i] - mean
        sqMeanDifference = meanDifference ** 2    #Square
        sumMeanDifference += sqMeanDifference
        
    #Getting the answer without the square root
    stdDevSq = (1 / (length - 1)) * sumMeanDifference
    
    #Square Root
    return stdDevSq ** (1/2)
    


#Calculating the Mode
def calcMode(numbers):
    numFreq = {}
    
    #Track frequencies
    for number in numbers:
        if number in numFreq:
            numFreq[number] += 1
        else:
            numFreq[number] = 1
    
    #Variables to track data 
    maxFreq = -1
    mode = -1
    
    #Traverse the Dictionary
    #Find key with the max frequecy(value)
    for k, v in numFreq.items():
        if v > maxFreq:
            mode = k
            maxFreq = v
        
    return mode
            


# Performing Standardization
def standardize(numbers):
    
    mean = calcMean(numbers)
    stdDev = calcStdDev(numbers, mean)
    length = len(numbers)
        
    for i in range(0, length, 1):
        meanDiff = numbers[i] - mean;
        zScore = meanDiff / stdDev
        numbers[i] = zScore
    
    return numbers
     
    
    
    
#Get 5 rows of ages from adult.data for testing purposes
def main():
    
    #getting the list of ages from the provided function
    ages = getAgeList()
          
    #storing the mean returned by the calcMean function after passing the age list as an argument
    mean = calcMean(ages)
    
    #storing the standard deviation returned by the calcStdDev after passing the list of ages and the mean of the ages
    stdDev = calcStdDev(ages, mean)
    
    #storing the mode returned by the calcMode function after passing in the list of ages
    mode = calcMode(ages)
    
    #printing the answer for testing purposes   
    print("Original List: ", ages)
    print("Mean: ", mean)
    print("StdDev: ", stdDev)
    print("Mode: ", mode)
    print(" ")
    
    
    #updating the ages list by each element's zScore to perform standardization
    stdAges = standardize(ages)
    
    #standardized list mean
    mean = calcMean(ages)
    
    #standardized list standard deviation
    stdDev = calcStdDev(ages, mean)
    
    #standardized list mode
    mode = calcMode(ages)
    
    #printing the answer for testing purposes
    print(" ")
    print("Standardized List: ", stdAges)
    print("Mean: ", mean)
    print("StdDev: ", stdDev)
    print("Mode: ", mode)
    
    
    
#calling the main function for testing purposes
main()


"""
Pandas has been one of the most commonly used tools for Data Science and Machine learning, which is used for data cleaning and analysis. 
Here, Pandas is the best tool for handling this real-world messy data. 
Pandas is built on top of two core Python libraries???matplotlib for data visualization and NumPy for mathematical operations. 
Pandas acts as a wrapper over these libraries, allowing you to access many of matplotlib's and NumPy's methods with less code.
"""
