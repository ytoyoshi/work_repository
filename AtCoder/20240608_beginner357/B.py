def main(s):
    upper_count = sum(1 for c in s if c.isupper())
    lower_count = sum(1 for c in s if c.islower())
    
    if upper_count > lower_count:
        return s.upper()
    else:
        return s.lower()
    
S = input()
print(main(S))