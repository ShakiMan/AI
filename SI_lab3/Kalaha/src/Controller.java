import game.Kalaha;
import minmax.MinMax;

import java.util.Random;
import java.util.Scanner;

public class Controller {
    Kalaha kalaha;

    public Controller() {
        kalaha = new Kalaha();
    }

    public void startGame(){
        /*Random random = new Random();
        int player = random.nextInt(2) + 1;*/
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

    public void startGameAIvsAI(){
        /*Random random = new Random();
        int player = random.nextInt(2) + 1;*/
        int player = 1;
        MinMax algorithm;
        int selectedField;
        do {
            if (kalaha.checkEndGameCondition(player)) {
                kalaha.getRestOfStones(player);
                player = kalaha.whoWon();
            } else {
                System.out.println("Current player: " + player + "\n");
                kalaha.printBoard();

                algorithm = new MinMax();
                selectedField = algorithm.findBest(kalaha, player);

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

    public void startGamePvsAI(){
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
                    algorithm = new MinMax();
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
