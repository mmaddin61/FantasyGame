import unittest
import dialogue.data_parser as data_parser

class TestJsonParser(unittest.TestCase):
    def test_load_json_data(self):
        data = None
        try:
            data = data_parser.load_json_data('resources/dialogue/scene_test2.json')
        except:
            self.fail("Failed to load the JSON data.")

        self.assertIsNotNone(data)

    def test_parse_characters(self):
        data = data_parser.load_json_data('resources/dialogue/scene_test2.json')
        characters = data_parser.parse_characters(data)

        self.assertIsNotNone(characters)
        self.assertEqual(len(characters), 1)

        character = characters[0]

        self.assertIsNotNone(character)
        self.assertEqual(character.get_guid(), 'a9878436-3348-945c-42b1-68333338ed75')
        self.assertEqual(character.get_name(), 'Narrator')

if __name__ == '__main__':
    unittest.main()