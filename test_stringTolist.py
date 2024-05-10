
"""Pre-requisite: Django & DRF"""

from unittest.mock import  Mock
from rest_framework.test import APITestCase
from django.db.utils import OperationalError

from .stringTolist import StringToList


class StringToListTestCase(APITestCase):
    """I want to test the stringTolist in three cases:
    - when the right format of string is passed in as argument;
    - when the wrong format of string is passed in as argument;
    - and when no string is given is given as argument
    """


    def test_StringToList(self):
            # testing the right format of string to be passed in
            jove = " [{'date': '2025-04', 'qte': 4, 'code_operation': '12dxx9'}, {'date': '2024-08', 'qte': 7, 'code_operation': '23dd'}] "
            obj = StringToList(jove=jove)
            result = obj.toList()
            assert type(result) == list

            # testing the wrong format of string
            jove = "jovie"
            obj = StringToList(jove=jove)
            result = obj.toList()
            assert result == None

            # in case no string is given
            obj = StringToList()
            result = obj.toList()
            assert result == None

