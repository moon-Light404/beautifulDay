#ifndef _MENU_H
#define _MENU_H
#define LEN 25
#include <windows.h>
#include "stu.h"

//�˵��� 
class Menu:public Check{
	public:
		Menu();
		char MainMenu();// ������
		bool IsAdministrator();// ����Ա��¼
		char SubAdministrator();// ����Ա�Ӳ˵�
		char ManageStudent();// ����ѧ�� 
		char ManageCourse();// ����γ� 
		bool IsUser();//�ж��Ƿ��Ƿ����û� 
		char SubUser();//�û��Ӳ˵� 
		void login();//ģ���¼���� 
		void End();//�������� 
		void DrawBox();
		
};



#endif
