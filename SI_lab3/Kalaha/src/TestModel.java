public class TestModel {
    private final long player, averageTime, moves;

    public TestModel(long player, long averageTime, long moves) {
        this.player = player;
        this.averageTime = averageTime;
        this.moves = moves;
    }

    @Override
    public String toString() {
        return "TestModel{ " +
                "player= " + player +
                ", averageTime= " + averageTime +
                ", moves= " + moves +
                " }";
    }

    public long getMoves() {
        return moves;
    }
}
