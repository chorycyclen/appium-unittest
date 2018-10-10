import unittest

from library import config, keywords
from library.preconditions import Preconditions


class C0006(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        keywords.Android.closed_current_driver()

    def setUp(self):
        print('[SetUp]')
        Preconditions.open_and_login_app_using_on_key_login()
        print('[SetUp OK]')

    def tearDown(self):
        pass

    def test_logout(self):
        """
        退出登录
        :return:
        """

        print('[Test Start]')
        keywords.HomePageFooter.open_page_me_by_click_me()
        keywords.swipe_by_percent(50, 80, 50, 20, 500)
        keywords.MePage.click_setting()
        keywords.swipe_by_percent(50, 80, 50, 20, 500)
        keywords.SettingHomePage.logout_app_by_click_quit()
        keywords.Login.wait_for_one_key_login_page_load()
        print('[Test OK]')