import game.Kalaha;
import minmax.MinMax;

import java.util.ArrayList;
import java.util.Scanner;

public class Controller {
    Kalaha kalaha;

    public Controller() {
        kalaha = new Kalaha();
    }

    public void startGame() {
        int player = 1;

        Scanner scanner = new Scanner(System.in);
        String line;
        int selectedField;
        boolean condition = false;

        do {
            if (kalaha.checkEndGameCondition(player)) {
                kalaha.getRestOfStones(player);
                player = kalaha.whoWon();
            } else {
                System.out.println("Current player: " + player + "\n");
                kalaha.printBoard();

                do {
                    System.out.println("Enter the field number:");
                    line = scanner.nextLine();
                    selectedField = tryParseInt(line);
                    if (selectedField != Integer.MIN_VALUE)
                        condition = true;
                } while (!condition);

                System.out.println("Player " + player + " moved from field " + selectedField + "\n");
                player = kalaha.move(selectedField, player);
            }
        } while (player != 10 && player != 20 && player != 30);

        kalaha.printBoard();

        if (player == 30) {
            System.out.println("Draw");
        } else if (player == 10) {
            System.out.println("Player 1 won");
        } else {
            System.out.println("Player 2 won");
        }
    }

    public long[] startGameAIvsAI(boolean isAlphaBeta, int depth) {
        int player = 1;
        int player1Moves, player2Moves;
        long player1Times, player2Times;
        player1Moves = 0;
        player2Moves = 0;
        player1Times = 0;
        player2Times = 0;
        MinMax algorithm;
        int selectedField;
        do {
            if (kalaha.checkEndGameCondition(player)) {
                kalaha.getRestOfStones(player);
                player = kalaha.whoWon();
            } else {
                System.out.println("Current player: " + player + "\n");
                kalaha.printBoard();

                long start = System.nanoTime();
                algorithm = new MinMax(isAlphaBeta, depth);
                selectedField = algorithm.findBest(kalaha, player);
                long end = System.nanoTime();
                System.out.println("Time: " + (end - start));

                System.out.println("Player " + player + " moved from field " + selectedField + "\n");
                if (player == 1) {
                    player1Moves++;
                    player1Times += (end - start);
                } else {
                    player2Moves++;
                    player2Times += (end - start);
                }
                player = kalaha.move(selectedField, player);
            }

        } while (player != 10 && player != 20 && player != 30);

        kalaha.printBoard();

        if (player == 30) {
            System.out.println("Draw");
            return new long[]{player, player1Times, player1Moves, player2Times, player2Moves};
        } else if (player == 10) {
            System.out.println("Player 1 won");
            return new long[]{player, player1Times, player1Moves};
        } else {
            System.out.println("Player 2 won");
            return new long[]{player, player2Times, player2Moves};
        }
    }

    public ArrayList<Long> startGameAIvsAIV2(boolean isAlphaBeta, int depth) {
        ArrayList<Long> times1 = new ArrayList<>();
        ArrayList<Long> times2 = new ArrayList<>();
        int player = 1;
        int player1Moves, player2Moves;
        long player1Times, player2Times;
        player1Moves = 0;
        player2Moves = 0;
        player1Times = 0;
        player2Times = 0;
        MinMax algorithm;
        int selectedField;
        do {
            if (kalaha.checkEndGameCondition(player)) {
                kalaha.getRestOfStones(player);
                player = kalaha.whoWon();
            } else {
                System.out.println("Current player: " + player + "\n");
                kalaha.printBoard();

                long start = System.nanoTime();
                algorithm = new MinMax(isAlphaBeta, depth);
                selectedField = algorithm.findBest(kalaha, player);
                long end = System.nanoTime();
                System.out.println("Time: " + (end - start));

                System.out.println("Player " + player + " moved from field " + selectedField + "\n");
                if (player == 1) {
                    player1Moves++;
                    times1.add(end - start);
                } else {
                    player2Moves++;
                    times2.add(end - start);
                }
                player = kalaha.move(selectedField, player);
            }

        } while (player != 10 && player != 20 && player != 30);

        kalaha.printBoard();

        if (player == 30) {
            System.out.println("Draw");
            times1.add((long) player1Moves);
            return times1;
        } else if (player == 10) {
            System.out.println("Player 1 won");
            times1.add((long) player1Moves);
            return times1;
        } else {
            System.out.println("Player 2 won");
            times2.add((long) player2Moves);
            return times2;
        }
    }

    public void startGamePvsAI() {
        int player = 1;

        Scanner scanner = new Scanner(System.in);
        String line;
        int selectedField;
        boolean condition = false;
        MinMax algorithm;

        do {
            if (kalaha.checkEndGameCondition(player)) {
                kalaha.getRestOfStones(player);
                player = kalaha.whoWon();
            } else {
                System.out.println("Current player: " + player + "\n");
                kalaha.printBoard();

                if (player == 1) {
                    do {
                        System.out.println("Enter the field number:");
                        line = scanner.nextLine();
                        selectedField = tryParseInt(line);
                        if (selectedField != Integer.MIN_VALUE)
                            condition = true;
                    } while (!condition);
                } else {
                    algorithm = new MinMax(true, 12);
                    selectedField = algorithm.findBest(kalaha, player);
                }

                System.out.println("Player " + player + " moved from field " + selectedField + "\n");
                player = kalaha.move(selectedField, player);
            }


        } while (player != 10 && player != 20 && player != 30);

        kalaha.printBoard();

        if (player == 30) {
            System.out.println("Draw");
        } else if (player == 10) {
            System.out.println("Player 1 won");
        } else {
            System.out.println("Player 2 won");
        }
    }

    private int tryParseInt(String value) {
        try {
            return Integer.parseInt(value);
        } catch (NumberFormatException e) {
            System.out.println("Incorrect value!");
            return Integer.MIN_VALUE;
        }
    }
}
