package game;

public class GameField {
    private int number, stonesAmount, player;
    private boolean store;

    public GameField(int number, int stonesAmount, int player, boolean isStore) {
        this.number = number;
        this.stonesAmount = stonesAmount;
        this.player = player;
        this.store = isStore;
    }

    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }

    public int getStonesAmount() {
        return stonesAmount;
    }

    public void setStonesAmount(int stonesAmount) {
        this.stonesAmount = stonesAmount;
    }

    public int getPlayer() {
        return player;
    }

    public void setPlayer(int player) {
        this.player = player;
    }

    public boolean isStore() {
        return store;
    }

    public void setStore(boolean store) {
        this.store = store;
    }
}
