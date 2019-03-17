/*
*@author:leacoder
*@des: 堆栈实现  map存储键值对 有效的括号 
*/

class Solution {
public:
    bool isValid(string s) {
        if (s.length() % 2){
            return false;
        }

        stack<char> mystack;

        map<char, char> mymap;  
        mymap.insert(make_pair('(', ')'));
		mymap.insert(make_pair('[', ']'));
		mymap.insert(make_pair('{', '}'));

        for(size_t i = 0; i < s.length(); i++){

            if(s[i] =='(' || s[i]=='{' || s[i] =='['){
                 mystack.push(s[i]);
            }
            else {
                if(mystack.empty() ){
                    return false;
                }else{
                    char c = mystack.top();
                    mystack.pop();
                    if(mymap[c]!=s[i]){
                        return false;
                    }
                }
            }
        }
        
        if(mystack.empty())
            return true;
        else 
            return false;
    }
};