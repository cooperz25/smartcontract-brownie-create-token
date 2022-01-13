from brownie import accounts, config, network, CRNToken
from scripts import helper
import time


def deploy():

    acc = helper.getAccount()
    token = CRNToken.deploy(1 * 10 ** 36, "Chris. Nolan", "CRN", {"from": acc})
    print(f" balance of root acc: {token.balanceOf(acc.address)}")

    addr = "0x752DfF17811dD45d8e5735b65B52b2b2E8CE6fD4"
    token.transfer(addr, 3 * 10 * 18)

    print(f" balance of root acc: {token.balanceOf(acc.address)}")
    print(f" balance of other acc: {token.balanceOf(addr)}")


def main():
    deploy()
