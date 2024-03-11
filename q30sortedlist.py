def is_sorted(lst):
    return lst == sorted(lst)

# Example usage
my_list = [1, 2, 3, 4, 5]
print(is_sorted(my_list))  # Output: True

my_list = [5, 4, 3, 2, 1]
print(is_sorted(my_list))  # Output: False