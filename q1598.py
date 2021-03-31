class Solution:
    def minOperations(self, logs):
        arr = []
        for i in range(len(logs)):
            if (logs[i] == "../"):
                arr = arr[:-1]
            elif (logs[i] == "./"):
                continue
            else:
                arr.append(logs[i])
        return len(arr)

logs = ["d1/","d2/","../","d21/","./"]
s = Solution()
print(s.minOperations(logs))