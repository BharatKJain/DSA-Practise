#include <stdio.h>

typedef struct{
    int minutes;
    int hour;
    int seconds;
}Time;
int main(void) {
	// your code goes here
    Time *time1,*time2;
    time2->hour=2;
    time2->minutes=1;
    time2->seconds=43;
    time1->hour=1;
    time1->minutes=58;
    time1->seconds=45;
    int hour_diff=(time2->hour-time1->hour)*60;
	int min_diff=(time2->minutes-time1->minutes);
	int main_diff=hour_diff+min_diff;
	int res=(main_diff*60)+(time2->seconds-time1->seconds);
    printf("%d",res)
    // return res;
	return 0;
}