"""The function should perform a linear search to find the target product in the list and return a list of indices of all occurrences of the product if found, or an empty list if the product is not found."""

def linearSearchProduct(product_List, targetProduct):
    indices = []

    for index, product in enumerate(product_List):
        if product == targetProduct:
            indices.append(index)

    return indices

products = ["apple", "orange", "graphs", "banana", "apple", "apple"]
target = input("Enter target: ")

if target in products:
    result = linearSearchProduct(products, target)
    print(result)
else:
    print([])

  