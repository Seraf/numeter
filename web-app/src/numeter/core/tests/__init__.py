from login import Login_TestCase
from storage import Storage_TestCase
from browsing import Index_TestCase, Multiviews_TestCase, Configuration_Profile_TestCase, Configuration_User_TestCase, Configuration_Group_TestCase, Configuration_Storage_TestCase
from management import Manage_User_TestCase, Manage_Storage_TestCase
from hosttree import Hosttree_TestCase
from group_restriction import Access_TestCase

def suite():
    import unittest
    TEST_CASES = (
        'core.tests.login',
        'core.tests.storage',
        'core.tests.browsing',
        'core.tests.management',
        'core.tests.hosttree',
        'core.tests.group_restriction',
    )
    suite = unittest.TestSuite()
    for t in TEST_CASES :
        suite.addTest(unittest.TestLoader().loadTestsFromModule(__import__(t, globals(), locals(), fromlist=["*"])))
    return suite
