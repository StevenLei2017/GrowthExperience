// c_answer.cpp : 此文件包含 "main" 函数。程序执行将在此处开始并结束。
//

#include "pch.h"
#include <iostream>
#include <map>
#include <string>
#include <stack>
#include <vector>
using namespace std;


class Solution {
public:
	map<char, char> char_dict;
	map<char, char>::iterator iter;
	Solution(void){
		this->char_dict.insert(pair<char, char>('[', ']'));
		this->char_dict.insert(pair<char, char>('{', '}'));
		this->char_dict.insert(pair<char, char>('(', ')'));
	};
	bool is_inKeys(char  c) {
		this->iter = this->char_dict.find(c);
		if (this->iter == this->char_dict.end())
			return false;
		else
			return true;
	};
	char get_value(char key) {
		this->iter = this->char_dict.find(key);
		char result = this->iter->second;
		return result;
	};
	bool isValid(string s) {
		stack<char> a_stack;
		for (int i = 0; i < s.length(); i++) {
			char every_char = s[i];
			if (this->is_inKeys(every_char))
				a_stack.push(this->get_value(every_char));
			else {
				if (a_stack.empty())
					return false;
				else {
					char pop_char = a_stack.top();
					a_stack.pop();
					if (pop_char != every_char)
						return false;
				}
			}
		}
		return a_stack.empty();
	};
};


int main()
{	
	Solution solution = Solution();
	string testCase_1 = "()";
	string testCase_2 = "()[]{}";
	string testCase_3 = "(]";
	string testCase_4 = "([)]";
	string testCase_5 = "{[]}";
	vector<string> testCase_list;
	testCase_list.push_back(testCase_1);
	testCase_list.push_back(testCase_2);
	testCase_list.push_back(testCase_3);
	testCase_list.push_back(testCase_4);
	testCase_list.push_back(testCase_5);
	int length = testCase_list.size();
	for (int i = 0; i < length; i++) {
		string testCase = testCase_list[i];
		cout << solution.isValid(testCase) << endl;
	};
}
