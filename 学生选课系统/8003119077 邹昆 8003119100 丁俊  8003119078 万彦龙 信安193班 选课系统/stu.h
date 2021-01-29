#ifndef _STU_H
#define _STU_H
#include <vector>
#define STUFILENAME "stu.data"
#define COUFILENAME "cou.data"
using namespace std;

//����ʽ�� 
class Check
{   
    public:
	bool checkStuID(long long ID);//���ѧ��ѧ���Ƿ���ȷ 
	int checkcourseCode(int code);//���γ̴����Ƿ���ȷ 
	int checkCreditFormat(int credit);//���ѧ���Ƿ���ȷ 
	int checkcoursejobnumber(int ID);//�����ʦ�����Ƿ���ȷ 
	int checkname(char name[]);//��������Ƿ���ȷ 
	int checkname_1(char name[]);//��������Ƿ���ȷ 
};

//ѧ���� 
class Student:public Check{
	private:
	char m_StuName[30]; //���� 
	int m_StuNumber;  //ѧ�ţ�����8003119XXX��
	char m_StuClass[30]; //�༶
	int  m_SelectedCourse[5]; //��ѡ�γ̣����5�ţ�,����γ̴���
	public:
		Student();
		void select_courses(); //ѡ��
		void quit_course(); //�˿�
		void show_selectedcourse(); //չʾ��ѡ��Ŀγ�
		void getm_StuName();//����ѧ������ 
		int getm_StuNumber();//����ѧ��ѧ�� 
		void getm_StuClass();//����ѧ���༶ 
		void setm_StuName();//����ѧ������ 
		void setm_StuNumber();//����ѧ��ѧ�� 
		void setm_StuClass();//����ѧ���༶ 
};


//�γ��� 
class Course:public Check{
	private:
		int m_nJobnumber; //���� 
		char m_strname[30]; //����	
		int m_nCourseCode; //�γ̴���
		char m_strCourseName[50]; //�γ�����
		int m_nCourseCredit; //�γ�ѧ��
		char m_strCourseTime[50]; //�Ͽ�ʱ��
		char m_strCoursePlace[50]; //�Ͽεص�
	public:
			Course();
			void getm_nJobnumber();//�����ʦ���� 
			void getm_strname();//�����ʦ���� 
			int getm_nCourseCode();//��ÿγ̴��� 
			void getm_strCourseName();//��ÿγ����� 
			void getm_nCourseCredit();//��ÿγ�ѧ�� 
			void getm_strCoursePlace();//��ÿγ����� 
			void getm_strCourseTime();//��ÿγ�ʱ�� 
			void setm_nJobnumber();//������ʦ���� 
			void setm_strname();//������ʦ���� 
			void setm_nCourseCode();//���ÿγ̴��� 
			void setm_strCourseName();//���ÿγ����� 
			void setm_nCourseCredit();//���ÿγ�ѧ�� 
			void setm_strCoursePlace();//���ÿγ̵ص� 
			void setm_strCourseTime();		//���ÿγ����� 
};

//����Ա�� 
class Manager{
	public:
		void addStuInf();//���ѧ����Ϣ 
		void deletStuInf();//ɾ��ѧ����Ϣ 
		void alterStuInf();//�޸�ѧ����Ϣ
		void displayStuInf();//չʾ����ѧ����Ϣ 
		void addCouInf();//��ӿγ���Ϣ 
		void deletCouInf();//ɾ���γ���Ϣ 
		void alterCouInf();//�޸Ŀγ���Ϣ 
		void displayCouInf();//չʾ���пγ���Ϣ 
};

//���ع�� 
extern void HideCursor();
//���ֹ�� 
extern void unHideCursor();
//���ƹ��λ�� 
extern void Gotoxy(int x, int y);
//��ʼ��
extern void init();
//����ѧ����Ϣ�ļ�
extern void UpdateStuFile();
//���¿γ���Ϣ�ļ�
extern void UpdateCouFile();
//��ͣ����
extern void pause(const char *str, ...);
extern Student* user;
//�����������������������е�ѧ���Ϳγ���Ϣ 
extern vector<Student*>  StudentInf;
extern vector<Course*> CourseInf;
//����һ��check����
extern Student* user;


#endif
