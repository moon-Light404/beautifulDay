#include <iostream>
#include <conio.h>
#include <string>
#include <cstdio>
#include <windows.h>
#include "stu.h"
#include "menu.h"

using namespace std;


Menu::Menu(){}
 // 主界面 
 char Menu::MainMenu(){
	char choice;
	system("cls");
	cout<<"********************欢迎使用学生信息管理系统********************"<<endl;
	cout<<"*                                                              *"<<endl;
	cout<<"*                ---------------------------------             *"<<endl;
	cout<<"*                |powered by  NUC 信息安全193班  |             *"<<endl;
	cout<<"*                     8003119077    邹昆                       *"<<endl;
	cout<<"*                     8003119100    丁俊                       *"<<endl;
	cout<<"*                     8003119078    万彦龙                     *"<<endl;
	cout<<"*                ---------------------------------             *"<<endl;
	cout<<"*                                                              *"<<endl;
	cout<<"*                        1)管理员登录                          *"<<endl;
	cout<<"*                                                              *"<<endl;
	cout<<"*                        2)用户登录                            *"<<endl;
	cout<<"*                                                              *"<<endl;
	cout<<"*                        0)退出软件                            *"<<endl;
	cout<<"*                                                              *"<<endl;
	cout<<"*                                                              *"<<endl;
	cout<<"****************************************************************"<<endl;
	fflush(stdin);
	choice = getch();
	return choice;
}

// 管理员登录
 bool Menu::IsAdministrator(){
 	// 是否登陆成功
	system("cls"); 
	cout<<"****************************************************************"<<endl;
	cout<<"*                                                              *"<<endl;
	cout<<"*                   欢迎使用学生管选课理系统                   *"<<endl;
	cout<<"*                                                              *"<<endl;
	cout<<"*                                                              *"<<endl;
	cout<<"*                                                              *"<<endl;
	cout<<"*                                                              *"<<endl;
	cout<<"*                                                              *"<<endl;
	cout<<"*                                                              *"<<endl;
	cout<<"*                                                              *"<<endl;
	cout<<"****************************************************************"<<endl;
 	bool flag;
 	string code;
 	Gotoxy(9,6);
 	cout<<"请输入登录密码(密码为666666) :";
 	cin>>code;
 	while(1){
 		if (code != "666666"){
 		Gotoxy(9,6);
 		cout<<"密码错误,请重新输入(密码为666666) :";
 		fflush(stdin);
 		cin>>code;
 		}
 		else{
 			flag = true;
 			break;
		}
		
	}
 	return flag;
 }
 
 //画边框
void Menu::DrawBox()
{
	
	cout<<"****************************************************************"<<endl;
	cout<<"*                                                              *"<<endl;
	cout<<"*                   欢迎使用学生管选课理系统                   *"<<endl;
	cout<<"*                                                              *"<<endl;
	cout<<"*                                                              *"<<endl;
	cout<<"*                                                              *"<<endl;
	cout<<"*                                                              *"<<endl;
	cout<<"*                                                              *"<<endl;
	cout<<"*                                                              *"<<endl;
	cout<<"*                                                              *"<<endl;
	cout<<"****************************************************************"<<endl;
	Gotoxy(0,7);
	//cout<<"\n\n\n\n\n\n\n";
    printf("*    ╔═══════════════════════════════════════════════════╗");
    putchar('\n');
    printf("*    ║                                                   ║");
    putchar('\n');
    printf("*    ╚═══════════════════════════════════════════════════╝");
}

 
 // 登录画面
void Menu:: login(){
	system("cls");
	DrawBox();
    int len;
    HideCursor();
    for(len = 1; len <= LEN; len++){
        Gotoxy(2 * len+5, 6 +2   );
        cout<<"█";
        Gotoxy(21+5, 3+2);
        cout<<"登陆中"<<4 * len+2<<"%"<<"......";
        Sleep(100);
    }
    Gotoxy(21+5, 3+2);
    cout<<"登陆成功 100%......";
    unHideCursor();
    Sleep(500);
} 
 
 // 管理员子菜单
 char Menu::SubAdministrator(){
 	char choice;
 	system("cls");
	cout<<"****************************************************************"<<endl;
	cout<<"*                                                              *"<<endl;
	cout<<"*                        1)管理学生                            *"<<endl;
	cout<<"*                        2)管理课程                            *"<<endl;
	cout<<"*                                                              *"<<endl;
	cout<<"*                        0)返回开始界面                        *"<<endl;
	cout<<"*                                                              *"<<endl;
	cout<<"****************************************************************"<<endl;
	fflush(stdin);
	choice = getch();
	return choice;
 }
 

 
// 管理学生 
 char Menu::ManageStudent(){
 	char choice;
 	system("cls");
 	cout<<"****************************************************************"<<endl;
	cout<<"*                                                              *"<<endl;
	cout<<"*                        1)增加学生                            *"<<endl;
	cout<<"*                        2)删除学生                            *"<<endl;
	cout<<"*                        3)修改学生                            *"<<endl;
	cout<<"*                        4)查询所有学生                        *"<<endl;
	cout<<"*                        0)返回上一界面                        *"<<endl;
	cout<<"*                                                              *"<<endl;
	cout<<"****************************************************************"<<endl;
	fflush(stdin);
	choice = getch();
	return choice;
 }
 // 管理课程 
 char Menu::ManageCourse(){
 	char choice;
 	system("cls");
 	cout<<"****************************************************************"<<endl;
	cout<<"*                                                              *"<<endl;
	cout<<"*                        1)增加课程                            *"<<endl;
	cout<<"*                        2)删除课程                            *"<<endl;
	cout<<"*                        3)修改课程                            *"<<endl;
	cout<<"*                        4)展示所有课程                        *"<<endl;
	cout<<"*                        0)返回上一界面                        *"<<endl;
	cout<<"*                                                              *"<<endl;
	cout<<"****************************************************************"<<endl;
	fflush(stdin);
	choice = getch();
	return choice;
 }
 
 bool Menu::IsUser(){
 	// 是否登陆成功 
 	system("cls");
 	int isStudentExist = 0;
 	bool flag;
 	long long ID;
	vector<Student*> :: iterator i; 	
 	cout<<"请输入你的学号（例如8003119XXX） :";
 	cin>>ID;
 	while(1){
 		if(checkStuID(ID)){
 			for (i = StudentInf.begin(); i != StudentInf.end(); ++i){
				if((*i)->getm_StuNumber() == ID%1000){
					user = *i;
					isStudentExist = 1;
					return true;
				}
			}
			if(! isStudentExist){
				pause("该学生不存在，请登录管理员账户录入该学生信息!");
				return false;
			} 
		}else{
			cout<<"格式错误，请重新输入:";
			fflush(stdin);
			cin>>ID;
		} 
	}
 } 
 
 char Menu::SubUser(){
 	char choice;
 	system("cls");
	cout<<"****************************************************************"<<endl;
	cout<<"*                                                              *"<<endl;
	cout<<"*                        1)选课                                *"<<endl;
	cout<<"*                        2)退课                                *"<<endl;
	cout<<"*                        3)查看选择课程                        *"<<endl;
	cout<<"*                        0)返回开始界面                        *"<<endl;
	cout<<"*                                                              *"<<endl;
	cout<<"****************************************************************"<<endl;
	fflush(stdin);
	choice = getch();
	return choice;
 }
 
void Menu::End(){
	system("cls"); 
	cout<<"****************************************************************"<<endl;
	cout<<"*                                                              *"<<endl;
	cout<<"*                  谢谢您使用选课管理系统                      *"<<endl;
	cout<<"*                                                              *"<<endl;
	cout<<"*                       再见！(＾ν＾)                         *"<<endl;
	cout<<"*                                                              *"<<endl;
	cout<<"*                                                              *"<<endl;
	cout<<"*                                                              *"<<endl;
	cout<<"*                                                              *"<<endl;
	cout<<"*                                                              *"<<endl;
	cout<<"****************************************************************"<<endl;
}





