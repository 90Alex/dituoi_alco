# Αλγόριθμοι και πολυπλοκότητα



## 1. Ανάλυση αλγορίθμων


## 5. Ουρές προτεραιότητας και σωροί

* [Οπτικοποίηση](https://www.cs.usfca.edu/~galles/visualization/Heap.html) δημιουργίας σωρού ελαχίστων (MINHEAP) με διαδοχικές εισαγωγές τιμών: π.χ. χρησιμοποιήστε το πλήκτρο **Insert** για τη διαδοχική εισαγωγή των τιμών 21,5,17,12,3,9,16 σε έναν σωρό ελαχίστων
* [Οπτικοποίηση](https://www.cs.usfca.edu/~galles/visualization/Heap.html) δημιουργίας σωρού ελαχίστων (MINHEAP) με τη διαδικασία heapify: χρησιμοποιήστε το πλήκτρο **BuildHeap** για τη δημιουργία ενός σωρού ελαχίστων από έναν πίνακα 31 τιμών με τους ακέραιους από 1 μέχρι και 31
* [Οπτικοποίηση](http://btv.melezinek.cz/binary-heap.html) λειτουργιών insert, delete, heapsort, buildheap σε σωρό μεγίστων (MAXHEAP) 

**Ουρά προτεραιότητας στην Python**

[heapq](https://docs.python.org/3/library/heapq.html)

Παράδειγμα: [heapq_example.py](./heapq_example.py)

**Ουρά προτεραιότητας στην C++**

[std::priority_queue](https://en.cppreference.com/w/cpp/container/priority_queue)

Παράδειγμα: [priority_queue_example.cpp](./priority_queue_example.cpp)

**Ουρά προτεραιότητας στην Java**

[PriorityQueue\<E\>](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/PriorityQueue.html)

Παραδείγματα: [Java PriorityQueue by Programiz](https://www.programiz.com/java-programming/priorityqueue)

**Ασκήσεις**
1. Δίνεται μια ακολουθία μεγάλου μεγέθους με τυχαίες ακέραιες τιμές. Ζητείται να βρεθούν οι 10 πλέον συχνές τιμές χρησιμοποιώντας μια ουρά προτεραιότητας. Αναζητήστε την αποδοτικότερη λύση. Γράψτε πρόγραμμα που να υλοποιεί τη λύση.
<!-- * [heap_exercise1a.py](./heap_exercise1a.py)
* [heap_exercise1b.py](./heap_exercise1b.py) -->
  
1. Έστω ένας μηχανισμός παραγωγής πραγματικών τιμών. Όταν παράγεται μια νέα τιμή να υπολογίζεται και να εμφανίζεται η διάμεσος από όλες τις τιμές που έχουν παραχθεί μέχρι εκείνη τη χρονική στιγμή. Γράψτε πρόγραμμα που να υλοποιεί τη λύση.
   * Σημείωση 1: η διάμεσος μιας λίστας παρατηρήσεων είναι η τιμή της μεσαίας παρατήρησης στη διατεταγμένη σε αύξουσα σειρά λίστας παρατηρήσεων όταν το πλήθος των παρατηρήσεων είναι περιττό, και το ημιάθροισμα των δύο μεσαίων παρατηρήσεων στη διατεταγμένη σε αύξουσα σειρά λίστας παρατηρήσεων όταν όταν το πλήθος των παρατηρήσεων είναι άρτιο. 
   * Σημείωση 2: Προσομοιώστε την παραγωγή πραγματικών τιμών με μια λίστα  τυχαίων πραγματικών τιμών. Θεωρείστε ότι στη χρονική στιγμή 0 παράγεται η τιμή που βρίσκεται στη θέση 0 της λίστας, στη χρονική στιγμή 1 παράγεται η τιμή που βρίσκεται στη θέση 1 της λίστας κ.ο.κ. 

    <!-- * [heap_exercise2.py](./heap_exercise2.py) -->

## 6. Πίνακες κατακερματισμού