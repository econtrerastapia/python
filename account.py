class Account:
    '''
    Represents a bank account
    '''
    def __init__(self, name: str) -> None:
        '''
        Creates a new account object
        :param name: account holder's name
        '''
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self,amount: float) -> bool:
        '''
        This function deposits amount user entered
        :param amount: Amount user is depositing
        :return: False if amount is less then or equal to 0;
                 True if amount is greater than 0
        '''
        if amount <= 0:
            return False
        else:
            self.__account_balance += amount
            return True

    def withdraw(self, amount: float) -> bool:
        '''
        This function withdraws amount user entered
        :param amount: Amount user is withdrawing
        :return: False if amount is less then or equal to 0, or if amount is greater than amount in account balance;
                 True if amount is greater 0 and less than or equal to account balance
        '''
        if amount <= 0 or amount > self.__account_balance:
            return False
        else:
            self.__account_balance -= amount
            return True

    def get_balance(self) -> float:
        '''
        Retreives the current balance of the account
        :return: The account balance
        '''
        return self.__account_balance

    def get_name(self) -> str:
        '''
        Retrives the name of the account holder
        :return: The account holder's name
        '''
        return self.__account_name
