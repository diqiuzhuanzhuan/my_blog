// love_cherish.cpp : 此文件包含 "main" 函数。程序执行将在此处开始并结束。
//

#include <iostream>
#include <tchar.h>
#include <Windows.h>
#include <stdio.h>
#include <atlstr.h>
#include <time.h>

BOOL _set_file_time(CString filename);


void write_my_first_letter()
{
	CString filename = "love_you_forever.txt";
	HANDLE handle = CreateFile(filename, GENERIC_WRITE, FILE_SHARE_WRITE, NULL, CREATE_NEW, FILE_ATTRIBUTE_NORMAL, NULL);
	const char *content = "一个好孩子真算是的大刀阔斧打的阿凡达发的卡夫卡的加分打卡积分打发\r\n 打客服加的今飞凯达发的发啊发"\
		"阿凡达发达开发 "\
		"发大发";
	DWORD writeLen;
	WriteFile(handle, content, strlen(content), &writeLen, NULL);
	CloseHandle(handle);
	_set_file_time(filename);
}


BOOL _set_directory_time(CString filename)
{
	HANDLE handle = CreateFile(filename, GENERIC_READ|GENERIC_WRITE|FILE_WRITE_ATTRIBUTES, FILE_SHARE_READ|FILE_SHARE_DELETE, NULL, OPEN_EXISTING, FILE_FLAG_BACKUP_SEMANTICS, NULL);
	SYSTEMTIME createTime, modifyTime, accessTime; //SYSTEMTIME(), SYSTEMTIME(), SYSTIMETIME();
	GetSystemTime(&createTime);
	GetSystemTime(&modifyTime);
	GetSystemTime(&accessTime);
	createTime.wYear = 2019;
	createTime.wMonth = 7;

	createTime.wDay = 20;
	createTime.wHour = 19;
	createTime.wMinute = 25;
	createTime.wSecond = 21;
	modifyTime.wYear = 2019;
	modifyTime.wMonth = 8;
	modifyTime.wDay = 24;
	modifyTime.wHour = 20;
	modifyTime.wMinute = 19;
	modifyTime.wSecond = 9;
	accessTime.wYear = 2019;
	accessTime.wMonth = 8;
	accessTime.wDay = 24;
	accessTime.wHour = 21;
	accessTime.wMinute = 11;
	accessTime.wSecond = 45;
	FILETIME ft_createTime, lc_createTime;
	FILETIME ft_modifyTime, lc_modifyTime;
	FILETIME ft_accessTime, lc_accessTime;
	SystemTimeToFileTime(&createTime, &ft_createTime);
	LocalFileTimeToFileTime(&ft_createTime, &lc_createTime);
	SystemTimeToFileTime(&modifyTime, &ft_modifyTime);
	LocalFileTimeToFileTime(&ft_modifyTime, &lc_modifyTime);
	SystemTimeToFileTime(&accessTime, &ft_accessTime);
	LocalFileTimeToFileTime(&ft_accessTime, &lc_accessTime);
	BOOL ret = SetFileTime(handle, &lc_createTime, &lc_accessTime, &lc_modifyTime);
	CloseHandle(handle);
	if (!ret) {
		printf("set file time error: %d\n", GetLastError());
	}
	return ret;
}

BOOL _set_file_time(CString filename)
{
	HANDLE handle = CreateFile(filename, GENERIC_READ|GENERIC_WRITE|FILE_WRITE_ATTRIBUTES, FILE_SHARE_WRITE|FILE_SHARE_DELETE, NULL, OPEN_EXISTING, FILE_FLAG_BACKUP_SEMANTICS, NULL);
	SYSTEMTIME createTime, modifyTime, accessTime; //SYSTEMTIME(), SYSTEMTIME(), SYSTIMETIME();
	GetSystemTime(&createTime);
	GetSystemTime(&modifyTime);
	GetSystemTime(&accessTime);
	createTime.wYear = 2019;
	createTime.wMonth = 7;
	createTime.wDay = 20;
	createTime.wHour = 19;
	createTime.wMinute = 25;
	createTime.wSecond = 21;
	modifyTime.wYear = 2019;
	modifyTime.wMonth = 8;
	modifyTime.wDay = 24;
	modifyTime.wHour = 20;
	modifyTime.wMinute = 19;
	modifyTime.wSecond = 9;
	accessTime.wYear = 2019;
	accessTime.wMonth = 8;
	accessTime.wDay = 24;
	accessTime.wHour = 21;
	accessTime.wMinute = 11;
	accessTime.wSecond = 45;
	FILETIME ft_createTime, lc_createTime;
	FILETIME ft_modifyTime, lc_modifyTime;
	FILETIME ft_accessTime, lc_accessTime;
	SystemTimeToFileTime(&createTime, &ft_createTime);
	LocalFileTimeToFileTime(&ft_createTime, &lc_createTime);
	SystemTimeToFileTime(&modifyTime, &ft_modifyTime);
	LocalFileTimeToFileTime(&ft_modifyTime, &lc_modifyTime);
	SystemTimeToFileTime(&accessTime, &ft_accessTime);
	LocalFileTimeToFileTime(&ft_accessTime, &lc_accessTime);
	BOOL ret = SetFileTime(handle, &lc_createTime, &lc_accessTime, &lc_modifyTime);

	CloseHandle(handle);
	if (!ret) {
		printf("set file time error: %d\n", GetLastError());
	}
	return ret;
}


CString get_user_directory()
{
	LPCWSTR homeProfile = _T("USERPROFILE");
	TCHAR homePath[1024] = { 0 };
	unsigned int pathSize = GetEnvironmentVariable(homeProfile, homePath, 1024);
	CString s;
	s.Format(_T("%s"), homePath);
	_tprintf(s);
	return s;
}


DWORD SetFileHidden(CString szFileName)
{
	//获取原来的文件属性
	DWORD dwFileAttributes = GetFileAttributes(szFileName);
	//将只读和隐藏属性附加到原来的文件属性上
	dwFileAttributes |= FILE_ATTRIBUTE_HIDDEN;
	//设置属性，并判断是否成功
	if (SetFileAttributes(szFileName, dwFileAttributes))
	{
		printf("成功\n");
	}
	else
	{
		printf("属性设置；%d", GetLastError());
	}
	return 0;
}


CString create_my_directory()
{
	CString basePath = get_user_directory();
	SetCurrentDirectory(basePath);
	CString firstPath = basePath + _T("//.774ffafaefcca1930f77");
	if (!PathFileExists(firstPath)) {
		CreateDirectory(firstPath, NULL);
		SetFileHidden(firstPath);
		_set_directory_time(firstPath);
	}
	SetCurrentDirectory(firstPath);
	CString secondPath = firstPath + _T("//love_cherish_forever");
	if (!PathFileExists(secondPath)) {
		CreateDirectory(secondPath, NULL);
		SetFileHidden(secondPath);
	}
	SetCurrentDirectory(secondPath);
	_set_directory_time(firstPath);
	_set_directory_time(secondPath);

	return firstPath;
}

int authority()
{
	std::cout << "请输入密码:";
	std::string password;
	std::cin >> password;
	if (password != "931122") {
		std::cout << "密码错误，你是谁，你休想从我这里获取任何东西！！";
		return -1;
	}
	std::cout << "密码正确";
	return 0;
}


int main()
{
	if (authority() != 0) {
		return -1;
	}
	CString s = create_my_directory();
	write_my_first_letter();
	return 0;
}

// 运行程序: Ctrl + F5 或调试 >“开始执行(不调试)”菜单
// 调试程序: F5 或调试 >“开始调试”菜单

// 入门使用技巧: 
//   1. 使用解决方案资源管理器窗口添加/管理文件
//   2. 使用团队资源管理器窗口连接到源代码管理
//   3. 使用输出窗口查看生成输出和其他消息
//   4. 使用错误列表窗口查看错误
//   5. 转到“项目”>“添加新项”以创建新的代码文件，或转到“项目”>“添加现有项”以将现有代码文件添加到项目
//   6. 将来，若要再次打开此项目，请转到“文件”>“打开”>“项目”并选择 .sln 文件
