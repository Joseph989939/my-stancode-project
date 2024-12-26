"""
File: webcrawler.py
Name: Joseph
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10900879
Female Number: 7946050
---------------------------
2000s
Male Number: 12977993
Female Number: 9209211
---------------------------
1990s
Male Number: 14146310
Female Number: 10644506
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:  # year to year
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html)
        print('---------------------------')
        print(year)
        # ----- Write your code below this line ----- #
        tags = soup.find_all('tbody')
        for line in tags:
            cleaned_line = line.text  # extract text
            cleaned_line_list = cleaned_line.split()  # merge texts into one list according space
            new_males_number_int = 0
            new_females_number_int = 0
            for i in range(200):  # only run 200 ranks
                males_number = cleaned_line_list[i*5+2]  # the index of each males_number (str)
                female_number = cleaned_line_list[i*5+4]  # the index of each females_number (str)
                new_males_number = ''
                new_females_number = ''
                # remove comma in males_number & females_number (str), put into new string
                for ch in males_number:
                    if ch.isdigit():
                        new_males_number += ch
                for ch in female_number:
                    if ch.isdigit():
                        new_females_number += ch
                # turn str (males_number & females_number) into int, add in new int (total number)
                new_males_number_int += int(new_males_number)
                new_females_number_int += int(new_females_number)
        print('Male Number: ' + str(new_males_number_int))
        print('Female Number: ' + str(new_females_number_int))



if __name__ == '__main__':
    main()
