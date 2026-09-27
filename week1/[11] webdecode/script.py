import base64

msg = "YWNhZGVteXt3ZWJfc3VjYzNzc2Z1bGx5X2QzYzBkZWRfM2NkMTQ0ZTV9"
decode = base64.b64decode(msg)
print(decode)
