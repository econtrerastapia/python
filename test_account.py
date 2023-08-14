import pytest
from account import *

class TestAccount:
    def test_deposit_method(self):
        account = Account('Rob')

        assert account.deposit(-2) is False
        assert account.get_balance() == pytest.approx(0)

        assert account.deposit(0) is False
        assert account.get_balance() == pytest.approx(0)

        assert account.deposit(50) is True
        assert account.get_balance() == pytest.approx(50)



    def test_withdraw_method(self):
        account = Account('Rob')
        account.deposit(100)

        assert account.withdraw(-5) is False
        assert account.get_balance() == pytest.approx(100)

        assert account.withdraw(0) is False
        assert account.get_balance() == pytest.approx(100)

        assert account.withdraw(200) is False
        assert account.get_balance() == pytest.approx(100)

        assert account.withdraw(50) is True
        assert account.get_balance() == pytest.approx(50)