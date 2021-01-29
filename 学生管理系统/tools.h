#ifndef _TOOLS_H
#define _TOOLS_H
#include <stdio.h>
#include "common.h"

extern long getFileSize(FILE *fp);  //��ȡ�ļ���С
extern long fcopy(FILE *fSource, long offsetSource, long len, FILE *fTarget, long offsetTarget);  //�ļ����ݸ���
extern int finsert(FILE *fp, long offset, void *buffer, int len);  //���ļ��в�������
extern int fdelete(FILE *fp, long offset, int len);  //ɾ���ļ�����
extern void pause(const char *str, ...);  //��ͣ����

#endif
