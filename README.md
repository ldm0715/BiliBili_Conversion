<p align="center">
  <img width="18%" align="center" src="https://z4a.net/images/2023/07/07/transform.png" alt="logo">
</p>
  <h1 align="center">
  BiliBili Conversion Tool
</h1>
<p align="center">
  哔哩哔哩客户端缓存视频转化工具
</p>

<p align="center">
  <img width="30%" align="center" src="https://z4a.net/images/2023/07/07/ui.png" alt="ui">
</p>

## 运行环境

本工具采用`ffmpeg`进行视频的转码与合并，因此需要自行安装`ffmpeg`,并将其放入**环境变量**中。除此之外无需安装任何其他环境，需要配合`BiliBili客户端`进行使用。

本界面使用`PyQt5`编写，相关代码可以在项目文件中查看。

## 使用方法

项目文件结构：

```Dir Tree
bilibili_transform_v1.2
├─ bilibili_transform_v1.2.exe
├─ image
│    ├─ bilibili.ico
│    └─ transform.ico
├─ temp
├─ output
├─ readme.txt
├─ update_log.txt
└─ videolist.txt
```

本工具提供两种转换方法：

1. 单个视频缓存转化为mp4。

   点击界面中**选择文件夹按钮**，选择一个视频文件缓存（路径示例：`F:\bilibili\1186953752`）,点击`转化`即可。

2. 多个缓存批量转化为mp4。

   项目文件夹中存在一个`videolist.txt`的txt（如果没有，点击**批量转化**的按钮后会自动生成），将你想要转化的所有视频路径写入，以回车的形式隔开，一个示例如下所示：

   <p align="center">
     <img width="35%" align="center" src="https://z4a.net/images/2023/07/07/videolist_example.png" alt="ui">
   </p>

   保存后，点击**批量转化**按钮即可。

   > 转化后的视频文件都存在项目的**output文件夹**中，点击**输出文件夹**即可直接打开。
3. 项目文件夹解释
    * image - 存储图像的文件夹
    * temp - 存储转化过程中的临时文件，转化完成后会自动删除
    * output - 存储转化后视频的文件夹
    * videolist.txt - 存储批量转化视频的路径，如果不存在，点击批量转化按钮后会自动生成
    * update_log.txt - 更新日志

## 更新日志

* v1.0
  * 自动完成视频缓存转化
  * 实现批量视频缓存文件转化


* v1.1

  * 修复因为视频标题空格导致的转化失败

  * 修复1080p以下画质转化失败的情况

  * 更改应用图标，防止与客户端弄混

  * 改进转码时的错误捕捉

- v1.2

  * 更新替换规则，将常见字符“ ”、“\\”、“:”、“\”、“<”、“>”、“=”、“|”替换

  * 应用添加全局拉伸效果

  * 优化批量转化的过程展示

## 注意事项

由于本人水平有限，考虑的情况不够周到，测试时在大部分场景应该是没问题的，但也可能存在疏漏。另外非官方开发的工具都具有时效性，可能会出现一些转化不了的情况。出现问题请留言，最后**祝大家使用愉快**。

Copyright © 2023 by gcnanmu.
