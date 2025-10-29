<?php

class LuckyNumbers
{
    public function sumUp(array $digitsOfNumber1, array $digitsOfNumber2): int
    {
        $number1 = implode($digitsOfNumber1);
        $number2 = implode($digitsOfNumber2); 
        return (int) $number1 + (int) $number2;
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
        if ($input === '') {
            return 'Required field';
        }
        
        if ((int) $input <= 0){
            return 'Must be a whole number larger than 0';
        }
        
        return '' ;
        
        throw new \BadFunctionCallException("Implement the function");
    }
}
