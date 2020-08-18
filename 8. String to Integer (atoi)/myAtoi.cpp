#include <cstdio>
#include <iostream>
/*
1、空字符串处理
2、正负的判断
3、超过 上下最值 溢出 处理  假设只能存储 32 位大小的有符号整数
4、使用  ascii 判断是否有效  0 - 9
*/

#define INT_MAX 0x7FFFFFFF
#define INT_MIN 0x80000000

int myAtoi(const char * str) {
	
	long long lNumValue = 0;	// 字符串处理后可能溢出，有符号int的最大最小值 故使用long long型
	bool iFlag = true;	// true 正数
	
	//跳过字符串前面 空字符
	for (; *str == ' '; str++);
	
	//正负判断
	if (*str == '-') {
		iFlag = false;
		str++;
	}
	else if (*str == '+')
	{
		str++;
	}

	// ascii 判断是否有效  0 - 9，并处理
	while ((*str>='0')&&(*str<='9'))
	{
		lNumValue = lNumValue * 10 + (*str - '0');
		str++;
		// 是否溢出判断  强转为int后是否相等
		if (iFlag && lNumValue>INT_MAX)
		{
			return INT_MAX;

		}
		else if (!iFlag && lNumValue>INT_MIN)
		{
			return INT_MIN;
		}
	}

	// 正负数
	return iFlag ? lNumValue : -lNumValue;
}

void Test(const char* string)
{
	int result = myAtoi(string);
	printf("number for %s is: %d.\n", string, result);
}

void main()
{
	printf("%d", INT_MAX);
	printf("%d", INT_MIN);
	Test("42");
	Test("-42");
	Test("4193 with words");
	Test("words and 987");
	Test("-91283472332");
	system("pause");
}