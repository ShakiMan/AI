package minmax;

import game.Kalaha;

import java.util.Random;

public class MinMax {
    private final int maxDepth;
    private int player = -1;
    private int nextMoveNumber = -1;
    private final boolean isAlphaBeta;

    public MinMax(boolean isAlphaBeta, int maxDepth) {
        this.isAlphaBeta = isAlphaBeta;
        this.maxDepth = maxDepth;
    }

    public int findBest(Kalaha initialPosition, int player) {
        if (initialPosition.isFirstMove() && player == 1) {
            return 1 + new Random().nextInt(6);
        }

        this.player = player;
        this.nextMoveNumber = -1;
        minimax(initialPosition, maxDepth, Integer.MIN_VALUE, Integer.MAX_VALUE, true);
        if (nextMoveNumber < 0) {
            if (player == 2) {
                for (int i = 8; i < 14; i++) {
                    if (!initialPosition.isEmptyField(i))
                        nextMoveNumber = i;
                }
            } else {
                for (int i = 1; i < 7; i++) {
                    if (!initialPosition.isEmptyField(i))
                        nextMoveNumber = i;
                }
            }
        }
        return nextMoveNumber;
    }

    private int minimax(Kalaha position, int depth, int alpha, int beta, boolean maximizingPlayer) {
        if (depth == 0 || position.gameOver()) {
            return position.evaluate(player, "anotherAndBeating", position.getLastFieldIndex(), position.getLastMoveIndex());
        }

        if (maximizingPlayer) {
            int maxEval = Integer.MIN_VALUE;
            for (Kalaha child : position.getAllChildren(player)) {
                int eval;
                if (child.checkIfAnotherTurn(child.getLastFieldIndex(), 1)) {
                    eval = minimax(child, depth - 1, alpha, beta, true);
                } else {
                    eval = minimax(child, depth - 1, alpha, beta, false);
                }
                if (depth == maxDepth && eval > maxEval)
                    nextMoveNumber = child.getLastMoveIndex();
                maxEval = Math.max(maxEval, eval);
                if (isAlphaBeta) {
                    alpha = Math.max(alpha, eval);
                    if (beta <= alpha)
                        break;
                }
            }
            return maxEval;
        } else {
            int minEval = Integer.MAX_VALUE;
            for (Kalaha child : position.getAllChildren(player)) {
                int eval;
                if (child.checkIfAnotherTurn(child.getLastFieldIndex(), 2)) {
                    eval = minimax(child, depth - 1, alpha, beta, false);
                } else {
                    eval = minimax(child, depth - 1, alpha, beta, true);
                }
                if (depth == maxDepth && eval > minEval)
                    nextMoveNumber = child.getLastMoveIndex();
                minEval = Math.min(minEval, eval);
                if (isAlphaBeta) {
                    beta = Math.min(beta, eval);
                    if (beta <= alpha)
                        break;
                }
            }
            return minEval;
        }
    }
}
