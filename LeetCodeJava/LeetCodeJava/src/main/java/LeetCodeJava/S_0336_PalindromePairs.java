/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package LeetCodeJava;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class S_0336_PalindromePairs {
    public boolean checkPalindromeIn(String pWord,int front, int back){
        while (back > front){
            if (pWord.charAt(front) != pWord.charAt(back)) return false;
            front++;
            back--;
        }
        System.out.println("TBD word :"+pWord+" front:"+front+"  back:"+back);
        return true;  
    }
    public List<String> allValidSuffixes(String word){
        List<String> validSuffixes = new ArrayList<>();
        
        for (int i = 0; i < word.length(); i++){
            if (checkPalindromeIn(word, 0, i)){
                validSuffixes.add(word.substring(i+1, word.length())) ;   
            }
        }
        return validSuffixes;
        
    }
    
        public List<String> allValidPrefixes(String word){
        List<String> validPrefixes = new ArrayList<>();
        
        for (int i = 0; i < word.length(); i++){
            if (checkPalindromeIn(word, i, word.length()-1)){
                validPrefixes.add(word.substring(0, i)) ;   
            }
        }
        return validPrefixes;
        
    }
    public List<List<Integer>> palindromePairs(String[] words) {
        
        Map<String, Integer> wordMap = new HashMap<>();
        
        for (int i = 0; i < words.length ; i ++){
            wordMap.put(words[i], i);
        }
        
        List<List<Integer>> result = new ArrayList<>();
        
        for (String word : wordMap.keySet()){
            int curWordIdx = wordMap.get(word);
            String reverseWord = new StringBuilder(word).reverse().toString();
            
            //Case 1 Direct Compare
            if (wordMap.containsKey(reverseWord) && wordMap.get(reverseWord) != curWordIdx){
                result.add(Arrays.asList(wordMap.get(reverseWord), curWordIdx));
            }
            //System.out.println("TBD word :"+word+"  reverseWord: "+reverseWord);
            
            
            for (String suff : allValidSuffixes(word)){
                String reversedSuffix = new StringBuilder(suff).reverse().toString();
                if (wordMap.containsKey(reversedSuffix)){
                    result.add(Arrays.asList(wordMap.get(reversedSuffix), curWordIdx));
                }
                
            }
            
            
            for (String pref : allValidPrefixes(word)){
                String reversedPrefix = new StringBuilder(pref).reverse().toString();
                if (wordMap.containsKey(reversedPrefix)){
                    result.add(Arrays.asList(curWordIdx, wordMap.get(reversedPrefix)));
                }
                
            }
        } 
        
        return result;
    }
}
