// https://leetcode.com/problems/print-in-order

#include <semaphore.h>

class Foo {
public:
    Foo() {
        sem_init(&m_sec_sem, 0, 0);
        sem_init(&m_third_sem, 0, 0);
    }

    void first(function<void()> printFirst) {
        
        // printFirst() outputs "first". Do not change or remove this line.
        printFirst();
        sem_post(&m_sec_sem);
    }

    void second(function<void()> printSecond) {
        
        // printSecond() outputs "second". Do not change or remove this line.
        sem_wait(&m_sec_sem);
        printSecond();
        sem_post(&m_third_sem);

    }

    void third(function<void()> printThird) {
        sem_wait(&m_third_sem);
        // printThird() outputs "third". Do not change or remove this line.
        printThird();
    }
private:
    sem_t m_sec_sem;
    sem_t m_third_sem;
};