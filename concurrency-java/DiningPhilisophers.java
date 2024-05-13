import java.util.Arrays;
import java.util.concurrent.locks.ReentrantLock;

/**
 * 1226. The Dining Philosophers:
 * <p>
 * Five silent philosophers sit at a round table with bowls of spaghetti.
 * Forks are placed between each pair of adjacent philosophers.
 * Each philosopher must alternately think and eat. However, a philosopher
 * can only eat spaghetti when they have both left and right forks.
 * Each fork can be held by only one philosopher and so a philosopher
 * can use the fork only if it is not being used by another philosopher.
 * After an individual philosopher finishes eating, they need to put down
 * both forks so that the forks become available to others. A philosopher
 * can take the fork on their right or the one on their left as they become
 * available, but cannot start eating before getting both forks.
 * <p>
 * <p>
 * Eating is not limited by the remaining amounts of spaghetti or
 * stomach space; an infinite supply and an infinite demand are assumed.
 * <p>
 * <p>
 * Design a discipline of behaviour (a concurrent algorithm) such that no
 * philosopher will starve; i.e., each can forever continue to alternate
 * between eating and thinking, assuming that no philosopher can know
 * when others may want to eat or think.
 * <p>
 * <p>
 * The philosophers' ids are numbered from 0 to 4 in a clockwise order.
 * Implement the function void wantsToEat(philosopher, pickLeftFork, pickRightFork,
 * eat, putLeftFork, putRightFork) where:
 * <ul>
 *  <li>philosopher is the id of the philosopher who wants to eat.</li>
 *  <li>pickLeftFork and pickRightFork are functions you can call to pick the corresponding forks of that philosopher.</li>
 *  <li>eat is a function you can call to let the philosopher eat once he has picked both forks.</li>
 *  <li>putLeftFork and putRightFork are functions you can call to put down the corresponding forks of that philosopher.</li>
 *  <li>The philosophers are assumed to be thinking as long as they are not asking to eat (the function is not being called with their number).</li>
 * </ul>
 * <p>
 * <p>
 * Five threads, each representing a philosopher, will simultaneously use one object of your class to simulate the process.
 * The function may be called for the same philosopher more than once, even before the last call ends.
 *
 * @author Priyak Dey
 */
public class DiningPhilosophers {

    private final ReentrantLock[] forks;

    public DiningPhilosophers() {
        this.forks = new ReentrantLock[5];
        Arrays.fill(forks, new ReentrantLock(false));
    }

    // call the run() method of any runnable to execute its code
    public void wantsToEat(int philosopher,
                           Runnable pickLeftFork,
                           Runnable pickRightFork,
                           Runnable eat,
                           Runnable putLeftFork,
                           Runnable putRightFork) throws InterruptedException {

        // for even philosopher get the same id fork first and then the other one
        // for odd philosopher get the id + 1 fork first and then the other one

        ReentrantLock fork1 = forks[(philosopher + (philosopher % 2)) % 5];
        ReentrantLock fork2 = forks[(philosopher + ((philosopher + 1) % 2)) % 5];

        fork1.lock();
        fork2.lock();
        try {
            pickLeftFork.run();
            pickRightFork.run();
            eat.run();
            putLeftFork.run();
            putRightFork.run();
        } finally {
            fork1.unlock();
            fork2.unlock();
        }


    }
}