class Lasagna
{
    public int ExpectedMinutesInOven() {
        return 40;
    }

    public int RemainingMinutesInOven(int timeElapsed) {
        return ExpectedMinutesInOven() - timeElapsed;
    }

    public int PreparationTimeInMinutes(int numLayers) {
        return 2 * numLayers;
    }

    public int ElapsedTimeInMinutes(int numLayers, int timeElapsed) {
        return PreparationTimeInMinutes(numLayers) + timeElapsed;
    }
}
