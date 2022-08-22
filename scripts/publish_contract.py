import os
from brownie import MyToken
from dotenv import load_dotenv

load_dotenv()


def main():
    contract = MyToken.at(os.environ.get("CONTRACT_ADDRESS"))
    MyToken.publish_source(contract)
