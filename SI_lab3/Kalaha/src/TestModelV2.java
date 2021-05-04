public class TestModelV2 {
    private final int id;
    private long time;
    private int counter;

    public TestModelV2(int id, long time, int counter) {
        this.time = time;
        this.counter = counter;
        this.id = id;
    }

    public long getTime() {
        return time;
    }

    public void setTime(long time) {
        this.time = time;
    }

    public int getCounter() {
        return counter;
    }

    public void setCounter(int counter) {
        this.counter = counter;
    }

    @Override
    public String toString() {
        return "TestModelV2{ " +
                "id= " + id +
                ", time= " + time +
                ", counter= " + counter +
                " }";
    }
}
