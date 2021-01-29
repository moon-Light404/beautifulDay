#include "menu.h" 
#include "stu.h"

int main(){

	//实例化一个菜单
	Menu menu;
	char menuID;
	char SubAdminmenuID;
	char SubUserID;
	//初始化 
	init();
	Manager manager;
	while(1){
		//选择管理员 or 用户
		menuID = menu.MainMenu(); 
		switch(menuID){
			//管理员登录 
			case '1':
				system("cls");
				if (menu.IsAdministrator()){
				menu.login();
				while(1){
						//选择管理对象
						SubAdminmenuID = menu.SubAdministrator(); 
						switch(SubAdminmenuID){
			
							//管理学生信息 
							case '1':
								while(1){
									menuID = menu.ManageStudent();
									switch(menuID){
										case '1': manager.addStuInf();break;
										case '2': manager.deletStuInf();break;
										case '3': manager.alterStuInf();break;
										case '4': manager.displayStuInf();break;
									}
									//返回上一级 
									if(menuID=='0') break;
								}break;
							//管理课程信息 
							case '2': 
								while(1){
									menuID = menu.ManageCourse();
									switch(menuID){
										case '1': manager.addCouInf();break;
										case '2': manager.deletCouInf();break;
										case '3': manager.alterCouInf(); break;
										case '4': manager.displayCouInf();break;
									}
									//返回上一级 
									if(menuID=='0') break;
								}break;	
						}
						if(SubAdminmenuID == '0') break;
					}
				}break;
			//用户登录 
			case '2':
				system("cls");
				if(menu.IsUser()){
				while(1){					
						SubUserID = menu.SubUser();
						switch(SubUserID){
							case '1': user->select_courses();UpdateStuFile();break;
							case '2': user->quit_course();UpdateStuFile();break;
							case '3': user->show_selectedcourse();UpdateStuFile();break;
						}
					//如果用户输入0，则返回上一级 
					if (SubUserID == '0') break;		
					}	
				}break;
			//退出程序	
			case '0':menu.End(); exit(0);
		}
	}
	
	return 0;
}
