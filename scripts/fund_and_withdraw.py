from brownie import FundMe, accounts
from scripts.help_scripts import get_acount


def fund():
    fund_me = FundMe[-1]
    account = get_acount()
    entrance_fee = fund_me.getEntranceFee()
    print(f"The current entry fees is {entrance_fee}")
    print("Funding...")
    fund_me.fund({"from": account, "value": entrance_fee})


def withdraw():
    fund_me = FundMe[-1]
    account = get_acount()
    print("Withdrawing...")
    fund_me.withdraw({"from": account})


def main():
    fund()
    withdraw()
