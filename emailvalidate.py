def validate_email_address(email):
    if email is None or email == "":
        return False
    
    if " " in email:
        return False
    
     if "@" not in email:
        return False
    
    email_parts = email.split("@")
    
    if len(email_parts) != 2:
        return False
    
    local_part, domain = eparts
    
    # Both parts should be non-empty
    if not local_part or not domain:
        return False
    
    # Domain should have at least one dot (for basic domain validation)
    if "." not in domain:
        return False
    
    return True


validate_email_address("benard@gmail.com")