
import os

# Module for reading CSV files
import csv

#csv file will be in Resources dir at our script level
csvpath = os.path.join('.', 'employee_data.csv')

output_list = []   # define our final output list (which will be the contents of our output file)

newfile = "employee_data2.csv"   # the name of the new output file
new_header_line = "Emp ID,First Name,Last Name,DOB,SSN,State"    #define the new output header line
output_list.append(new_header_line)    # put the header there


# In[2]:


us_state_abbrev = {
            'Alabama': 'AL',
            'Alaska': 'AK',
            'Arizona': 'AZ',
            'Arkansas': 'AR',
            'California': 'CA',
            'Colorado': 'CO',
            'Connecticut': 'CT',
            'Delaware': 'DE',
            'Florida': 'FL',
            'Georgia': 'GA',
            'Hawaii': 'HI',
            'Idaho': 'ID',
            'Illinois': 'IL',
            'Indiana': 'IN',
            'Iowa': 'IA',
            'Kansas': 'KS',
            'Kentucky': 'KY',
            'Louisiana': 'LA',
            'Maine': 'ME',
            'Maryland': 'MD',
            'Massachusetts': 'MA',
            'Michigan': 'MI',
            'Minnesota': 'MN',
            'Mississippi': 'MS',
            'Missouri': 'MO',
            'Montana': 'MT',
            'Nebraska': 'NE',
            'Nevada': 'NV',
            'New Hampshire': 'NH',
            'New Jersey': 'NJ',
            'New Mexico': 'NM',
            'New York': 'NY',
            'North Carolina': 'NC',
            'North Dakota': 'ND',
            'Ohio': 'OH',
            'Oklahoma': 'OK',
            'Oregon': 'OR',
            'Pennsylvania': 'PA',
            'Rhode Island': 'RI',
            'South Carolina': 'SC',
            'South Dakota': 'SD',
            'Tennessee': 'TN',
            'Texas': 'TX',
            'Utah': 'UT',
            'Vermont': 'VT',
            'Virginia': 'VA',
            'Washington': 'WA',
            'West Virginia': 'WV',
            'Wisconsin': 'WI',
            'Wyoming': 'WY',
        }


# In[3]:



with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    
    #new_line = ""  # init this variable to hold our new line content
    
    # Read each row of data after the header
    for row in csvreader:
        #print(row)
        EmployeeID = row[0]
        FullName = row[1]
        DOB = row[2]
        SSN = row[3]
        State = row[4]

        #split up FullName to first and last name per the output request
        TempSplit =  FullName.split(" ")
        FirstName = TempSplit[0]
        LastName = TempSplit[1]

        #convert date format from 1985-12-04  to  12/04/1985
        TempSplit = DOB.split("-")
        NewDOB = TempSplit[1] + "/" + TempSplit[2] + "/" + TempSplit[0]

        TempSplit = SSN.split("-")
        NewSSN = "***-**-" + TempSplit[2]


        for long_state_name, abbrev in us_state_abbrev.items():    #loop thru the dict to find the long state name match
            if State == long_state_name:   #when the given State name matches the dict long state name
                state_abbrev = abbrev   # assign that state's abbrvaition to our abbreviation variable
                break   #break out of the loop, we found the state
        
        #we have our new data now from this row, make it a new string (row) for output file
        newline = EmployeeID + "," + FirstName + "," + LastName + "," + NewDOB + "," +         NewSSN + "," + state_abbrev
        output_list.append(newline)    # put the new row
        
with open(newfile, 'w') as file_object:
    for row in output_list:
        file_object.write(row + "\n")    # need LF at end of each row
        
print("\nFinished!")   



