#include<stdio.h>
#include<stdlib.h>
int mutex=1,full=0,empty=3,x=0;
void producer();
void consumer();
void consumer();
int wait(int);
int signal(int);
int main(){
printf("\n 1.producer \n 2.consumer \n 3.exit \n");
while(1){
int n;
printf("\n enter your choice:");
scanf("%d",&n);
if(mutex==1){
switch(n){
case 1:
if(empty!=0){
producer();
}
else{
printf("buffer is full \n");
}
break;
case 2:
if(full!=0){
consumer();
}
else{
printf("buffer is empty \n");
}
break;
case 3:
exit(1);
}
}
}
}
int wait(int s){
return --s;
}
int signal(int s){
return ++s;
}
void producer(){
mutex=wait(mutex);
full=signal(full);
empty=wait(empty);
x++;
printf("producer produces the item %d \n",x);
mutex=signal(mutex);
}
void consumer(){
mutex=wait(mutex);
full=wait(full);
empty=signal(empty);
printf("consumer consumes item %d \n",x);
x--;
mutex=signal(mutex);
}
