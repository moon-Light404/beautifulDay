#include <math.h>
#include <conio.h>
#include <stdarg.h>
#include "tools.h"

//��ȡ�ļ���С�����ֽڼƣ�
long getFileSize(FILE *fp){
	long fsize;
	fpos_t fpos;  //��ǰλ��
	fgetpos(fp, &fpos);  //��ȡ��ǰλ��
	fseek(fp, 0, SEEK_END);
	fsize = ftell(fp);
	fsetpos(fp,&fpos);  //�ָ�֮ǰ��λ��

	return fsize;
}

/**
 * �ļ����ƺ���
 * @param  fSource       Ҫ���Ƶ�ԭ�ļ�
 * @param  offsetSource  ԭ�ļ���λ��ƫ�ƣ�����ļ���ͷ����Ҳ���Ǵ����￪ʼ����
 * @param  len           Ҫ���Ƶ����ݳ��ȣ�С��0��ʾ����offsetSource��ߵ���������
 * @param  fTarget       Ŀ���ļ���Ҳ���ǽ��ļ����Ƶ�����
 * @param  offsetTarget  Ŀ���ļ���λ��ƫ�ƣ�Ҳ���Ǹ��Ƶ�Ŀ���ļ���ʲôλ��
 * @return  �ɹ����Ƶ��ֽ���
**/

long fcopy(FILE *fSource, long offsetSource, long len, FILE *fTarget, long offsetTarget){
	int bufferLen = 1024*4;  // ����������
    char *buffer = (char*)malloc(bufferLen);  // ���ٻ���
    int readCount;  // ÿ�ε���fread()��ȡ���ֽ���
	long nBytes = 0;  //�ܹ������˶��ٸ��ֽ�
	int n = 0;  //��Ҫ���ö��ٴ�fread()����
	int i;  //ѭ�����Ʊ���

	fseek(fSource, offsetSource, SEEK_SET);
	fseek(fTarget, offsetTarget, SEEK_SET);

	if(len<0){  //������������
		while( (readCount=fread(buffer, 1, bufferLen, fSource)) > 0 ){
			nBytes += readCount;
			fwrite(buffer, readCount, 1, fTarget);
		}
	}else{  //����len���ֽڵ�����
		n = (int)ceil((double)((double)len/bufferLen));
		for(i=1; i<=n; i++){
			if(len-nBytes<bufferLen){ bufferLen = len-nBytes; }
			readCount=fread(buffer, 1, bufferLen, fSource);
			fwrite(buffer, readCount, 1, fTarget);
			nBytes += readCount;
		}
	}
	fflush(fTarget);
    free(buffer);
	return nBytes;
}

/**
 * ���ļ��в�������
 * @param  fp      Ҫ�������ݵ��ļ�
 * @param  buffer  ��������Ҳ����Ҫ���������
 * @param  offset  ƫ����������ļ���ͷ����Ҳ���Ǵ����￪ʼ����
 * @param  len     Ҫ��������ݳ���
 * @return  �ɹ�������ֽ���
**/
int finsert(FILE *fp, long offset, void *buffer, int len){
	long fileSize = getFileSize(fp);
	FILE *fpTemp;  //��ʱ�ļ�

	if(offset>fileSize || offset<0 || len<0){  //�������
		return -1;
	}

	if(offset == fileSize){  //���ļ�ĩβ����
		fseek(fp, offset, SEEK_SET);
		if(!fwrite(buffer, len, 1, fp)){
			return -1;
		}
	}

	if(offset < fileSize){  //�ӿ�ͷ�����м�λ�ò���
		fpTemp = tmpfile();
		fcopy(fp, 0, offset, fpTemp, 0);
		fwrite(buffer, len, 1, fpTemp);
		fcopy(fp, offset, -1, fpTemp, offset+len);
		freopen(FILENAME, "wb+", fp );
		fcopy(fpTemp, 0, -1, fp, 0);
		fclose(fpTemp);
	}
	
	return 0;
}

/**
 * ���ļ���ɾ������
 * @param  fp      Ҫ�������ݵ��ļ�
 * @param  buffer  ��������Ҳ����Ҫ���������
 * @param  offset  ƫ����������ļ���ͷ����Ҳ���Ǵ����￪ʼ����
 * @param  len     Ҫ��������ݳ���
 * @return  �ɹ�������ֽ���
**/
int fdelete(FILE *fp, long offset, int len){
	long fileSize = getFileSize(fp);
	FILE *fpTemp;

	if(offset>fileSize || offset<0 || len<0){  //����
		return -1;
	}

	fpTemp = tmpfile();
	fcopy(fp, 0, offset, fpTemp, 0);
	fcopy(fp, offset+len, -1, fpTemp, offset);
	freopen(FILENAME, "wb+", fp );
	fcopy(fpTemp, 0, -1, fp, 0);

	fclose(fpTemp);
	return 0;
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
	printf(buf);
	getch();
	printf("\n");
}
