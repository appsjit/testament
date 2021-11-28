/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package LeetCodeJava.fromViraj;


/**
 List                 | Add  | Remove | Get  | Contains | Next | Size |  Data Structure
 ---------------------|------|--------|------|----------|------|------|-----------------------
 ArrayList            | O(1) |  O(n)  | O(1) |   O(n)   | O(1) | O(1) | Array
 LinkedList           | O(1) |  O(1)  | O(n) |   O(n)   | O(1) | O(1) | Linked List
 Set                   |    Add   |  Remove  | Contains |   Next   | Size | Data Structure
 ----------------------|----------|----------|----------|----------|------|-------------------------
 HashSet               | O(1)     | O(1)     | O(1)     | O(h/n)   | O(1) | Hash Table
 LinkedHashSet         | O(1)     | O(1)     | O(1)     | O(1)     | O(1) | Hash Table + Linked List
 EnumSet               | O(1)     | O(1)     | O(1)     | O(1)     | O(1) | Bit Vector
 TreeSet               | O(log n) | O(log n) | O(log n) | O(log n) | O(1) | Red-black tree
 Map                   |   Get    | ContainsKey |   Next   | Data Structure
 ----------------------|----------|-------------|----------|-------------------------
 HashMap               | O(1)     |   O(1)      | O(h / n) | Hash Table
 LinkedHashMap         | O(1)     |   O(1)      | O(1)     | Hash Table + Linked List
 EnumMap               | O(1)     |   O(1)      | O(1)     | Array
 TreeMap               | O(log n) |   O(log n)  | O(log n) | Red-black tree
 * Stack is a class
 *  st.empty(); => boolean st.empty();
 *  st.push(); => E st.push(E);
 *  st.peek(); => E st.peek(); EmptyStackException Runtime
 *  st.pop(); => E st.pop(); EmptyStackException Runtime
 Queue                   |  Offer   | Peak |   Poll   | Remove | Size | Data Structure
 ------------------------|----------|------|----------|--------|------|---------------
 PriorityQueue           | O(log n) | O(1) | O(log n) |  O(n)  | O(1) | Priority Heap
 LinkedList              | O(1)     | O(1) | O(1)     |  O(1)  | O(1) | Array
 ArrayDequeue            | O(1)     | O(1) | O(1)     |  O(n)  | O(1) | Linked List
 ConcurrentLinkedQueue   | O(1)     | O(1) | O(1)     |  O(n)  | O(n) | Linked List
 ArrayBlockingQueue      | O(1)     | O(1) | O(1)     |  O(n)  | O(1) | Array
 PriorirityBlockingQueue | O(log n) | O(1) | O(log n) |  O(n)  | O(1) | Priority Heap
 SynchronousQueue        | O(1)     | O(1) | O(1)     |  O(n)  | O(1) | None!
 DelayQueue              | O(log n) | O(1) | O(log n) |  O(n)  | O(1) | Priority Heap
 LinkedBlockingQueue     | O(1)     | O(1) | O(1)     |  O(n)  | O(1) | Linked List
 * Queue is an interface.
 * 			Throws exception	Returns special value
 * Insert	add(e)				offer(e)
 * Remove	remove()			poll()
 * Examine	element()			peek()
 PriorityQueue keeps elements Sorted by default.
 * O(log(n)) time for the enqueing and dequeing methods (offer, poll, remove() and  add);
 * linear time for the remove(Object) and contains(Object) methods; and
 * constant time for the retrieval methods (peek,  element, and size).
 Combinations - Use start in backtrack, When t size == k save t to r. Next start is i+1
 Subsets - Use start in backtrack. Always save t to r.  Next start is i+1
 Subsets ii Unique - Use start in backtrack. Always save t to r.  Next start is i+1. If ((i>start) && (n[i] == n[i-1])) continue
 Permutations - No start in backtrack. When t szie == n.length save t to r.
 Permutations ii Unique - No start in backtrack. When t szie == n.length save t to r. Use boolean[] used to continue. If used[i] or((i>0) && (n[i] == n[i-1]) && (!used[i-1])) continue
 Combination Sum - Use start in backtrack, When remain == 0 save t to r. Next start is i
 Combination Sum ii - Use start in backtrack, When remain == 0 save t to r. Next start is i +1. If ((i>start) && (n[i] == n[i-1])) continue
 */
public class App 
{
    public static void main( String[] args )
    {
        System.out.println( "Hello World!" );
    }
}
