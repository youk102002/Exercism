<?php

class LuckyNumbers
{
    public function sumUp(array $digitsOfNumber1, array $digitsOfNumber2): int
    {
        return (int) implode($digitsOfNumber1) + (int) implode($digitsOfNumber2);
        
        throw new \BadFunctionCallException("Implement the function");
    }

    public function isPalindrome(int $number): bool
    {
        $reversed_number = strrev((string) $number);
        return ($number == (int) $reversed_number);
        throw new \BadFunctionCallException("Implement the function");
    }

    public function validate(string $input): string
    {
        if (strlen($input)==0){
            return 'Required field';
        }
        
        if ((int) $input <= 0){
            return 'Must be a whole number larger than 0';
        }
        
        return '';
                
        throw new \BadFunctionCallException("Implement the function");
    }
}
