class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:

        peopleTransactionMapper = defaultdict(list)
        formatedTransactions = []

        for transaction in transactions:
            currTransaction =  transaction.split(",")
            formatedTransactions.append(currTransaction[:])
        
        for eachTransaction in formatedTransactions:
            peopleTransactionMapper[eachTransaction[0]].append(list(eachTransaction[1:]))

        for key in peopleTransactionMapper:
            peopleTransactionMapper[key].sort()
        
        invalidTransaction = []

        for TransactionOwner in peopleTransactionMapper:
            curr = peopleTransactionMapper[TransactionOwner]
        
            leftPointer = 0

            while leftPointer < len(curr):
                rightPointer = 0
                flag = False
                first = ",".join(curr[leftPointer])
                while rightPointer < len(curr):
                    if rightPointer != leftPointer:                    
                        if abs(int(curr[rightPointer][0]) - int(curr[leftPointer][0])) <= 60:
                            if curr[rightPointer][2] != curr[leftPointer][2]:
                                
                                invalidTransaction.append(f"{TransactionOwner},{first}")
                                flag = True
                                break

                    rightPointer += 1

                if not flag:
                    if int(peopleTransactionMapper[TransactionOwner][leftPointer][1]) > 1000:
                    
                        first = ",".join(curr[leftPointer])
                        print(f"{TransactionOwner},{first}")
                        invalidTransaction.append(f"{TransactionOwner},{first}")

                leftPointer += 1

   

        return list(invalidTransaction)
