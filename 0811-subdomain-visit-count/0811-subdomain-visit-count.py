class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        map_web = defaultdict(int)
        for string in cpdomains:
            list_string = string.split()
            count = int(list_string[0])
            domain = list_string[1]
            map_web[domain] += count
            length = len(domain)
            for letter in range(length):
                if domain[letter] == '.':
                    key = domain[letter+1:]
                    map_web[key] += count
        
        answer = []
        for word in map_web:
            subdomain = str(map_web[word]) + " " + word
            answer.append(subdomain)
        return answer
        