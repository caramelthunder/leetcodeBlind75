from collections import deque

class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        email_to_accountIds = {}

        for id, account in enumerate(accounts):
            _, *emails = account
            for email in emails:
                email_to_accountIds[email] = email_to_accountIds.get(email, [])
                email_to_accountIds[email].append(id)
        
        output = [[] for _ in accounts]
        visited_emails = set()

        for id in range(len(accounts)):
            if not output[id]:
                self.bfs(accounts, email_to_accountIds, id, visited_emails, output)

        return [[accounts[id][0]] + sorted(output[id]) for id in range(len(output)) if output[id]]

    def bfs(self, accounts, email_to_accountIds, id, visited_emails, output):
        q = deque([(id, email) for email in accounts[id][1:]])

        while q:
            id, email = q.popleft()
            if email not in visited_emails:
                output[id].append(email)
                visited_emails.add(email)

                for neighbor_id in email_to_accountIds[email]:
                    if neighbor_id != id:
                        for neighbor_email in accounts[neighbor_id][1:]:
                            if neighbor_email not in visited_emails:
                                q.append((id, neighbor_email))