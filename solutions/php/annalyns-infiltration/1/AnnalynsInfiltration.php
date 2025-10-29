<?php

class AnnalynsInfiltration
{
    public function canFastAttack($is_knight_awake)
    {
        return !$is_knight_awake;
        throw new \BadFunctionCallException("Implement the function");
    }

    public function canSpy(
        $is_knight_awake,
        $is_archer_awake,
        $is_prisoner_awake
    ) {
        return ($is_knight_awake || $is_archer_awake)?true:($is_prisoner_awake);
        throw new \BadFunctionCallException("Implement the function");
    }

    public function canSignal(
        $is_archer_awake,
        $is_prisoner_awake
    ) {        
        if($is_archer_awake){
            return false;
        }else{
            return $is_prisoner_awake;
        }
            
        throw new \BadFunctionCallException("Implement the function");
    }

    public function canLiberate(
        $is_knight_awake,
        $is_archer_awake,
        $is_prisoner_awake,
        $is_dog_present
    ) {
        if($is_dog_present){
            return $is_archer_awake?false:true;            
        }else{
            return ($is_prisoner_awake)?(!($is_knight_awake||$is_archer_awake)):false;
        }
        throw new \BadFunctionCallException("Implement the function");
    }
}
