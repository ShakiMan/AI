package game;

import java.util.ArrayList;
import java.util.List;

public class Kalaha {
    private final GameBoard gameBoard;
    private int lastFieldIndex = -1;
    private int lastMoveIndex = -100;

    public Kalaha() {
        this.gameBoard = new GameBoard();
        this.gameBoard.initBoard();
    }

    public Kalaha(Kalaha kalaha) {
        this.gameBoard = new GameBoard(kalaha.gameBoard);
        this.lastMoveIndex = kalaha.lastMoveIndex;
        this.lastFieldIndex = kalaha.lastFieldIndex;
    }

    public int getLastFieldIndex() {
        return lastFieldIndex;
    }

    public void setLastFieldIndex(int lastFieldIndex) {
        this.lastFieldIndex = lastFieldIndex;
    }

    public int getLastMoveIndex() {
        return lastMoveIndex;
    }

    public void setLastMoveIndex(int lastMoveIndex) {
        this.lastMoveIndex = lastMoveIndex;
    }

    public int move(int field, int player) {
        /*int end = gameBoard.checkEndGameCondition();
        if (end == -1) {

            int lastField = gameBoard.moveStones(field, player);
            if (lastField > 0) {
                boolean another = gameBoard.checkIfAnotherTurn(lastField, player);
                if (another)
                    return player;
                else {
                    if (player == 1)
                        return 2;
                    else
                        return 1;
                }
            } else {
                if (lastField == -4) {
                    if (player == 1)
                        return 2;
                    else
                        return 1;
                }
                return player;
            }

        } else {
            gameBoard.getRestOfStones(end);
            return whoWon();
        }*/
        int lastField = this.gameBoard.moveStones(field, player);
        int end = this.gameBoard.checkEndGameCondition();

        this.lastMoveIndex = field;
        this.lastFieldIndex = lastField;

        if (end != -1) {
            this.gameBoard.getRestOfStones(end);
            return whoWon();
        }

        if (lastField > 0) {
            boolean another = this.gameBoard.checkIfAnotherTurn(lastField, player);
            if (another)
                return player;
            else {
                if (player == 1)
                    return 2;
                else
                    return 1;
            }
        } else {
            if (lastField == -4) {
                if (player == 1)
                    return 2;
                else
                    return 1;
            }
            return player;
        }
    }

    public boolean isFirstMove(){
        return this.lastMoveIndex == -100;
    }

    public boolean isEmptyField(int field) {
        return gameBoard.isEmptyField(field);
    }

    public void printBoard() {
        gameBoard.printBoard();
    }

    public int whoWon() {
        int result = gameBoard.whoWon();
        if (result > 0) {
            return 10;
        } else if (result < 0) {
            return 20;
        } else
            return 30;
    }

    public boolean gameOver() {
        return gameBoard.checkEndGameCondition() > 0;
    }

    public int evaluate(int player) {
        int eval = gameBoard.evaluate();
        if (player == 1) {
            return eval;
        } else {
            return -eval;
        }
    }

    public List<Kalaha> getAllChildren(int player) {
        List<Kalaha> children = new ArrayList<>();
        if (player == 1) {
            for (int i = 0; i < 6; i++) {
                Kalaha child = new Kalaha(this);
                if (!isEmptyField(i + 1)) {
                    child.move(i + 1, player);
                    children.add(child);
                }
            }
        } else {
            for (int i = 7; i < 13; i++) {
                Kalaha child = new Kalaha(this);
                if (!isEmptyField(i + 1)) {
                    child.move(i + 1, player);
                    children.add(child);
                }
            }
        }

        return children;
    }

}
