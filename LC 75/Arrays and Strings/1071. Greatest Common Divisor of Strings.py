def gcdOfStrings(str1: str, str2: str):
    if str1 + str2 != str2 + str1: return ''
    return str1[:gcd_(len(str1), len(str2))]
def gcd_(a, b):
    while(b): a, b = b, a % b
    return a