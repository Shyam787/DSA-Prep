def is_anagram(s, t):

    if len(s) != len(t):
        return False
    
    freq = {}

    for ch in s:
        if ch in freq:
            freq[ch] +=1  # freq[ch] = freq.get(ch, 0) + 1
        else:
            freq[ch] = 1

    for ch in t:
        if ch not in freq:
            return False
        
        freq[ch] -= 1

        if freq[ch] < 0:
            return False
        
    return True

s = 'abb'
t = 'aab'

print(is_anagram(s, t))