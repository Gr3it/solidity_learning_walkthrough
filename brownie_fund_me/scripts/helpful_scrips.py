from brownie import accounts, config, network, MockV3Aggregator
from web3 import Web3

FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork","mainnet-fork-dev"]
LOCAL_CHAIN_ENVIRONMENTS = ["development","ganache-local"]

DECIMALS = 8
# This is 4,000
INITIAL_VALUE = 400000000000

def get_account():
  if (
    network.show_active() in LOCAL_CHAIN_ENVIRONMENTS
    or network.show_active() in FORKED_LOCAL_ENVIRONMENTS
  ):
    return accounts[0]
  else:
    return accounts.add(config["wallets"]["from_key"])

def deploy_mocks():
    """
    Use this script if you want to deploy mocks to a testnet
    """
    print(f"The active network is {network.show_active()}")
    print("Deploying Mocks...")
    account = get_account()
    MockV3Aggregator.deploy(DECIMALS, INITIAL_VALUE, {"from": account})
    print("Mocks Deployed!")