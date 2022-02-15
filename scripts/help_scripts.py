from brownie import accounts, config, network, MockV3Aggregator, accounts
from web3 import Web3

DECIMALS = 8
STARTING_PRICE = 200000000
LOCAL_BLOCKCHAIN = ["development", "ganache_local"]
FORK_NETWORK = ["mainnet-fork-dev"]


def get_acount():
    if network.show_active() in LOCAL_BLOCKCHAIN or FORK_NETWORK:
        return accounts[0]
    else:
        return accounts.add(config['wallets']['from_key'])


def deploy_mocks():
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(DECIMALS, Web3.toWei(
            STARTING_PRICE, "ether"),  {'from': get_acount()})
    print("Deployed to Mock...")
