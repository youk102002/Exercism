<?php

class ProgramWindow
{
    public $x, $y, $width, $height;
    
    function __construct(){
        $this->x=0;
        $this->y=0;
        $this->width=800;
        $this->height=600;
    }

    function resize($size){
        $this->height = $size->height;
        $this->width = $size->width;
    }

    function move($position){
        $this->x = $position->x;
        $this->y = $position->y;
    }
}

class Size
{
    public $height, $width;
    
    function __construct($height, $width){
        $this->height = $height;
        $this->width = $width;
    }
}

class Position
{
    public $x, $y;
    
    function __construct($y, $x){
        $this->x = $x;
        $this->y = $y;
    }
}

$window = new ProgramWindow();
$window->x; // => null
$window->y; // => null
$window->width; // => null
$window->height; // => null