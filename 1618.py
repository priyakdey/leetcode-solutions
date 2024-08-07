"""
1618. Maximum Font to Fit a Sentence in a Screen

You are given a string text. We want to display text on a screen of width w and 
height h. You can choose any font size from array fonts, which contains the 
available font sizes in ascending order.

You can use the FontInfo interface to get the width and height of any 
character at any available font size.

The FontInfo interface is defined as such:

interface FontInfo {
  // Returns the width of character ch on the screen using font size fontSize.
  // O(1) per call
  public int getWidth(int fontSize, char ch);

  // Returns the height of any character on the screen using font size fontSize.
  // O(1) per call
  public int getHeight(int fontSize);
}

The calculated width of text for some fontSize is the sum of every 
getWidth(fontSize, text[i]) call for each 0 <= i < text.length (0-indexed). 
The calculated height of text for some fontSize is getHeight(fontSize). 
Note that text is displayed on a single line.

It is guaranteed that FontInfo will return the same value if you call getHeight 
or getWidth with the same parameters.

It is also guaranteed that for any font size fontSize and any character ch:
- getHeight(fontSize) <= getHeight(fontSize+1)
- getWidth(fontSize, ch) <= getWidth(fontSize+1, ch)

Return the maximum font size you can use to display text on the screen. 
If text cannot fit on the display with any font size, return -1.
"""

from typing import List


class FontInfo(object):
    """
    This is FontInfo's API interface.
    You should not implement it, or speculate about its implementation
    """

    def getWidth(self, fontSize, ch) -> int:  # type: ignore
        """Return the width of char ch when fontSize is used.
        :type fontSize: int
        :type ch: char
        :rtype int
        """
        pass

    def getHeight(self, fontSize) -> int:  # type: ignore
        """
        :type fontSize: int
        :rtype int
        """
        pass


class Solution:
    def maxFont(
        self, text: str, w: int, h: int, fonts: List[int], fontInfo: "FontInfo"
    ) -> int:
        left, right = 0, len(fonts) - 1
        index = -1

        while left <= right:
            mid = left + (right - left) // 2
            fontSize = fonts[mid]

            textHeight = fontInfo.getHeight(fontSize)

            if textHeight > h:
                right = mid - 1
            else:
                textWidth = 0
                for ch in text:
                    textWidth += fontInfo.getWidth(fontSize, ch)
                if textWidth <= w:
                    index = mid
                    left = mid + 1
                else:
                    right = mid - 1

        return fonts[index] if index != -1 else -1
