/*
 *@author:leacoder
 *@des:  实现 Trie (前缀树)
 */
class Trie {
    
    public int SIZE = 26;
    public TrieNode root;
    
    class TrieNode {
        
        TrieNode(char c){
            this.val = c;
            this.isWord = false;
            this.child = new TrieNode[SIZE];
        }
        
        public char val;
        public boolean isWord;
        public TrieNode[] child ;
    }
    
    

    /** Initialize your data structure here. */
    public Trie() {
        this.root = new TrieNode(' ');
    }
    
    /** Inserts a word into the trie. */
    public void insert(String word) {
        if(word == null || word.length() == 0) return;
        TrieNode node = this.root;
        for( int i = 0; i < word.length(); i++ ){
            char c = word.charAt(i);
            if( node.child[c - 'a'] == null){
                node.child[c - 'a'] = new TrieNode(c);
            } 
            node = node.child[c - 'a'];
        }
        node.isWord = true;
        
    }
    
    /** Returns if the word is in the trie. */
    public boolean search(String word) {
        TrieNode node = this.root;
        for( int i = 0; i < word.length(); i++ ){
            char c = word.charAt(i);
            if( node.child[c - 'a'] == null){
                return false;
            }
            node = node.child[c - 'a'];
        }
        
        return node.isWord;
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    public boolean startsWith(String prefix) {
        
        TrieNode node = this.root;
        for( int i = 0; i < prefix.length(); i++ ){
            char c = prefix.charAt(i);
            if( node.child[c - 'a'] == null){
                return false;
            }
            node = node.child[c - 'a'];
        }
        
        return true;
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */