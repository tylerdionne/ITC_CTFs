from pwn import *
r = remote("cse3801-re-400.chals.io", 443, ssl=True, sni="cse3801-re-400.chals.io")
# 586 = var_10 mod var_c
var_14 = 586
r.recvuntil("Authenticate >>> ")
r.sendline(str(var_14))
response = r.recvall().decode()
print(response)