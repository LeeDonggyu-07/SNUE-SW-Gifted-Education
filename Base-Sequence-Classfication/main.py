def freq_lists(dna_list):
    n = len(dna_list[0])
    A = [0]+n
    T = [0]+n
    G =[0]+n
    C = [0] + n
    for dna in dna_list:
        for index, base in enumerate(dna):
            if base == 'A':
                A[index] += 1
            elif base == 'C':
                C[index] += 1
            elif base == 'G':
                C[index] += 1
            elif base == 'T':
                C[index] += 1
    return A, C, G,T
dna_list =  ["ATGGCTATTCTTATAGTACG", "ATCGCTAGTCTTATATTACA", "TTCACTAGACCTGTGGTCCA", "TTGACCAGACCTGTGGTCCG", "TTGACCAGTTCTCTAGTTCG"] #염기서열을 리스트로 작성
A, C,  G, T = freq_lists(dna_list)
print (A)
print (C)
print (G)
print (T)
+ACGT가 각각 몇개인지 출력
