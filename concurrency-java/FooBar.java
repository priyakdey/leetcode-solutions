public interface FooBar {

    void foo(Runnable printFoo) throws InterruptedException;

    void bar(Runnable printBar) throws InterruptedException;
}

class FooBarWithCondition implements FooBar {

    private int n;

    private final ReentrantLock lock = new ReentrantLock(false);
    private final Condition shouldFooWaitCondition = lock.newCondition();
    private final Condition shouldBarWaitCondition = lock.newCondition();

    private volatile boolean shouldFooWait = false;
    private volatile boolean shouldBarWait = false;

    public FooBarWithCondition(int n) {
        this.n = n;
    }

    @Override
    public void foo(Runnable printFoo) throws InterruptedException {
        for (int i = 0; i < n; i++) {
            try {
                lock.lock();

                while (shouldFooWait) {
                    shouldFooWaitCondition.await();
                }

                printFoo.run();

                // reset the flags
                shouldFooWait = true;
                shouldBarWait = false;
                shouldBarWaitCondition.signalAll();
            } finally {
                lock.unlock();
            }
        }
    }

    @Override
    public void bar(Runnable printBar) throws InterruptedException {
        for (int i = 0; i < n; i++) {
            try {
                lock.lock();
                while (shouldBarWait) {
                    shouldBarWaitCondition.await();
                }

                printBar.run();

                // reset the flags
                shouldBarWait = true;
                shouldFooWait = false;

                shouldFooWaitCondition.signalAll();
            } finally {
                lock.unlock();
            }
        }
    }
}


class FooBarWithSemaphore implements FooBar {

    private int n;

    // initialize this with 1, since we want to start the sequence with foo
    private final Semaphore fooSemaphore = new Semaphore(1);

    // initialize this with 0, since we want to start the sequence with foo
    private final Semaphore barSemaphore = new Semaphore(0);

    public FooBarWithSemaphore(int n) {
        this.n = n;
    }

    public void foo(Runnable printFoo) throws InterruptedException {
        for (int i = 0; i < n; i++) {
            fooSemaphore.acquire();
            // printFoo.run() outputs "foo". Do not change or remove this line.
            printFoo.run();
            barSemaphore.release();
        }
    }

    public void bar(Runnable printBar) throws InterruptedException {

        for (int i = 0; i < n; i++) {
            barSemaphore.acquire();
            // printBar.run() outputs "bar". Do not change or remove this line.
            printBar.run();
            fooSemaphore.release();
        }
    }

}


class FooBarWithWaitNotify implements FooBar {

    private int n;

    private final Object mutex = new Object();

    // init value is false, since we want to print FO) first
    private volatile boolean shouldFooWait = false;
    private volatile boolean shouldBarWait = true;

    public FooBarWithWaitNotify(int n) {
        this.n = n;
    }

    public void foo(Runnable printFoo) throws InterruptedException {
        for (int i = 0; i < n; i++) {
            synchronized (mutex) {
                // wait till the flag is set to true
                while (shouldFooWait) {
                    // wait this flag is set to true.
                    mutex.wait();
                }

                // printFoo.run() outputs "foo". Do not change or remove this line.
                printFoo.run();

                // reset the flags
                shouldFooWait = true;
                shouldBarWait = false;

                // once done, notify all waiting threads to go ahead
                mutex.notifyAll();
            }
        }
    }

    public void bar(Runnable printBar) throws InterruptedException {

        for (int i = 0; i < n; i++) {
            synchronized (mutex) {
                while (shouldBarWait) {
                    mutex.wait();
                }

                // printBar.run() outputs "bar". Do not change or remove this line.
                printBar.run();

                // reset the flags
                shouldFooWait = false;
                shouldBarWait = true;

                mutex.notifyAll();
            }
        }
    }

}
