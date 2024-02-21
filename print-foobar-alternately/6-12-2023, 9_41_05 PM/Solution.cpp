// https://leetcode.com/problems/print-foobar-alternately

#include <semaphore.h>

class FooBar {
private:
    int n;

public:
    FooBar(int n) {
        this->n = n;
        sem_init(&m_fooDone, 0, 0);
        sem_init(&m_barDone, 0, 1);
    }

    void foo(function<void()> printFoo) {
        
        for (int i = 0; i < n; i++) {
            sem_wait(&m_barDone);
        	// printFoo() outputs "foo". Do not change or remove this line.
        	printFoo();
            sem_post(&m_fooDone);
        }
    }

    void bar(function<void()> printBar) {
        
        for (int i = 0; i < n; i++) {
        	// printBar() outputs "bar". Do not change or remove this line.
            sem_wait(&m_fooDone);
        	printBar();
            sem_post(&m_barDone);
        }
    }
private:
    sem_t m_fooDone;
    sem_t m_barDone;
};