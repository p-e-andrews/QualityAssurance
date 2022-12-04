"""To calculate this
(birth_year + birth_month) + (required_age_years +  required_age_months) = retirement_year + retirement_month"""
# create chronological list of birth years or ranges when applicable
birth_years = [(range(1900, 1938, 1)), 1938, 1939, 1940, 1941, 1942, (range(1943, 1955, 1)), 1955, 1956, 1957, 1958,
               1959, (range(1960, 2023, 1))]
# create list of retirement age in month and years that aligns with birth_years list
retirement_years_months = [(65, 0), (65, 2), (65, 4), (65, 6), (65, 8), (65, 10), (66, 0), (66, 2), (66, 4), (66, 6),
                           (66, 8), (66, 10), (67, 0)]
# create a dict to pair birth_years and retirement_years_months together
birth_retire_pairs = dict()

# iterate to assign pairs
i = 0
while i < len(birth_years):
    birth_retire_pairs[birth_years[i]] = retirement_years_months[i]
    i += 1
# Test to make sure pairs aligned correctly
# for i in birth_retire_pairs.items():
#     print(i)
# Now I need to bring in their birth year and month
# First find their birth year aka key in the dict
# Then find their retirement value in the dict
# Then add their retirement value to their birth year add birth month for their retirement year and month


def retire(num_year, num_month):
    # find birth year in dict
    year_key = 0
    num_year = int(num_year)    # it comes in as a string, change it to int
    num_month = int(num_month)

    for key in birth_retire_pairs:
        try:    # check to see if key is in a range
            if isinstance(key, range):  # just learned from: https://www.geeksforgeeks.org/type-isinstance-python/
                for range_value in key:    # for range value in key
                    if range_value == num_year:    # if the range value equals the birth year
                        year_key = key
                    else:
                        pass
            else:   # check keys that aren't ranges
                if key == num_year:
                    year_key = key
        except ValueError:
            print("Reference not found")

    # find retirement value in dict
    retirement_value = (birth_retire_pairs.get(year_key))
    # display retirement requirements
    req_year = retirement_value[0]
    req_month = retirement_value[1]
    print(f'Your full retirement age is {req_year} years and {req_month} months')

    # add birth to retirement to find date
    # remember that months can roll over into years, add both month variables for this and compensate
    temp_year = req_year + num_year
    temp_month = req_month + num_month
    final_year = 0
    final_month = 0
    if temp_month >= 12:
        final_month = temp_month - 12
        final_year = temp_year + 1
    else:
        final_month = temp_month
        final_year = temp_year
    month_names = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August',
                   9: 'September', 10: 'October', 11: 'November', 12: 'December'}
    print(f'Your retirement date will be {month_names.get(final_month)} of {final_year}')
