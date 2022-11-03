#include<stdio.h>

/*
RC4初始化函数
*/
void rc4_init(unsigned char* s, unsigned char* key, unsigned long Len_k)
{
	int i = 0, j = 0;
	char k[256] = { 0 };
	unsigned char tmp = 0;
	for (i = 0; i < 256; i++) {
		s[i] = i;
		k[i] = key[i % Len_k];
	}
	for (i = 0; i < 256; i++) {
		j = (j + s[i] + k[i]) % 256;
		tmp = s[i];
		s[i] = s[j];
		s[j] = tmp;
	}
}

/*
RC4加解密函数
unsigned char* Data     加解密的数据
unsigned long Len_D     加解密数据的长度
unsigned char* key      密钥
unsigned long Len_k     密钥长度
*/
void rc4_crypt(unsigned char* Data, unsigned long Len_D, unsigned char* key, unsigned long Len_k) //加解密
{
	unsigned char s[256];
	rc4_init(s, key, Len_k);
	int i = 0, j = 0, t = 0;
	unsigned long k = 0;
	unsigned char tmp;
	for (k = 0; k < Len_D; k++) {
		i = (i + 1) % 256;
		j = (j + s[i]) % 256;
		tmp = s[i];
		s[i] = s[j];
		s[j] = tmp;
		t = (s[i] + s[j]) % 256;
		Data[k] = Data[k] ^ s[t];
	}
}
int main()
{
	//字符串密钥
	unsigned char key[] = "zstuctf";
	unsigned long key_len = sizeof(key) - 1;
	//数组密钥
	//unsigned char key[] = {};
	//unsigned long key_len = sizeof(key);

	//加解密数据
	unsigned char data[] = { 0x7E, 0x6D, 0x55, 0xC0, 0x0C, 0xF0, 0xB4, 0xC7, 0xDC, 0x45,
		0xCE, 0x15, 0xD1, 0xB5, 0x1E, 0x11, 0x14, 0xDF, 0x6E, 0x95,
		0x77, 0x9A, 0x12, 0x99 };
	//加解密
	rc4_crypt(data, sizeof(data), key, key_len);

	for (int i = 0; i < sizeof(data); i++)
	{
		printf("%c", data[i]);
	}
	printf("\n");
	return;
}
//zstuctf{xXx_team_Is_GooD

