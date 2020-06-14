'''Build in library'''
import hashlib


m = hashlib.sha3_224()
msg = "The red fox jumps over the blue dog"
# for ascii message, encoding='ascii' also generate the same result
byte_msg = bytearray(msg, encoding='utf-8')
m.update(byte_msg)
# output ascii message
msg_hex_digest = m.hexdigest()
print(msg_hex_digest)
# 82a10c2dfbd9d956cebaeb69e376b184ddd19a4911121a4a9f0adf84
