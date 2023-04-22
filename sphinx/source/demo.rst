.. code::

    -<< -< -<- <-- <--- <<- <- -> ->> --> ---> ->- >- >>- <-> <--> <---> <----> <!--
    =<< =< =<= <== <=== <<= <= => =>> ==> ===> =>= >= >>= <=> <==> <===> <====> <!---
    <------ ------> <=====> <~~ <~ ~> ~~> :: ::: \/ /\ == != /= ~= <> === !== =/= =!=
    := :- :+ <* <*> *> <| <|> |> <. <.> .> +: -: =: <******> (* comm *) ++ +++ |- -|

.. code-block:: c
    :caption: C

    #include <stdlib.h>  /* qsort() */
    #include <stdio.h>   /* printf() */

    int intcmp(const void *aa, const void *bb)
    {
        const int *a = aa, *b = bb;
        return (*a < *b) ? -1 : (*a > *b);
    }

    int main() // C sorting
    {
        int nums[5] = {2,4,3,1,2};
        qsort(nums, 5, sizeof(int), intcmp);
        printf("result: %d %d %d %d %d\n",
          nums[0], nums[1], nums[2], nums[3], nums[4]);
        return 0;
    }

.. code-block:: java
    :linenos:
    :caption: Java

    import java.util.Arrays; // Java sorting
    import java.util.Collections;
    import java.util.List;

    public class example {
        public static void main(String[] args)
        {
            List<Integer> nums = Arrays.asList(2,4,3,1,2);
            Collections.sort(nums);
        }
    }

.. code-block:: rust
    :caption: Rust

    fn main() { // Rust sorting
        let mut a = vec!(9, 8, 7, 6, 5, 4, 3, 2, 1, 0);

        a.sort();
        println!("{:?}", a);
    }

.. code-block:: js
    :caption: JavaScript

    function int_arr(a, b) { // Javascript sorting
      return a - b;
    }
    var numbers = [20, 7, 65, 10, 3, 0, 8, -60];
    numbers.sort(int_arr);
    document.write(numbers);

.. code-block:: cpp
    :caption: C++

    #include <algorithm>

    int main() // C++ sorting
    {
        int nums[] = {2,4,3,1,2};
        std::sort(nums, nums+sizeof(nums)/sizeof(int));
        return 0;
    }

.. code-block:: go
    :caption: Go

    package main // Go sorting
    import "fmt"
    import "sort"

    func main() {
      nums := []int {2, 4, 3, 1, 2}
      sort.Ints(nums)
      fmt.Println(nums)
    }

.. code-block:: hs
    :caption: Haskell

    nums = [2,4,3,1,2] :: [Int] -- Haskell sorting
    sorted = List.sort nums

.. code-block:: py
    :caption: Python
    
    nums = [2,4,3,1,2] # Python sorting
    nums.sort()
