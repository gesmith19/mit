import string
def buildCoder(shift):
    
    d = {}
    
    uc = string.ascii_uppercase
    lc = string.ascii_lowercase

    
    for i in range(len(uc)):    
        d[uc[i]]=uc[(i+shift)%26]
    
    for j in range(len(uc), len(lc) + len(uc)):
        d[lc[j%26]] = lc[(j+shift)%26]
    return d 

 