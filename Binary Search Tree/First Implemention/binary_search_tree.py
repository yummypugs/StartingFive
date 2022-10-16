# Pretty sure Vahe wants this done differently!! Not sure why he changed the assignment requirements...



sorted_book = [
    {"#": 1, "name": "A"},
    {"#": 2, "name": "B"},
    {"#": 3, "name": "C"},
    {"#": 4, "name": "D"},
    {"#": 5, "name": "E"},
    {"#": 6, "name": "F"},
    {"#": 7, "name": "G"},
    {"#": 8, "name": "H"}
]

def binary_search_tree(original_list, query_number):
    length = len(original_list)
    middle_index = length // 2

    if query_number == original_list[middle_index]["#"]:
        return original_list[middle_index]
    elif query_number < original_list[middle_index]["#"]:
        return binary_search_tree(original_list[:middle_index], query_number)
    elif query_number > original_list[middle_index]["#"]:
        return binary_search_tree(original_list[middle_index + 1:], query_number)


print(binary_search_tree(sorted_book, 6))