def suggestedProducts(products, searchWord):
    products.sort()
    result = []
    prefix = ""
    
    for char in searchWord:
        prefix += char
        suggestions = [product for product in products if product.startswith(prefix)]
        result.append(suggestions[:3])
    
    return result

products = ["mobile","mouse","moneypot","monitor","mousepad"]
searchWord = "mouse"
print(suggestedProducts(products, searchWord))