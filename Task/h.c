#include<stdio.h>
#include<string.h>

struct professor
{
    char name[10];
    char *dept;
};

struct student{
    char name[10];
    int number;
    struct professor *prof;
};

int main(void){
    int i;
    struct professor p[2] = {"이동규", "인터넷정보", "이종만", "인터넷정보"};
    struct student s[3] = {"전지현", 20120003, p, "김태희", 20130005, p+1, "장동건", 201200161, p+1};

    for(i = 0; i < 3; i++){
        printf("%s %d %s %s\n", s[i].name, s[i].number, s[i].prof->name, s[i].prof->dept);
    }
    return 0;
}