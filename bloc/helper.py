import secrets
import string

def generate_password(length=12, use_symbols=True):
    chars = string.ascii_letters + string.digits
    if use_symbols:
        chars += "!@#$%&*"

    # Guarantee at least one of each type
    password = [
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.digits),
    ]
    if use_symbols:
        password.append(secrets.choice("!@#$%&*"))

    # Fill the rest
    password += [secrets.choice(chars) for _ in range(length - len(password))]

    # Shuffle so guaranteed chars aren't always at the start
    secrets.SystemRandom().shuffle(password)

    return "".join(password)


# ── Usage ──────────────────────────────────────────────────────
print(generate_password())           # 12 chars with symbols  → K#9mX&2pLqR!
print(generate_password(16))         # 16 chars with symbols  → Xm3@kL9#Pq2&RnYw
print(generate_password(10, False))  # 10 chars no symbols    → Kx9mL2pQrT