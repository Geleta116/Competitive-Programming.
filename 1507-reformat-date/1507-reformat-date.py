class Solution:
    def reformatDate(self, date: str) -> str:
        monthes = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        d = date.split()
        temp = d[0]
        day = "0"
        if len(temp)==4:
            day = temp[:2]
        else:
            day += temp[0]
            
        mon = monthes.index(d[1])+1
        mon = str(mon)
        mont = "0"
        if len(mon)<2:
            mont += mon
        else:
            mont = mon
            
        year = d[2]
        
        out = str(year)+"-"+str(mont)+"-"+str(day)
        return out
        