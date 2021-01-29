#ifndef _STU_H
#define _STU_H
#include <vector>
#define STUFILENAME "stu.data"
#define COUFILENAME "cou.data"
using namespace std;

//检查格式类 
class Check
{   
    public:
	bool checkStuID(long long ID);//检查学生学号是否正确 
	int checkcourseCode(int code);//检查课程代号是否正确 
	int checkCreditFormat(int credit);//检查学分是否正确 
	int checkcoursejobnumber(int ID);//检查老师工号是否正确 
	int checkname(char name[]);//检查名字是否正确 
	int checkname_1(char name[]);//检查名字是否正确 
};

//学生类 
class Student:public Check{
	private:
	char m_StuName[30]; //姓名 
	int m_StuNumber;  //学号（例如8003119XXX）
	char m_StuClass[30]; //班级
	int  m_SelectedCourse[5]; //所选课程（最多5门）,存入课程代号
	public:
		Student();
		void select_courses(); //选课
		void quit_course(); //退课
		void show_selectedcourse(); //展示已选择的课程
		void getm_StuName();//返回学生姓名 
		int getm_StuNumber();//返回学生学号 
		void getm_StuClass();//返回学生班级 
		void setm_StuName();//设置学生姓名 
		void setm_StuNumber();//设置学生学号 
		void setm_StuClass();//设置学生班级 
};


//课程类 
class Course:public Check{
	private:
		int m_nJobnumber; //工号 
		char m_strname[30]; //姓名	
		int m_nCourseCode; //课程代号
		char m_strCourseName[50]; //课程名称
		int m_nCourseCredit; //课程学分
		char m_strCourseTime[50]; //上课时间
		char m_strCoursePlace[50]; //上课地点
	public:
			Course();
			void getm_nJobnumber();//获得老师工号 
			void getm_strname();//获得老师名字 
			int getm_nCourseCode();//获得课程代号 
			void getm_strCourseName();//获得课程姓名 
			void getm_nCourseCredit();//获得课程学分 
			void getm_strCoursePlace();//获得课程名字 
			void getm_strCourseTime();//获得课程时间 
			void setm_nJobnumber();//设置老师工号 
			void setm_strname();//设置老师姓名 
			void setm_nCourseCode();//设置课程代号 
			void setm_strCourseName();//设置课程名字 
			void setm_nCourseCredit();//设置课程学分 
			void setm_strCoursePlace();//设置课程地点 
			void setm_strCourseTime();		//设置课程名字 
};

//管理员类 
class Manager{
	public:
		void addStuInf();//添加学生信息 
		void deletStuInf();//删除学生信息 
		void alterStuInf();//修改学生信息
		void displayStuInf();//展示所有学生信息 
		void addCouInf();//添加课程信息 
		void deletCouInf();//删除课程信息 
		void alterCouInf();//修改课程信息 
		void displayCouInf();//展示所有课程信息 
};

//隐藏光标 
extern void HideCursor();
//显现光标 
extern void unHideCursor();
//控制光标位置 
extern void Gotoxy(int x, int y);
//初始化
extern void init();
//更新学生信息文件
extern void UpdateStuFile();
//更新课程信息文件
extern void UpdateCouFile();
//暂停程序
extern void pause(const char *str, ...);
extern Student* user;
//定义两个总容器，保存所有的学生和课程信息 
extern vector<Student*>  StudentInf;
extern vector<Course*> CourseInf;
//定义一个check对象
extern Student* user;


#endif
