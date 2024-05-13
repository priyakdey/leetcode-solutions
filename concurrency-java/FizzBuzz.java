import java.util.function.IntConsumer;

/**
 * 1195. Fizz Buzz Multithreaded
 * <p>
 * You have the four functions:
 * <ul>
 * <li>printFizz that prints the word "fizz" to the console,</li>
 * <li>printBuzz that prints the word "buzz" to the console,</li>
 * <li>printFizzBuzz that prints the word "fizzbuzz" to the console, and</li>
 * <li>printNumber that prints a given integer to the console.</li>
 * </ul>
 * <p>
 * You are given an instance of the class FizzBuzz that has four functions: fizz, buzz, fizzbuzz and number.
 * The same instance of FizzBuzz will be passed to four different threads:
 * <ul>
 * <li>Thread A: calls fizz() that should output the word "fizz".</li>
 * <li>Thread B: calls buzz() that should output the word "buzz".</li>
 * <li>Thread C: calls fizzbuzz() that should output the word "fizzbuzz".</li>
 * <li>Thread D: calls number() that should only output the integers.</li>
 * </ul>
 * <p>
 * Modify the given class to output the series [1, 2, "fizz", 4, "buzz", ...] where the ith token (1-indexed) of the series is:
 * <p>
 *     <ul>
 * <li>"fizzbuzz" if i is divisible by 3 and 5,</li>
 * <li>"fizz" if i is divisible by 3 and not 5,</li>
 * <li>"buzz" if i is divisible by 5 and not 3, or</li>
 * <li>i if i is not divisible by 3 or 5.</li>
 * </ul>
 * <p>
 * Implement the FizzBuzz class:
 * <p>
 *     <ul>
 * <li>FizzBuzz(int n) Initializes the object with the number n that represents the length of the sequence that should be printed.</li>
 * <li>void fizz(printFizz) Calls printFizz to output "fizz".</li>
 * <li>void buzz(printBuzz) Calls printBuzz to output "buzz".</li>
 * <li>void fizzbuzz(printFizzBuzz) Calls printFizzBuzz to output "fizzbuzz".</li>
 * <li>void number(printNumber) Calls printnumber to output the numbers.</li>
 * </ul>
 *
 * @author Priyak Dey
 */
 public class FizzBuzz {

    private final int n;

    private volatile int curr;

    private final Object mutex = new Object();
    private volatile boolean canPrintFizz = false;
    private volatile boolean canPrintBuzz = false;
    private volatile boolean canPrintFizzBuzz = false;
    private volatile boolean canPrintNumber = true;

    public FizzBuzz(int n) {
        this.n = n;
        this.curr = 1;
        setFlags();
    }

    // printFizz.run() outputs "fizz".
    public void fizz(Runnable printFizz) throws InterruptedException {
        while (curr <= n) {
            synchronized (mutex) {
                if (curr > n) {
                    canPrintFizz = true;
                    canPrintBuzz = true;
                    canPrintFizzBuzz = true;
                    canPrintNumber = true;
                    mutex.notifyAll();
                    return;
                }

                while (!canPrintFizz) {
                    mutex.wait();
                }

                if (curr > n) {
                    canPrintFizz = true;
                    canPrintBuzz = true;
                    canPrintFizzBuzz = true;
                    canPrintNumber = true;
                    mutex.notifyAll();
                    return;
                }

                printFizz.run();
                curr += 1;
                setFlags();
                mutex.notifyAll();
            }

        }
    }

    // printBuzz.run() outputs "buzz".
    public void buzz(Runnable printBuzz) throws InterruptedException {
        while (curr <= n) {
            synchronized (mutex) {
                if (curr > n) {
                    canPrintFizz = true;
                    canPrintBuzz = true;
                    canPrintFizzBuzz = true;
                    canPrintNumber = true;
                    mutex.notifyAll();
                    return;
                }

                while (!canPrintBuzz) {
                    mutex.wait();
                }

                if (curr > n) {
                    canPrintFizz = true;
                    canPrintBuzz = true;
                    canPrintFizzBuzz = true;
                    canPrintNumber = true;
                    mutex.notifyAll();
                    return;
                }

                printBuzz.run();
                curr += 1;
                setFlags();
                mutex.notifyAll();
            }

        }
    }

    // printFizzBuzz.run() outputs "fizzbuzz".
    public void fizzbuzz(Runnable printFizzBuzz) throws InterruptedException {
        while (curr <= n) {
            synchronized (mutex) {
                if (curr > n) {
                    canPrintFizz = true;
                    canPrintBuzz = true;
                    canPrintFizzBuzz = true;
                    canPrintNumber = true;
                    mutex.notifyAll();
                    return;
                }

                while (!canPrintFizzBuzz) {
                    mutex.wait();
                }

                if (curr > n) {
                    canPrintFizz = true;
                    canPrintBuzz = true;
                    canPrintFizzBuzz = true;
                    canPrintNumber = true;
                    mutex.notifyAll();
                    return;
                }

                printFizzBuzz.run();
                curr += 1;
                setFlags();
                mutex.notifyAll();
            }

        }
    }

    // printNumber.accept(x) outputs "x", where x is an integer.
    public void number(IntConsumer printNumber) throws InterruptedException {
        while (curr <= n) {
            synchronized (mutex) {
                if (curr > n) {
                    canPrintFizz = true;
                    canPrintBuzz = true;
                    canPrintFizzBuzz = true;
                    canPrintNumber = true;
                    mutex.notifyAll();
                    return;
                }

                while (!canPrintNumber) {
                    mutex.wait();
                }

                if (curr > n) {
                    canPrintFizz = true;
                    canPrintBuzz = true;
                    canPrintFizzBuzz = true;
                    canPrintNumber = true;
                    mutex.notifyAll();
                    return;
                }

                printNumber.accept(curr);
                curr += 1;
                setFlags();
                mutex.notifyAll();
            }

        }
    }

    public void setFlags() {
        if (curr > n) {
            canPrintFizz = true;
            canPrintBuzz = true;
            canPrintFizzBuzz = true;
            canPrintNumber = true;
        } else if (curr % 3 == 0 && curr % 5 == 0) {
            canPrintFizz = false;
            canPrintBuzz = false;
            canPrintFizzBuzz = true;
            canPrintNumber = false;
        } else if (curr % 3 == 0) {
            canPrintFizz = true;
            canPrintBuzz = false;
            canPrintFizzBuzz = false;
            canPrintNumber = false;
        } else if (curr % 5 == 0) {
            canPrintFizz = false;
            canPrintBuzz = true;
            canPrintFizzBuzz = false;
            canPrintNumber = false;
        } else {
            canPrintFizz = false;
            canPrintBuzz = false;
            canPrintFizzBuzz = false;
            canPrintNumber = true;
        }
    }


    public static void main(String[] args) throws InterruptedException {
        Runnable printFizz = () -> System.out.println("FIZZ");
        Runnable printBuzz = () -> System.out.println("BUZZ");
        Runnable printFizzBuzz = () -> System.out.println("FIZZBUZZ");
        IntConsumer printNumber = System.out::println;

        FizzBuzz fizzBuzz = new FizzBuzz(1);

        Thread t1 = new Thread(() -> {
            try {
                fizzBuzz.fizz(printFizz);
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            }
        });

        Thread t2 = new Thread(() -> {
            try {
                fizzBuzz.buzz(printBuzz);
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            }
        });

        Thread t3 = new Thread(() -> {
            try {
                fizzBuzz.fizzbuzz(printFizzBuzz);
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            }
        });

        Thread t4 = new Thread(() -> {
            try {
                fizzBuzz.number(printNumber);
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            }
        });

        t1.start();
        t2.start();
        t3.start();
        t4.start();

        t1.join();
        t2.join();
        t3.join();
        t4.join();

    }

}
