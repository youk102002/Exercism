def find_anagrams(word, candidates):
    word_lower = word.lower()
    target_sorted = sorted(word_lower)
    anagrams = []
    
    for candidate in candidates :
        candidate_lower = candidate.lower()
        
        if candidate_lower == word_lower :
            continue

        if sorted(candidate_lower) ==  target_sorted : 
            anagrams.append(candidate)
    return anagrams