import re

def check_password_strength(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long")

    # Uppercase check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter")

    # Lowercase check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter")

    # Number check
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Include at least one number")

    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Include at least one special character")

    # Strength level
    if score <= 2:
        strength = "Weak Password"
        crack_time = "Very fast (few seconds)"
    elif score <= 4:
        strength = "Medium Password"
        crack_time = "Moderate (minutes to hours)"
    else:
        strength = "Strong Password"
        crack_time = "Very slow (years to crack)"

    return strength, feedback, crack_time
