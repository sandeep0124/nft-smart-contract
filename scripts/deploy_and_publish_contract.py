import os
from brownie import MyToken, accounts
from dotenv import load_dotenv

load_dotenv()


def main():
    account = accounts.load(os.environ.get("ETH_ACCOUNT"), os.environ.get("ETH_ACCOUNT_PASSWORD"))
    MyToken.deploy({'from': account}, publish_source=True)
