import unittest
from room_service import RoomService

# Read more here: https://docs.python.org/3/library/unittest.html# 

class RoomServiceTest(unittest.TestCase):

    def setUp(self) -> None:
        self._room_service = RoomService()

    def test_reserve_room_with_invalid_room_id_returns_false(self):
        self.assertFalse(self._room_service.reserve_room(100))

    def test_reserve_room_with_valid_room_id_returns_true(self):
        self.assertEquals(self._room_service.reserve_room(1), 1)

    def test_reserve_room_with_room_having_max_occupants_returns_false(self):
        pass

    def test_reserve_room_with_room_having_availability_returns_true(self):
        pass

    def test_reserve_room_that_can_only_hold_one_person_returns_false(self):
        pass
        

if __name__ == '__main__':
    unittest.main()