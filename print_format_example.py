'''ref: https://docs.python.org/3.6/library/string.html#formatstrings
'''

print("[1234567890123456]")
print("[{: <16}]".format(-45.346))
print("[{: >16}]".format(-45.346))
print("[{: =16}]".format(-45.346))
print("[{: ^16}]".format(-45.346))

print("[{:<16.2f}]".format(-45.346))
print("[{:>16.2f}]".format(-45.346))
print("[{:=16.2f}]".format(-45.346))
print("[{:^16.2f}]".format(-45.346))

