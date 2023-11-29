from pwn import *
r = remote("cse3801-re-200.chals.io", 443, ssl=True, sni="cse3801-re-200.chals.io")
r.recvuntil("Authenticate >>> ")
# want sum of var_10 and var_c to be 0x7a69
r.sendline(“31337 0”)
response = r.recvall().decode()
print(response)