package game;

class GameBoard {
    private final GameField[] board;
    private static final int N = 14;
    private static final int stonesPerField = 4;

    GameBoard() {
        board = new GameField[14];
    }

    GameBoard(GameBoard gameBoardObj) {
        board = new GameField[gameBoardObj.board.length];
        //System.arraycopy(gameBoardObj.board, 0, board, 0, gameBoardObj.board.length);
        for (int i = 0; i < N; i++) {
            if (i < N / 2) {
                if (i == (N / 2 - 1)) {
                    board[i] = new GameField(i + 1, gameBoardObj.board[i].getStonesAmount(), 1, true);
                    continue;
                }
                board[i] = new GameField(i + 1, gameBoardObj.board[i].getStonesAmount(), 1, false);
            } else {
                if (i == (N - 1)) {
                    board[i] = new GameField(i + 1, gameBoardObj.board[i].getStonesAmount(), 2, true);
                    continue;
                }
                board[i] = new GameField(i + 1, gameBoardObj.board[i].getStonesAmount(), 2, false);
            }
        }
    }

    void initBoard() {
        for (int i = 0; i < N; i++) {
            if (i < N / 2) {
                if (i == (N / 2 - 1)) {
                    board[i] = new GameField(i + 1, 0, 1, true);
                    continue;
                }
                board[i] = new GameField(i + 1, stonesPerField, 1, false);
            } else {
                if (i == (N - 1)) {
                    board[i] = new GameField(i + 1, 0, 2, true);
                    continue;
                }
                board[i] = new GameField(i + 1, stonesPerField, 2, false);
            }
        }

        /*for (int i = 0; i < N; i++) {
            if (i < N / 2) {
                if (i == (N / 2 - 1)) {
                    board[i] = new GameField(i + 1, 0, 1, true);
                    continue;
                }
                board[i] = new GameField(i + 1, 0, 1, false);
            } else {
                if (i == (N - 1)) {
                    board[i] = new GameField(i + 1, 0, 2, true);
                    continue;
                }
                board[i] = new GameField(i + 1, 0, 2, false);
            }
        }

        board[2].setStonesAmount(1);
        board[5].setStonesAmount(1);
        board[9].setStonesAmount(1);
        board[11].setStonesAmount(3);*/

        /*board[5].setStonesAmount(8);
        board[6].setStonesAmount(23);
        board[10].setStonesAmount(10);
        board[11].setStonesAmount(1);
        board[12].setStonesAmount(2);
        board[13].setStonesAmount(4);*/

    }

    GameField[] getBoard() {
        return board;
    }

    void printBoard() {
        System.out.println("Player 2");
        int index = board.length - 2;
        for (int i = 0; i < 6; i++) {
            System.out.print("\t" + board[index].getStonesAmount());
            index--;
        }
        System.out.println("\n" + board[board.length - 1].getStonesAmount() + "\t\t\t\t\t\t\t" +
                board[index].getStonesAmount());
        index = 0;

        for (int i = 0; i < 6; i++) {
            System.out.print("\t" + board[index].getStonesAmount());
            index++;
        }
        System.out.println("\n\t\t\t\t\t\tPlayer 1\n");
    }

    int moveStones(int field, int player) {
        int notUsedField, stonesToMove;

        if (field < 0 || field > 14) {
            System.out.println("No such field.");
            return -1;
        }
        if ((player == 1 && field > 6) || (player == 2 && field < 8)) {
            System.out.println("It's not your field.");
            return -2;
        }
        if (field == 7 || field == 14) {
            System.out.println("It's store.");
            return -2;
        }

        stonesToMove = board[field - 1].getStonesAmount();
        if (player == 1)
            notUsedField = 13;
        else
            notUsedField = 6;

        if (stonesToMove == 0) {
            System.out.println("You can't choose this filed, because it's have no stones on it.");
            return -3;
        }

        board[field - 1].setStonesAmount(0);
        int index = field;

        for (int i = 0; i < stonesToMove - 1; i++) {
            if (index == notUsedField)
                index = (index + 1) % board.length;
            board[index].setStonesAmount(board[index].getStonesAmount() + 1);
            index = (index + 1) % board.length;
        }

        if (index == notUsedField)
            index = (index + 1) % board.length;

        int[] copy = new int[14];
        for (int i = 0; i < board.length; i++) {
            copy[i] = board[i].getStonesAmount();
        }

        int isBeating = checkIfBeating(copy, index, player);
        if (isBeating != -1) {
            if (player == 1) {
                board[N / 2 - 1].setStonesAmount(board[N / 2 - 1].getStonesAmount() + 1 + board[isBeating].getStonesAmount());
                board[isBeating].setStonesAmount(0);
            }
            if (player == 2) {
                board[N - 1].setStonesAmount(board[N - 1].getStonesAmount() + 1 + board[isBeating].getStonesAmount());
                board[isBeating].setStonesAmount(0);
            }
            return -4;
        } else {
            board[index].setStonesAmount(board[index].getStonesAmount() + 1);
        }

        return (index);
    }

    int checkEndGameCondition() {
        boolean stop = false;
        for (int i = 0; i < N / 2 - 1; i++) {
            if (board[i].getStonesAmount() == 0)
                stop = true;
            else {
                stop = false;
                break;
            }
        }
        if (stop)
            return 1;
        for (int i = N / 2; i < N - 1; i++) {
            if (board[i].getStonesAmount() == 0)
                stop = true;
            else {
                stop = false;
                break;
            }
        }
        if (stop)
            return 2;
        return -1;
    }

    boolean checkEndGameCondition(int player) {
        boolean stop = false;
        if (player == 1) {
            for (int i = 0; i < N / 2 - 1; i++) {
                if (board[i].getStonesAmount() == 0)
                    stop = true;
                else {
                    stop = false;
                    break;
                }
            }
        }
        if (player == 2) {
            for (int i = N / 2; i < N - 1; i++) {
                if (board[i].getStonesAmount() == 0)
                    stop = true;
                else {
                    stop = false;
                    break;
                }
            }
        }
        return stop;
    }

    boolean checkIfAnotherTurn(int field, int player) {
        if (player == 1 && field == 6) {
            return true;
        }
        return player == 2 && field == 13;
    }

    int checkIfBeating(int[] stones, int field, int player) {
        if (player == 1) {
            if (field < 6) {
                if (stones[field] == 0) {
                    if (stones[stones.length - field - 2] != 0) {
                        return stones.length - field - 2;
                    }
                }
            }
        }
        if (player == 2) {
            if (field > 6 && field < 13) {
                if (stones[field] == 0) {
                    if (stones[stones.length - field - 2] != 0) {
                        return stones.length - field - 2;
                    }
                }
            }
        }
        return -1;
    }

    void getRestOfStones(int player) {
        if (player == 1) {
            for (int i = N / 2; i < N - 1; i++) {
                board[N - 1].setStonesAmount(board[N - 1].getStonesAmount() + board[i].getStonesAmount());
                board[i].setStonesAmount(0);
            }
        }
        if (player == 2) {
            for (int i = 0; i < N / 2 - 1; i++) {
                board[N / 2 - 1].setStonesAmount(board[N / 2 - 1].getStonesAmount() + board[i].getStonesAmount());
                board[i].setStonesAmount(0);
            }
        }
    }

    int whoWon() {
        return board[N / 2 - 1].getStonesAmount() - board[N - 1].getStonesAmount();
    }

    int evaluate() {
        return board[N / 2 - 1].getStonesAmount() - board[N - 1].getStonesAmount();
    }

    int evaluate(int player, String heuristic, int lastField, int moveField) {
        int eval = board[N / 2 - 1].getStonesAmount() - board[N - 1].getStonesAmount();
        int beating = 0;
        int anotherTurn = 0;
        int howFar = 0;
        switch (heuristic) {
            case "beating":
                int[] copy = new int[14];
                for (int i = 0; i < board.length; i++) {
                    copy[i] = board[i].getStonesAmount();
                }

                if (player == 1) {
                    if (checkIfBeating(copy, moveField, player) != -1) {
                        beating += 5;
                    }
                } else {
                    if (checkIfBeating(copy, moveField, player) != -1) {
                        beating -= 5;
                    }
                }

                return beating;
            case "anotherTurn":
                if (player == 1) {
                    if (checkIfAnotherTurn(lastField, player))
                        anotherTurn += 5;
                } else {
                    if (checkIfAnotherTurn(lastField, player))
                        anotherTurn -= 5;
                }

                return anotherTurn;
            case "anotherAndBeating":
                copy = new int[14];
                for (int i = 0; i < board.length; i++) {
                    copy[i] = board[i].getStonesAmount();
                }

                if (player == 1) {
                    if (checkIfBeating(copy, moveField, player) != -1)
                        beating += 5;

                    if (checkIfAnotherTurn(lastField, player))
                        anotherTurn += 5;
                } else {
                    if (checkIfBeating(copy, moveField, player) != -1)
                        beating -= 5;

                    if (checkIfAnotherTurn(lastField, player))
                        anotherTurn -= 5;
                }

                return beating + anotherTurn;
            case "howFarToWin":
                if (player == 1){
                    howFar = -(25 - board[6].getStonesAmount());
                } else {
                    howFar = 25 - board[13].getStonesAmount();
                }
                return howFar;
            case "everything":
                copy = new int[14];
                for (int i = 0; i < board.length; i++) {
                    copy[i] = board[i].getStonesAmount();
                }

                if (player == 1) {
                    howFar = -(25 - board[6].getStonesAmount());
                    if (checkIfBeating(copy, moveField, player) != -1)
                        beating += 5;

                    if (checkIfAnotherTurn(lastField, player))
                        anotherTurn += 5;
                } else {
                    eval = -eval;
                    howFar = 25 - board[13].getStonesAmount();
                    if (checkIfBeating(copy, moveField, player) != -1)
                        beating -= 5;

                    if (checkIfAnotherTurn(lastField, player))
                        anotherTurn -= 5;
                }
                eval += howFar + beating + anotherTurn;
                return eval;
            default:
                if (player == 1)
                    return eval;
                else
                    return -eval;
        }
    }

    boolean isEmptyField(int field) {
        return board[field - 1].getStonesAmount() == 0;
    }
}
