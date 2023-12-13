class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        answer=[]
        freq={}
        for cpdomain in cpdomains:
            rep,domain=cpdomain.split()
            domain=domain.split(".")
            for d in range(len(domain)):
                freq[".".join(domain[d:])]=freq.get(".".join(domain[d:]),0)+int(rep)
        for domain,rep in freq.items():
            answer.append(str(rep)+" "+domain)
        return answer
        