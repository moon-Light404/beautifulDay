#ifndef _STU_H
#define _STU_H

#include "common.h"

#define FIND_BY_MATH 1
#define FIND_BY_CN 2
#define FIND_BY_EN 3
#define FIND_BY_TOTAL 4

FILE *fp;  //�ļ�ָ��
int stuSize;  //һ��ѧ����Ϣ�ĳ��ȣ��ֽ�����
int stuCount;  //�ܹ��ж�����ѧ����Ϣ
long fileSize;  //�ļ����ȣ�ռ�õ��ֽ�����
int *stuIndex;  //ѧ����Ϣ����

//ѧ����Ϣ�ṹ��
typedef struct _STU{
	int id;  //ѧ��
	char name[20];  //����
	char sex[4];  //�Ա�
	int age;  //����
	float math;  //��ѧ�ɼ�
	float cn;  //���ĳɼ�
	float en;  //Ӣ��ɼ�
}STU;

//��ʼ��
extern void init();

//ѧ����Ϣ��ɾ�Ĳ�
extern void addStuInfo();
extern void deleteStuInfo();
extern void alterStuInfo();
extern void findStuByID();
extern void findStuByName();
extern void findStuByScores(int flag);
extern void showAllStu();

//��������
extern void updateIndex();

//У��ѧ����Ϣ
extern int checkStuID(int stuID);
extern int checkStuName(char name[]);
extern int checkStuSex(char sex[]);
extern int checkStuAge(int age);
extern int checkStuMath(float math);
extern int checkStuCN(float cn);
extern int checkStuEN(float en);

//����ѧ����Ϣ
extern void getStuID(int *id);
extern void getStuName(char name[]);
extern void getStuSex(char sex[]);
extern void getStuAge(int *age);
extern void getStuMath(float *math);
extern void getStuCN(float *cn);
extern void getStuEN(float *en);

#endif
