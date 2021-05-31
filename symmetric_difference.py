
m = input()
m_set = set(map(int, input().split()))
n = input()
n_set = set(map(int, input().split()))


m_res = m_set.difference(n_set)
n_res = n_set.difference(m_set)
res = m_res.union(n_res)


print(*sorted(res), sep='\n')

