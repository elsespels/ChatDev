import unittest
import file_modifier
class TestFileModifier(unittest.TestCase):
    def test_modify_file(self):
        file_name = "main.py"
        correction = "/Users/marcelo/Documents/dev/chat-dev/ChatDev/WareHouse/project_reviewer_DefaultOrganization_20231226214519"
        expected_result = "main.py /Users/marcelo/Documents/dev/chat-dev/ChatDev/WareHouse/project_reviewer_DefaultOrganization_20231226214519"
        result = file_modifier.modify_file(file_name, correction)
        self.assertEqual(result, expected_result)
if __name__ == "__main__":
    unittest.main()