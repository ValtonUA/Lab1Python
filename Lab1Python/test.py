import unittest
import arrow
import requests
from app.models import Date


class PythonApi(unittest.TestCase):
    
    def test_get_schedule(self):
        utc = arrow.utcnow()
        res = requests.get('http://localhost:5000/schedule')

        if res.status_code == 200:
            print("Test 'get_schedule()' PASS at " + str(utc))
        else:
            print("Test 'get_schedule()' FAIL at " + str(utc))

    def test_get_date(self):
        utc = arrow.utcnow()
        res = requests.get('http://localhost:5000/schedule/1')

        if res.status_code == 200:
            print("Test 'get_date())' PASS at " + str(utc))
        else:
            print("Test 'get_date()' FAIL at " + str(utc))

    def test_add_schedule(self):
        utc = arrow.utcnow()

        date = Date("2019-03-26", "water some flowers").as_json()

        res = requests.post('http://localhost:5000/schedule', json=date)

        if res.status_code == 201:
            print("Test 'add_games()' PASS at " + str(utc))
        else:
            print("Test 'add_games()' FAIL at " + str(utc))

    def test_edit_date(self):
        utc = arrow.utcnow()

        date = Date("2019-03-26", "water roses", True).as_json()

        res = requests.put('http://localhost:5000/schedule/0', json=date)
        if res.status_code == 200:
            print("Test 'edit_date()' PASS at " + str(utc))
        else:
            print("Test 'edit_date()' FAIL at " + str(utc))
            
    def test_delete_date(self):
        utc = arrow.utcnow()

        res = requests.delete('http://localhost:5000/schedule/3')
        if res.status_code == 200:
            print("Test 'delete_date()' PASS at " + str(utc))
        else:
            print("Test 'delete_date()' FAIL at " + str(utc))

if __name__ == "__main__":
    unittest.main()