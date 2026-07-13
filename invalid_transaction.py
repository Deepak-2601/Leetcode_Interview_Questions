def invalid_transactions(transactions):
    invalid = []
    transaction_dict = {}
    for transaction in transactions:
        name, time, amount, city = transaction.split(',')
        time = int(time)
        amount = int(amount)
        if amount > 1000:
            invalid.append(transaction)
        if name not in transaction_dict:
            transaction_dict[name] = []
        for prev_time, prev_city in transaction_dict[name]:
            if abs(prev_time - time) <= 60 and prev_city != city:
                invalid.append(transaction)
                break
        transaction_dict[name].append((time, city))
    return list(set(invalid))

transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
print(invalid_transactions(transactions))
