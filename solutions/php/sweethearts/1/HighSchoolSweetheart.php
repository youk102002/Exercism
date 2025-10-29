<?php

class HighSchoolSweetheart
{
    public function firstLetter(string $name): string
    {
        return substr(trim($name),0,1);
        throw new \BadFunctionCallException("Implement the function");
    }

    public function initial(string $name): string
    { 
        return mb_strtoupper($this->firstLetter($name)).'.';
        throw new \BadFunctionCallException("Implement the function");
    }

    public function initials(string $name): string
    {
        $names = explode(' ', $name);
        return $this->initial($names[0]).' '.$this->initial($names[1]);
        throw new \BadFunctionCallException("Implement the function");
    }

    public function pair(string $sweetheart_a, string $sweetheart_b): string
    {
        $first = $this->initials($sweetheart_a);
        $second = $this->initials($sweetheart_b);
        $heart = <<<EXPECTED_HEART
         ******       ******
       **      **   **      **
     **         ** **         **
    **            *            **
    **                         **
    **     {$first}  +  {$second}     **
     **                       **
       **                   **
         **               **
           **           **
             **       **
               **   **
                 ***
                  *
    EXPECTED_HEART;
              
        return $heart;
        throw new \BadFunctionCallException("Implement the function");
    }
}
