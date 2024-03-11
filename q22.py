def concatenate_list_with_range(sample_list, n):
    result_list = [item + str(i) for i in range(1, n+1) for item in sample_list]
    return result_list

sample_list = ['p', 'q']
n = 5
output_list = concatenate_list_with_range(sample_list, n)
print(output_list)
