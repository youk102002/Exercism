<?php

/*
 * By adding type hints and enabling strict type checking, code can become
 * easier to read, self-documenting and reduce the number of potential bugs.
 * By default, type declarations are non-strict, which means they will attempt
 * to change the original type to match the type specified by the
 * type-declaration.
 *
 * In other words, if you pass a string to a function requiring a float,
 * it will attempt to convert the string value to a float.
 *
 * To enable strict mode, a single declare directive must be placed at the top
 * of the file.
 * This means that the strictness of typing is configured on a per-file basis.
 * This directive not only affects the type declarations of parameters, but also
 * a function's return type.
 *
 * For more info review the Concept on strict type checking in the PHP track
 * <link>.
 *
 * To disable strict typing, comment out the directive below.
 */

declare(strict_types=1);

class Tournament
{
    private string $header = "Team                           | MP |  W |  D |  L |  P";
    public function __construct()
    {
        return $header;
        throw new \BadFunctionCallException("Please implement the Tournament class!");
    }

    private function check_team($team, $teams)
    {
		if(!(array_key_exists($team, $teams)))
        {
            $teams[$team] = ["MP"=>0,"W"=>0,"D"=>0,"L"=>0,"P"=>0];
        }

        return $teams;
    }

    private function add_win($teams, $winner, $loser)
    {
        $teams[$winner]["W"] += 1;
        $teams[$winner]["P"] += 3;
        $teams[$loser]["L"] += 1;        
        return $teams;
    }

    private function add_draw($teams, $home, $away)
    {
        $teams[$home]["D"] += 1;
        $teams[$home]["P"] += 1;
        $teams[$away]["D"] += 1;
        $teams[$away]["P"] += 1;
        return $teams;
    }
    function add_result($teams, $home, $away, $match_result)
    {
        $teams[$home]["MP"] += 1;
        $teams[$away]["MP"] += 1;
        
        if ($match_result == 'win'){
            return $this->add_win($teams, $home, $away);
        }
        
        if ($match_result == 'loss'){
            return $this->add_win($teams, $away, $home);
        }

        if ($match_result == 'draw'){
            return $this->add_draw($teams,$home, $away);
        }
        
        return $teams;
    }

    private function sort($teams)
    {
        $P_column = array_column($teams, 'P');
        // 2. Extraire la colonne secondaire de tri (les noms d'équipe/clés)
        $Team_column = array_keys($teams);

        // 3. Appliquer le tri
        array_multisort(
            // Critère 1 : P (Points)
            $P_column, SORT_DESC, SORT_NUMERIC, // Descendant, comme des nombres        
            // Critère 2 : Nom de l'équipe (Clé)
            $Team_column, SORT_ASC, SORT_STRING,  // Ascendant (alphabétique), comme des chaînes        
            // Le tableau à trier lui-même
            $teams
        );

        return $teams;
    }
            
    private function format_draw($teams)
    {
        // L'en-tête est correct, il définit les alignements souhaités.
        $str = "Team                           | MP |  W |  D |  L |  P\n";
        
        // Convertir les données en une liste de lignes formatées
        $lines = [];
        foreach ($teams as $team => $draw) {
            $line = str_pad((string)$team, 31) . "| "; // 1. Largeur de 31 caractères
            $line .= str_pad((string)$draw["MP"], 2, " ", STR_PAD_LEFT) . " | ";
            $line .= str_pad((string)$draw["W"], 2, " ", STR_PAD_LEFT) . " | ";
            $line .= str_pad((string)$draw["D"], 2, " ", STR_PAD_LEFT) . " | ";
            $line .= str_pad((string)$draw["L"], 2, " ", STR_PAD_LEFT) . " | ";
            $line .= str_pad((string)$draw["P"], 2, " ", STR_PAD_LEFT);
            
            $lines[] = $line;
        }
    
        // 2. Utiliser implode pour joindre les lignes avec '\n', 
        //    ce qui garantit qu'il n'y ait PAS de '\n' après la dernière ligne.
        $str .= implode("\n", $lines); 

        return $str;
    }
    
    public function tally($score)
    {
        if (strlen($score) === 0){
            return $this->header;
        }   

        $results = explode("\n",$score);
        $teams = [];
        foreach ($results as $team){
	        $home = trim(explode(";",$team)[0]);
            $away = trim(explode(";",$team)[1]);
	        $match_result = trim(explode(";",$team)[2]);
            $teams = $this->check_team($home, $teams);
            $teams = $this->check_team($away, $teams);
            $teams = $this->add_result($teams, $home, $away, $match_result);
        }
        $teams = $this->sort($teams);
        
        return $this->format_draw($teams);
    }

}
