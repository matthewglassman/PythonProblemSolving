#You know a family with three children. Their ages form an arithmetic sequence: the difference in ages between the middle child and youngest child is the same as the difference in ages between the oldest child and the middle child.

youngest = int(input())
middle = int(input())

oldest = (middle - youngest) + middle

print(oldest)