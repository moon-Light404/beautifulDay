#include <iostream>
#include <conio.h>
#include <string>
#include <cstdio>
#include <windows.h>
#include "stu.h"
#include "menu.h"

using namespace std;


Menu::Menu(){}
 // ������ 
 char Menu::MainMenu(){
	char choice;
	system("cls");
	cout<<"********************��ӭʹ��ѧ����Ϣ����ϵͳ********************"<<endl;
	cout<<"*                                                              *"<<endl;
	cout<<"*                ---------------------------------             *"<<endl;
	cout<<"*                |powered by  NUC ��Ϣ��ȫ193��  |             *"<<endl;
	cout<<"*                     8003119077    ����                       *"<<endl;
	cout<<"*                     8003119100    ����                       *"<<endl;
	cout<<"*                     8003119078    ������                     *"<<endl;
	cout<<"*                ---------------------------------             *"<<endl;
	cout<<"*                                                              *"<<endl;
	cout<<"*                        1)����Ա��¼                          *"<<endl;
	cout<<"*                                                              *"<<endl;
	cout<<"*                        2)�û���¼                            *"<<endl;
	cout<<"*                                                              *"<<endl;
	cout<<"*                        0)�˳����                            *"<<endl;
	cout<<"*                                                              *"<<endl;
	cout<<"*                                                              *"<<endl;
	cout<<"****************************************************************"<<endl;
	fflush(stdin);
	choice = getch();
	return choice;
}

// ����Ա��¼
 bool Menu::IsAdministrator(){
 	// �Ƿ��½�ɹ�
	system("cls"); 
	cout<<"****************************************************************"<<endl;
	cout<<"*                                                              *"<<endl;
	cout<<"*                   ��ӭʹ��ѧ����ѡ����ϵͳ                   *"<<endl;
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
 	cout<<"�������¼����(����Ϊ666666) :";
 	cin>>code;
 	while(1){
 		if (code != "666666"){
 		Gotoxy(9,6);
 		cout<<"�������,����������(����Ϊ666666) :";
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
 
 //���߿�
void Menu::DrawBox()
{
	
	cout<<"****************************************************************"<<endl;
	cout<<"*                                                              *"<<endl;
	cout<<"*                   ��ӭʹ��ѧ����ѡ����ϵͳ                   *"<<endl;
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
    printf("*    �X�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�[");
    putchar('\n');
    printf("*    �U                                                   �U");
    putchar('\n');
    printf("*    �^�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�a");
}

 
 // ��¼����
void Menu:: login(){
	system("cls");
	DrawBox();
    int len;
    HideCursor();
    for(len = 1; len <= LEN; len++){
        Gotoxy(2 * len+5, 6 +2   );
        cout<<"��";
        Gotoxy(21+5, 3+2);
        cout<<"��½��"<<4 * len+2<<"%"<<"......";
        Sleep(100);
    }
    Gotoxy(21+5, 3+2);
    cout<<"��½�ɹ� 100%......";
    unHideCursor();
    Sleep(500);
} 
 
 // ����Ա�Ӳ˵�
 char Menu::SubAdministrator(){
 	char choice;
 	system("cls");
	cout<<"****************************************************************"<<endl;
	cout<<"*                                                              *"<<endl;
	cout<<"*                        1)����ѧ��                            *"<<endl;
	cout<<"*                        2)����γ�                            *"<<endl;
	cout<<"*                                                              *"<<endl;
	cout<<"*                        0)���ؿ�ʼ����                        *"<<endl;
	cout<<"*                                                              *"<<endl;
	cout<<"****************************************************************"<<endl;
	fflush(stdin);
	choice = getch();
	return choice;
 }
 

 
// ����ѧ�� 
 char Menu::ManageStudent(){
 	char choice;
 	system("cls");
 	cout<<"****************************************************************"<<endl;
	cout<<"*                                                              *"<<endl;
	cout<<"*                        1)����ѧ��                            *"<<endl;
	cout<<"*                        2)ɾ��ѧ��                            *"<<endl;
	cout<<"*                        3)�޸�ѧ��                            *"<<endl;
	cout<<"*                        4)��ѯ����ѧ��                        *"<<endl;
	cout<<"*                        0)������һ����                        *"<<endl;
	cout<<"*                                                              *"<<endl;
	cout<<"****************************************************************"<<endl;
	fflush(stdin);
	choice = getch();
	return choice;
 }
 // ����γ� 
 char Menu::ManageCourse(){
 	char choice;
 	system("cls");
 	cout<<"****************************************************************"<<endl;
	cout<<"*                                                              *"<<endl;
	cout<<"*                        1)���ӿγ�                            *"<<endl;
	cout<<"*                        2)ɾ���γ�                            *"<<endl;
	cout<<"*                        3)�޸Ŀγ�                            *"<<endl;
	cout<<"*                        4)չʾ���пγ�                        *"<<endl;
	cout<<"*                        0)������һ����                        *"<<endl;
	cout<<"*                                                              *"<<endl;
	cout<<"****************************************************************"<<endl;
	fflush(stdin);
	choice = getch();
	return choice;
 }
 
 bool Menu::IsUser(){
 	// �Ƿ��½�ɹ� 
 	system("cls");
 	int isStudentExist = 0;
 	bool flag;
 	long long ID;
	vector<Student*> :: iterator i; 	
 	cout<<"���������ѧ�ţ�����8003119XXX�� :";
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
				pause("��ѧ�������ڣ����¼����Ա�˻�¼���ѧ����Ϣ!");
				return false;
			} 
		}else{
			cout<<"��ʽ��������������:";
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
	cout<<"*                        1)ѡ��                                *"<<endl;
	cout<<"*                        2)�˿�                                *"<<endl;
	cout<<"*                        3)�鿴ѡ��γ�                        *"<<endl;
	cout<<"*                        0)���ؿ�ʼ����                        *"<<endl;
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
	cout<<"*                  лл��ʹ��ѡ�ι���ϵͳ                      *"<<endl;
	cout<<"*                                                              *"<<endl;
	cout<<"*                       �ټ���(�ަͣ�)                         *"<<endl;
	cout<<"*                                                              *"<<endl;
	cout<<"*                                                              *"<<endl;
	cout<<"*                                                              *"<<endl;
	cout<<"*                                                              *"<<endl;
	cout<<"*                                                              *"<<endl;
	cout<<"****************************************************************"<<endl;
}





