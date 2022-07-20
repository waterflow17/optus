from app import app

import os
import unittest

class AppTestCase(unittest.TestCase):

   def test_root_text(self):
        tester = app.test_client(self)
        response = tester.get('/')
        assert response.status_code == 200
        
   def test_root_text2(self):
        tester = app.test_client(self)
        response = tester.get('/?apparent_t=15')
        assert response.status_code == 200
        
   def test_root_text3(self):
        tester = app.test_client(self)
        response = tester.get('/?apparent_t=xyz')
        assert response.status_code == 200
        
   def test_root_text_with_error(self):
        tester = app.test_client(self)
        response = tester.get('/?createErrorResponse=True')
        assert response.status_code == 503
        

if __name__ == '__main__':
    unittest.main()
