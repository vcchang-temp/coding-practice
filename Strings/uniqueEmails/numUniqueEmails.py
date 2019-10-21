# Unique email addresses

# Time: O(nm)  -> n = # of emails, m = len of each email 
#                 (m can be at most m-2 chars (@ + following char) ~= m)
# Space: O(nm) -> make two sets with at most n emails of len m

from typing import List

def numUniqueEmails(emails: List[str]):
    uniqueEmails = set(emails)
    uniqueEmailsParsed = set()
        
    for email in uniqueEmails:
        i = 0
        localName = []
            
        while email[i] != '@':
            currChar = email[i]
            if currChar == '+':
                uniqueEmailsParsed.add(makeEmail(localName, email))
                break
            if currChar == '.':
                i += 1
                continue
            localName.append(currChar)
            i += 1
        uniqueEmailsParsed.add(makeEmail(localName, email))
            
    return len(uniqueEmailsParsed)
        
def makeEmail(localName: List[str], email: str):
    domainName = email[email.index('@'):]
    return "".join(localName) + domainName

if __name__ == "__main__":
    emails = ["test@email.com", "test+name@email.com", "t.est+name@email.com", "test2+na.me@email.com", "test@em.ail.com"]
    expected = 3
    actual = numUniqueEmails(emails)
    assert actual == expected
    print(f"There are {actual} unique emails in {emails}!")

    emails = ["test@email.com", "test@e+mail.com", "test+name@e", "test+name@gmail.com"]
    expected = 4
    actual = numUniqueEmails(emails)
    assert actual == expected
    print(f"There are {actual} unique emails in {emails}!")