# this prog for recording dict in file
import pickle

l1 = ['happiness', 'sadness', 'hello', 'rabbit', 'pain', 'trooper']

f = open('dict1.txt', 'wb')
pickle.dump(l1, f)
f.close()   