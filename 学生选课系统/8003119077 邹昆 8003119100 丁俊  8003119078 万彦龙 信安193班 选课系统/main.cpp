#include "menu.h" 
#include "stu.h"

int main(){

	//ʵ����һ���˵�
	Menu menu;
	char menuID;
	char SubAdminmenuID;
	char SubUserID;
	//��ʼ�� 
	init();
	Manager manager;
	while(1){
		//ѡ�����Ա or �û�
		menuID = menu.MainMenu(); 
		switch(menuID){
			//����Ա��¼ 
			case '1':
				system("cls");
				if (menu.IsAdministrator()){
				menu.login();
				while(1){
						//ѡ��������
						SubAdminmenuID = menu.SubAdministrator(); 
						switch(SubAdminmenuID){
			
							//����ѧ����Ϣ 
							case '1':
								while(1){
									menuID = menu.ManageStudent();
									switch(menuID){
										case '1': manager.addStuInf();break;
										case '2': manager.deletStuInf();break;
										case '3': manager.alterStuInf();break;
										case '4': manager.displayStuInf();break;
									}
									//������һ�� 
									if(menuID=='0') break;
								}break;
							//����γ���Ϣ 
							case '2': 
								while(1){
									menuID = menu.ManageCourse();
									switch(menuID){
										case '1': manager.addCouInf();break;
										case '2': manager.deletCouInf();break;
										case '3': manager.alterCouInf(); break;
										case '4': manager.displayCouInf();break;
									}
									//������һ�� 
									if(menuID=='0') break;
								}break;	
						}
						if(SubAdminmenuID == '0') break;
					}
				}break;
			//�û���¼ 
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
					//����û�����0���򷵻���һ�� 
					if (SubUserID == '0') break;		
					}	
				}break;
			//�˳�����	
			case '0':menu.End(); exit(0);
		}
	}
	
	return 0;
}
