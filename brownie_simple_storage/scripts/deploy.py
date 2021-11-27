from brownie import accounts, config, SimpleStorage, network

def deploy_simple_storage():
  # account = accounts[0] per rete locale con ganache
  # account = accounts.load("greit") per usare l'account inserito in brownie
  # account = accounts.add(config["wallets"]["from_key"])
  account = get_account()
  simple_storage = SimpleStorage.deploy({"from": account})
  stored_value = simple_storage.retrieve()
  print(stored_value)
  transaction = simple_storage.store(15, {"from": account})
  transaction.wait(1)
  update_stored_value = simple_storage.retrieve()
  print(update_stored_value)

def get_account():
  if(network.show_active() == "development"):
    return accounts[0]
  else:
    return accounts.add(config["wallets"]["from_key"])

def main():
  deploy_simple_storage()