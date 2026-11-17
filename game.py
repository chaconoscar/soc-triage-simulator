# 1. Create a LIST of email dictionaries (using square brackets [ ])
emails = [
    {
        "sender": "support@micr0soft-security.com",
        "subject": "URGENT: Reset your password now!",
        "is_phishing": True
    },
    {
        "sender": "hr@company-internal.com",
        "subject": "Reminder: Submit your timesheet by Friday",
        "is_phishing": False
    },
    {
        "sender": "billing@paypa1-support.net",
        "subject": "Invoice #9942 Attached - Action Required",
        "is_phishing": True
    }
]

# 2. Create a variable to track the player's score
score = 0

print("=== SOC ANALYST SHIFT STARTED ===\n")

# 3. Use a FOR LOOP to go through each email one by one
for email in emails:
    print("----------------------------")
    print("From:", email["sender"])
    print("Subject:", email["subject"])
    print("----------------------------")

    # .strip().lower() cleans up accidental spaces or capital letters (e.g., "YES " -> "yes")
    choice = input("Is this phishing? (yes/no): ").strip().lower()

    # Convert the player's text ("yes" or "no") into a True/False boolean
    player_thinks_phishing = (choice == "yes")

    # Compare the player's guess to the actual answer
    if player_thinks_phishing == email["is_phishing"]:
        print("CORRECT! +100 points\n")
        score += 100
    else:
        print("INCORRECT! -50 points\n")
        score -= 50

# 4. Show final results after the loop finishes
print("============================")
print("SHIFT COMPLETE! Final Score:", score)
