"""
In a file called seasons.py, implement a program that prompts the user for their date of birth in YYYY-MM-DD format and then sings prints how old they are in minutes, rounded to the nearest integer, using English words instead of numerals, just like the song from Rent, without any and between words. Since a user might not know the time at which they were born, assume, for simplicity, that the user was born at midnight (i.e., 00:00:00) on that date. And assume that the current time is also midnight. In other words, even if the user runs the program at noon, assume that it’s actually midnight, on the same date. Use datetime.date.today to get today’s date, per docs.python.org/3/library/datetime.html#datetime.date.today.
"""
import sys
from datetime import date
import re
import inflect



def main():
    p = inflect.engine()
    try:
        user_birthday = input('Enter your birthdate: ')
        year,month,day = check_date(user_birthday)
    except (ValueError,TypeError):
        sys.exit('Invalid input')
    valid_date_birth = date(year,month,day)
    date_of_today = date.today()
    date_diff = date_of_today - valid_date_birth
    diff_min = date_diff.days* 24 * 60
    date_diff_word = p.number_to_words(diff_min , andword="")
    print(date_diff_word)


def check_date(user_birthday):
   if checked_birthday := re.search('^([0-9]{4})-([0-9]+)-([0-9]+)$',user_birthday):
      year,month,day = checked_birthday.groups()
      if  int(month) <= 12 and int(day) <= 31 and  int(year) <=2025 :
         return int(year), int(month) , int(day) 
 





if __name__ == "__main__":
    main()  