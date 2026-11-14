#1. Store a single fake email using a Python Dictionary 
email = {
    "sender": "support@micr0soft-security.com",
    "subject": "URGENT: Reset your password now!",
    "is_phishing": True
}

# 2. Display the email to the player
print("=== INCOMING EMAIL ===")
print("From:", email["sender"])
print("Subject:", email["subject"])
print("=======================")

# 3. Ask the player for their decision
choice = input("Is this phishing? (yes/no): ")

# 4. Check if te player got it right
if choice == "yes" and email["is_phishing"] == True:
    print("Good catch! That is a phishing email.")
else:
    print("Missed! Look closer at the spelling of 'micr0soft'.")