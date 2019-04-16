
[https://leetcode-cn.com/problems/word-search-ii/](https://leetcode-cn.com/problems/word-search-ii/)

212.单词搜索 II

给定一个二维网格 board 和一个字典中的单词列表 
words，找出所有同时在二维网格和字典中出现的单词。


单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。

示例:

输入: 
words = ["oath","pea","eat","rain"] and board =
[

  ['o','a','a','n'],

  ['e','t','a','e'],

  ['i','h','k','r'],

  ['i','f','l','v']

]

输出: ["eat","oath"]

说明:

你可以假设所有输入都由小写字母 a-z 组成。

[https://leetcode.com/problems/word-search-ii/](https://leetcode.com/problems/word-search-ii/)

212.Word Search II

Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 

Example:

Input: 
board = [

  ['o','a','a','n'],

  ['e','t','a','e'],

  ['i','h','k','r'],

  ['i','f','l','v']

]

words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]
 

Note:

All inputs are consist of lowercase letters a-z.
The values of words are distinct.