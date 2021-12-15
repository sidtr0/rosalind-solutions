def hamming_distance(s, t):
    ham_dist = 0
    if len(s) != len(t):
        raise Exception("unequal string length!")
    else:
        s, t = list(s), list(t)
        for i in range(len(s)):
            if s[i] != t[i]:
                ham_dist = ham_dist + 1
            else:
                pass
        print(ham_dist)


hamming_distance("GCGTTGCCTATCCAGGGACGTCTTGTTGATGGCACCAGCCGTCCGGCCTATCTGGAATCCCAAGGAGTGCAGTCGATAAGTAAAGCTACATAGACTTGTTCATACTCCTATCGTAAGAACCTGGTTCCGAGCGCCATGGGGGCTGTATCATACAGGTTAAACGCCTAGCTCCGCAATGGTAAGATGAAGTCCAATCGGTTTCAGTCCCGGTGTAGAAACTAAATCTTCGTGAAGTTCCCTTTATGTCTCCAATACGCGATAAGTACCTAGGGCCCCGATAATTATATTTGATGGCGGCACGGTGTATCGTATCTCATCGTGTGGACATCATGTACCCGTGACCCCGCGCGGGGAGGAAGGAGTTTTCGTACTGCGGTTTCGGGACTAAAGTGAACACCCCCTATCCAAGTATATTCATTGGCTTAACACTGATTGTGGTAAACCAAGCAGACTGGGAACGTAGAGGCACCGAACCTCGCACAGTGGATCGCCACCGGGCCATTGCTATTAGGCCTGCGCACGTAGTTTACCGCCCAAATAGCAAGTACATTATCTGCTCCGTTCTATTGGCCCACCTTCCAAGTTTGCTTCTCACTCCTGCGGACAGGGTAACCTGTCTCTTGTACCGCCGAGGGGAGGAGGTAAGTGATTAAGCGTAAACGCTGTAACTATTCCTGATGCGCCTTTTTAAACCAAGAAGTGCAAAGGTCTTAGAGTATCGCGTCCCCCCCAGGATCTAATATTTGGACCACAACTCGGTGCCTAAATAATTCAACTTGTTCTTACAATAAACACGGGCTCAAGAGCACCATTACTAACTAATAATAGGCGAGGACGAGAGATCCCGTTTAAGGAGGATTCCGAAAATATCGGGGCGACACACCACTAGATCTCTGACTTGTCCTGGGCCAAGCTAGACCCACTAAAAGTATGACTTTACGATAGCCTCTACTG", "ATGGTGACTTGGGCGAACGTTCCCGAAGTAGCCACCCTCCTTTAAACTGAAGTGGAATCCCAGAGAGTGCAGGTGCGCAGTGTAGGCCTTCAAACTGTATTGGAATCCGTTTCTTAGGCATCGCGTTCGAGTCGTTTAGCCGCGGTGTGGGCCAGTTGAAATGCTTTGCCGCGCATCTTTATAATTTACAATCGGCGGACTCCCTGCCCGTGTAGAATGTCGGCCCTCATAAGTCATCCTTTTTGCGTCCCTTACGCACGACACCCTAAAGTCCATTACGAGAGATGCCTTTGGGCCGACGGTTCGTACCAGCTCTGGGCGAGAACCTAATCTGTCAGCGTGCGCTCGGGGTAAGGAATCGGTTCTCGCACCCTGGCTTGGGTACCAATGTTACGAATCGGTGACCTCGAAGAGCGATTGTCGTAACATTGCGGGTCTTCAAACAACACGTTTAGGTAAGCAGAATCGCGCAACGAGTCACAGAAGTACGAAGCCCGGCCTTTGCTAAGGATACAACACATATATTTCAACGCTCGAATAAGGAGGAGCCGTAATTGTACATTCTCCTGGCCCGGCTCCGAACTTTGATTTTCAATCCTACTCCCAGACGCTGCTCTCTTTCGAAGCTGGCTGACGAGCAAGTTAGGCGTGACGCGGATAAGGTGGAACCAATCCCGACAATCATGATTACACAAACAAACGCATAGCTCATGGGGCGACAAATATGCCCAAGGTTCTCAGATTAGGCAAACGAATAGGCACTGATAGGATGCGACTCCTTCGCTCAATAAACAGGTGGTGCCCACGACATTTGCTAGTTCGTGATCGCCGAGGAGTGGCGAACTTGCTTGTGTGTGATTCCGAAGCTAGAGGGTCCGGGCATCCACAGACGTCTTTCCTAGCGTGGTTCAAGGATGCGACGTCATAAATATGGATTTGAAAAAACGATTGGTG")