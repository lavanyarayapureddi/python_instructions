# Write a function to check if two sets are disjoint (i.e., have no common elements).
s1={1,2,3}
s2={6,4,5}
a=s1.isdisjoint(s2)
print(a)

s1={1,2,3}
s2={3,4,5}
a=s1.isdisjoint(s2)
print(a)

#Given a list of words, return a set of unique characters found in all words.
l1=['apple','banana','goa']
uni=set("".join(l1))
print(uni)

#Find the symmetric difference of two sets without using symmetric_difference().
#no common elements
s1={1,2,3,4}
s2={3,4,5,6}
a=s1.union(s2)
print(a)
b=s1.intersection(s2)
print(b)
print(a-b)
