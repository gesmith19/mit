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
    
def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    ### TODO.

    res = ''
    for ch in text:
        if coder.get(ch,0) > 0:
            res += coder[ch]
        else:
            res += ch
    return res       
            
            