<?php

declare(strict_types=1);

function isWordIdentic(string $word, string $anagram): bool
{
    return mb_strtolower($word) === mb_strtolower($anagram);
}

function haveWordsEqualLength(string $word, string $anagram): bool
{
    return mb_strlen($word) === mb_strlen($anagram);
}

function compare(string $word, string $anagram): bool
{
    // Décomposition en caractères Unicode
    $tabWord = mb_str_split(mb_strtolower($word));
    $tabAnagram = mb_str_split(mb_strtolower($anagram));

    sort($tabWord);
    sort($tabAnagram);

    return $tabWord === $tabAnagram;
}

function detectAnagrams(string $word, array $anagrams): array
{
    $results = [];

    foreach ($anagrams as $a) {
        // Un anagramme NE DOIT PAS être le même mot, ET DOIT avoir la même longueur
        if (isWordIdentic($word, $a) || !haveWordsEqualLength($word, $a)) {
            continue;
        }

        if (compare($word, $a)) {
            $results[] = $a; // Fix de la faute de frappe ($results au lieu de $result)
        }
    }

    return array_values($results);
}