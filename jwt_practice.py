import jwt
# from datetime import timedelta, timezone,datetime

# payload = {
#     'sub':'str{user.id}',
#     'role':'user',
#     'exp':datetime.now(timezone.utc) + timedelta(minutes=1)

# }
# secret_key = "my_super_ecret_key_1234567890a"


# token = jwt.encode(
#     payload,
#     secret_key,
#     algorithm="HS256"
# )
# if secret_key != secret_key:
#     print("Invalid key ")
# else:
#     token_decode = jwt.decode(
#     token,
#     secret_key,
#     algorithms="HS256"
# )

# print(f"Your  encoded token is {token}")
# print("________________________________")
# print(f"Your decoded token is {token_decode}")


payload = {
    "sub": "15",
    "role": "user"
}
secret_key = "my_super_secret_key_1234567890abcd"


encoded_token = jwt.encode(
    payload,
    secret_key,
    algorithm="HS256"
)

decoded = jwt.decode(
    encoded_token,
    secret_key,
    algorithms=["HS256"]
)

print(decoded)

modified_payload = {
    "sub": "15",
    "role": "admin"
}
modified_token = jwt.encode(
    modified_payload,
    secret_key,
    algorithm="HS256"
)
modified_decoded_token = jwt.decode(
    modified_token,
    secret_key,
    algorithms="HS256"
)

print(f"Orginal Encoded Token{encoded_token}")
print("_______________________________________")
print(f"decoded Orginal token{decoded}")
print("_______________________________________")
print(f"Modified token is {modified_token}")
print("_______________________________________")
print(f"Modifed decoded token {modified_decoded_token}")