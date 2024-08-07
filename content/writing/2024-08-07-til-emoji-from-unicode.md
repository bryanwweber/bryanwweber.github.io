---
title: "TIL: How to convert hexadecimal code points to emoji in Python"
date: 2024-08-07 14:09
category: personal
status: published
---

Today I learned how to convert hexadecimal code points, represented as strings, to emoji characters using Python.

I'm processing data from the Slack messages API, and messages often contain emoji. These have a special block type in the rich text format that looks like:

```json
{
    "type": "emoji",
    "name": "fire",
    "unicode": "1f525"
}
```

The `unicode` string listed there is actually a string of hexadecimal characters that represent the Unicode code point. Since there are more than 4 characters in the string, this represents a two-byte code point.

We need to use the `int()` and `chr()` built-in functions to do this conversion. First, convert the string to a base-16 integer; then use the `chr()` function to return the bytes for the Unicode code point:

```python
fire = "1f525"
print(chr(int(fire, 16)))
```

This will print 🔥 to your console, if you have a supported font installed. To see the actual bytes, we can encode this to `utf-8`:

```python
print(chr(int(fire, 16)).encode("utf-8"))
```

will print `b'\xf0\x9f\x94\xa5'` to the console.
