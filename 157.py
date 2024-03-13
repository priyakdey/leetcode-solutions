"""
157. Read N Characters Given Read4

Given a file and assume that you can only read the file using a given method 
read4, implement a method to read n characters.

Method read4:
The API read4 reads four consecutive characters from file, then writes those 
characters into the buffer array buf4.

The return value is the number of actual characters read.

Note that read4() has its own file pointer, much like FILE *fp in C.

Definition of read4:

    Parameter:  char[] buf4
    Returns:    int

buf4[] is a destination, not a source. The results from read4 will be copied to buf4[].
Below is a high-level example of how read4 works:

File file("abcde"); // File is "abcde", initially file pointer (fp) points to 'a'
char[] buf4 = new char[4]; // Create buffer with enough space to store characters
read4(buf4); // read4 returns 4. Now buf4 = "abcd", fp points to 'e'
read4(buf4); // read4 returns 1. Now buf4 = "e", fp points to end of file
read4(buf4); // read4 returns 0. Now buf4 = "", fp points to end of file


Method read:

By using the read4 method, implement the method read that reads n characters 
from file and store it in the buffer array buf. 
Consider that you cannot manipulate file directly.

The return value is the number of actual characters read.

Definition of read:

    Parameters:	char[] buf, int n
    Returns:	int

buf[] is a destination, not a source. You will need to write the results to buf[].

Note:
- Consider that you cannot manipulate the file directly. The file is only 
  accessible for read4 but not for read.
- The read function will only be called once for each test case.
- You may assume the destination buffer array, buf, is guaranteed to have 
  enough space for storing n characters.
"""

from typing import List


def read4(buf4: List[str]) -> int:
    """
    The read4 API is already defined for you.

        @param buf4, a list of characters
        @return an integer
        def read4(buf4):

    # Below is an example of how the read4 API can be called.
    file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
    buf4 = [' '] * 4 # Create buffer with enough space to store characters
    read4(buf4) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
    read4(buf4) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
    read4(buf4) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
    """
    pass


class Solution:
    def read(self, buf: List[str], n: int) -> int:
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        buf0: List[str] = [""] * 4

        cursor = 0
        while cursor < n:
            bytes_read = read4(buf0)
            for i in range(bytes_read):
                buf[cursor] = buf0[i]
                cursor += 1
                if cursor == n:
                    break

            if bytes_read < 4:
                break

        return cursor
