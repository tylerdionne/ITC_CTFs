from pwn import *
r = remote("cse3801-re-300.chals.io", 443, ssl=True, sni="cse3801-re-300.chals.io")
r.recvuntil("<<< Nonce ")
# prints random value for rax each time take it in
rax = int(r.recvline().decode().strip())
# want to send a value for var 10 so that (var_10 + rax = 0x7a69)
var_10 = 31337 - rax
r.recvuntil("Authenticate >>> ")
r.sendline(str(var_10))
response = r.recvall().decode()
print(response)