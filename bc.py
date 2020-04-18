blockchain = []


def get_last_blockchain_value():
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_value(value, last_transactoin=[1]):
    if last_transactoin == None:
        last_transactoin = [1]
    blockchain.append([last_transactoin, value])


def get_user_choice():
    user_input = input()


def print_blockchain_history():
    for block in blockchain:
    print("Outputting Block")
    print(block)


def verify_chain():
    block_index - 0
    is_valid = True
    for block in blockchain:
        if block_index == 0:
            block_index += 1
            continue
        if block[0] == blockchain[block_index - 1]
        is_valid = True
        else:
            is_valid = False
            break
        block_index += 1
    return True


while True:
    print('1: transaction')
    print('2: history')
    print('3: manipulate chain')
    print('q: exit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_value(tx_amount, get_last_blockchain_value())
    elif user_choice == '2':
        print_blockchain_history()
    elif user_choice == '3':
        if len(blockchain) > = 1:
            blockchain[0] = [2]
    elif user_choice == 'q':
        break
    else:
        print("input invalid")
    if not verify_chain():
        print("invalid blockchain")
        break
