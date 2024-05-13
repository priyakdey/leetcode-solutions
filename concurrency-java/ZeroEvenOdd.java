import java.util.function.IntConsumer;

public class ZeroEvenOdd {
    private final int n;
    private volatile int curr;

    private final Object mutex = new Object();
    private volatile boolean isZero = true;
    private volatile boolean isEven = false;
    private volatile boolean isOdd = false;

    public ZeroEvenOdd(int n) {
        this.n = n;
        this.curr = 1;
    }

    // printNumber.accept(x) outputs "x", where x is an integer.
    public void zero(IntConsumer printNumber) throws InterruptedException {
       synchronized (mutex) {
           for (int i = 0; i < n; i++) {
               while(!isZero) {
                   mutex.wait();
               }

               printNumber.accept(0);
               isZero = false;
               if (curr % 2 != 0) {
                   isOdd = true;
               } else {
                   isEven = true;
               }

               mutex.notifyAll();
           }
       }
    }

    public void even(IntConsumer printNumber) throws InterruptedException {
        synchronized (mutex) {
            for (int i = 2; i <= n; i = i + 2) {
                while (!isEven) {
                    mutex.wait();
                }

                printNumber.accept(curr);
                curr += 1;

                // reset the flags
                isZero = true;
                isEven = false;

                mutex.notifyAll();
            }
        }
    }

    public void odd(IntConsumer printNumber) throws InterruptedException {
        synchronized (mutex) {
            for (int i = 1; i <= n; i = i + 2) {
                while (!isOdd) {
                    mutex.wait();
                }

                printNumber.accept(curr);
                curr += 1;

                // reset the flags
                isZero = true;
                isOdd = false;

                mutex.notifyAll();
            }
        }
    }
}