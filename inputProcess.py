#Author: jjsume (Jere Sumell@ Github), January 2019
#You can prevent the SQL-Injection attack by processing the form input data
#With no need of Whitelists or blacklists

forminput = "SELECT * FROM HACKIERSTARGETTABLE"
inputArr = forminput.split(" ")
processedInput = "".join(inputArr).lower()

print("Original input: " +"\n"+ forminput)
print ("Hacker can't input the Malicous code, because after processing:" +"\n" +processedInput) 
