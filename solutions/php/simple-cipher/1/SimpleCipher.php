<?php

declare(strict_types=1);

class SimpleCipher
{
    public string $key;

    public function __construct(?string $key = null)
    {
        // 1. Si aucune clé n'est fournie, en générer une de 100 caractères
        if ($key === null) {
            $this->key = $this->generateRandomKey();
            return;
        }

        // 2. Validation : La clé ne doit pas être vide et contenir uniquement des minuscules
        if ($key === '' || !preg_match('/^[a-z]+$/', $key)) {
            throw new InvalidArgumentException("La clé doit être composée uniquement de lettres minuscules.");
        }

        $this->key = $key;
    }

    public function encode(string $plainText): string
    {
        return $this->shiftText($plainText, 1);
    }

    public function decode(string $cipherText): string
    {
        return $this->shiftText($cipherText, -1);
    }

    /**
     * Méthode générique pour décaler le texte (direction: +1 pour encode, -1 pour decode)
     */
    private function shiftText(string $text, int $direction): string
    {
        $result = '';
        $keyLength = strlen($this->key);

        for ($i = 0; $i < strlen($text); $i++) {
            // Position de la lettre dans l'alphabet (0 à 25)
            $textCharOffset = ord($text[$i]) - ord('a');
            
            // Décalage fourni par la clé (répétée avec modulo %)
            $keyCharOffset = ord($this->key[$i % $keyLength]) - ord('a');

            // Calcul du nouveau décalage avec modulo 26 pour boucler de 'z' vers 'a'
            $newOffset = ($textCharOffset + ($direction * $keyCharOffset)) % 26;

            // En PHP, le modulo sur un nombre négatif reste négatif (ex: -3 % 26 = -3)
            // On ajoute 26 pour garantir un résultat positif lors du décodage
            if ($newOffset < 0) {
                $newOffset += 26;
            }

            $result .= chr(ord('a') + $newOffset);
        }

        return $result;
    }

    private function generateRandomKey(): string
    {
        $key = '';
        for ($i = 0; $i < 100; $i++) {
            $key .= chr(random_int(ord('a'), ord('z')));
        }
        return $key;
    }
}