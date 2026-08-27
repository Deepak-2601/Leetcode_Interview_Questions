def numberToWords(num):
    if num == 0:
        return "Zero"    
    ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    thousands = ["", "Thousand", "Million", "Billion"]

    def convert_hundreds(n):
        result = ""
        if n >= 100:
            result += ones[n // 100] + " Hundred"
            n %= 100
        if n >= 20:
            result += (" " + tens[n // 10]) if result else tens[n // 10]
            n %= 10
        elif n >= 10:
            result += (" " + teens[n - 10]) if result else teens[n - 10]
            n = 0
        if n > 0:
            result += (" " + ones[n]) if result else ones[n]
        return result
    
    if num == 0:
        return "Zero"
    result = ""
    thousand_index = 0
    while num > 0:
        chunk = num % 1000
        if chunk != 0:
            chunk_words = convert_hundreds(chunk)
            if thousand_index > 0:
                chunk_words += " " + thousands[thousand_index]
            result = chunk_words + (" " + result if result else "")
        num //= 1000
        thousand_index += 1
    return result

num = 1234
print(numberToWords(num))