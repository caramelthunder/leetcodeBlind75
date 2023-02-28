class UnionFind:
    def __init__(self):
        self.groups = {}

    def find(self, x):
        group_x = self.groups.get(x, x)
        if group_x == x:
            self.groups[x] = group_x
        else:
            self.groups[x] = self.find(group_x)
        return self.groups[x] 
    
    def union(self, x, y):
        group_x = self.find(x)
        group_y = self.find(y)
        if group_x != group_y:
            self.groups[group_y] = group_x

class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        graph = {}
        uf = UnionFind()

        for account_id in range(len(accounts)):
            _, *emails = accounts[account_id]
            for email in emails:
                if email not in graph:
                    graph[email] = account_id
                uf.union(graph[email], account_id)
    
        output = {}
        for email, account_id in graph.items():
            group = uf.find(account_id)
            output[group] = output.get(group, [])
            output[group].append(email)

        return [[accounts[name][0]] + sorted(emails) for name, emails in output.items()]