# Start with a copy of user_profile.py from page 149. Build a profile of yourself by calling build_profile(),
# using your first and last names and three other key-value pairs that describe you

def build_profile(f_name, l_name, gender, country, language, **info):
    """Build a dictionary containing everything we know about a user."""
    info['first name'] = f_name
    info['last name'] = l_name
    info['gender'] = gender
    info['country'] = country
    info['language'] = language
    return info

user_info = build_profile("Harry", "Won", "female", "Korea", "Korean")
print(user_info)
