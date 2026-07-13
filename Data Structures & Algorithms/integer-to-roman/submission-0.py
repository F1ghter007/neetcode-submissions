class Solution:
    def intToRoman(self, num: int) -> str:
        d={1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M',4:'IV',9:'IX',40:'XL',90:'XC',400:'CD',900:'CM'}
        temp=num
        ans=""
        x=10
        while temp:
            rem=temp%x
            temp-=rem
            x=x*10
            if d.get(rem,0)!=0:
                ans=d[rem]+ans
            elif rem<5:
                t=d[1]*(rem//1)
                ans=t+ans
            elif rem<10:
                rem-=5
                t=d[5]+(d[1]*(rem//1))
                ans=t+ans
            elif rem<50:
                t=d[10]*(rem//10)
                ans=t+ans
            elif rem<100:
                rem-=50
                t=d[50]+(d[10]*(rem//10))
                ans=t+ans
            elif rem<500:
                t=d[100]*(rem//100)
                ans=t+ans
            elif rem<1000:
                rem-=500
                t=d[500]+(d[100]*(rem//100))
                ans=t+ans
            elif rem<5000:
                t=d[1000]*(rem//1000)
                ans=t+ans
        return ans