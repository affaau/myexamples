'''Build in library'''
import hashlib


m = hashlib.sha1()
msg = "The red fox jumps over the blue dog"
# for ascii message, encoding='ascii' also generate the same result
byte_msg = bytearray(msg, encoding='utf-8')
m.update(byte_msg)
# output ascii message
msg_hex_digest = m.hexdigest()
print(msg_hex_digest)
# 0fec050f02cd6201e2ef871ecf8f9d94c1dab7ae
