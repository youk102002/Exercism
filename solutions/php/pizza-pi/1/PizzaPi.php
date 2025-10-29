<?php

class PizzaPi
{
    public function calculateDoughRequirement($pizzas, $persons )
    {
        return $pizzas * (($persons * 20) + 200);
        throw new \BadFunctionCallException("Implement the function");
    }

    public function calculateSauceRequirement($pizzas, $can_volume)
    {
        $sauce_per_pizza = 125;
        return $pizzas * $sauce_per_pizza / $can_volume;
        throw new \BadFunctionCallException("Implement the function");
    }

    public function calculateCheeseCubeCoverage($cheese_dimension, $thickness, $diameter)
    {
        return floor((fpow($cheese_dimension,3))/($thickness * M_PI * $diameter));
        throw new \BadFunctionCallException("Implement the function");
    }

    public function calculateLeftOverSlices($pizzas, $friends)
    {
        return ($pizzas * 8) % $friends;
        throw new \BadFunctionCallException("Implement the function");
    }
}
