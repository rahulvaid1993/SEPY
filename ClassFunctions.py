import unittest
from ClassFunctions import webdriver


class TestDemo(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("")

    # as soon as we added test to the begining,then it is main method
    def test_tab_navigation(self):
        driver = self.driver

        driver

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
# now this is the main class and would be executed first, and the above two lines
# need to be put at the end in order to make it as a main class

