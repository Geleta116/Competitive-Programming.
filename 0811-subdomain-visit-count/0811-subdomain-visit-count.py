class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        subdomain = defaultdict(int)
        for domain in cpdomains:
            domain = domain.replace(" ",".")
            domain_list = domain.split(".")
            index = len(domain_list)-1
            while index>0:
                subdomain[".".join(domain_list[index:])]+= int(domain_list[0])
                index-=1
        answer = []
        for doms in subdomain:
            each_dom = str(subdomain[doms]) + " " + doms
            answer.append(each_dom)
       
       
        return answer
                
        
        
        