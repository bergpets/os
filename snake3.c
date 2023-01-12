#include <ncurses.h>
#include <stdio.h>
int main(int arqc, char* argv[]){
    initscr();
    noecho();
    curs_set(0);
    keypad(stdscr,TRUE);
    int C1 = COLS / 2;
    int C2 = LINES / 2;
    int arrL[2][6] = {{C1-1,C1-1,C1-1,C1-1,C1-1,C1-1},{C2,C2,C2,C2,C2,C2}};
    int arrR[2][6] = {{C1 + 1,C1 + 1,C1 + 1,C1 + 1,C1 + 1,C1 + 1},{C2,C2,C2,C2,C2,C2}};
    int arrU[2][6] = {{C1,C1,C1,C1,C1,C1},{C2 + 1,C2 + 1,C2 + 1,C2 + 1,C2 + 1,C2 + 1}};
    int arrD[2][6] = {{C1,C1,C1,C1,C1,C1},{C2 - 1,C2 - 1,C2 - 1,C2 - 1,C2 - 1,C2 - 1}};
    int ch = 0;
    while(ch != 'q'){
	mvaddch(arrL[1][0],arrL[0][0],'*');
        mvaddch(arrR[1][0],arrR[0][0],'*');
        mvaddch(arrU[1][0],arrU[0][0],'*');
        mvaddch(arrD[1][0],arrD[0][0],'*');    
        refresh();
        ch = getch();
	for (int i = 5; i > 0; i--){
		arrD[0][i] = arrD[0][i-1];
                arrD[1][i] = arrD[1][i-1];
                arrU[0][i] = arrU[0][i-1];
                arrU[1][i] = arrU[1][i-1];
                arrL[0][i] = arrL[0][i-1];
                arrL[1][i] = arrL[1][i-1];
                arrR[0][i] = arrR[0][i-1];
                arrR[1][i] = arrR[1][i-1];
        }
        switch(ch){
            case KEY_LEFT:
                arrL[1][0] = (arrL[1][0] + 1) % LINES;
                arrR[1][0] = (arrR[1][0] + LINES - 1) % LINES;
                arrU[0][0] = (arrU[0][0] + 1) % COLS;
                arrD[0][0] = (arrD[0][0] + COLS - 1) % COLS;
                break;
            case KEY_RIGHT:
                arrL[1][0] = (arrL[1][0] + LINES - 1) % LINES;
                arrR[1][0] = (arrR[1][0] + 1) % LINES;
                arrU[0][0] = (arrU[0][0] + COLS - 1) % COLS;
                arrD[0][0] = (arrD[0][0] + 1) % COLS;
                break;
            case KEY_DOWN:
                arrL[0][0] = (arrL[0][0] + 1) % COLS;
                arrR[0][0] = (arrR[0][0] + COLS - 1)%COLS;
                arrU[1][0] = (arrU[1][0] + LINES - 1) % LINES;
                arrD[1][0] = (arrD[1][0] + 1) % LINES;
                break;
            case KEY_UP:
                arrL[0][0] = (arrL[0][0] + COLS - 1)%COLS;
                arrR[0][0] = (arrR[0][0] + 1) % COLS;
                arrU[1][0] = (arrU[1][0] + 1) % LINES;
                arrD[1][0] = (arrD[1][0] + LINES - 1) % LINES;
                break;
            default:
                break;
            }
        mvaddch(arrL[1][5],arrL[0][5],' ');
        mvaddch(arrR[1][5],arrR[0][5],' ');
        mvaddch(arrU[1][5],arrU[0][5],' ');
        mvaddch(arrD[1][5],arrD[0][5],' ');
    }
endwin();
return 0;
}
