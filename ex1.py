s1 = "AAAAAAAB"
s2 = "AAAAB"

s1 = "AAF"
s1 = "AAF"
s2 = "ABCDCBDCBDACBDABDCBADF"
s2 = "ADF"


i = 0
j = 0
nested = 0
iters = 0

while i < len(s1):
    while j < len(s2):
        iters += 1
        c = s1[i]
        p = s2[j]
        i += 1
        if c == p:
            j += 1
            nested += 1
        else:
            j = 0
            if nested:
                i -= nested
            nested = 0


print(i - len(s2))
print(iters)
    


