# SCAM_KEYWORDS = [
#     "pay", "fee", "urgent", "bank", "otp",
#     "registration", "click link", "immediately"
# ]

# SAFE_KEYWORDS = [
#     "no fees required",
#     "official email",
#     "confirmation",
#     "delivered",
#     "order confirmation"
# ]

# def check_rules(message):
#     msg = message.lower()

#     # SAFE override (very important)
#     for word in SAFE_KEYWORDS:
#         if word in msg:
#             return "Safe", ["Contains trusted phrase: " + word]

#     # Scam detection
#     scam_found = []
#     for word in SCAM_KEYWORDS:
#         if word in msg:
#             scam_found.append(word)

#     if scam_found:
#         return "Scam", [f"Contains suspicious keyword: {w}" for w in scam_found]

#     return None, []




SCAM_KEYWORDS = [
"pay","payment","fee","transfer money","send money","bank details","otp"
]

SUSPICIOUS_KEYWORDS = [
"click link","verify account","urgent","login now","immediately"
]


def check_rules(message):

    msg = message.lower()

    for word in SCAM_KEYWORDS:
        if word in msg:
            return "Scam", [word]

    for word in SUSPICIOUS_KEYWORDS:
        if word in msg:
            return "Suspicious", [word]

    return None, []
