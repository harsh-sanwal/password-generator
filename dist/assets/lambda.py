# Python code to count occurrences of an element in a list using lambda expression
def count_occurrences(lst, target):
    count = sum(map(lambda x: x == target, lst))
    return count

# Example usage
my_list = [1, 2, 3, 4, 1, 1, 2, 3, 4, 1]
element_to_count = 1
occurrences = count_occurrences(my_list, element_to_count)
print(f"The element {element_to_count} occurs {occurrences} times in the list.")
