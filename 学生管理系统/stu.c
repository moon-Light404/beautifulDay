#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <conio.h>
#include "common.h"
#include "stu.h"

//��ʼ��
void init(){
	//���ļ�
	if( (fp=fopen(FILENAME, "rb+")) == NULL && (fp=fopen(FILENAME, "wb+")) == NULL ){
		pause("Error on open %s file!", FILENAME);
		exit(EXIT_FAILURE);
	}

	stuSize = sizeof(STU);
	fileSize = getFileSize(fp);
	stuIndex = NULL;

	updateIndex();
}

//���ѧ����Ϣ
void addStuInfo(){
	STU stu;
	int i, nPreEleCount = 0;

	getStuID(&stu.id);
	getStuName(stu.name);
	getStuSex(stu.sex);
	getStuAge(&stu.age);
	getStuMath(&stu.math);
	getStuCN(&stu.cn);
	getStuEN(&stu.en);

	for(i=0; i<stuCount; i++){
		if(stu.id == stuIndex[i]){
			pause("���󣺸�ѧ����Ϣ�Ѵ��ڣ������ظ���ӣ������������...");
			return;
		}else if(stu.id > stuIndex[i]){
			nPreEleCount++;
		}else{
			break;
		}
	}

	finsert(fp, nPreEleCount*stuSize, &stu, stuSize);
	updateIndex();
	pause("��ʾ����ӳɹ��������������...");
}

//ɾ��ѧ����Ϣ
void deleteStuInfo(){
	STU stu;
	int i, index = -1;

	getStuID(&stu.id);
	for(i=0; i<stuCount; i++){
		if(stu.id == stuIndex[i]){
			index = i;
		}else if(stu.id < stuIndex[i]){
			break;
		}
	}

	if(index<0){
		pause("���󣺸�ѧ����Ϣ�����ڣ�ɾ��ʧ�ܣ������������...");
		return;
	}else{
		fdelete(fp, index*stuSize, stuSize);
	}

	updateIndex();
	pause("��ʾ��ɾ���ɹ��������������...");
}

//�޸�ѧ����Ϣ
void alterStuInfo(){
	STU stu;
	int i, index = -1;

	getStuID(&stu.id);
	for(i=0; i<stuCount; i++){
		if(stu.id == stuIndex[i]){
			index = i;
		}else if(stu.id < stuIndex[i]){
			break;
		}
	}

	if(index<0){
		pause("���󣺸�ѧ����Ϣ�����ڣ��޸�ʧ�ܣ������������...");
		return;
	}else{
		getStuName(stu.name);
		getStuSex(stu.sex);
		getStuAge(&stu.age);
		getStuMath(&stu.math);
		getStuCN(&stu.cn);
		getStuEN(&stu.en);
		fseek(fp, index*stuSize, SEEK_SET);
		fwrite(&stu, stuSize, 1, fp);
	}
	pause("��ʾ���޸ĳɹ��������������...");
}

//����ID��ѯѧ����Ϣ
void findStuByID(){
	STU stu;
	int i, index = -1;
	float total;

	getStuID(&stu.id);
	for(i=0; i<stuCount; i++){
		if(stu.id == stuIndex[i]){
			index = i;
		}else if(stu.id < stuIndex[i]){
			break;
		}
	}
	if(index<0){
		pause("���󣺸�ѧ����Ϣ�����ڣ���ѯʧ�ܣ������������...");
		return;
	}else{
		fseek(fp, stuSize*index, SEEK_SET);
		fread(&stu, stuSize, 1, fp);
		total = stu.math + stu.cn + stu.en;
		printf("-----------------------------------------------------------------------\n");
		printf("  ѧ��  |  ����  |  �Ա�  |  ����  |  ��ѧ  |  ����  |  Ӣ��  | �ܳɼ�\n");
		printf("--------+--------+--------+--------+--------+--------+--------+--------\n");
		printf("   %.2d   | %-6s |   %-3s  |   %-3d  | %-6.2f | %-6.2f | %-6.2f | %-6.2f\n", stu.id, stu.name, stu.sex, stu.age, stu.math, stu.cn, stu.en, total);
		printf("-----------------------------------------------------------------------\n");
		pause("\n�����������...");
	}
}

//����������ѯѧ����Ϣ
void findStuByName(){
	STU stu;
	int n = 0;  //ƥ�䵽����ѧ����¼
	float total;
	char name[20];

	getStuName(name);
	fseek(fp, 0, SEEK_SET);
	while(fread(&stu, stuSize, 1, fp)){
		if(strstr(stu.name, name)){
			n++;
			total = stu.math + stu.cn + stu.en;
			if(n==1){
				printf("-----------------------------------------------------------------------\n");
				printf("  ѧ��  |  ����  |  �Ա�  |  ����  |  ��ѧ  |  ����  |  Ӣ��  | �ܳɼ�\n");
				printf("--------+--------+--------+--------+--------+--------+--------+--------\n");
			}
			printf("   %.2d   | %-6s |   %-3s  |   %-3d  | %-6.2f | %-6.2f | %-6.2f | %-6.2f\n", stu.id, stu.name, stu.sex, stu.age, stu.math, stu.cn, stu.en, total);
		}
	}

	if(n>0){
		printf("-----------------------------------------------------------------------\n");
		pause("\n����ѯ��%d����¼�������������...", n);
	}else if(n==0){
		pause("����û�в�ѯ����ؼ�¼�������������...");
	}
}

//���ݳɼ���ѯѧ����Ϣ
void findStuByScores(int flag){
	STU stu;
	int n = 0;  //ƥ�䵽����ѧ����¼
	float *scores = NULL;  //��ǰѧ���ĳɼ�
	float min = 0, max = 0;  //�û��������߷ֺ���ͷ�
	int MAX = 0;  //common.h ��ָ���ĳɼ���߷�
	char *courseName = NULL;  //��Ŀ����
	float total = 0;  //��ǰѧ���ܷ�

	if(flag == FIND_BY_MATH){
		courseName = "��ѧ�ɼ�";
		MAX = MAX_STU_MATH;
		scores = &stu.math;
	}else if(flag == FIND_BY_CN){
		courseName = "���ĳɼ�";
		MAX = MAX_STU_CN;
		scores = &stu.cn;
	}else if(flag == FIND_BY_EN){
		courseName = "Ӣ��ɼ�";
		MAX = MAX_STU_EN;
		scores = &stu.en;
	}else if(flag == FIND_BY_TOTAL){
		courseName = "�ܳɼ�";
		MAX = MAX_STU_MATH + MAX_STU_CN + MAX_STU_EN;
		scores = &total;
	}else{
		return;
	}

	while(1){
		printf("Ҫ��ѯ��%s�ķ�Χ��", courseName);
		fflush(stdin);
		scanf("%f %f", &min, &max);
		if(min<0 || min>MAX || max<0 || max>MAX){
			pause("����%s��ȡֵ��ΧΪ0~%d�����������������...", courseName, MAX);
			continue;
		}
		if(min>max){
			pause("������߷�Ҫ������ͷ֣����������������...");
			continue;
		}
		break;
	}

	fseek(fp, 0, SEEK_SET);
	while(fread(&stu, stuSize, 1, fp)){
		total = stu.math + stu.cn + stu.en;

		if(min <= *scores && *scores <= max){
			n++;
			if(n==1){
				printf("-----------------------------------------------------------------------\n");
				printf("  ѧ��  |  ����  |  �Ա�  |  ����  |  ��ѧ  |  ����  |  Ӣ��  | �ܳɼ�\n");
				printf("--------+--------+--------+--------+--------+--------+--------+--------\n");
			}
			printf("   %.2d   | %-6s |   %-3s  |   %-3d  | %-6.2f | %-6.2f | %-6.2f | %-6.2f\n", stu.id, stu.name, stu.sex, stu.age, stu.math, stu.cn, stu.en, total);
		}
	}

	if(n>0){
		printf("-----------------------------------------------------------------------\n");
		pause("\n����ѯ��%d����¼�������������...", n);
	}else if(n==0){
		pause("����û�в�ѯ����ؼ�¼�������������...");
	}
}

//��ʾ����ѧ����Ϣ
void showAllStu(){
	STU stu;
	//stuCount = getStuCount();
	float mathTotal = 0, cnTotal = 0, enTotal = 0, ageTotal = 0, totalStu = 0, allTotal = 0;
	int manTotal = 0, womanTotal = 0, n = 0;

	if(!stuCount){
		pause("��δ����κ�ѧ����Ϣ�������������...");
		return;
	}
	fseek(fp, 0, SEEK_SET);
	system("cls");
	printf("-----------------------------------------------------------------------\n");
	printf("  ѧ��  |  ����  |  �Ա�  |  ����  |  ��ѧ  |  ����  |  Ӣ��  | �ܳɼ�\n");
	printf("--------+--------+--------+--------+--------+--------+--------+--------\n");
	while( fread(&stu, stuSize, 1, fp) ){
		totalStu = stu.math + stu.cn + stu.en;
		allTotal += totalStu;
		mathTotal += stu.math;
		cnTotal += stu.cn;
		enTotal += stu.en;
		ageTotal += stu.age;
		n++;
		if(strcmp(stu.sex, "��")){
			womanTotal++;
		}else{
			manTotal++;
		}
		printf("   %.2d   | %-6s |   %-3s  |   %-3d  | %-6.2f | %-6.2f | %-6.2f | %-6.2f\n", stu.id, stu.name, stu.sex, stu.age, stu.math, stu.cn, stu.en, totalStu);
	}
	printf("--------+--------+--------+--------+--------+--------+--------+--------\n");
	printf("   --   |   --   | %2d/%-2d  | %-6.2f | %-6.2f | %-6.2f | %-6.2f | %-6.2f\n", manTotal, womanTotal, ageTotal/stuCount, mathTotal/stuCount, cnTotal/stuCount, enTotal/stuCount, allTotal/stuCount);
	printf("-----------------------------------------------------------------------\n");
	pause("\n����%d��ѧ����Ϣ�������������...", n);
}

//��������
void updateIndex(){
	int i;
	free(stuIndex);
	stuCount = getFileSize(fp)/stuSize;
	stuIndex = (int*)malloc(stuCount*sizeof(int));
	for(i=0; i<stuCount; i++){
		fseek(fp, stuSize*i, SEEK_SET);
		fread(&stuIndex[i], sizeof(int), 1, fp);
	}
}

//����ѧ��ID
void getStuID(int *id){
	while(1){
		printf("����ѧ�ţ�");
		fflush(stdin);
		scanf("%d", id);
		if(checkStuID(*id)){
			break;
		}
	}
}

//����ѧ������
void getStuName(char name[]){
	while(1){
		printf("����������");
		fflush(stdin);
		scanf("%s", name);
		if(checkStuName(name)){
			break;
		}
	}
}

//����ѧ���Ա�
void getStuSex(char sex[]){
	while(1){
		printf("�����Ա�");
		fflush(stdin);
		scanf("%s", sex);
		if(checkStuSex(sex)){
			break;
		}
	}
}

//����ѧ������
void getStuAge(int *age){
	while(1){
		printf("�������䣺");
		fflush(stdin);
		scanf("%d", age);
		if(checkStuAge(*age)){
			break;
		}
	}
}

//������ѧ�ɼ�
void getStuMath(float *math){
	while(1){
		printf("��ѧ�ɼ���");
		fflush(stdin);
		scanf("%f", math);
		if(checkStuMath(*math)){
			break;
		}
	}
}

//�������ĳɼ�
void getStuCN(float *cn){
	while(1){
		printf("���ĳɼ���");
		fflush(stdin);
		scanf("%f", cn);
		if(checkStuCN(*cn)){
			break;
		}
	}
}

//����Ӣ��ɼ�
void getStuEN(float *en){
	while(1){
		printf("Ӣ��ɼ���");
		fflush(stdin);
		scanf("%f", en);
		if(checkStuEN(*en)){
			break;
		}
	}
}

//���ѧ��ID�Ƿ���ȷ
int checkStuID(int stuID){
	if(stuID <= 0 || stuID > MAX_STU_ID){
		printf("����ѧ�ű����Ǵ���0��С�ڵ���%d��������\n", MAX_STU_ID);
		return 0;
	}
	return 1;
}

//���ѧ�������Ƿ���ȷ
int checkStuName(char name[]){
	if(strlen(name) > MAX_STU_NAME){
		printf("�������ֵ���󳤶Ȳ�����%d���ֽڣ�\n", MAX_STU_NAME);
		return 0;
	}
	return 1;
}

//���ѧ���Ա��Ƿ���ȷ
int checkStuSex(char sex[]){
	if(strcmp(sex, "��") && strcmp(sex, "Ů")){
		printf("�����Ա�ֻ�����л�Ů��\n");
		return 0;
	}else{
		return 1;
	}
}

//���ѧ�������Ƿ���ȷ
int checkStuAge(int age){
	if(age <=0 || age > MAX_STU_AGE){
		printf("���������ȡֵ��ΧΪ1~%d��\n", MAX_STU_AGE);
		return 0;
	}
	return 1;
}

//�����ѧ�ɼ��Ƿ���ȷ
int checkStuMath(float math){
	if(math < 0 || math > MAX_STU_MATH){
		printf("������ѧ�ɼ���ȡֵ��ΧΪ0~%d��\n", MAX_STU_MATH);
		return 0;
	}
	return 1;
}

//������ĳɼ��Ƿ���ȷ
int checkStuCN(float cn){
	if(cn < 0 || cn > MAX_STU_CN){
		printf("�������ĳɼ���ȡֵ��ΧΪ0~%d��\n", MAX_STU_CN);
		return 0;
	}
	return 1;
}

//���Ӣ��ɼ��Ƿ���ȷ
int checkStuEN(float en){
	if(en < 0 || en > MAX_STU_EN){
		printf("����Ӣ��ɼ���ȡֵ��ΧΪ0~%d��\n", MAX_STU_EN);
		return 0;
	}
	return 1;
}
