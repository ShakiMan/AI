import game.Kalaha;

import java.util.Random;
import java.util.Scanner;

public class Controller {
    Kalaha kalaha;

    public Controller() {
        kalaha = new Kalaha();
    }

    public void startGame(){
        Random random = new Random();
        int player = random.nextInt(2) + 1;

        Scanner scanner = new Scanner(System.in);
        String line;
        int selectedField;
        boolean condition = false;

        do {
            System.out.println("Current player: " + player + "\n");
            kalaha.printBoard();
            do {
                System.out.println("Enter the field number:");
                line = scanner.nextLine();
                selectedField = tryParseInt(line);
                if (selectedField != Integer.MIN_VALUE)
                    condition = true;
            } while (!condition);

            player = kalaha.move(selectedField, player);
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