/*
*@author:leacoder
*@des: 堆栈实现  map存储键值对 有效的括号 
*/

class Solution {
    public boolean isValid(String s) {
        if (1==s.length() % 2){
            return false;
        }
        Stack<Character> stack = new Stack<>();
        char[] chars = s.toCharArray();
        
        Map m1 = new HashMap(); 
        m1.put('}', '{');
        m1.put(']', '[');
        m1.put(')', '(');
        
        for (char aChar : chars) {
            //Object get(Object k) 返回指定键所映射的值；如果此映射不包含该键的映射关系，则返回 null。
            if(m1.get(aChar)==null){ //不是左括号  是右括号类型 入栈
                stack.push(aChar);
            }
            else if(stack.empty()){//栈已经空了
                return false;
            }
            else if(m1.get(aChar)!=stack.pop()){
                return false;
            }          
        }
        
        if(stack.empty()){
            return true;
        }
        else{
            return false;
        }
        
    }
}