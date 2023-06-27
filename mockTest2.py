def firstUniqChar(s):
          

        for i in range(len(s)):
            char = s[i]
      
            if s[:i].count(char) == 0 and s[i+1:].count(char) == 0:
                return i

        return -1
