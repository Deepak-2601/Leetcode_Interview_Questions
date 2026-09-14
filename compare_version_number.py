def compareVersion(version1, version2):
    v1 = list(map(int, version1.split('.')))
    v2 = list(map(int, version2.split('.')))
    max_length = max(len(v1), len(v2))
    v1.extend([0] * (max_length - len(v1)))
    v2.extend([0] * (max_length - len(v2)))    
    for i in range(max_length):
        if v1[i] < v2[i]:
            return -1
        elif v1[i] > v2[i]:
            return 1
    return 0

v1 = "1.0.1"
v2 = "1"
result = compareVersion(v1, v2)
if result == 0:
    print("Version {} is equal to version {}".format(v1, v2))   
elif result < 0:
    print("Version {} is less than version {}".format(v1, v2))
else:
    print("Version {} is greater than version {}".format(v1, v2))
