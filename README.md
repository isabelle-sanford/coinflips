# coinflips
Trying to prove a generalized max for a coin flipping game

Rules:
* You have a nxn board where n is odd. The board has coins on each square, either heads or tails. 
* Two players take turns, where player A flips rows and player B flips columns
* You can only flip a row that has more heads than tails
* When no move is possible, the game ends

Problem: 
Compute a tight upper bound on the number of moves. That is, find positive integer t(n) such that:
* Every possible starting configuration ends in at most t(n) moves
* There is a configuration and sequence of moves such that the game ends in exactly t(n) moves.

(Question taken from EECS 376 at the University of Michigan in Fall 2020, courtesy of a friend in that class.) 
