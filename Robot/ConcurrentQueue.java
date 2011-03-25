import java.util.Queue;
import java.util.EmptyQueueException;

/**
 * Extends the Queue class to provide a sort-of concurrent
 * safe queue, since lejos doesnt have java.util.concurrent =[ */
public class ConcurrentQueue<E> extends Queue {

  public ConcurrentQueue() {
    super();
  }

  public synchronized boolean isEmpty() {
    return super.isEmpty();
  }

  public synchronized Object push(Object obj) {
    return super.push(obj);
  }

  public synchronized void insertElementAt(Object aObj, int aIndex) {
    super.insertElementAt(aObj, aIndex);
  }

  public synchronized Object pop() throws EmptyQueueException {
    return super.pop();
  }

}
