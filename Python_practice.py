# Import the datetime class from the datetime module.
##mport datetime as dt
# Use the now() attribute on the datetime class to get the present time.
##now = dt.datetime.now()
# Print the present time.
##print("The time right now is ", now)


#counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

#for county, voters in counties_dict.items():
#    print(f"{county} county has {voters} registered voters.")

#for county in counties_dict.keys():
#    print(county)

#for voters in counties_dict.values():
#    print(voters)

#for county in counties_dict:
#    print(counties_dict[county])

#for county, voters in counties_dict.items():
#    print(str(county)+" county has "+str(voters)+" registered voters")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

#for counti in voting_data:
#    print(f" {voting_data.__getitem__('county')} county has {voting_data.__getitem__('registered_voters')} registered voters")

#for county, voters in voting_data.items():


#    print(county, voters)
#    print(f"{county} county has {voting_data.get(county)} registered voters.")

#for county_dict in voting_data:
#    for value in county_dict.values():
#        print(value)