def get_only_duplicate_value_from_array(inputArray: list):
    for row in range(0, len(inputArray)):
        for col in range(row + 1, len(inputArray)):
            if inputArray[row] == inputArray[col]:
                print(inputArray[col])


class RemoveDuplicateValues:
    inputArray = [1, 2, 3, 3, 4, 5]
    get_only_duplicate_value_from_array(inputArray)
