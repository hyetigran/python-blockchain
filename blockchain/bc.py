from functools import reduce
import json
from block import Block
from transaction import Transaction
from utility.hash_util import hash_block
from utility.verification import Verification
from wallet import Wallet
MINING_REWARD = 10


class Blockchain:
    def __init__(self, hosting_node_id):
        genesis_block = Block(0, "", [], 100, 0)
        self.__chain = [genesis_block]
        self.__open_transactions = []
        self.load_data()
        self.hosting_node = hosting_node_id

    def get_chain(self):
        return self.__chain[:]

    def get_open_transactions(self):
        return self.__open_transactions[:]

    def load_data(self):
        try:
            with open('blockchain.txt', mode='r') as f:
                # file_content = pickle.loads(f.read())
                file_content = f.readlines()
                # blockchain = file_content['chain']
                # open_transactions = file_content['ot']
                blockchain = json.loads(file_content[0][:-1])
                updated_blockchain = []
                for block in blockchain:
                    converted_tx = [Transaction(
                        tx['sender'], tx['recipient'], tx['amount']) for tx in block['transactions']]
                    # converted_tx = [OrderedDict(
                    #         [('sender', tx['sender']), ('recipient', tx['recipient']), ('amount', tx['amount'])])
                    #         tx for tx in block['transactions']]
                    updated_block = Block(
                        block['index'], block['previous_hash'], converted_tx, block['proof'], block['time'])
                    updated_blockchain.append(updated_block)
                self.__chain = updated_blockchain
                self.__open_transactions = json.loads(file_content[1])
                updated_transactions = []
                for tx in self.__open_transactions:
                    updated_tx = Transaction(
                        tx['sender'], tx['recipient'], tx['amount'])
                    # updated_tx = [OrderedDict(
                    #         [('sender', tx['sender']), ('recipient',
                    #         tx['recipient']), ('amount', tx['amount'])]
                    # }
                    updated_transactions.append(updated_tx)
                open_transactions = updated_transactions
        # except (IOError, ValueError):
        #     print('File not found!')
        # except:
        #     print("WildCard")
        except (IOError, IndexError):
            print('Handled exception')
        finally:
            print('Cleanup!')

    def save_data(self):
        try:
            with open('blockchain.txt', mode='w') as f:
                saveable_chain = saveable_chain = [block.__dict__ for block in [Block(block_el.index, block_el.previous_hash, [
                    tx.__dict__ for tx in block_el.transactions], block_el.proof, block_el.timestamp) for block_el in self.__chain]]
                f.write(json.dumps(saveable_chain))
                f.write('\n')
                saveable_tx = [tx.__dict__ for tx in self.__open_transactions]
                f.write(json.dumps(saveable_tx))
                # save_data={
                #     'chain': blockchain,
                #     'ot': open_transactions
                # }
                # f.write(pickle.dumps(save_data))
        except IOError:
            print("Saving failed")

    def proof_of_work(self):
        last_block = self.__chain[-1]
        last_hash = hash_block(last_block)
        proof = 0
        while not Verification.valid_proof(self.__open_transactions, last_hash, proof):
            proof += 1
        return proof

    def get_balance(self):
        participant = self.hosting_node
        tx_sender = [[tx.amount for tx in block.transactions
                      if tx.sender == participant] for block in self.__chain]
        open_tx_sender = [tx.amount
                          for tx in self.__open_transactions if tx.sender == participant]
        tx_sender.append(open_tx_sender)
        amount_sent = reduce(
            lambda acc, cur: acc + sum(cur) if len(cur) > 0 else acc + 0, tx_sender, 0)
        tx_recipient = [[tx.amount for tx in block.transactions
                         if tx.recipient == participant] for block in self.__chain]
        amount_recieved = reduce(
            lambda acc, cur: acc + sum(cur) if len(cur) > 0 else acc + 0, tx_recipient, 0)
        return amount_recieved - amount_sent

    def get_last_blockchain_value(self):
        if len(self.__chain) < 1:
            return None
        return self.__chain[-1]

    def add_transaction(self, recipient, sender, signature, amount=1.0):
        if self.hosting_node == None:
            return False
        # transaction = {"sender": sender, 'recipient': recipient, "amount": amount}
        transaction = Transaction(sender, recipient, signature, amount)
        # transaction = OrderedDict(
        #     [('sender', sender), ('recipient', recipient), ('amount', amount)])
        if Verification.verify_transaction(transaction, self.get_balance):
            self.__open_transactions.append(transaction)
            self.save_data()
            return True
        return False

    def mine_block(self):
        if self.hosting_node == None:
            return False
        last_block = self.__chain[-1]
        hashed_block = hash_block(last_block)
        proof = self.proof_of_work()
        # reward_transaction = {
        #     'sender': 'MINING',
        #     'recipient': owner,
        #     'amount': MINING_REWARD
        # }
        reward_transaction = Transaction(
            "Mining", self.hosting_node, '', MINING_REWARD)
        # reward_transaction = OrderedDict(
        #     [('sender', 'MINING'), ('recipient', owner), ('amount', MINING_REWARD)])
        copied_transactions = self.__open_transactions[:]
        for tx in copied_transactions:
            if not Wallet.verify_transaction(tx):
                return False
        copied_transactions.append(reward_transaction)
        block = Block(len(self.__chain), hashed_block,
                      copied_transactions, proof)
        self.__chain.append(block)
        self.__open_transactions = []
        self.save_data()
        return True
