from bc import Blockchain
from uuid import uuid4
from utility.verification import Verification
from wallet import Wallet


class Node:
    def __init__(self):
        self.wallet = Wallet()
        self.wallet.create_keys()
        self.blockchain = Blockchain(self.wallet.public_key)

    def get_transaction_value(self):
        tx_recipient = input('Enter sender of txn:')
        tx_amount = float(input('Enter txn amount'))
        return (tx_recipient, tx_amount)

    def get_user_choice(self):
        user_input = input("User choice: ")

    def print_blockchain_history(self):
        for block in self.blockchain.get_chain:
            print("Outputting Block")
            print(block)

    def listen_for_inputs(self):
        waiting_for_input = True
        while waiting_for_input:
            print('1: transaction')
            print('2: mine block')
            print('3: history')
            print('4: validity')
            print('5: create wallet')
            print('6: load wallet')
            print('7: save wallet')
            print('q: exit')
            user_choice = self.get_user_choice()
            if user_choice == '1':
                tx_data = self.get_transaction_value()
                recipient, amount = tx_data
                if self.blockchain.add_transaction(recipient, self.wallet_public_key, amount=amount):
                    print("added transaction")
                else:
                    print('transaction failed')
            elif user_choice == '2':
                if not self.blockchain.mine_block():
                    print("Mining failed")
            elif user_choice == '3':
                self.print_blockchain_history()
            elif user_choice == '4':
                if Verification.verify_transactions(self.blockchain.get_open_transactions(), self.blockchain.get_balance):
                    print('all true')
                else:
                    print("invalid exist")
            elif user_choice == '5':
                self.wallet.create_keys()
                self.blockchain = Blockchain(self.wallet.public_key)
            elif user_choice == '6':
                self.wallet.load_keys()
                self.blockchain = Blockchain(self.wallet.public_key)
            elif user_choice == '7':
                self.wallet.save_keys()
            elif user_choice == 'q':
                waiting_for_input = False
            else:
                print("input invalid")
            if not Verification.verify_chain(self.blockchain.get_chain()):
                self.print_blockchain_history()
                print("invalid blockchain")
                break


if __name__ == '__main__':
    node = Node()
    node.listen_for_inputs()
