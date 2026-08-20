def  licenseKeyFormatting(s,k):
    s = s.replace("-", "").upper()
    first_group_length = len(s) % k or k
    reformatted_key = s[:first_group_length]
    for i in range(first_group_length, len(s), k):
        reformatted_key += '-' + s[i:i+k]
    return reformatted_key

s = "5F3Z-2e-9-w"
k = 4
formatted_key = licenseKeyFormatting(s, k)
print(formatted_key)