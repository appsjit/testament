import java.io.*;
import java.util.*;

class MyCode {
	public static void main (String[] args) {
		String[] words1 = {"apple","alpha", "appling","africa"};
    String[] words2 = {"car","carter","carb","crab","cart"};

    Trie trie = new Trie();
    trie.addWords(words1);
    trie.addWords(words2);
    System.out.println(trie.autoComplete("cr"));
	}

  public static void printArr(ArrayList<String> arr){
    for(String str: arr) System.out.println(arr);
  }
}


class TrieNode {
  Character value;
  HashMap<Character, TrieNode> children;
  boolean endOfWord;

  public TrieNode(Character ch){
    this.value = ch;
    this.children = new HashMap<Character, TrieNode>();
    this.endOfWord = false;
  }
}

class Trie {

  private TrieNode root;

  public Trie(){
    this.root = new TrieNode('\u0000');
  }

  //Add words
  public void addWords(String[] words){
    for(String word: words) this.addWord(word);
  }

  //Add word
  public void addWord(String word){
    //Get the root of trie
    TrieNode curr = this.root;

    //Loop over characters in word, while traversing trie
    for(Character ch: word.toCharArray()){
      //  adding TrieNodes where they don't exist
      if(!curr.children.containsKey(ch)){
        curr.children.put(ch, new TrieNode(ch));
      }
      curr = curr.children.get(ch);
    }

    //Set the end word flag of last TrieNode to true
    curr.endOfWord = true;

  }


  //Remove word
  public void removeWord(String word){

  }

  //GetEndOfPrefixNode
  public TrieNode getEndPrefixNode(String prefix){
    //Get the root of trie
    TrieNode curr = this.root;

    //Loop over characters in word
    for(Character ch: prefix.toCharArray()){
      //  adding TrieNodes where they don't exist
      if(!curr.children.containsKey(ch)){
        return null;
      }
      curr = curr.children.get(ch);
    }
    return curr;

  }


  //IsWord
  public boolean isWord(String word){
    TrieNode endofPrefix = getEndPrefixNode(word);
    return endofPrefix != null && endofPrefix.endOfWord;
  }


  //Autocomplete
  public ArrayList<String> autoComplete(String prefix){
    //Get end prefix node
    TrieNode endofPrefix = getEndPrefixNode(prefix);

    ArrayList<String> result = new ArrayList<>();
    //DFS to get all possible words
    if(endofPrefix != null){
      dfs(prefix, '\u0000', endofPrefix, result);
    }
    return result;
  }

  public void dfs(String currStr, Character addCh,
      TrieNode currNode, ArrayList<String> result) {

    //Add the character we need to add to currstr
    currStr += addCh;

    //Check if current Node is end of a word
    if(currNode.endOfWord) result.add(currStr);

    //recurse through all children of current node
    for(TrieNode child: currNode.children.values()){
      dfs(currStr, child.value, child, result);
    }


  }

}






