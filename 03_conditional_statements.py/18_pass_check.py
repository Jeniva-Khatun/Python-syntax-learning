
password = "dcg543@#"
pass_len = len(password)

if pass_len < 6:
    strength = "weak"

elif pass_len <= 10:
    strength = "medium"

else:
    strength = "strong"

print("password strength is :", strength)    