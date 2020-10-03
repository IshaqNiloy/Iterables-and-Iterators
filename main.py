# Enter your code here. Read input from STDIN. Print output to STDOUT

import itertools#To use the combination function

class Itertools():
    def __init__(self, string, k):
        self.string = string
        self.k = k
    
    def find_probability(self):
        counter = 0
        my_list = string.split()
        comination_object = itertools.combinations(my_list, k)#Creates all the combinations
        comination_list = list(comination_object)
        for item in comination_list:
            if 'a' in item:
                counter += 1
        
        print(counter/len(comination_list))

if __name__ == '__main__':
    size_of_list = input()
    string = input()
    k = int(input())
    my_object = Itertools(string, k)
    my_object.find_probability()
