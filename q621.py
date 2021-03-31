freq = collections.Counter(tasks).values()
max_freq = max(freq)

num_max_freq = 0
for i in freq:
    if i == max_freq:
        num_max_freq += 1

ans = (max_freq - 1) * (n + 1) + num_max_freq

s = Solution()
tasks = ["A", "A", "A", "B", "B" ,"B"]
print(s.leastInterval(tasks, 2))