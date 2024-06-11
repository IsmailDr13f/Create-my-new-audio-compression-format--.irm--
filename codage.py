import numpy as np

def rle_compress(data):
    compressed_data = []
    count = 1
    for i in range(1, len(data)):
        if data[i] == data[i-1]:
            count += 1
        else:
            compressed_data.append((count, data[i-1]))
            count = 1
    compressed_data.append((count, data[-1]))
    return compressed_data

def rle_decompress(compressed_data):
    data = []
    for count, value in compressed_data:
        data.extend([value] * count)
    return data

def RLE(seq):   
    L=len(seq)
    seq=seq+" "
    change_index=[0]
    codage=[]
    for i in range(len(seq)-1):
        if seq[i]!=seq[i+1]:
            S=seq[i+1:]
            l=len(S)
            change_index.append(S.index(S[0])+(L-l)+1)

    for j in range(len(change_index)-1):
        occ=seq[int(change_index[j]):int(change_index[j+1])].count(seq[change_index[j]])
        etiq=(seq[change_index[j]],occ)
        codage.append(etiq)
    return codage
def gainRLE(seq,codeRLE):
    L=len(seq)
    G=len(codeRLE)
    return  round(((L-G)/L)*100, 2)
def DecoRLE(code_RLE):
    decoseq=""
    for etiq in code_RLE:
        decoseq+=etiq[0]*etiq[1]
    return decoseq
"""application de codage RLE sur un image binaire"""
def RLE_img_bin(img_arr):
    shp=img_arr.shape
    flat=img_arr.flatten().tolist()
    seq=''.join(str(int(pix)) for pix in flat)
    codage=RLE(seq)
    codage.insert(0,shp)
    return codage
"""application de decodage RLE sur un image binaire"""
def Deco_RLE_img_bin(code_img_bin):
    seq=DecoRLE(code_img_bin[1:])
    pixels=np.array(list(seq),'uint8')
    return pixels.reshape(codage_img_bin[0])
"""application de codage RLE sur un image niveau de gris"""
def RLE_img_ng(img_arr):
    A=img_arr.ravel().tolist()
    shp=img_arr.shape
    binlist=[]
    for i in range(len(A)):
        Z=np.binary_repr(int(A[i]),8)
        binlist.append(Z)
    seq=''.join(str(pix) for pix in binlist)
    codage=RLE(seq)
    codage.insert(0,shp)
    return codage
"""application de decodage RLE sur un image niveau de gris"""
def Deco_RLE_img_ng(code_img_ng):
    seq=DecoRLE(code_img_ng[1:])
    pixels=np.array(list(seq),'uint8')
    E=np.reshape(pixels,(15,11,8))
    decolista=[]
    for i in range(E.shape[0]):
        for j in range(E.shape[1]):
            H=str(''.join(str(pix) for pix in E[i,j]))
            decolista.append(int(H, 2))
    return np.array(decolista).reshape((15,11))
"""Calcule de frequence"""
def symb_freq(txt): 
    l=set(txt)
    long=len(txt)
    dicthuff={}
    for alpha in l:
        dicthuff[alpha]=round(txt.count(alpha)/long,3)
    A={k: v for k, v in sorted(dicthuff.items(), key=lambda item: item[1])}
    return A
"""Huffman"""
def huffman_codage(s):
    # calculer la frequence des caracteres
    freq = symb_freq(s)
    # Creer les noeuds de l arbre de huffman
    nodes = [ [f, [c, ""]] for c, f in freq.items() ]
    # Construire l'arbre de Huffman
    while len(nodes) > 1:
        # Trier les noeuds par ordre de fréquence
        nodes = sorted(nodes, key=lambda x: x[0])
        # recuperer les deux noeuds les moins frequents
        left = nodes[0]
        right = nodes[1]
        # Attribuer un code binaire aux branches de l'arbre
        for pair in left[1:]:
            pair[1] = '0' + pair[1]
        for pair in right[1:]:
            pair[1] = '1' + pair[1]
        # dupliquer les deux noeuds en un seul noeud 
        dup = [left[0] + right[0]] + left[1:] + right[1:]
        nodes = nodes[2:]
        nodes.append(dup)
    # Rcuperer le code binaire de chaque caractere
    codes = {}
    for pair in nodes[0][1:]:
        codes[pair[0]] = pair[1]
    # Encoder la chaîne d'entre avec les codes binaires
    encoded = ''.join([codes[c] for c in s])
    # Retourner la chaîne encodée et la table des codes binaires
    return encoded, codes
"""decodage huffman"""
def huffman_decodage(encoded,codes):
    if type(encoded)==int:
        encoded=str(encoded)
    #Pour stocker les code trover
    decodage=""
    #pour stocker un partie de sequence
    code_actuel=""
    #inversement des valeurs "binnaires" par les clès "caracteres"
    inverse_codes={v:k for k,v in codes.items()}
    #chercher le decodage de chaque partie de encoded
    for binn in encoded:
        code_actuel+=binn
        if code_actuel in inverse_codes.keys():
            decodage+=inverse_codes[code_actuel]
            code_actuel=""
            
    return decodage

def LZW(data):
    codes = {}
    for i in range(256):
        codes[chr(i)] = i
    code = 256
    result = []
    buffer = ""
    for c in data:
        bc = buffer + c
        if bc in codes:
            buffer = bc
        else:
            result.append(codes[buffer])
            codes[bc] = code
            code += 1
            buffer = c
    if buffer:
        result.append(codes[buffer])
    return result

def lzw_compress(data):
    data = np.clip(data, 0, 255).astype(np.uint32)
    dictionary = {}
    for i in range(256):
        dictionary[chr(i)] = i
    compressed_data = []
    s = ""
    for c in data:
        sc = s + chr(c)
        if sc in dictionary:
            s = sc
        else:
            compressed_data.append(dictionary[s])
            dictionary[sc] = len(dictionary)
            s = chr(c)
    if s:
        compressed_data.append(dictionary[s])
    return compressed_data

def lzw_decompress(compressed_data):
    dictionary = {}
    for i in range(256):
        dictionary[i] = chr(i)
    next_code = 256
    decompressed_data = []
    s = chr(compressed_data.pop(0))
    for c in compressed_data:
        if c in dictionary:
            entry = dictionary[c]
        elif c == next_code:
            entry = s + s[0]
        else:
            raise ValueError("Bad compressed code")
        decompressed_data.extend([ord(x) for x in entry])
        dictionary[next_code] = s + entry[0]
        next_code += 1
        s = entry
    return decompressed_data

def LZW_decompress(codes):
    strings = {}
    for i in range(256):
        strings[i] = chr(i)
    code = 256
    result = ""
    buffer = ""
    prev_code = None
    for curr_code in codes:
        if curr_code in strings:
            curr_string = strings[curr_code]
        elif curr_code == code:
            curr_string = buffer + buffer[0]
        else:
            raise ValueError("Invalid LZW code")
        if prev_code is not None:
            strings[code] = strings[prev_code] + curr_string[0]
            code += 1
        result += curr_string
        buffer = curr_string
        prev_code = curr_code
    return result
