import java.io.FileWriter;
import java.io.IOException;

public class Main {

    public static void main(String[] args) {
        testByHeuristicAndFirstRandom("beating", false);
        testByHeuristicAndFirstRandom("beating", true);

        testByHeuristicAndFirstRandom("anotherTurn", false);
        testByHeuristicAndFirstRandom("anotherTurn", true);

        testByHeuristicAndFirstRandom("anotherAndBeating", false);
        testByHeuristicAndFirstRandom("anotherAndBeating", true);

        testByHeuristicAndFirstRandom("howFarToWin", false);
        testByHeuristicAndFirstRandom("howFarToWin", true);

        testByHeuristicAndFirstRandom("everything", false);
        testByHeuristicAndFirstRandom("everything", true);

        testByHeuristicAndFirstRandom("difference", false);
        testByHeuristicAndFirstRandom("difference", true);
    }

    public static void testByHeuristicAndFirstRandom(String heuristic, boolean isFirstRandom) {
        Test test = new Test(25, 4, true, heuristic, isFirstRandom);
        test.runTest();
        test.runTestV2();
        Test test2 = new Test(25, 4, false, heuristic, isFirstRandom);
        test2.runTest();
        test2.runTestV2();

        Test test3 = new Test(25, 7, true, heuristic, isFirstRandom);
        test3.runTest();
        test3.runTestV2();
        Test test4 = new Test(25, 7, false, heuristic, isFirstRandom);
        test4.runTest();
        test4.runTestV2();

        Test test5 = new Test(25, 10, true, heuristic, isFirstRandom);
        test5.runTest();
        test5.runTestV2();
        Test test6 = new Test(25, 10, false, heuristic, isFirstRandom);
        test6.runTest();
        test6.runTestV2();

        Test test7 = new Test(25, 13, true, heuristic, isFirstRandom);
        test7.runTest();
        test7.runTestV2();
        Test test8 = new Test(25, 13, false, heuristic, isFirstRandom);
        test8.runTest();
        test8.runTestV2();
    }
}
