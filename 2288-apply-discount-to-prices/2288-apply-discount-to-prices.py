class Solution:
    
    '''
    exp-1
    1x50=50//100-->0.5
    2x50=100//100-->1
    
    
    exp-2
    3x0=0//100-->0
    4x0=------>0
    
    '1','2' '$3'......... using the split function 
    and a[0]==$ and a[1:].isnumeric()
    f'${dollars}.{cents:02}'
    '''
    def discountPrices(self, sentence: str, discount: int) -> str:
        c=sentence.split(' ')
        discount=100-discount
        
        def go(a):
            if a[0]=='$' and a[1:].isnumeric():
                
                c=int(a[1:])
                c*=discount
                dollars=c//100
                cents=c%100
                
                return f"${dollars}.{cents:02}"
            else:
                return  a
            
        
        
        l=[]
        for a in c:
            l.append(go(a))
        
        return " ".join(l)
        