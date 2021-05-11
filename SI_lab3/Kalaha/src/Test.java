import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class Test {
    Controller controller;
    private final int loops, depth;
    boolean isAlphaBeta;
    private final List<TestModel> results;
    private final List<TestModelV2> results2;
    private final String heuristic;
    private final boolean isFirstRandom;

    public Test(int loops, int depth, boolean isAlphaBeta, String heuristic, boolean isFirstRandom) {
        this.loops = loops;
        this.depth = depth;
        this.isAlphaBeta = isAlphaBeta;
        results = new ArrayList<>();
        results2 = new ArrayList<>();
        this.heuristic = heuristic;
        this.isFirstRandom = isFirstRandom;

    }

    public void runTest() {
        for (int i = 0; i < loops; i++) {
            controller = new Controller();
            long[] gameResult = controller.startGameAIvsAI(isAlphaBeta, depth, heuristic, isFirstRandom);
            results.add(new TestModel(gameResult[0] / 10, gameResult[1] / gameResult[2], gameResult[2]));
        }

        double avg = 0;

//        System.out.println("Test\n");
        try {
            FileWriter fileWriter = new FileWriter("results.txt", true);
            fileWriter.append("Test v1\n" );
            fileWriter.append("loops: ").append(String.valueOf(loops)).append(" depth: ")
                    .append(String.valueOf(depth)).append(" isAlphaBeta: ").append(String.valueOf(isAlphaBeta))
                    .append(" heuristic: ").append(heuristic).append(" isFirstRandom: ")
                    .append(String.valueOf(isFirstRandom)).append("\n\n");

            for (TestModel m : results) {
//                System.out.println(m);
                fileWriter.append(m.toString()).append("\n");
                avg += m.getMoves();
            }
            avg /= results.size();

//            System.out.println("Average amount of moves = " + avg);
            fileWriter.append("Average amount of moves = ").append(String.valueOf(avg));
            fileWriter.append("\n\n\n\n\n\n");
            fileWriter.close();
        } catch (IOException e) {
            e.printStackTrace();
        }

    }

    public void runTestV2() {
        double moves = 0;
        for (int i = 0; i < loops; i++) {
            controller = new Controller();
            ArrayList<Long> gameResult = controller.startGameAIvsAIV2(isAlphaBeta, depth, heuristic, isFirstRandom);
            for (int j = 0; j < gameResult.size() - 1; j++) {
                if (j < results2.size()) {
                    results2.get(j).setTime(results2.get(j).getTime() + gameResult.get(j));
                    results2.get(j).setCounter(results2.get(j).getCounter() + 1);
                } else {
                    results2.add(new TestModelV2(j + 1, gameResult.get(j), 1));
                }
            }
            moves += gameResult.get(gameResult.size() - 1);
        }

        double avg = 0;
        avg = moves / loops;
//        System.out.println("Average amount of moves = " + avg);

//        System.out.println("Test\n");

        try {
            FileWriter fileWriter = new FileWriter("results.txt", true);
            fileWriter.append("Test v2\n");
            fileWriter.append("loops: ").append(String.valueOf(loops)).append(" depth: ")
                    .append(String.valueOf(depth)).append(" isAlphaBeta: ").append(String.valueOf(isAlphaBeta))
                    .append(" heuristic: ").append(heuristic).append(" isFirstRandom: ")
                    .append(String.valueOf(isFirstRandom)).append("\n\n");

            fileWriter.append("Average amount of moves = ").append(String.valueOf(avg));

            for (TestModelV2 m : results2) {
                m.setTime(m.getTime() / m.getCounter());
//            System.out.println(m);
                fileWriter.append(m.toString()).append("\n");
            }
            fileWriter.append("\n\n\n\n\n\n");
            fileWriter.close();

        } catch (IOException e) {
            e.printStackTrace();
        }


    }
}
