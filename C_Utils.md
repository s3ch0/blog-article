

```c

#include <stdio.h>
#include <stdlib.h>

#define ASNI_FG_BLACK   "\33[1;30m"
#define ASNI_FG_RED     "\33[1;31m"
#define ASNI_FG_GREEN   "\33[1;32m"
#define ASNI_FG_YELLOW  "\33[1;33m"
#define ASNI_FG_BLUE    "\33[1;34m"
#define ASNI_FG_MAGENTA "\33[1;35m"
#define ASNI_FG_CYAN    "\33[1;36m"
#define ASNI_FG_WHITE   "\33[1;37m"
#define ASNI_BG_BLACK   "\33[1;40m"
#define ASNI_BG_RED     "\33[1;41m"
#define ASNI_BG_GREEN   "\33[1;42m"
#define ASNI_BG_YELLOW  "\33[1;43m"
#define ASNI_BG_BLUE    "\33[1;44m"
#define ASNI_BG_MAGENTA "\33[1;35m"
#define ASNI_BG_CYAN    "\33[1;46m"
#define ASNI_BG_WHITE   "\33[1;47m"
#define ASNI_NONE       "\33[0m"

#define ASNI_FMT(str, fmt) fmt str ASNI_NONE
#define SIMPLE(mystr) "This is a good for your health" mystr


int main(int argc,char* argv[]){

    fprintf(stdout,ASNI_FMT("Hello World",ASNI_FG_BLUE));
    fprintf(stdout,SIMPLE(" --> zhouhao"));

    return 0;

}

```

[<++>](https://developer.arm.com/documentation/dui0375/g/Compiler-specific-Features)  
[<++>](https://developer.arm.com/documentation/101754/0618/armclang-Reference/Compiler-specific-Function--Variable--and-Type-Attributes) 

`x macro` 的使用
[<++>](https://c-faq.com/decl/spiral.anderson.html) 

I know I can do this:

```c
#define MACRO(api, ...) \
  bool ret = api(123, ##__VA_ARGS__);
```
[](https://stackoverflow.com/questions/52891546/what-does-va-args-mean)

This is just an example, it's part of a more complicated solution. The point is that I need to append the variable number of arguments to the first 123. **The ## makes the compiler strip out the comma after the 123 argument if no arguments were passed into MACRO.**

you can use `xxd -i logo_file > logo.c` to generate a print logo.c
