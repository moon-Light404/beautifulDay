#ifndef _MENU_H
#define _MENU_H
#define LEN 25
#include <windows.h>
#include "stu.h"

//菜单类 
class Menu:public Check{
	public:
		Menu();
		char MainMenu();// 主界面
		bool IsAdministrator();// 管理员登录
		char SubAdministrator();// 管理员子菜单
		char ManageStudent();// 管理学生 
		char ManageCourse();// 管理课程 
		bool IsUser();//判断是否是否是用户 
		char SubUser();//用户子菜单 
		void login();//模拟登录界面 
		void End();//结束画面 
		void DrawBox();
		
};



#endif
