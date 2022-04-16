n, k, l, c, d, p, nl, np=map(int, input().strip().split())
no_toasts =int(min(((k*l)/nl),c*d,p//np)/n)
print(no_toasts)