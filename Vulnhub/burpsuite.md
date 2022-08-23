

```bash
sudo apt-get update
sudo apt-get install -y libc6-x32
sudo apt-get install openjdk-17-jdk
```

```bash
java --version # 17.0.3
```

每次启动都还是需要运行下面命令 <font color='red' face=Monaco size=3>(在Burp Suite 目录下)</font>

```bash
/usr/lib/jvm/java-1.17.0-openjdk-amd64/bin/java --illegal-access=permit -Dfile.encoding=utf-8 -javaagent:burploader.jar -noverify -jar burpsuite_pro_v2022.2.4.jar
```