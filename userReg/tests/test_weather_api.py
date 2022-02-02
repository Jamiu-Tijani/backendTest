from unittest import result
from userReg.tests.test_setup import TestSetUp
from userReg.weather_api import get_weather


class weatherTest(TestSetUp):
    def test_weather_returns_response(self):
        """
        Test the weather api returns json response
        """
        result = get_weather(self.location)
        self.assertEqual(type(result) ,type({}))
        

        