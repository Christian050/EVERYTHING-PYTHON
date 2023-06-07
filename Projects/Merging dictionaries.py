# Merging dictionaries with union operator (|)


Database  = {
    'name' : 'N/A', 
    'age' : 'N/A',
    'country' : 'N/A',
    'contact' : 'N/A'
}


UserData = {
    'name' : 'Christian',
    'country' : 'Ghana',
    'contact' : '+233 54-681-2052'
}


# Union Operator
Database |= UserData


# Update Function
# Database.update(UserData)

# Unpacking Operator
# Database = {**Database, **UserData}







# Printing only values with join method
# print('\t'.join(str(v) for v in Database.values()))

    
print(Database)