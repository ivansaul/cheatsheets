# File Processing

## File processing function

| Function    | Description                                       |
| ----------- | :------------------------------------------------ |
| `fopen()`   | `open` a new or existing file                     |
| `fprintf()` | write data to `file`                              |
| `fscanf()`  | `read` data from a file                           |
| `fputc()`   | write a character to `file`                       |
| `fgetc()`   | `read` a character from a file                    |
| `fclose()`  | `close` the file                                  |
| `fseek()`   | set the file pointer to `the given position`      |
| `fputw()`   | Write an integer `to` a file                      |
| `fgetw()`   | `read` an integer from a file                     |
| `ftell()`   | returns the current `position`                    |
| `rewind()`  | set the file pointer to the beginning of the file |

There are many functions in the C library to `open`/`read`/`write`/`search` and `close` files

## Open mode parameter

| Mode  | Description                                                                                                 |
| ----- | :---------------------------------------------------------------------------------------------------------- |
| `r`   | Open a text file in `read` mode, allowing the file to be read                                               |
| `w`   | Open a text file in `write` mode, allowing writing to the file                                              |
| `a`   | Open a text file in `append` mode<br /><small>If the file does not exist, a new one will be created</small> |
| `r+`  | Open a text file in `read-write` mode, allowing reading and writing of the file                             |
| `w+`  | Open a text file in `read-write` mode, allowing reading and writing of the file                             |
| `a+`  | Open a text file in `read-write` mode, allowing reading and writing of the file                             |
| `rb`  | Open a binary file in `read` mode                                                                           |
| `wb`  | Open binary file in `write` mode                                                                            |
| `ab`  | Open a binary file in `append` mode                                                                         |
| `rb+` | open binary file in `read-write` mode                                                                       |
| `wb+` | Open binary file in `read-write` mode                                                                       |
| `ab+` | open binary file in `read-write` mode                                                                       |

## Open the file: fopen()

```c
#include <stdio.h>

void main() {
  FILE *fp;
  char ch;

  fp = fopen("file_handle.c", "r");

  while (1) {
    ch = fgetc(fp);
    if (ch == EOF)
      break;
    printf("%c", ch);
  }
  fclose(fp);
}
```

After performing all operations on the file, the file must be closed with `fclose()`

## Write to file: fprintf()

```c
#include <stdio.h>

void main() {
  FILE *fp;
  fp = fopen("file.txt", "w"); // open the file

  // write data to file
  fprintf(fp, "Hello file for fprintf..\n");
  fclose(fp); // close the file
}
```

## Read the file: fscanf()

```c
#include <stdio.h>

void main() {
  FILE *fp;

  char buff[255]; // Create a char array to store file data
  fp = fopen("file.txt", "r");

  while(fscanf(fp, "%s", buff) != EOF) {
    printf("%s ", buff);
  }
  fclose(fp);
}
```

## Write to file: fputc()

```c
#include <stdio.h>

void main() {
  FILE *fp;
  fp = fopen("file1.txt", "w"); // open the file
  fputc('a',fp); // write a single character to the file
  fclose(fp); // close the file
}
```

## Read the file: fgetc()

```c
#include <stdio.h>
#include <conio.h>

void main() {
  FILE *fp;
  char c;

  clrscr();

  fp = fopen("myfile.txt", "r");

  while( (c = fgetc(fp) ) != EOF) {
    printf("%c", c);
  }
  fclose(fp);

  getch();
}
```

## Write to file: fputs()

```c
#include<stdio.h>
#include<conio.h>

void main() {
  FILE *fp;

  clrscr();

  fp = fopen("myfile2.txt","w");
  fputs("hello c programming",fp);
  fclose(fp);

  getch();
}
```

## Read files: fgets()

```c
#include<stdio.h>
#include<conio.h>

void main() {
  FILE *fp;
  char text[300];

  clrscr();

  fp = fopen("myfile2.txt", "r");
  printf("%s", fgets(text, 200, fp));
  fclose(fp);

  getch();
}
```

## fseek()

```c
#include <stdio.h>

void main(void) {
  FILE *fp;

  fp = fopen("myfile.txt","w+");
  fputs("This is Book", fp);

  // Set file pointer to the given position
  fseek(fp, 7, SEEK_SET);

  fputs("Kenny Wong", fp);
  fclose(fp);
}
```

Set the file pointer to the given position

## rewind()

```c
#include <stdio.h>
#include <conio.h>

void main() {
  FILE *fp;
  char c;

  clrscr();

  fp = fopen("file.txt", "r");

  while( (c = fgetc(fp) ) != EOF) {
    printf("%c", c);
  }

  rewind(fp); // move the file pointer to the beginning of the file

  while( (c = fgetc(fp) ) != EOF) {
    printf("%c", c);
  }
  fclose(fp);

  getch();
}
// output
// Hello World! Hello World!
```

## ftell()

```c
#include <stdio.h>
#include <conio.h>

void main () {
   FILE *fp;
   int length;

   clrscr();

   fp = fopen("file.txt", "r");

   fseek(fp, 0, SEEK_END);
   length = ftell(fp); // return current position
   fclose(fp);

   printf("File size: %d bytes", length);

   getch();
}
// output
// file size: 18 bytes
```
