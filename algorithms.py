import logging
import time

logging.basicConfig(
    # filename='algorithm-output.log',
    level=logging.INFO,
    format='[%(asctime)s] {%(filename)s:%(funcName)s:%(lineno)d} %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger(__name__)



def knapsack_repeat(weight_list: list,value_list: list,total_capactiy: int) -> int:
    """ find the best solution for total_capacity by building up solutions for all capacities up to total_capacity"""
    
    logger.info('knapsack repeat: (weight_list: {}) (value_list: {}) (total_capacity:{})'.format(weight_list,value_list,total_capactiy))
    knapsack = []
    for b in range(total_capactiy):
        logger.info('Checking capacity: {}'.format(b))
        knapsack.append(0)
        for i in range(len(weight_list)):
            logger.info('Checking weight: {} of {}'.format(i,weight_list[i]))
            if weight_list[i] <= b & knapsack[b] < value_list[i] + knapsack[b-weight_list[i]]:
                logger.info('{} greater than {}'.format(
                    value_list[i] + knapsack[b-weight_list[i]], knapsack[b]))
                knapsack[b] = value_list[i] + knapsack[b-weight_list[i]]
        logger.info('Current value: {}'.format(knapsack[-1]))
    logger.info('final max value: {}'.format(knapsack[-1]))
    return knapsack[-1]


def knapsack_repeat_test():
    weight_list = [1,5,2,7,3]
    value_list = [5,5,1,10,1]
    total_capacity = 100
    
    start_time = time.time()
    output = knapsack_repeat(weight_list, value_list, total_capacity)
    total_time = time.time() - start_time
    logger.info('knapsack_repeat {}: {} in {}s'.format(output, total_time))

    
    
    
def fibonacci_recursive(n):
    """
        runtime of n is atleast the nth fibonacci number ,T(n) >= Fn
        sub problems recomputed many times
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def fibonacci_dp(n):
    """
        No recursion, O(n) total time
    """
    f = [0,1] # O(1)
    for i in range(2,n+1): # O(n)
        f.append(f[i-1] + f[i-2]) # O(1)
    return f[-1]
    

def fibonacci_recursive_test():
    n = 35
    start_time = time.time()
    output = fibonacci_recursive(n)
    total_time = time.time() - start_time
    logger.info('fibonacci_recursive {}: {} in {}s'.format(n,output,total_time))
    
def fibonacci_dp_test():
    n = 35
    start_time = time.time()
    output = fibonacci_dp(n)
    total_time = time.time() - start_time
    logger.info('fibonacci_dp {}: {} in {}s'.format(
        n, output, total_time))
    


def longest_increasing_subsequence_dp(input_sequence=[-3,1,4,5,8,9]):
    logger.info('input sequence: {}'.format(input_sequence))
    subsequences = [[] for _ in range(len(input_sequence))]
    subsequence_lengths = []
    
    n = len(input_sequence)
    for i in range(0,n): # O(n^2)
        subsequence_lengths.append(1)
        subsequences[i].append(input_sequence[i])
        for j in range(0,i): # O(n) for n
            if input_sequence[j] < input_sequence[i]:
                if subsequence_lengths[i] < subsequence_lengths[j] + 1:
                    subsequence_lengths[i] = subsequence_lengths[j] + 1
                    subsequences[i] = subsequences[j] + [input_sequence[i]]
                    
    index_max = 0
    for i in range(1,len(input_sequence)): # O(n)
        if subsequence_lengths[i] > subsequence_lengths[index_max]:
            index_max = i 
    logger.info('subsequence lengths: {}'.format(subsequence_lengths))
    logger.info('all subsequences: {}'.format(subsequences))
    logger.info('longest subsequence: {}'.format(subsequences[index_max]))
    return subsequence_lengths[index_max]


def longest_increasing_subsequence_dp_test():
    # input_sequence = [-3, 1, 4, 5, 8, 9]
    input_sequence = [400,-3, 1, 4, 5, 8, 9,1,2,3,4,-1,99,999,5,6,7,8,9]
    start_time = time.time()
    output = longest_increasing_subsequence_dp(input_sequence=input_sequence)
    total_time = time.time() - start_time
    logger.info('longest_increasing_subsequence_dp: {} in {}s'.format(output, total_time))


def longest_common_subsequence_dp(x,y):
    # get subsequence lengths
    lcs = [[0]*(len(y)+1) for _ in range(len(x)+1)] # O(n)
    
    # print('initialized table')
    # for r in lcs:
    #     print(r)
    # print()
    
    for i in range(1,len(x)+1): # O(n^2)
        for j in range(1,len(y)+1): # O(n)
            if x[i-1] == y[j-1]:
                lcs[i][j] = 1 + lcs[i-1][j-1]
            else:
                lcs[i][j] = max(lcs[i][j-1], lcs[i-1][j])
    
    # print('filled table')      
    # for r in lcs:
    #     print(r)
    # print()
        
    sequence = []
    i, j = len(x), len(y)
    while i != 0 and j != 0:
        if lcs[i][j-1] == lcs[i][j]:
            j -= 1
        elif lcs[i-1][j] == lcs[i][j]:
            i -= 1
        elif lcs[i-1][j-1] == lcs[i][j]:
            j -= 1
            i -= 1
        elif lcs[i-1][j-1] < lcs[i][j]:
            sequence.insert(0,x[i-1])
            j -= 1
            i -= 1
            
    sequence = ''.join(sequence)
    logger.info('sequence: {}'.format(sequence))
    return lcs[-1][-1]
    

def longest_common_subsequence_dp_test():
    # x = [400, -3, 1, 4, 5, 8, 9, 1, 2, 3, 4, -1, 99, 999, 5, 6, 7, 8, 9]
    # y = [5, 8, 9, 1, 3, 4, -1, 99]
    # x = 'BCDBCDA'
    # y = 'ABECBA'
    x = 'hdjkgafhsdgfhoiashdufiasdifhaskuidfhgbluiasgdfliasdf'
    y = 'aluskidgfhuioasghydfoiu7asghfuiasdfgaisyudfgliasghfuilasghfd'
    start_time = time.time()
    output = longest_common_subsequence_dp(x,y)
    total_time = time.time() - start_time
    logger.info('longest_common_subsequence_dp: {} in {}s'.format(
        output, total_time))


def main():
    # knapsack_repeat_test()
    # fibonacci_recursive_test()
    # fibonacci_dp_test()
    # longest_increasing_subsequence_dp_test()
    longest_common_subsequence_dp_test()
    
    
if __name__ == '__main__':
    main()
