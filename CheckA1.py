#!/usr/bin/env python3

import unittest
from datetime import date, timedelta
from random import randint, shuffle
import sys, os
import subprocess as sp
from importlib import import_module
import ast, inspect

'''
ASSIGNMENT 1 CHECK SCRIPT
Author: Eric Brauer eric.brauer@senecapolytechnic.ca

Description:
TestAfter .. TestDayCount all are testing functions inside students' code. 
TestFinal will run the code as a subprocess and evaluate the std.output.

The precise requirements of each student-created function are specified elsewhere.

The script assumes that the student's filename is named 'assignment1.py' and exists in the same directory as this check script.

NOTE: Feel free to _fork_ and modify this script to suit needs. I will try to fix any issues that arise but this script is provided as-is, with no obligation of warranty or support.
'''

class TestAfter(unittest.TestCase):

    def setUp(self):
        self.filename = 'assignment1.py'
        self.pypath = sys.executable
        error_output = f'{self.filename} cannot be found (HINT: make sure this script AND your file are in the same directory)'
        file = os.path.join(os.getcwd(), self.filename)
        self.assertTrue(os.path.exists(file), msg=error_output)
        try:
            self.a1 = import_module(self.filename.split('.')[0])
        except ModuleNotFoundError:
            print("Cannot find a function inside your assignment1.py. Do not rename or delete any of the required functions.")

    def test_dtypes(self):
        "after() is returning string"
        i = '2023-01-10'
        error_msg = 'Your after() function should accept one string as arg, and return a string.'
        self.assertIsInstance(self.a1.after(i), str, error_msg)

    def test_dates(self):
        "after() will give next date"
        testdat = {
            '2023-01-23': '2023-01-22',
            '2022-11-01': '2022-10-31',
            '2024-06-15': '2024-06-14',
            '2022-03-01': '2022-02-28',
            '2022-01-01': '2021-12-31'
        }
        error_msg = 'Your after() function is not returning the correct output.'
        for e, i in testdat.items():
            self.assertEqual(self.a1.after(i), e, error_msg)
        
    def test_leap(self):
        "after() works with leap year"
        i = '2020-02-28'
        e = '2020-02-29'
        error_msg = "Your after() function is returning the wrong answer for a leap year"
        self.assertEqual(self.a1.after(i), e, error_msg)


class TestDayOfWeek(unittest.TestCase):

    def setUp(self):
        self.filename = 'assignment1.py'
        self.pypath = sys.executable
        error_output = f'{self.filename} cannot be found (HINT: make sure this script AND your file are in the same directory)'
        file = os.path.join(os.getcwd(), self.filename)
        self.assertTrue(os.path.exists(file), msg=error_output)
        try:
            self.a1 = import_module(self.filename.split('.')[0])
        except ModuleNotFoundError:
            print("Cannot find a function inside your assignment1.py. Do not rename or delete any of the required functions.")

    def test_dow(self):
        "test day of week function"
        testdates = [
            '2023-01-23', '2023-01-22',
            '2022-11-01', '2022-10-31',
            '2024-06-15', '2024-06-14',
            '2022-03-01', '2022-02-28',
            '2022-01-01', '2021-12-31'
        ]
        error_msg = 'day_of_week() not returning the expected day of week'
        for datestr in testdates:
            y, m, d = datestr.split('-')
            dobj = date.fromisoformat(datestr)
            e = dobj.strftime('%a').lower()
            self.assertEqual(self.a1.day_of_week(int(y), int(m), int(d)), e, error_msg)

class TestMonMax(unittest.TestCase):

    def setUp(self):
        self.filename = 'assignment1.py'
        self.pypath = sys.executable
        error_output = f'{self.filename} cannot be found (HINT: make sure this script AND your file are in the same directory)'
        file = os.path.join(os.getcwd(), self.filename)
        self.assertTrue(os.path.exists(file), msg=error_output)
        try:
            self.a1 = import_module(self.filename.split('.')[0])
        except ModuleNotFoundError:
            print("Cannot find a function inside your assignment1.py. Do not rename or delete any of the required functions.")

    def test_mon_max(self):
        "test the mon_max function"
        y = 2023
        mon_dict= {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
            7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        for i, e in mon_dict.items():
            error_msg = f'bad output from mon_max function. Input month: {i}. Expected: {e}'
            self.assertEqual(self.a1.mon_max(i, y), e, error_msg)

    def test_leap_max(self):
        "test mon_max with feb of leap/non-leap years"
        years = {2022: 28, 2020: 29, 2024: 29, 2023: 28, 1960: 29, 1969: 28, 2000: 29, 1900: 28}
        for i, e in years.items():
            error_msg = f'bad output from mon_max function. Input year: {i}. Input month: 2. Expected: {e}'
            self.assertEqual(self.a1.mon_max(2, i), e, error_msg)


class TestLeap(unittest.TestCase):

    def setUp(self):
        self.filename = 'assignment1.py'
        self.pypath = sys.executable
        error_output = f'{self.filename} cannot be found (HINT: make sure this script AND your file are in the same directory)'
        file = os.path.join(os.getcwd(), self.filename)
        self.assertTrue(os.path.exists(file), msg=error_output)
        try:
            self.a1 = import_module(self.filename.split('.')[0])
        except ModuleNotFoundError:
            print("Cannot find a function inside your assignment1.py. Do not rename or delete any of the required functions.")

    def test_leap_func(self):
        "leap_year function exists and returns True/False"
        test_dat = {
            2022: False,
            2020: True,
            2024: True,
            2023: False,
            1960: True,
            1969: False,
            2000: True,
            1900: False
        }
        error_msg = 'leap_year() not returning correct True/False for a specific year'
        for i,e in test_dat.items():
            self.assertEqual(self.a1.leap_year(i), e, error_msg)


class TestValidDate(unittest.TestCase):

    def setUp(self):
        self.filename = 'assignment1.py'
        self.pypath = sys.executable
        error_output = f'{self.filename} cannot be found (HINT: make sure this script AND your file are in the same directory)'
        file = os.path.join(os.getcwd(), self.filename)
        self.assertTrue(os.path.exists(file), msg=error_output)
        try:
            self.a1 = import_module(self.filename.split('.')[0])
        except ModuleNotFoundError:
            print("Cannot find a function inside your assignment1.py. Do not rename or delete any of the required functions.")

    def test_valid_dates(self):
        "making sure valid dates return True"
        test_dat = [
            '2022-01-25',
            '2011-03-13',
            '2001-01-01',
            '1539-11-30',
            '2020-02-29',
            '2038-01-19'
        ]
        for date in test_dat:
            error_msg = f'valid_date() not returning true for {date}\n'
            self.assertEqual(self.a1.valid_date(date), True, error_msg)
    
    def test_invalid_dates(self):
        "making sure invalid dates return False"
        test_dat = [
            '2022-25-01',
            '20-03-13',
            '2001-20-01',
            '1539-11-00',
            '2021-02-29',
            '2023-04-31'
        ]
        for date in test_dat:
            error_msg = f'valid_date() not returning false for {date}\n'
            self.assertEqual(self.a1.valid_date(date), False, error_msg)

@unittest.skip("just use sorted bro")
class TestLatestDate(unittest.TestCase):

    def setUp(self):
        self.filename = 'assignment1.py'
        self.pypath = sys.executable
        error_output = f'{self.filename} cannot be found (HINT: make sure this script AND your file are in the same directory)'
        file = os.path.join(os.getcwd(), self.filename)
        self.assertTrue(os.path.exists(file), msg=error_output)
        try:
            self.a1 = import_module(self.filename.split('.')[0])
        except ModuleNotFoundError:
            print("Cannot find a function inside your assignment1.py. Do not rename or delete any of the required functions.")

    def rando_date_str(self):
        y = randint(1800, 2100)
        m = randint(1, 12)
        d = randint(1, 28)  # leave it there to prevent issues
        return f'{y}-{m:02}-{d:02}'

    def test_latest_date(self):
        for _ in range(1, 11):
            date1 = self.rando_date_str()
            date2 = self.rando_date_str()
            dobj1 = date.fromisoformat(date1)
            dobj2 = date.fromisoformat(date2)
            eobj = max(dobj1, dobj2)
            e = eobj.strftime('%Y-%m-%d')
            error_msg = (f'latest_date function not returning correct answer.'
                         f'inputs: {date1} and {date2}.'
                         f'expected: {e}')
            self.assertEqual(self.a1.latest_date(date1, date2), e, error_msg)

    def test_latest_equal(self):
            date1 = self.rando_date_str()
            dobj1 = date.fromisoformat(date1)
            eobj = max(dobj1, dobj1)
            e = eobj.strftime('%Y-%m-%d')
            error_msg = (f'latest_date function not returning correct answer. When given two equal dates, return that date.'
                         f'inputs: {date1} and {date1}.'
                         f'expected: {e}')
            self.assertEqual(self.a1.latest_date(date1, date1), e, error_msg)


class TestDayCount(unittest.TestCase):

    def setUp(self):
        self.filename = 'assignment1.py'
        self.pypath = sys.executable
        error_output = f'{self.filename} cannot be found (HINT: make sure this script AND your file are in the same directory)'
        file = os.path.join(os.getcwd(), self.filename)
        self.assertTrue(os.path.exists(file), msg=error_output)
        try:
            self.a1 = import_module(self.filename.split('.')[0])
        except ModuleNotFoundError:
            print("Cannot find a function inside your assignment1.py. Do not rename or delete any of the required functions.")

    def rando_date_str(self):
        y = randint(2022, 2023)
        m = randint(1, 12)
        d = randint(1, 28)  # leave it there to prevent issues
        return f'{y}-{m:02}-{d:02}'
    
    def count_work_days(self, start_date, end_date):

        WEEKDAY_FRIDAY = 4
        if start_date.weekday() > WEEKDAY_FRIDAY:
            start_date = start_date + timedelta(days=7 - start_date.weekday())

        # if the end date is on a weekend, rewind the date to the previous Friday
        if end_date.weekday() > WEEKDAY_FRIDAY:
            end_date = end_date - timedelta(days=end_date.weekday() - WEEKDAY_FRIDAY)

        if start_date > end_date:
            return 0
        # that makes the difference easy, no remainders etc
        diff_days = (end_date - start_date).days + 1
        weeks = int(diff_days / 7)

        remainder = end_date.weekday() - start_date.weekday() + 1

        if remainder != 0 and end_date.weekday() < start_date.weekday():
            remainder = 5 + remainder

        return weeks * 5 + remainder

    def test_daycount(self):
        "given a start  and end date, returns number of weekends"
        # test_input = {8:['2023-05-01', '2023-05-29'],
        #               2:['2023-05-06', '2023-05-10'],
        #               6:['2023-05-01', '2023-05-21'],
        #               6:['2023-05-18', '2023-06-04']}
        for _ in range(0, 10):
            d1 = self.rando_date_str()
            d2 = self.rando_date_str()
            weekends = 0
            start, end = sorted([d1, d2])
            startobj = date.fromisoformat(start)
            stopobj = date.fromisoformat(end)
            delta = stopobj - startobj + timedelta(days=1)  # inclusive
            workdays = self.count_work_days(startobj, stopobj)
            weekends = delta.days - workdays
            error_msg = (f'day_count() not returning the expected number.'
                         f'start: {start}. end: {end}. given: {weekends}')
            self.assertEqual(self.a1.day_count(start, end), weekends, error_msg)


class TestModuleRestriction(unittest.TestCase):
    "no modules apart from allowed are being imported"
    
    def setUp(self):
        self.filename = 'assignment1.py'
        self.pypath = sys.executable
        error_output = f'{self.filename} cannot be found (HINT: make sure this script AND your file are in the same directory)'
        file = os.path.join(os.getcwd(), self.filename)
        try:
            self.assertTrue(os.path.exists(file), msg=error_output)
        except AssertionError:
            print("Cannot find a function inside your assignment1.py. Do not rename or delete any of the required functions.")
    
    def test_unallowed_module(self):
        "you have imported a prohibited module"
        allowed = ["sys"]  # list of permitted modules
        try:
            src = inspect.getsource(import_module(self.filename.split('.')[0]))
            tree = ast.parse(src)
        except ModuleNotFoundError:
            print("Cannot find a function inside your assignment1.py. Do not rename or delete any of the required functions.")
        stimp = []
        for node in ast.walk(tree):
            if isinstance(node, (ast.Import, ast.ImportFrom)):
                for alias in node.names:
                    stimp.append(alias.name)
        for modname in stimp:
            if modname not in allowed:
                raise AssertionError(f'You have imported a prohibited module.\n'
                    f'module {modname} is not allowed. Review the Wiki' 
                    ' instructions again.')


class TestFinal(unittest.TestCase):

    def setUp(self):
        self.filename = 'assignment1.py'
        self.pypath = sys.executable
        error_output = f'{self.filename} cannot be found (HINT: make sure this script AND your file are in the same directory)'
        file = os.path.join(os.getcwd(), self.filename)
        self.assertTrue(os.path.exists(file), msg=error_output)

    def rando_date_str(self):
        y = randint(2022, 2023)
        m = randint(1, 12)
        d = randint(1, 28)  # leave it there to prevent issues
        return f'{y}-{m:02}-{d:02}'
    
    def count_work_days(self, start_date, end_date):

        WEEKDAY_FRIDAY = 4
        if start_date.weekday() > WEEKDAY_FRIDAY:
            start_date = start_date + timedelta(days=7 - start_date.weekday())

        # if the end date is on a weekend, rewind the date to the previous Friday
        if end_date.weekday() > WEEKDAY_FRIDAY:
            end_date = end_date - timedelta(days=end_date.weekday() - WEEKDAY_FRIDAY)

        if start_date > end_date:
            return 0
        # that makes the difference easy, no remainders etc
        diff_days = (end_date - start_date).days + 1
        weeks = int(diff_days / 7)

        remainder = end_date.weekday() - start_date.weekday() + 1

        if remainder != 0 and end_date.weekday() < start_date.weekday():
            remainder = 5 + remainder

        return weeks * 5 + remainder
    
    def test_weekends_with_proper_order(self):
        "output contains 'X weekend days' w/ dates in correct order"
        for _ in range(0, 10):
            d1 = self.rando_date_str()
            d2 = self.rando_date_str()
            weekends = 0
            start, end = sorted([d1, d2])
            startobj = date.fromisoformat(start)
            stopobj = date.fromisoformat(end)
            delta = stopobj - startobj + timedelta(days=1)  # inclusive
            workdays = self.count_work_days(startobj, stopobj)
            weekends = delta.days - workdays
            input = [start, end]
            e = f'The period between {start} and {end} includes {weekends}'
            cmd = [self.pypath, self.filename] + input
            error_msg = f'Running your script with arguments is not returning the expected result. Review the sample output section of the Wiki.'
            p = sp.Popen(cmd, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.PIPE)
            output, error = p.communicate(timeout=15)
            if p.returncode != 0:
                raise IOError("Error running the script.")
            self.assertRegex(output.decode('utf-8'), e, error_msg)

    def test_weekends_with_reversed_order(self):
        "output contains 'X weekend days'  w/ dates reversed"
        for _ in range(0, 10):
            d1 = self.rando_date_str()
            d2 = self.rando_date_str()
            weekends = 0
            start, end = sorted([d1, d2])
            startobj = date.fromisoformat(start)
            stopobj = date.fromisoformat(end)
            delta = stopobj - startobj + timedelta(days=1)  # inclusive
            workdays = self.count_work_days(startobj, stopobj)
            weekends = delta.days - workdays
            input = [end, start]  # dates are reversed
            e = f'The period between {start} and {end} includes {weekends}'
            cmd = [self.pypath, self.filename] + input
            error_msg = f'Running your script with arguments is not returning the expected result. Review the sample output section of the Wiki.'
            p = sp.Popen(cmd, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.PIPE)
            output, error = p.communicate(timeout=15)
            if p.returncode != 0:
                raise IOError("Error running the script.")
            self.assertRegex(output.decode('utf-8'), e, error_msg)
        

    def test_invalid_date(self):
        "output contains usage when bad date"
        test_dat = [
            '2022-25-01',
            '20-03-13',
            '2001-20-01',
            '1539-11-00',
            '2021-02-29',
            '2023-04-31'
        ]
        error_msg = "Error: Entering an invalid date should call the usage function, return a usage message, and exit."
        e = r'(?i)Usage.*'  # ignore case
        for datestr in test_dat:
            input = [datestr, '2023-05-24']
            shuffle(input)
            cmd = [self.pypath, self.filename] + input
            p = sp.Popen(cmd, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.PIPE)
            output, error = p.communicate(timeout=10)
            self.assertRegex(output.decode('utf-8'), e, error_msg)

    def test_arg_length(self):
        "when args != 2, output contains usage"
        error_msg = "Error: Entering wrong number of args should call the usage function, return a usage message, and exit."
        e = r'(?i)Usage.*'  # ignore case
        input = ['2023-01-25']
        cmd = [self.pypath, self.filename] + input
        p = sp.Popen(cmd, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.PIPE)
        output, error = p.communicate()
        self.assertRegex(output.decode('utf-8'), e, error_msg)

if __name__ == "__main__":
    unittest.main(buffer=True)  # buffer line suppresses a1 printlines from check script output.


