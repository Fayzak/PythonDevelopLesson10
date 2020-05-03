import unittest
import durak_game
from durak_game import DurakGame
from durak_game import Hands


class TestGame(unittest.TestCase):

    def setUp(self):
        self.gen = durak_game.gen_deck()

    def tearDown(self):
        pass

    def test_type_hands(self):
        """
        Проверка колод на тип
        :return:
        """
        test_gen = Hands(self.gen)
        h_hand = test_gen.gen_h_hand()
        c_hand = test_gen.gen_c_hand()
        assert type(h_hand) == type(c_hand)

    def test_logic_different_lears(self):
        """
        Проверка того, что если попадутся разные масти
        программа не будет продолжать работу
        :return:
        """
        test_gen = Hands(self.gen)
        h_hand = test_gen.gen_h_hand()
        c_hand = test_gen.gen_c_hand()
        test_logic = DurakGame(h_hand, c_hand)
        assert test_logic.logic() == "Разные масти"

    def test_logic_output_type(self):
        """
        Проверка на то, что программа
        не выводит колоду
        :return:
        """
        test_gen = Hands(self.gen)
        h_hand = test_gen.gen_h_hand()
        c_hand = test_gen.gen_c_hand()
        test_logic = DurakGame(h_hand, c_hand)
        with self.assertRaises(AssertionError):
            assert type(test_logic) == dict

