import pytest
from scripts.help_scripts import get_acount, LOCAL_BLOCKCHAIN
from scripts.deploy import deploy_fund_me
from brownie import network, accounts, exceptions
import pytest


def test_can_fund_and_withdraw():
    account = get_acount()
    fund_me = deploy_fund_me()
    entrance_fee = fund_me.getEntranceFee() + 1000
    tx = fund_me.fund({"from": account, "value": entrance_fee})
    tx.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == entrance_fee
    tx2 = fund_me.withdraw({"from": account})
    tx2.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == 0


def test_only_owner():
    if network.show_active() not in LOCAL_BLOCKCHAIN:
        pytest.skip("Only for local testing")
    account = accounts.add()
    fund_me = deploy_fund_me()
    with pytest.raises(exceptions.VirtualMachineError):
        fund_me.withdraw({"from": account})
