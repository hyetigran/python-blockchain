from functools import reduce
import hashlib as hl
import json
from collections import OrderedDict
from hash_util import hash_string_256, hash_block

MINING_REWARD = 10
genesis_block = {
    'previous_hash': '',
    'index': 0,
    'transactions': [],
    'proof': 100
}
blockchain = [genesis_block]

open_transactions = []
owner = "Bob"
participants = {'Bob'}


def valid_proof(transactions, last_hash, proof):
    guess = (str(transactions) + str(last_hash) + str(proof)).encode()
    guess_hash = hash_string_256(guess)
    return guess_hash[0:2] == '00'


def proof_of_work():
    last_block = blockchain[-1]
    last_hash = hash_block(last_block)
    proof = 0
    while not valid_proof(open_transactions, last_hash, proof):
        proof += 1
    return proof


def get_balances(participant):
    tx_sender = [[tx['amount'] for tx in block['transactions']
                  if tx['sender'] == participant] for block in blockchain]
    open_tx_sender = [tx['amount']
                      for tx in open_transactions if tx['sender'] == participant]
    tx_sender.append(open_tx_sender)
    amount_sent = reduce(
        lambda acc, cur: acc + sum(cur) if len(cur) > 0 else acc + 0, tx_sender, 0)
    tx_recipient = [[tx['amount'] for tx in block['transactions']
                     if tx['recipient'] == participant] for block in blockchain]
    amount_recieved = reduce(
        lambda acc, cur: acc + sum(cur) if len(cur) > 0 else acc + 0, tx_recipient, 0)
    return amount_recieved - amount_sent


def get_last_blockchain_value():
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def verify_transaction(transaction):
    sender_balance = get_balance(transaction['sender'])
    return sender_balance >= transaction['amount']:


def add_transaction(recipient, sender=owner, amount=1.0,):
    # transaction = {"sender": sender, 'recipient': recipient, "amount": amount}
    transaction = OrderedDict(
        [('sender', sender), ('recipient', recipient), ('amount', amount)])
    if verify_transaction(transaction):
        open_transactions.append(transaction)
        participants.add(sender)
        participants.add(recipient)
        return True
    return False


def mine_block():
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    proof = proof_of_work()
    # reward_transaction = {
    #     'sender': 'MINING',
    #     'recipient': owner,
    #     'amount': MINING_REWARD
    # }
    reward_transaction = OrderedDict(
        [('sender', 'MINING'), ('recipient', owner), ('amount', MINING_REWARD)])
    copied_transactions = open_transactions[:]
    copied_transactions.append(reward_transaction)
    block = {
        'previous_hash': hashed_block,
        'index': len(blockchain),
        'transactions': copied_transactions,
        'proof': proof
    }
    blockchain.append(block)
    return True


def get_transaction_value():
    tx_recipient = input('Enter sender of txn:')
    tx_amount = float(input('Enter txn amount'))
    return (tx_recipient, tx_amount)


def get_user_choice():
    user_input = input()


def print_blockchain_history():
    for block in blockchain:
    print("Outputting Block")
    print(block)


def verify_chain():
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        if block['previous_hash'] != hash_block(blockchain[index-1]):
            return False
        if not valid_proof(block['transactions'][:-1], block['previous_hash'], block['proof']):
            return False
    return True


def verify_transactions():
    return all([verify_transaction(tx) for tx in open_transactions])


waiting_for_input = True
while waiting_for_input:
    print('1: transaction')
    print('2: mine block')
    print('3: history')
    print('4: participants')
    print('5: validity')
    print('h: manipulate chain')
    print('q: exit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        if add_transaction(recipient, amount=amount):
            print("added transaction")
        else:
            print('transaction failed')
    elif user_choice == '2':
        if mine_block():
            open_transactions = []
    elif user_choice == '3':
        print_blockchain_history()
    elif user_choice == '4':
        print(participants)
    elif user_choice == '5':
        if verify_transactions():
            print('all true')
        else:
            print("invalid exist")
    elif user_choice == 'h':
        if len(blockchain) > = 1:
            blockchain[0] = {
                'previous_hash': '222',
                'index': 1,
                'transactions': []
            }
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print("input invalid")
    if not verify_chain():
        print("invalid blockchain")
        break
