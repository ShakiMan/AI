package minmax;

import game.Kalaha;

import java.util.Random;

public class MinMax {
    private int maxDepth = 8;
    private int player = -1;
    private int nextMoveNumber = -1;

    public int findBest(Kalaha initialPosition, int player) {
        if (initialPosition.isFirstMove()){
            int result = 1 + new Random().nextInt(6);
            if (player == 2){
                result += 7;
            }
            return result;
        }

        this.player = player;
        this.nextMoveNumber = -1;
        minimax(initialPosition, maxDepth, Integer.MIN_VALUE, Integer.MAX_VALUE, true);
        return nextMoveNumber;
    }

    private int minimax(Kalaha position, int depth, int alpha, int beta, boolean maximizingPlayer) {
//        System.out.println(depth);

        if (depth == 0 || position.gameOver()) {
            return position.evaluate(player);
        }


        if (maximizingPlayer) {
            int maxEval = Integer.MIN_VALUE;
            for (Kalaha child : position.getAllChildren(player)) {
                int eval = minimax(child, depth - 1, alpha, beta, false);
                if (depth == maxDepth && eval > maxEval)
                    nextMoveNumber = child.getLastMoveIndex();
                maxEval = Math.max(maxEval, eval);
                alpha = Math.max(alpha, eval);
                /*if (beta <= alpha)
                    break;*/
            }
            return maxEval;
        } else {
            int minEval = Integer.MAX_VALUE;
            for (Kalaha child : position.getAllChildren(player)) {
                int eval = minimax(child, depth - 1, alpha, beta, true);
                if (depth == maxDepth && eval > minEval)
                    nextMoveNumber = child.getLastMoveIndex();
                minEval = Math.min(minEval, eval);
                beta = Math.min(beta, eval);
                /*if (beta <= alpha)
                    break;*/
            }
            return minEval;
        }
    }
}
