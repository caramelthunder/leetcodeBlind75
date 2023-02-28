
class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        email_to_accountIds = {}

        for id, account in enumerate(accounts):
            _, *emails = account
            for email in emails:
                email_to_accountIds[email] = email_to_accountIds.get(email, [])
                email_to_accountIds[email].append(id)
        
        output = []
        visited_emails = set()

        for account_id in range(len(accounts)):
            emails = self.dfs(accounts, email_to_accountIds, visited_emails, account_id)
            if emails:
                output.append([accounts[account_id][0]] + sorted(emails))

        return output

    
    def dfs(self, accounts, email_to_accountIds, visited_emails, account_id):
        emails = []
        for email in accounts[account_id][1:]:
            if email not in visited_emails:
                visited_emails.add(email)
                emails.append(email)
                for id in email_to_accountIds[email]:
                    emails += self.dfs(accounts, email_to_accountIds, visited_emails, id)
        
        return emails