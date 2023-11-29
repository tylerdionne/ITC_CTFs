from pwn import *
r = remote("cse3801-re-100.chals.io", 443, ssl=True, sni="cse3801-re-100.chals.io")
r.recvuntil("Authenticate >>> ")
r.sendline("AdAstraPerExplotium")
response = r.recvall().decode()
print(response)