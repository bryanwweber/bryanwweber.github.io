---
title: "TIL: What Big-endian and Little-Endian mean"
date: 2023-06-17 14:09
category: personal
status: published
---

Today, I was curious why we often represent values in computer memory with hexadecimal numbers. I found [the answer][1] on a course page from the [Vienna University of Economics and Business](https://statmath.wu.ac.at/). While I was there, though, I found the answer to a question that's been bugging me for a long time! What is the difference between big-endian and little-endian memory layout?

The answer turns out to be related to how the computer represents multi-byte integer types in memory. A 32-bit integer will consume 4 bytes of memory. If the least significant digit, starting in the ones place, of the integer is represented first in memory, the layout is **little-endian.** This would look like:

```text
00000000 00000000 00000000 00000000 | 0
00000001 00000000 00000000 00000000 | 1
00000010 00000000 00000000 00000000 | 2
...
11111111 00000000 00000000 00000000 | 255
00000000 00000001 00000000 00000000 | 256
...
00000000 00000000 00000000 00000001 | 16777216
...
00000000 00000000 00000000 11111111 | 4278190080
...
11111111 11111111 11111111 11111111 | 4294967295
```

Notice that the left most set of 8 bits is increasing first until it reaches (2<sup>8</sup>-1) = 255, then the second group of bits starts counting. Since the order of bytes is going from left-to-right, it is called little-endian (even though each byte is still read right-to-left).

The alternative is called **big-endian**. In this case, the left most byte represents the highest significant digit. So, we'd represent the examples above as:

```text
00000000 00000000 00000000 00000001 | 1
00000000 00000000 00000000 00000010 | 2
...
00000000 00000000 00000000 11111111 | 255
00000000 00000000 00000001 00000000 | 256
...
00000001 00000000 00000000 00000000 | 16777216
...
11111111 00000000 00000000 00000000 | 4278190080
...
11111111 11111111 11111111 11111111 | 4294967295
```

The answer is that each character in the hexadecimal represents 4 bits, so two hexadecimal characters can represent one byte. One byte is enough to express an ASCII letter, which turns out to be very convenient.

---

The answer to my original question is that hexadecimal is a compact way of representing 8-bit bytes with two characters. Since 4 bits can take on 16 possible values, we use a base-16 counting system. To do the conversion, break each byte into two segments of 4 bits and turn each of those into a hexadecimal digit.

For example, the letter `A` in ASCII encoding is represented by the integer 65, or in binary 1000001. This only takes 7 bits to represent, but the computer will store things in blocks of 8 bits, or one byte. Putting `A` into a byte means we have one bit/digit that isn't used, so it remains zero and `A` becomes `01000001`[^1]

Now take those 8 bits and break them into chunks of 4 bits, or `0100 0001`. Each quad of bits is represented by a hexadecimal digit, from 0-9 and then letters a-f. So `A` in hexadecimal is `0x41` since `0100 = 4` and `0001 = 1`. The `0x` prefix is purely for human understanding that this is a hexadecimal number, not a binary, decimal, or octal number.

[1]: https://statmath.wu.ac.at/courses/data-analysis/itdtHTML/node55.html#:~:text=An%20even%20more%20efficient%20way,requires%20only%202%20hexadecimal%20digits

[^1]: Notice that the zero is added to the left of the binary number. This is a bit like writing the base-10 integer 100 as 0100. We have zero in the thousands place, one in the hundreds place, zero in the tens place, and zero in the ones place. We typically treat the leading zero as implied in base-10 counting because we don't have a natural place to stop. We could also include a zero for the ten-thousands place, one-hundred-thousands place, and so on.
