
# The task in this interview question is: given a sequence of numbers (A), find a pair of numbers that add up to a second input argument (B). There may not be a valid pair. 

def find_pair_in_seq_naive(seq_of_nums,target_sum): 
    # This is the most basic solution which does a greedy search. 
    # An option exists to copy the list for second iteration and pop index of first number during each iteration. 
    # However, this is not a major efficiency improvement
    sum_equals_target = False
    for index_first_number, value_first_number in enumerate(seq_of_nums): 
        for index_second_number, value_second_number in enumerate(seq_of_nums): 
            if index_second_number != index_first_number: 
                sum_equals_target = target_sum == (value_first_number + value_second_number)
                if sum_equals_target: 
                    print('The matching numbers are: ' + str(value_first_number) + ' and '+ str(value_second_number))
                    return [index_first_number, index_second_number]
    
    # If no values returned during search, nothing was found - return empty 
    print('No pair of numbers which adds to sum.')
    return ''


def find_pair_in_seq_complement(seq_of_nums,target_sum): 
    # Given a number, check if any remaining number complements it to make sum. 
    # Check/assume - numbers can be negative - cannot exclude numbers higher than sum. 
    for num in seq_of_nums: 
        complement = target_sum - num
        if complement in seq_of_nums: 
            print('The matching numbers are: ' + str(num) + ' and '+ str(complement))
            return [num,complement]
    # If no values returned during search, nothing was found - return empty 
    print('No pair of numbers which adds to sum.')
    return ''


if __name__ == '__main__': 
    # seq_of_nums = [1,2,3,9]
    # target_sum = 8
    # print('Test 1: ')
    # find_pair_in_seq_naive(seq_of_nums,target_sum) 

    # seq_of_nums = [1,2,4,4]
    # target_sum = 8
    # print('Test 2: ')
    # find_pair_in_seq_naive(seq_of_nums,target_sum)

    seq_of_nums = [1,2,3,9]
    target_sum = 8
    print('Test 1: ')
    find_pair_in_seq_complement(seq_of_nums,target_sum) 

    seq_of_nums = [1,2,4,4]
    target_sum = 8
    print('Test 2: ')
    find_pair_in_seq_complement(seq_of_nums,target_sum)