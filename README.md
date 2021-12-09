# CherryKiller
用以监听某一个视频的数据，以判断该视频是否被限流。

## 使用方法
确保`main.exe`、`config.txt`和`crnmsl.txt`位于同一目录下。双击运行`main.exe`。

生成的报告在同目录下的`report.txt`中

可以修改`config.txt`（配置文件）中的内容。以示例为例，具体参数意义为：
```
{
	"aid": 209712177, #视频aid
	"listen_freq": 3, #监听频率，单位秒。高监听频率会使结果更加准确，但是也会增加ip被短暂禁止访问的风险
	"print_beat": 20 #报告生成频率，即每监听多少次保存一次报告
}
```
