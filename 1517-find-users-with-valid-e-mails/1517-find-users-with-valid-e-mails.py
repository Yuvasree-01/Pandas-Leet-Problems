import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    # pattern = r'^[A-Za-z][A-Za-z0-9_.-]*@leetcode\.com$'
    
    # return users[users["mail"].str.match(pattern)]

    def is_valid(email):
        
        if not email.endswith("@leetcode.com"):
            return False

        username = email[:-13]

        if not username:
            return False

        if not username[0].isalpha():
            return False

        for ch in username:
            if not (
                ch.isalnum()
                or ch in "_.-"
            ):
                return False

        return True


    return users[users["mail"].apply(is_valid)]