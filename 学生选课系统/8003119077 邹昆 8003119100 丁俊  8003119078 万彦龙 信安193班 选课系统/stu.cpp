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
//定义一个check对象

//extern Check check;  

//检查学号格式是否正确 
bool Check::checkStuID(long long ID)
{
	long long  id = ID/1000;
	if(id == 8003119){
	return true;
	}
	return false;
}
//检查课程代号 
int Check::checkcourseCode(int code)
{
	int flag=0;
	if(code>=1 && code<100)
	flag=1;
	return flag; //结果为1表示格式均正确，0表示格式错误 
}
//检查学分 
int Check::checkCreditFormat(int credit)
{
	int flag=0;
	if(credit>=1 && credit<=10)
	flag=1;
	return flag;
}
//检查工号 
int Check::checkcoursejobnumber(int ID){
	int flag = 0;
	if(ID>0 &&ID <100) flag = 1;
	return flag;
}
//检查姓名 
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

//定义一个check对象

//Check check;


Course::Course(){
	m_nCourseCode = 0;
}
//输入工号 
void Course::setm_nJobnumber(){
	int number;
	cout<<"请输入任课老师的工号（1-100）：";
	cin>>number;
	while(1){
		if(checkcoursejobnumber(number)){
			m_nJobnumber = number;
			break;
		}else{
			cout<<"请输入一个大于1小于100的数:"; 
			fflush(stdin);
			cin>>number;
		}
	}
	cout<<endl;
}
//输入姓名 
void Course::setm_strname(){
	char name[30];
	cout<<"请输入老师的姓名:";
	cin>>name;
	while(1){
		if(checkname(name)){
			strcpy(m_strname, name);
			break;
		}else{
			cout<<"错误：名字的最大长度不超过15个字节,请重新输入:";
			fflush(stdin);
			cin>>name;
		}
	}
	cout<<endl;
}
//输入课程代号
void Course::setm_nCourseCode() {
	int code;
	cout<<"请输入课程代号（1-99）:";
	cin>>code;
	while(1){
		if(checkcourseCode(code)){
			m_nCourseCode = code;
			break;
		}else{
			cout<<"请输入一个大于0小于100的数:";
			fflush(stdin);
			cin>>code; 
		}
	}
	cout<<endl;
}
//输入课程姓名 
void Course::setm_strCourseName(){
	char name[50];
	cout<<"请输入课程名称:";
	cin>>name;
	while(1){
		if(checkname_1(name)){
			strcpy(m_strCourseName, name);
			break;
		}else{
			cout<<"错误：名字的最大长度不超过35个字节,请重新输入:";
			fflush(stdin);
			cin>>name;
		}
	}
	cout<<endl;
}
//课程学分 
void Course::setm_nCourseCredit(){
	int number;
	cout<<"请输入课程学分（1-10）：";
	cin>>number;
	while(1){
		if(checkCreditFormat(number)){
			m_nCourseCredit = number;
			break;
		}else{
			cout<<"请输入一个大于1小于10的数:"; 
			fflush(stdin);
			cin>>number;
		}
	}
	cout<<endl;
} 
//课程地点 
void Course::setm_strCoursePlace(){
	char name[50];
	cout<<"请输入课程地点:";
	cin>>name;
	while(1){
		if(checkname_1(name)){
			strcpy(m_strCoursePlace, name);
			break;
		}else{
			cout<<"错误：地点名字的最大长度不超过35个字节,请重新输入:";
			fflush(stdin);
			cin>>name;
		}
	}
	cout<<endl;
} 
//课程时间
 void Course::setm_strCourseTime(){
 	char time[50];
	cout<<"请输入课程时间:";
	cin>>time;
	while(1){
		if(checkname_1(time)){
			strcpy(m_strCourseTime, time);
			break;
		}else{
			cout<<"错误：时间的最大长度不超过35个字节,请重新输入:";
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
	    //返回姓名 
void Course::getm_strname()
		{
			cout<<m_strname;
		}
		//返回课程代号
int Course::getm_nCourseCode()
		 {
		 	return m_nCourseCode;
		 }
		//返回课程名称 
void Course::getm_strCourseName()
		{
       		cout<<m_strCourseName; 
		}
		 //返回 课程学分  
void Course::getm_nCourseCredit()
		{
			cout<<m_nCourseCredit;
		}
		 //返回上课地点 
void Course::getm_strCoursePlace()
		{
			cout<<m_strCoursePlace;
		}
		 //返回上课时间
void Course::getm_strCourseTime()
		{
			cout<<m_strCourseTime;
		}

//存储课程信息
//vector<Course*> CourseInf;  

Student::Student(){
	int i = 0;
	for(;i<5;i++){
		m_SelectedCourse[i] = 0;
	}
}
//输入姓名 
void Student::setm_StuName(){
	char name[30];
	cout<<"请输入学生的姓名:";
	cin>>name;
	while(1){
		if(checkname(name)){
			strcpy(m_StuName, name);
			break;
		}else{
			fflush(stdin);
			cout<<"错误：名字的最大长度不超过15个字节,请重新输入:";
			cin>>name;
		}
	}
	cout<<endl;
}

//输入学号 
void Student::setm_StuNumber(){
	long long number;
	cout<<"请输入你的学号(8003119XXX):";
	cin>>number;
	while(1){
		if(checkStuID(number)){
			m_StuNumber= number % 1000;
			break;
		}else{
			
			cout<<"格式错误，请重新输入:";
			 fflush(stdin);
			cin>>number;
		}
	}
	cout<<endl;
}

//输入班级 
void Student::setm_StuClass(){
	char cla[30];
	cout<<"请输入该学生的班级:";
	cin>>cla;
	while(1){
		if(checkname_1(cla)){
			strcpy(m_StuClass, cla);
			break;
		}else{
			cout<<"错误：班级的最大长度不超过35个字节,请重新输入:";
			fflush(stdin);
			cin>>cla;
		}
	}
	cout<<endl;
}
//选择课程 
void Student::select_courses()
	{  
	int id;
	int count = 0;
	int isCourseExist = 0;
	bool flag = false;
	bool flag2 = false; // 判断是否满课 
	vector<Course*>:: iterator i;
	int j;
	cout<<"------所有的课程信息如下------"<<endl;
	cout<<" 课程代号"<<setw(30)<<" 名称 "<<endl;
	for (i = CourseInf.begin(); i != CourseInf.end(); ++i){
		count++;
		cout<<" "<<setw(4)<<*right<<(*i)->getm_nCourseCode();
		cout<<setw(30)<<" "<<*right;
		(*i)->getm_strCourseName();
		cout<<endl; 
	}
	cout<<"\n共有"<<count<<"条课程信息"<<endl;;
	cout<<"请输入你要选择的课程代号(1--100):";
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
						cout<<"你已选择此课程";
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
			pause("该课程不存在,按任意键返回......");
			break;
	}
	}else{
		cout<<"错误，代号范围在1-100！请重新输入：";
		fflush(stdin);
		cin>>id;
	}
	if(flag){
		pause("选课成功！按任意键");
		break; 
	}
	if(flag2){
		pause("你已经选择5门课程！");
		break; 
	}
	}

}

//退课
 void Student::quit_course()
{
	int id;
	int i;
	int flag = 1;//判断是否选课 
	int flag2 = 0;
	if(m_SelectedCourse[0]==0){
		flag = 0;
	}
	if(flag){
		cout<<"你选择的课程如下："<<endl;
		for(i = 0;i<5;i++){
		if(m_SelectedCourse[i] != 0)
			cout<<m_SelectedCourse[i]<<endl;
	}
	}else{
		cout<<"你还未开始选课!";
	}
	
	cout<<"请输入你要退的课程代号：";
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
				pause("您未选择此课程！,按任意键继续");
				break;
				}				
		}else{
			cout<<"错误，代号范围在1-100！请重新输入：";
			fflush(stdin);
			cin>>id;
		}
		if(flag2)
		pause("退课成功！");
		break;
	}
	
}

//展示所选课程
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
	cout<<"------所选课程信息如下------"<<endl;
	cout<<" 课程代号"<<setw(30)<<" 名称 "<<endl;
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
	cout<<"\n共有"<<count<<"条选课信息"<<endl;
	cout<<"是否查看课程详细信息（Y/N）：";
	cin>> choice;
	while(1){
		if(choice == 'Y'|| choice =='y'){
			cout<<"请输入你需要查看的课程代号：";
			cin>>ID;
			flag = 1; //已经查看
			for (m=0;m<count;m++){
				for (i = CourseInf.begin(); i != CourseInf.end(); ++i){
				if((*i)->getm_nCourseCode() == celected[m]){
					cout<<" 课程代号:  "<<(*i)->getm_nCourseCode()<<endl;
					cout<<" 课程名称:  "; (*i)->getm_strCourseName();cout<<endl;
					cout<<" 任课老师:  "; (*i)->getm_strname();cout<<endl;
					cout<<" 老师工号:  "; (*i)->getm_nJobnumber();cout<<endl;
					cout<<" 课程地点:  "; (*i)->getm_strCoursePlace();cout<<endl;
					cout<<" 课程时间： "; (*i)->getm_strCourseTime();cout<<endl;
					cout<<" 课程学分:  "; (*i)->getm_nCourseCredit();cout<<endl;
					isIdExist = 1; 
					break;
				}
			}
		}
		}else if(choice == 'n' || choice == 'N'){
			break;
		}else{
			fflush(stdin);
			cout<<"输入错误，请重新输入：";
			cin>>choice;
		}
		if(flag && !isIdExist){
			cout<<"课程不存在"<<endl;
			break; 
		}
		if(flag){
			cout<<"是否继续查看课程详细信息（Y/N）：";
			cin>>choice;
		}
	}
} 
//返回名字
void Student::getm_StuName(){
	cout<<m_StuName;
} 
//返回学号
int Student::getm_StuNumber(){
	return m_StuNumber;
} 
//返回班级 
void Student::getm_StuClass(){
	cout<<m_StuClass;
}


//储存学生信息 

//vector<Student*>  StudentInf;


//添加课程信息 
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
			pause("提示：添加成功！按任意键返回...");
		}else{
			pause("该课程信息已存在，无需重复添加！按任意键返回...");
		}
	}
	UpdateCouFile();
}

//删除课程信息
void Manager::deletCouInf() {
	int ID;
	vector<Course*> ::iterator i;
	int isIdExist = 0;
	cout<<"请输入你需要删除的课程代号:";
	cin>>ID;
	for (i = CourseInf.begin(); i != CourseInf.end(); ++i){
		if((*i)-> getm_nCourseCode()== ID){
			isIdExist = 1;
			delete (*i);
			CourseInf.erase(i);
			UpdateCouFile();
			pause("删除成功"); 
			break;
		}
	}
	if( ! isIdExist){
		pause("该课程不存在!");
	}
} 

//修改课程
void Manager::alterCouInf(){
	int ID;
	Course cou;
	vector<Course*>:: iterator i;
	int isIdExist = 0;
	cout<<"请输入你需要修改的课程代号:";
	cin>>ID;
	for (i = CourseInf.begin(); i != CourseInf.end(); ++i){
		if((*i)->getm_nCourseCode() == ID){
			cout<<"请输入新的课程信息:"<<endl;
			cout<<"您正在修改代号为"<<ID<<"的课程"<<endl;
			(*i)->setm_strCourseName();
			(*i)->setm_strname();
			(*i)->setm_nJobnumber();
			(*i)->setm_nCourseCredit();
			(*i)->setm_strCourseTime();
			(*i)->setm_strCoursePlace();
			UpdateCouFile();
			isIdExist = 1;
			pause("修改成功");
		}
	}
	if( ! isIdExist){
		pause("该课程不存在!");
	}
	fflush(stdin);
} 

//展示所有的课程信息
void Manager::displayCouInf(){
	int flag = 0;
	int count = 0;
	int ID;
	char choice;
	int isIdExist = 0;
	vector<Course*> :: iterator i;
	cout<<"------所有的课程信息如下------"<<endl;
	cout<<" 课程代号"<<setw(30)<<" 名称 "<<endl;
	for (i = CourseInf.begin(); i != CourseInf.end(); ++i){
		count++;
		cout<<" "<<setw(4)<<*right<<(*i)->getm_nCourseCode();
		cout<<setw(30)<<" "<<*right;
		(*i)->getm_strCourseName();
		cout<<endl; 
	}
	cout<<"\n共有"<<count<<"条课程信息"<<endl;
	cout<<endl;
	cout<<"是否查看课程详细信息（Y/N）：";
	cin>> choice;
	while(1){
		if(choice == 'Y'|| choice =='y'){
			cout<<"请输入你需要查看的课程代号：";
			cin>>ID;
			flag = 1; //已经查看
			for (i = CourseInf.begin(); i != CourseInf.end(); ++i){
				if((*i)->getm_nCourseCode() == ID){
					cout<<" 课程代号:  "<<(*i)->getm_nCourseCode()<<endl;
					cout<<" 课程名称:  "; (*i)->getm_strCourseName();cout<<endl;
					cout<<" 任课老师:  "; (*i)->getm_strname();cout<<endl;
					cout<<" 老师工号:  "; (*i)->getm_nJobnumber();cout<<endl;
					cout<<" 课程地点:  "; (*i)->getm_strCoursePlace();cout<<endl;
					cout<<" 课程时间： "; (*i)->getm_strCourseTime();cout<<endl;
					cout<<" 课程学分:  "; (*i)->getm_nCourseCredit();cout<<endl;
					isIdExist = 1; 
					break;
				}
			}
		}else if(choice == 'n' || choice == 'N'){
			break;
		}else{
			fflush(stdin);
			cout<<"输入错误，请重新输入：";
			cin>>choice;
		}
		if(flag && !isIdExist){
			cout<<"课程不存在"<<endl; 
		}
		if(flag){
			cout<<"是否继续查看课程详细信息（Y/N）：";
			cin>>choice;
		}
	}
	pause("按任意键返回..."); 
}
//添加学生信息 
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
		pause("提示：添加成功！按任意键返回...");
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
			pause("提示：添加成功！按任意键返回...");
		}else{
			pause("该学生信息已存在，无需重复添加！按任意键返回...");
		}
	}
	UpdateStuFile();
}
//删除学生信息
void Manager::deletStuInf() {
	long long ID;
	vector<Student*> ::iterator i;
	int isIdExist = 0;
	cout<<"请输入你需要删除的学生学号:";
	cin>>ID;
	for (i = StudentInf.begin(); i != StudentInf.end(); ++i){
		if((*i)-> getm_StuNumber()== ID%1000){
			isIdExist = 1;
			delete (*i);
			StudentInf.erase(i);
			UpdateStuFile();
			pause("删除成功"); 
			break;
		}
	}
	if( ! isIdExist){
		pause("该学生不存在!");
	}
} 

//修改学生信息 
void Manager::alterStuInf(){
	long long ID;
	Student stu;
	vector<Student*>:: iterator i;
	int isIdExist = 0;
	cout<<"请输入你需要修改的学生学号:";
	cin>>ID;
	for (i = StudentInf.begin(); i != StudentInf.end(); ++i){
		if((*i)->getm_StuNumber() == ID%1000){
			cout<<"请输入新的学生信息:"<<endl;
			cout<<"您正在修改学号为"<<ID<<"的学生信息"<<endl;
			(*i)->setm_StuName();
			(*i)->setm_StuClass();
			UpdateStuFile();
			isIdExist = 1;
			pause("修改成功");
		}
	}
	if( ! isIdExist){
		pause("该学生不存在!");
	}
	fflush(stdin);
}
//展示所有学生信息
void Manager::displayStuInf(){
	int count = 0;
	vector<Student*> :: iterator i;
	cout<<"--------所有学生信息如下--------"<<endl;
	cout<<" 学号"<<setw(30)<<" 名字 "<<setw(19)<<"班级"<<endl;
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
	pause("\n共有%d条学生信息，按任意键返回...", count);
}

// 文件类，用来将学生和课程信息保存在文件中 
fstream ioCouFile;
fstream ioStuFile;


void init(){
	
	Student stu;
	Course cou;
	//打开学生信息文件
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
	//打开课程信息文件
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

//更新学生信息文件
void UpdateStuFile(){
	vector<Student*> :: iterator i;
	ioStuFile.open("stu.data", ios::in | ios::out | ios::trunc | ios::binary); //重新打开文件并清空文件中的数据
	for (i = StudentInf.begin(); i != StudentInf.end(); ++i){
		ioStuFile.write((char*)&(**i), sizeof(Student));
	}
	ioStuFile.close();
}
//更新课程信息文件
void UpdateCouFile(){
	vector<Course*> :: iterator i;
	ioCouFile.open("cou.data", ios::in | ios::out | ios::trunc | ios::binary); //重新打开文件并清空文件中的数据
	for (i = CourseInf.begin(); i != CourseInf.end(); ++i){
		ioCouFile.write((char*)&(**i), sizeof(Course));
	}
	ioCouFile.close();
}

/**
 * 暂停程序
 * @param  str  程序暂停时显示的字符串，可以包含格式控制符
 * @param  ...  变长参数
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

//隐藏光标
void HideCursor()
{
    CONSOLE_CURSOR_INFO cursor_info = {1, 0};//后边的0代表光标不可见
    SetConsoleCursorInfo(GetStdHandle(STD_OUTPUT_HANDLE), &cursor_info);
    
}
//显现光标
void unHideCursor()
{
    CONSOLE_CURSOR_INFO cursor_info = {1, 1};//后边的0代表光标不可见
    SetConsoleCursorInfo(GetStdHandle(STD_OUTPUT_HANDLE), &cursor_info);
}

//光标移动
void Gotoxy(int x, int y)
{
    HANDLE hout; //定义句柄变量hout
    COORD coord; //定义结构体coord
    coord.X = x;
    coord.Y = y;
    hout = GetStdHandle(STD_OUTPUT_HANDLE);//获得标准输出（屏幕）句柄
    SetConsoleCursorPosition(hout, coord);//移动光标
}


