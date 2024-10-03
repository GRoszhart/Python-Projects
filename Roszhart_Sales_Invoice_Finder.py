SearchOption = ''
CountOfRecords = 0
while True:
    SearchOption = input("Search by invoice id (id) or by customer's last name (lname)? ")
    if SearchOption.lower() == 'id' or SearchOption.lower() == 'lname':
        SearchTerm = input("Enter your search term: ")
        break
    else:
        print("Error: You must enter 'id' or 'lname'")
print()
with open('sales_data.csv') as s:
    next(s)
    for DataLines in s:
        DataLines = DataLines.replace("\n","")
        DataSequence = DataLines.split(",")
        if (SearchOption.lower() == 'id' and int(DataSequence[0]) == int(SearchTerm)) or (SearchOption.lower() == 'lname' and DataSequence[2].lower() == SearchTerm.lower()):
            print(DataLines)
            CountOfRecords = CountOfRecords + 1
if CountOfRecords > 0:
    print("Number of records found: ", str(CountOfRecords))
else:
    print("No records were found.")
print("Thank you for using my sales invoice program!")