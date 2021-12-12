def trunc_str(s,n=8):
    ln = len(s)
    if ln <=n:
        return s
    ns = s[:n]
    return ns + ' ...'