def search(pat, txt):
    m = len(pat)
    n = len(txt)

    pat_hash = hash(pat)

    for i in range(n - m + 1):
        piece = txt[i:i+m]
        print(piece)
        txt_hash = hash(piece)
        if txt_hash == pat_hash:
            return i
    return -1

res = search("ADF", "ABCDCBDCBDACBDABDCBADF")

print(res)
