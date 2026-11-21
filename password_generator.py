import secrets
import string


def generate_password(length: int) -> str:
    if length < 4:
        raise ValueError(
            "Password length should be at least 4 to include all character types."
        )

    # Character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Guarantee at least one of each character type
    password_chars = [
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(digits),
        secrets.choice(symbols),
    ]

    # Combine all characters and fill the remaining length
    all_chars = lowercase + uppercase + digits + symbols
    for _ in range(length - 4):
        password_chars.append(secrets.choice(all_chars))

    # Shuffle the result so the guaranteed characters aren't always at the start
    secrets.SystemRandom().shuffle(password_chars)

    return "".join(password_chars)


def main():
    try:
        user_input = input("Enter desired password length (minimum 4): ")
        length = int(user_input)
        password = generate_password(length)
        print(f"Generated password: {password}")
    except ValueError as e:
        print(f"Invalid input: {e}")


if __name__ == "__main__":
    main()
