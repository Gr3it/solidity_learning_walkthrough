from brownie import accounts, config, FundMe, network, MockV3Aggregator
from scripts.helpful_scrips import (get_account, deploy_mocks, LOCAL_CHAIN_ENVIRONMENTS)

def deploy_fund_me():
  # account = accounts[0] per rete locale con ganache
  # account = accounts.load("greit") per usare l'account inserito in brownie
  # account = accounts.add(config["wallets"]["from_key"])
  account = get_account()
  if network.show_active() not in LOCAL_CHAIN_ENVIRONMENTS:
    price_feed_address = config["networks"][network.show_active()]["eth_usd_price_feed"]
  else:
    deploy_mocks()
    price_feed_address = MockV3Aggregator[-1].address

  fund_me = FundMe.deploy(price_feed_address,{"from": account},publish_source = config["networks"][network.show_active()].get("verify"))
  return fund_me

def main():
  deploy_fund_me()