import base64

msg = "YWNhZGVteXtNRTc0RDQ3QV9ISUREM05fYTgxZDk0MzF9Cg=="
decode = base64.b64decode(msg)
print(decode)
