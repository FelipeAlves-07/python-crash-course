age = 18

print("Is age == 18? I predict True.")
print(age == 18)

print("\nIs age != 18? I predict False.")
print(age != 18)

print("\nIs age >= 18? I predict True.")
print(age >= 18)

print("\nIs age > 18? I predict False.")
print(age > 18)

users = ["gabriel", "lucas", "pedro"]
banned_users = ["gabriel", "felipe"]

user = "Gabriel"
print(f"\nIs {user} in users? I predict False")
print(user in users)

user = user.lower()
print(f"\nIs {user} in users? I predict True")
print(user in users)

print(f"\nIs {user} in users and in banned_users? I predict True")
print(user in users and user in banned_users)

user = "lucas"
print(f"\nIs {user} in users and banned_users? I predict False")
print(user in users and user in banned_users)

print(f"\nIs {user} in users or banned_users? I predict True")
print(user in users or user in banned_users)

print(f"\nIs {user} in banned_users? I predict False")
print(user in banned_users)