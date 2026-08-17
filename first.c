#include <stdio.h>
#include <string.h>
#include <ctype.h>

char p[20][20];
int n;

void first(char c) {
    int i;
    for (i = 0; i < n; i++) {
        if (p[i][0] == c) {
            char x = p[i][2];

            if (!isupper(x))
                printf("%c ", x);
            else
                first(x);
        }
    }
}

void follow(char c) {
    int i, j;

    if (p[0][0] == c)
        printf("$ ");

    for (i = 0; i < n; i++) {
        for (j = 2; p[i][j] != '\0'; j++) {
            if (p[i][j] == c) {
                if (p[i][j + 1] != '\0') {
                    char x = p[i][j + 1];

                    if (!isupper(x))
                        printf("%c ", x);
                    else
                        first(x);
                } else if (p[i][0] != c) {
                    follow(p[i][0]);
                }
            }
        }
    }
}

int main() {
    char c;

    printf("Enter number of productions: ");
    scanf("%d", &n);

    printf("Enter productions:\n");
    for (int i = 0; i < n; i++)
        scanf("%s", p[i]);

    printf("Enter non-terminal: ");
    scanf(" %c", &c);

    printf("FIRST(%c) = { ", c);
    first(c);
    printf("}\n");

    printf("FOLLOW(%c) = { ", c);
    follow(c);
    printf("}\n");

    return 0;
}
