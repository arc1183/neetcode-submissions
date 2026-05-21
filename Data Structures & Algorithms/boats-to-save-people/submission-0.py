class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        i=0
        j=len(people)-1
        count=0
        people.sort()
        print(people)
        while(i<=j):
            print(people[i],people[j],people[i]+people[j],i,j,count)
            if people[i]+people[j]>limit:
                j-=1
            else:
                i+=1
                j-=1
            
            count+=1
            
        return count
