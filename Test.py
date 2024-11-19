from datetime import datetime, timedelta

def is_legal_drinking_age(birth_date):
    legal_age_date = datetime.now() - timedelta(days=21 * 365.25)  
    return birth_date <= legal_age_date
  
def run_tests():
    today = datetime.now()
    
    exact_21_years = today - timedelta(days=21 * 365.25)
    print("Test 1 (exactly 21 years):", is_legal_drinking_age(exact_21_years))  # Expected: True
    
    older_than_21 = today - timedelta(days=(21 * 365.25) + 1)
    print("Test 2 (older than 21 years):", is_legal_drinking_age(older_than_21)) 
    
    younger_than_21 = today - timedelta(days=(21 * 365.25) - 1)
    print("Test 3 (younger than 21 years):", is_legal_drinking_age(younger_than_21)) 
    
    print("Test 4 (today's date):", is_legal_drinking_age(today))  
    
    leap_year_date = datetime(2004, 2, 29) 
    print("Test 5 (leap year date):", is_legal_drinking_age(leap_year_date)) 

run_tests()
