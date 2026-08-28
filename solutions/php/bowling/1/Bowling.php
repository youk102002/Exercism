<?php

declare(strict_types=1);

class Game
{
    private array $rolls = [];

    public function roll(int $pins): void
    {
        // 1. Validation basique des quilles
        if ($pins < 0) {
            throw new Exception('Rolls cannot score negative points');
        }
        if ($pins > 10) {
            throw new Exception('A roll cannot score more than 10 points');
        }

        // 2. Vérifier si la partie est déjà terminée avant d'accepter un nouveau lancer
        if ($this->isGameComplete()) {
            throw new Exception('Cannot roll if game already has ten frames');
        }

        // 3. Validation du cumul de quilles par frame
        $this->validateRoll($pins);

        $this->rolls[] = $pins;
    }

    public function score(): int
    {
        // On ne peut calculer le score que si la partie est terminée
        if (!$this->isGameComplete()) {
            throw new Exception('An incomplete game can not be scored');
        }

        $score = 0;
        $rollIndex = 0;

        for ($frame = 0; $frame < 10; $frame++) {
            if ($this->rolls[$rollIndex] === 10) { // Strike
                $score += 10 + $this->rolls[$rollIndex + 1] + $this->rolls[$rollIndex + 2];
                $rollIndex += 1;
            } elseif ($this->rolls[$rollIndex] + $this->rolls[$rollIndex + 1] === 10) { // Spare
                $score += 10 + $this->rolls[$rollIndex + 2];
                $rollIndex += 2;
            } else { // Open Frame
                $score += $this->rolls[$rollIndex] + $this->rolls[$rollIndex + 1];
                $rollIndex += 2;
            }
        }

        return $score;
    }

    /**
     * Détermine si les 10 frames (et leurs éventuels lancers bonus) sont terminés.
     */
    private function isGameComplete(): bool
    {
        $rollIndex = 0;
        $count = count($this->rolls);

        for ($frame = 0; $frame < 10; $frame++) {
            if ($rollIndex >= $count) {
                return false;
            }

            if ($this->rolls[$rollIndex] === 10) { // Strike
                $rollIndex += 1;
                if ($frame === 9) { // 10ème frame : exige 2 lancers bonus
                    return ($rollIndex + 2) <= $count;
                }
            } else {
                if ($rollIndex + 1 >= $count) {
                    return false;
                }
                if ($this->rolls[$rollIndex] + $this->rolls[$rollIndex + 1] === 10) { // Spare
                    $rollIndex += 2;
                    if ($frame === 9) { // 10ème frame : exige 1 lancer bonus
                        return ($rollIndex + 1) <= $count;
                    }
                } else { // Open Frame
                    $rollIndex += 2;
                }
            }
        }

        return true;
    }

    /**
     * Valide le nombre de quilles du lancer courant par rapport au lancer précédent.
     */
    private function validateRoll(int $pins): void
    {
        $rollIndex = 0;
        $count = count($this->rolls);

        for ($frame = 0; $frame < 10; $frame++) {
            if ($rollIndex >= $count) {
                // Premier lancer de la frame
                return;
            }

            if ($this->rolls[$rollIndex] === 10) { // Strike
                $rollIndex += 1;
                if ($frame === 9) { // Lancers bonus de la 10ème frame
                    if ($rollIndex === $count - 1) { // 2nd lancer bonus
                        $firstBonus = $this->rolls[$count - 1];
                        if ($firstBonus < 10 && ($firstBonus + $pins) > 10) {
                            throw new Exception('Two bonus rolls after a strike cannot score more than 10 points');
                        }
                    }
                }
            } else {
                if ($rollIndex + 1 >= $count) {
                    // Deuxième lancer de la frame normale ou du spare au 10ème frame
                    if (($this->rolls[$rollIndex] + $pins) > 10) {
                        throw new Exception('Pin count exceeds limit for frame');
                    }
                    return;
                }
                $rollIndex += 2;
            }
        }
    }
}