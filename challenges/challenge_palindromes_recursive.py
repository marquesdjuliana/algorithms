def is_palindrome_recursive(word, low_index, high_index):

    if len(word) == 0:
        return False

    if low_index >= high_index:
        return True

    if word[low_index] == word[high_index]:
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)

    return False


# word = "Ana"
# low_index = 0
# high_index = len(word) - 1

# result = is_palindrome_recursive(word, low_index, high_index)
# print(result)
