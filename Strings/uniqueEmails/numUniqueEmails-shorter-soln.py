# Unique email addresses

# Shorter, more efficient solution that uses Python library fcns
# Time: O(nm)  -> n = # of emails, m = len of each email 
#                 (m can be at most m-2 chars (@ + following char) ~= m)
#                 (.split, .replace, .index each likely O(n))
# Space: O(nm) -> make a set with at most n emails of len m

from typing import List

def numUniqueEmails(emails: List[str]):
    uniqueEmails = set()
    for email in emails:
        local, domain = email.split('@')
        if '+' in local:
            local = local[:local.index('+')]
        uniqueEmails.add(local.replace('.', "") + '@' + domain)
    return len(uniqueEmails)

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