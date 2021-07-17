Topics: 
1. Array/list basic - defining, append & pop function
2. Complexity - Time & space complexity
3. Array example problem - observe complexity
4. Reverse the array problem & reduce the space complexity

# Array/list basic
**Define Array**

1. `arr = []`
2. `arr = [1,2,3,4,5,6,7,8,9]`

**Append**
Insert value in an array:
`arr.append(100)`

**Pop**
Delete/Pop value from an array:
`arr.pop()`

# Complexity - Time & space complexity
*In Short Actually*
It is a constant value. 
It represents the max() value.

Some common scenarios are:
```
    O(n)
    O(nlogn)
    O(n²)
``` 
I have decent idea about time complexity. 
But today I have learned about memory/space complexity. 
I got some shock surprise when I was said to reduce memory from O(n) to O(1).

Today I have learned that, (and the summary), If the programm doesn't take extra memory over per command, there is nothing to be concerned of. For example, 

```python=
    a = [1,2,3,4,5,6,7,8,9]

    s = 0
    e = len(a) - 1

    while s < e:
        temp = a[s]
        a[s] = a[e]
        a[e] = temp

        s+=1
        e-=1

    print(a)
```
in every single line there is one block of memory consumption. It takes a memory, do operaion and release it, then it goes for the next line. there is no momory consumption holding. In short there is no memory stack using.

But if we look down the next example, 
```python=
    a = [1,2,3,4,5,6,7,8,9]
    res = []

    n = len(a)

    for i in range(n , 0, -1):
        res.append(i)

    print(res)
```
No need to focus on the second line of code. 
inside the for loop, there is an append function adding value to an array and there is no instruction to release it. 
That is why the first block of code has memory complexity of 1, O(1) and the second block has memory complexity of N, O(N).

Here is another point I would like to add that, 

---
 Memory complexity is the size of work memory used by an algorithm. In the relevant Turing machine model, there is an read-only input tape, a write-only output tape, and a read-write work tape; you're interested only in the work tape. This makes sense since work memory is the additional memory that the specific algorithm uses. For example, if it is called recursively, then it is only this additional memory that is added per each recursive call.

Under this definition, the first code snippet that you provided uses O(1)

memory (when memory is measured in machine words rather than bits). Perhaps the algorithm enclosing it allocates the array d, and in that case the memory taken by the array is considered work memory; but if the array is given as an input, then it isn't considered work memory.

The second algorithm constructs a list of size N
(where N is the length of the input), and so uses Θ(N) work memory. The third algorithm uses two local variables, and so uses Θ(1) work memory.
---
Those are the example algorithoms:
```
for i = 1 to n-1
     if d[i] == d[i + 1]
           d[i] = (d[i] + 5) mod 13
```
```
reverse_list(n)

    Stack res
    while (n != NULL)
         res push n
         n = n->next
    while (res != null) 
         a = pop res
         print a
```
```
reverse_list(head)
    last = NULL;
    while(last != head)
        current = head
        while(current->next != last)
            current = current->next
        print current
        last = current
```

[Shafaet's planets BLOG](http://www.shafaetsplanet.com/?p=1313)