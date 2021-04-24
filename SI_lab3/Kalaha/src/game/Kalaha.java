package game;

public class Kalaha {
    private GameBoard gameBoard;

    public Kalaha() {
        gameBoard = new GameBoard();
        gameBoard.initBoard();
    }

    public Kalaha(Kalaha kalaha) {
        this.gameBoard = new GameBoard(kalaha.gameBoard);
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
        int lastField = gameBoard.moveStones(field, player);
        int end = gameBoard.checkEndGameCondition();

        if (end != -1){
            gameBoard.getRestOfStones(end);
            return whoWon();
        }

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
    }

    public void printBoard() {
        gameBoard.printBoard();
    }

    public int whoWon(){
        int result = gameBoard.whoWon();
        if (result > 0) {
            return 10;
        } else if (result < 0){
            return 20;
        } else
            return 30;
    }
}
