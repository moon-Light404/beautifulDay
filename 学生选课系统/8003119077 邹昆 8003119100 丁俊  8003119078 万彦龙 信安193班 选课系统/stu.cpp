#define LEN 25
#include <iostream>
#include <windows.h>
#include<iomanip>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <math.h>
#include <conio.h>
#include <fstream>
#include <stdarg.h>
#include <vector>
#include "stu.h"

using namespace std;


Student* user;
vector<Student*>  StudentInf;
vector<Course*> CourseInf;
//Check check;  
//����һ��check����

//extern Check check;  

//���ѧ�Ÿ�ʽ�Ƿ���ȷ 
bool Check::checkStuID(long long ID)
{
	long long  id = ID/1000;
	if(id == 8003119){
	return true;
	}
	return false;
}
//���γ̴��� 
int Check::checkcourseCode(int code)
{
	int flag=0;
	if(code>=1 && code<100)
	flag=1;
	return flag; //���Ϊ1��ʾ��ʽ����ȷ��0��ʾ��ʽ���� 
}
//���ѧ�� 
int Check::checkCreditFormat(int credit)
{
	int flag=0;
	if(credit>=1 && credit<=10)
	flag=1;
	return flag;
}
//��鹤�� 
int Check::checkcoursejobnumber(int ID){
	int flag = 0;
	if(ID>0 &&ID <100) flag = 1;
	return flag;
}
//������� 
int Check::checkname(char name[]){
	if(strlen(name) > 15){
		return 0;
	}
	return 1;
}
int Check::checkname_1(char name[]){
	if(strlen(name) > 35){
		return 0;
	}
	return 1;
}

//����һ��check����

//Check check;


Course::Course(){
	m_nCourseCode = 0;
}
//���빤�� 
void Course::setm_nJobnumber(){
	int number;
	cout<<"�������ο���ʦ�Ĺ��ţ�1-100����";
	cin>>number;
	while(1){
		if(checkcoursejobnumber(number)){
			m_nJobnumber = number;
			break;
		}else{
			cout<<"������һ������1С��100����:"; 
			fflush(stdin);
			cin>>number;
		}
	}
	cout<<endl;
}
//�������� 
void Course::setm_strname(){
	char name[30];
	cout<<"��������ʦ������:";
	cin>>name;
	while(1){
		if(checkname(name)){
			strcpy(m_strname, name);
			break;
		}else{
			cout<<"�������ֵ���󳤶Ȳ�����15���ֽ�,����������:";
			fflush(stdin);
			cin>>name;
		}
	}
	cout<<endl;
}
//����γ̴���
void Course::setm_nCourseCode() {
	int code;
	cout<<"������γ̴��ţ�1-99��:";
	cin>>code;
	while(1){
		if(checkcourseCode(code)){
			m_nCourseCode = code;
			break;
		}else{
			cout<<"������һ������0С��100����:";
			fflush(stdin);
			cin>>code; 
		}
	}
	cout<<endl;
}
//����γ����� 
void Course::setm_strCourseName(){
	char name[50];
	cout<<"������γ�����:";
	cin>>name;
	while(1){
		if(checkname_1(name)){
			strcpy(m_strCourseName, name);
			break;
		}else{
			cout<<"�������ֵ���󳤶Ȳ�����35���ֽ�,����������:";
			fflush(stdin);
			cin>>name;
		}
	}
	cout<<endl;
}
//�γ�ѧ�� 
void Course::setm_nCourseCredit(){
	int number;
	cout<<"������γ�ѧ�֣�1-10����";
	cin>>number;
	while(1){
		if(checkCreditFormat(number)){
			m_nCourseCredit = number;
			break;
		}else{
			cout<<"������һ������1С��10����:"; 
			fflush(stdin);
			cin>>number;
		}
	}
	cout<<endl;
} 
//�γ̵ص� 
void Course::setm_strCoursePlace(){
	char name[50];
	cout<<"������γ̵ص�:";
	cin>>name;
	while(1){
		if(checkname_1(name)){
			strcpy(m_strCoursePlace, name);
			break;
		}else{
			cout<<"���󣺵ص����ֵ���󳤶Ȳ�����35���ֽ�,����������:";
			fflush(stdin);
			cin>>name;
		}
	}
	cout<<endl;
} 
//�γ�ʱ��
 void Course::setm_strCourseTime(){
 	char time[50];
	cout<<"������γ�ʱ��:";
	cin>>time;
	while(1){
		if(checkname_1(time)){
			strcpy(m_strCourseTime, time);
			break;
		}else{
			cout<<"����ʱ�����󳤶Ȳ�����35���ֽ�,����������:";
			fflush(stdin);
			cin>>time;
		}
	}
	cout<<endl;
 }
void Course::getm_nJobnumber()
		{
			cout<<m_nJobnumber;
	    }
	    //�������� 
void Course::getm_strname()
		{
			cout<<m_strname;
		}
		//���ؿγ̴���
int Course::getm_nCourseCode()
		 {
		 	return m_nCourseCode;
		 }
		//���ؿγ����� 
void Course::getm_strCourseName()
		{
       		cout<<m_strCourseName; 
		}
		 //���� �γ�ѧ��  
void Course::getm_nCourseCredit()
		{
			cout<<m_nCourseCredit;
		}
		 //�����Ͽεص� 
void Course::getm_strCoursePlace()
		{
			cout<<m_strCoursePlace;
		}
		 //�����Ͽ�ʱ��
void Course::getm_strCourseTime()
		{
			cout<<m_strCourseTime;
		}

//�洢�γ���Ϣ
//vector<Course*> CourseInf;  

Student::Student(){
	int i = 0;
	for(;i<5;i++){
		m_SelectedCourse[i] = 0;
	}
}
//�������� 
void Student::setm_StuName(){
	char name[30];
	cout<<"������ѧ��������:";
	cin>>name;
	while(1){
		if(checkname(name)){
			strcpy(m_StuName, name);
			break;
		}else{
			fflush(stdin);
			cout<<"�������ֵ���󳤶Ȳ�����15���ֽ�,����������:";
			cin>>name;
		}
	}
	cout<<endl;
}

//����ѧ�� 
void Student::setm_StuNumber(){
	long long number;
	cout<<"���������ѧ��(8003119XXX):";
	cin>>number;
	while(1){
		if(checkStuID(number)){
			m_StuNumber= number % 1000;
			break;
		}else{
			
			cout<<"��ʽ��������������:";
			 fflush(stdin);
			cin>>number;
		}
	}
	cout<<endl;
}

//����༶ 
void Student::setm_StuClass(){
	char cla[30];
	cout<<"�������ѧ���İ༶:";
	cin>>cla;
	while(1){
		if(checkname_1(cla)){
			strcpy(m_StuClass, cla);
			break;
		}else{
			cout<<"���󣺰༶����󳤶Ȳ�����35���ֽ�,����������:";
			fflush(stdin);
			cin>>cla;
		}
	}
	cout<<endl;
}
//ѡ��γ� 
void Student::select_courses()
	{  
	int id;
	int count = 0;
	int isCourseExist = 0;
	bool flag = false;
	bool flag2 = false; // �ж��Ƿ����� 
	vector<Course*>:: iterator i;
	int j;
	cout<<"------���еĿγ���Ϣ����------"<<endl;
	cout<<" �γ̴���"<<setw(30)<<" ���� "<<endl;
	for (i = CourseInf.begin(); i != CourseInf.end(); ++i){
		count++;
		cout<<" "<<setw(4)<<*right<<(*i)->getm_nCourseCode();
		cout<<setw(30)<<" "<<*right;
		(*i)->getm_strCourseName();
		cout<<endl; 
	}
	cout<<"\n����"<<count<<"���γ���Ϣ"<<endl;;
	cout<<"��������Ҫѡ��Ŀγ̴���(1--100):";
	cin>>id;
	while(1){
	if(checkcourseCode(id)){
	   	for (i = CourseInf.begin(); i != CourseInf.end(); ++i){
			if((*i)->getm_nCourseCode() == id){
				isCourseExist = 1;
				for(j = 0;j<5;j++){
					if(m_SelectedCourse[4] !=0 ){
						flag2 = true;
						break;
					}
					if(m_SelectedCourse[j]==id){
						cout<<"����ѡ��˿γ�";
						flag = false;
						isCourseExist = 1;
						break;
					}
					if(m_SelectedCourse[j]==0){
						m_SelectedCourse[j] = id;
						isCourseExist = 1;
						flag = true;
						flag2 = false;
						//UpdateStuFile();
						break;
					}
				}
			}
		}
		if(!isCourseExist){
			pause("�ÿγ̲�����,�����������......");
			break;
	}
	}else{
		cout<<"���󣬴��ŷ�Χ��1-100�����������룺";
		fflush(stdin);
		cin>>id;
	}
	if(flag){
		pause("ѡ�γɹ����������");
		break; 
	}
	if(flag2){
		pause("���Ѿ�ѡ��5�ſγ̣�");
		break; 
	}
	}

}

//�˿�
 void Student::quit_course()
{
	int id;
	int i;
	int flag = 1;//�ж��Ƿ�ѡ�� 
	int flag2 = 0;
	if(m_SelectedCourse[0]==0){
		flag = 0;
	}
	if(flag){
		cout<<"��ѡ��Ŀγ����£�"<<endl;
		for(i = 0;i<5;i++){
		if(m_SelectedCourse[i] != 0)
			cout<<m_SelectedCourse[i]<<endl;
	}
	}else{
		cout<<"�㻹δ��ʼѡ��!";
	}
	
	cout<<"��������Ҫ�˵Ŀγ̴��ţ�";
	cin>>id;
	while(1){
		if(checkcourseCode(id)){
			for(i = 0;i<5;i++){
				if(m_SelectedCourse[i] ==id){
					m_SelectedCourse[i] = 0;
					//UpdateStuFile();
					flag2 = 1;
					break;
				}
			}
			if(!flag2){
				pause("��δѡ��˿γ̣�,�����������");
				break;
				}				
		}else{
			cout<<"���󣬴��ŷ�Χ��1-100�����������룺";
			fflush(stdin);
			cin>>id;
		}
		if(flag2)
		pause("�˿γɹ���");
		break;
	}
	
}

//չʾ��ѡ�γ�
void Student::show_selectedcourse(){
	int isIdExist = 0;
	int flag = 0;
	int ID;
	int m;
	int celected[5] = {0,0,0,0,0};
	int count=0;
	int j = 0;
	char choice;
	vector<Course*> :: iterator i;
	cout<<"------��ѡ�γ���Ϣ����------"<<endl;
	cout<<" �γ̴���"<<setw(30)<<" ���� "<<endl;
	for(j = 0;j<5;j++){
		if(m_SelectedCourse[j] != 0){
			for (i = CourseInf.begin(); i != CourseInf.end(); ++i){
				if(m_SelectedCourse[j] == (*i)->getm_nCourseCode()){
					celected[count] = m_SelectedCourse[j];
					count++;
					cout<<" "<<setw(4)<<*right<<(*i)->getm_nCourseCode();
					cout<<setw(30)<<" "<<*right;
					(*i)->getm_strCourseName();
					cout<<endl; 
				}
			}
		}
	}
	cout<<"\n����"<<count<<"��ѡ����Ϣ"<<endl;
	cout<<"�Ƿ�鿴�γ���ϸ��Ϣ��Y/N����";
	cin>> choice;
	while(1){
		if(choice == 'Y'|| choice =='y'){
			cout<<"����������Ҫ�鿴�Ŀγ̴��ţ�";
			cin>>ID;
			flag = 1; //�Ѿ��鿴
			for (m=0;m<count;m++){
				for (i = CourseInf.begin(); i != CourseInf.end(); ++i){
				if((*i)->getm_nCourseCode() == celected[m]){
					cout<<" �γ̴���:  "<<(*i)->getm_nCourseCode()<<endl;
					cout<<" �γ�����:  "; (*i)->getm_strCourseName();cout<<endl;
					cout<<" �ο���ʦ:  "; (*i)->getm_strname();cout<<endl;
					cout<<" ��ʦ����:  "; (*i)->getm_nJobnumber();cout<<endl;
					cout<<" �γ̵ص�:  "; (*i)->getm_strCoursePlace();cout<<endl;
					cout<<" �γ�ʱ�䣺 "; (*i)->getm_strCourseTime();cout<<endl;
					cout<<" �γ�ѧ��:  "; (*i)->getm_nCourseCredit();cout<<endl;
					isIdExist = 1; 
					break;
				}
			}
		}
		}else if(choice == 'n' || choice == 'N'){
			break;
		}else{
			fflush(stdin);
			cout<<"����������������룺";
			cin>>choice;
		}
		if(flag && !isIdExist){
			cout<<"�γ̲�����"<<endl;
			break; 
		}
		if(flag){
			cout<<"�Ƿ�����鿴�γ���ϸ��Ϣ��Y/N����";
			cin>>choice;
		}
	}
} 
//��������
void Student::getm_StuName(){
	cout<<m_StuName;
} 
//����ѧ��
int Student::getm_StuNumber(){
	return m_StuNumber;
} 
//���ذ༶ 
void Student::getm_StuClass(){
	cout<<m_StuClass;
}


//����ѧ����Ϣ 

//vector<Student*>  StudentInf;


//��ӿγ���Ϣ 
void Manager:: addCouInf(){
	int index = 0;
	Course cou;
	Course *p = new Course;
	vector<Course*> :: iterator i;
	int IsCourseExist = 0;
	cou.setm_nCourseCode();
	//*p = cou;
	if(CourseInf.empty()){
		cou.setm_strCourseName();
		cou.setm_strname();
		cou.setm_nJobnumber();
		cou.setm_nCourseCredit();
		cou.setm_strCourseTime();
		cou.setm_strCoursePlace();
		*p = cou;
		CourseInf.push_back(p);
		IsCourseExist = 1;
	}else{
		for (i = CourseInf.begin(); i != CourseInf.end(); ++i){
			if((*i)->getm_nCourseCode()==cou.getm_nCourseCode()){
				IsCourseExist = 1;
				delete p;
				break;
			}
		}
		for (i = CourseInf.begin(); i != CourseInf.end(); ++i){
			if((*i)->getm_nCourseCode() > cou.getm_nCourseCode()) break;
			index++;
		}
		
	
		if(! IsCourseExist){
			cou.setm_strCourseName();
			cou.setm_strname();
			cou.setm_nJobnumber();
			cou.setm_nCourseCredit();
			cou.setm_strCourseTime();
			cou.setm_strCoursePlace();
			*p = cou;
			CourseInf.insert(CourseInf.begin()+index, p);
			pause("��ʾ����ӳɹ��������������...");
		}else{
			pause("�ÿγ���Ϣ�Ѵ��ڣ������ظ���ӣ������������...");
		}
	}
	UpdateCouFile();
}

//ɾ���γ���Ϣ
void Manager::deletCouInf() {
	int ID;
	vector<Course*> ::iterator i;
	int isIdExist = 0;
	cout<<"����������Ҫɾ���Ŀγ̴���:";
	cin>>ID;
	for (i = CourseInf.begin(); i != CourseInf.end(); ++i){
		if((*i)-> getm_nCourseCode()== ID){
			isIdExist = 1;
			delete (*i);
			CourseInf.erase(i);
			UpdateCouFile();
			pause("ɾ���ɹ�"); 
			break;
		}
	}
	if( ! isIdExist){
		pause("�ÿγ̲�����!");
	}
} 

//�޸Ŀγ�
void Manager::alterCouInf(){
	int ID;
	Course cou;
	vector<Course*>:: iterator i;
	int isIdExist = 0;
	cout<<"����������Ҫ�޸ĵĿγ̴���:";
	cin>>ID;
	for (i = CourseInf.begin(); i != CourseInf.end(); ++i){
		if((*i)->getm_nCourseCode() == ID){
			cout<<"�������µĿγ���Ϣ:"<<endl;
			cout<<"�������޸Ĵ���Ϊ"<<ID<<"�Ŀγ�"<<endl;
			(*i)->setm_strCourseName();
			(*i)->setm_strname();
			(*i)->setm_nJobnumber();
			(*i)->setm_nCourseCredit();
			(*i)->setm_strCourseTime();
			(*i)->setm_strCoursePlace();
			UpdateCouFile();
			isIdExist = 1;
			pause("�޸ĳɹ�");
		}
	}
	if( ! isIdExist){
		pause("�ÿγ̲�����!");
	}
	fflush(stdin);
} 

//չʾ���еĿγ���Ϣ
void Manager::displayCouInf(){
	int flag = 0;
	int count = 0;
	int ID;
	char choice;
	int isIdExist = 0;
	vector<Course*> :: iterator i;
	cout<<"------���еĿγ���Ϣ����------"<<endl;
	cout<<" �γ̴���"<<setw(30)<<" ���� "<<endl;
	for (i = CourseInf.begin(); i != CourseInf.end(); ++i){
		count++;
		cout<<" "<<setw(4)<<*right<<(*i)->getm_nCourseCode();
		cout<<setw(30)<<" "<<*right;
		(*i)->getm_strCourseName();
		cout<<endl; 
	}
	cout<<"\n����"<<count<<"���γ���Ϣ"<<endl;
	cout<<endl;
	cout<<"�Ƿ�鿴�γ���ϸ��Ϣ��Y/N����";
	cin>> choice;
	while(1){
		if(choice == 'Y'|| choice =='y'){
			cout<<"����������Ҫ�鿴�Ŀγ̴��ţ�";
			cin>>ID;
			flag = 1; //�Ѿ��鿴
			for (i = CourseInf.begin(); i != CourseInf.end(); ++i){
				if((*i)->getm_nCourseCode() == ID){
					cout<<" �γ̴���:  "<<(*i)->getm_nCourseCode()<<endl;
					cout<<" �γ�����:  "; (*i)->getm_strCourseName();cout<<endl;
					cout<<" �ο���ʦ:  "; (*i)->getm_strname();cout<<endl;
					cout<<" ��ʦ����:  "; (*i)->getm_nJobnumber();cout<<endl;
					cout<<" �γ̵ص�:  "; (*i)->getm_strCoursePlace();cout<<endl;
					cout<<" �γ�ʱ�䣺 "; (*i)->getm_strCourseTime();cout<<endl;
					cout<<" �γ�ѧ��:  "; (*i)->getm_nCourseCredit();cout<<endl;
					isIdExist = 1; 
					break;
				}
			}
		}else if(choice == 'n' || choice == 'N'){
			break;
		}else{
			fflush(stdin);
			cout<<"����������������룺";
			cin>>choice;
		}
		if(flag && !isIdExist){
			cout<<"�γ̲�����"<<endl; 
		}
		if(flag){
			cout<<"�Ƿ�����鿴�γ���ϸ��Ϣ��Y/N����";
			cin>>choice;
		}
	}
	pause("�����������..."); 
}
//���ѧ����Ϣ 
void Manager::addStuInf(){
	int index = 0;
	Student stu;
	Student *p = new Student;
	vector<Student*> :: iterator i;
	int IsStudentExist = 0;
	stu.setm_StuNumber();
	//*p = cou;
	if(StudentInf.empty()){
		stu.setm_StuName();
		stu.setm_StuClass();
		*p = stu;
		StudentInf.push_back(p);
		IsStudentExist = 1;
		pause("��ʾ����ӳɹ��������������...");
	}else{
		for (i = StudentInf.begin(); i != StudentInf.end(); ++i){
			if((*i)->getm_StuNumber()==stu.getm_StuNumber()){
				IsStudentExist = 1;
				delete p;
				break;
			}
		}
		for (i = StudentInf.begin(); i != StudentInf.end(); ++i){
			if((*i)->getm_StuNumber() > stu.getm_StuNumber()) break;
			index++;
		}
		
	
		if(! IsStudentExist){
			stu.setm_StuName();
			stu.setm_StuClass();
			*p = stu;
			StudentInf.insert(StudentInf.begin()+index, p);
			pause("��ʾ����ӳɹ��������������...");
		}else{
			pause("��ѧ����Ϣ�Ѵ��ڣ������ظ���ӣ������������...");
		}
	}
	UpdateStuFile();
}
//ɾ��ѧ����Ϣ
void Manager::deletStuInf() {
	long long ID;
	vector<Student*> ::iterator i;
	int isIdExist = 0;
	cout<<"����������Ҫɾ����ѧ��ѧ��:";
	cin>>ID;
	for (i = StudentInf.begin(); i != StudentInf.end(); ++i){
		if((*i)-> getm_StuNumber()== ID%1000){
			isIdExist = 1;
			delete (*i);
			StudentInf.erase(i);
			UpdateStuFile();
			pause("ɾ���ɹ�"); 
			break;
		}
	}
	if( ! isIdExist){
		pause("��ѧ��������!");
	}
} 

//�޸�ѧ����Ϣ 
void Manager::alterStuInf(){
	long long ID;
	Student stu;
	vector<Student*>:: iterator i;
	int isIdExist = 0;
	cout<<"����������Ҫ�޸ĵ�ѧ��ѧ��:";
	cin>>ID;
	for (i = StudentInf.begin(); i != StudentInf.end(); ++i){
		if((*i)->getm_StuNumber() == ID%1000){
			cout<<"�������µ�ѧ����Ϣ:"<<endl;
			cout<<"�������޸�ѧ��Ϊ"<<ID<<"��ѧ����Ϣ"<<endl;
			(*i)->setm_StuName();
			(*i)->setm_StuClass();
			UpdateStuFile();
			isIdExist = 1;
			pause("�޸ĳɹ�");
		}
	}
	if( ! isIdExist){
		pause("��ѧ��������!");
	}
	fflush(stdin);
}
//չʾ����ѧ����Ϣ
void Manager::displayStuInf(){
	int count = 0;
	vector<Student*> :: iterator i;
	cout<<"--------����ѧ����Ϣ����--------"<<endl;
	cout<<" ѧ��"<<setw(30)<<" ���� "<<setw(19)<<"�༶"<<endl;
	for (i = StudentInf.begin(); i != StudentInf.end(); ++i){
		if((*i)->getm_StuNumber()>=100){
		cout<<"8003119"<<(*i)->getm_StuNumber();
		}else if(100>(*i)->getm_StuNumber()&& (*i)->getm_StuNumber()>=10){
		cout<<"80031190"<<(*i)->getm_StuNumber();
		}else{
		cout<<"800311900"<<(*i)->getm_StuNumber();	
		}
		
		Gotoxy(30, 11+count);
		(*i)->getm_StuName();
		Gotoxy(50, 11+count);
		(*i)->getm_StuClass();
		cout<<endl;
		count++;
	}
	pause("\n����%d��ѧ����Ϣ�������������...", count);
}

// �ļ��࣬������ѧ���Ϳγ���Ϣ�������ļ��� 
fstream ioCouFile;
fstream ioStuFile;


void init(){
	
	Student stu;
	Course cou;
	//��ѧ����Ϣ�ļ�
	ioStuFile.open("stu.data", ios::in | ios::app | ios::binary);
	if(!ioStuFile){
		cout<<"open error"<<endl;
	}

	if(ioStuFile.peek()==EOF){
		StudentInf.reserve(20);
		ioStuFile.clear();
	}else{
		while(ioStuFile.read((char *)&stu, sizeof(Student))){
			Student* p1 = new Student;
			*p1 = stu;
			StudentInf.push_back(p1);
		}
	}
	ioStuFile.close();
	//�򿪿γ���Ϣ�ļ�
	ioCouFile.open("cou.data", ios::in | ios::app | ios::binary);
	if(!ioCouFile){
		cout<<"open error"<<endl;
	}

	if(ioCouFile.peek()==EOF){
		CourseInf.reserve(20);
		ioCouFile.clear();
	}else{
		while(ioCouFile.read((char *)&cou, sizeof(Course))){
			Course* p2 = new Course;
			*p2 = cou;
			CourseInf.push_back(p2);
		}
	}
	ioCouFile.close();
}

//����ѧ����Ϣ�ļ�
void UpdateStuFile(){
	vector<Student*> :: iterator i;
	ioStuFile.open("stu.data", ios::in | ios::out | ios::trunc | ios::binary); //���´��ļ�������ļ��е�����
	for (i = StudentInf.begin(); i != StudentInf.end(); ++i){
		ioStuFile.write((char*)&(**i), sizeof(Student));
	}
	ioStuFile.close();
}
//���¿γ���Ϣ�ļ�
void UpdateCouFile(){
	vector<Course*> :: iterator i;
	ioCouFile.open("cou.data", ios::in | ios::out | ios::trunc | ios::binary); //���´��ļ�������ļ��е�����
	for (i = CourseInf.begin(); i != CourseInf.end(); ++i){
		ioCouFile.write((char*)&(**i), sizeof(Course));
	}
	ioCouFile.close();
}

/**
 * ��ͣ����
 * @param  str  ������ͣʱ��ʾ���ַ��������԰�����ʽ���Ʒ�
 * @param  ...  �䳤����
**/
void pause(const char *str, ...){
	va_list vl;
	char buf[500] = {0};
	va_start(vl, str);
	vsnprintf(buf, 500, str, vl);
	va_end(vl);
	cout<<buf;
	getch();
	cout<<"\n";
}

//���ع��
void HideCursor()
{
    CONSOLE_CURSOR_INFO cursor_info = {1, 0};//��ߵ�0�����겻�ɼ�
    SetConsoleCursorInfo(GetStdHandle(STD_OUTPUT_HANDLE), &cursor_info);
    
}
//���ֹ��
void unHideCursor()
{
    CONSOLE_CURSOR_INFO cursor_info = {1, 1};//��ߵ�0�����겻�ɼ�
    SetConsoleCursorInfo(GetStdHandle(STD_OUTPUT_HANDLE), &cursor_info);
}

//����ƶ�
void Gotoxy(int x, int y)
{
    HANDLE hout; //����������hout
    COORD coord; //����ṹ��coord
    coord.X = x;
    coord.Y = y;
    hout = GetStdHandle(STD_OUTPUT_HANDLE);//��ñ�׼�������Ļ�����
    SetConsoleCursorPosition(hout, coord);//�ƶ����
}


