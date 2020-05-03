import pytest
import durak_game
from durak_game import DurakGame
from durak_game import Hands


class TestGame:

    def setup(self):
        self.gen = durak_game.gen_deck()

    def teardown(self):
        pass

    def test_gen(self):
        """
        Проверка на правильное неповторное генерирование колод
        :return:
        """
        test_gen = Hands(self.gen)
        h_hand = test_gen.gen_h_hand()
        c_hand = test_gen.gen_c_hand()
        assert h_hand != c_hand

    def test_count_cards(self):
        """
        Проверка на количество кард в колоде
        :return:
        """
        with pytest.raises(AssertionError):
            assert len(self.gen) == 34

    def test_count_hands(self):
        """
        Проверка на одинаковое количество кард в руке
        :return:
        """
        test_gen = Hands(self.gen)
        h_hand = test_gen.gen_h_hand()
        c_hand = test_gen.gen_c_hand()
        assert len(h_hand) == len(c_hand)
