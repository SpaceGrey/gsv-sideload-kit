# Goodbye Short Video

简体中文 | [English](README.md)

`gsv` 是一个 macOS 的命令行工具：它会为受支持的 IPA 注入 `GoodbyeShortVideo.framework`，然后对连接的 iPhone 或 iPad 进行签名和安装。

> 仅将本项目用于你有权使用的 IPA；请遵守应用、Apple Developer 和当地法律的相关条款。项目与小红书、哔哩哔哩及 Apple 均无隶属关系。

> 使用本项目即表示你自行承担风险。在适用法律允许的最大范围内，作者和贡献者不对因使用本项目导致的账号封禁、访问受限、数据丢失或其他后果承担责任。

## 1. 项目效果

当前支持以下应用：

- 小红书（Bundle ID：`com.xingin.discover`；已验证版本：9.43）
- 哔哩哔哩（Bundle ID：`tv.danmaku.bilianime`；已验证版本：9.8）

注入后，可在应用内的 **GSV 设置** 中按需开启或关闭以下功能：

- 过滤 Feed 广告和开屏广告
- 禁止短视频循环、短视频下滑，并可隐藏短视频 UI
- 过滤竖屏视频，以及视频和直播卡片
- 查看各类内容的拦截统计，并可重置统计

<p align="center">
  <img src="https://i.ibb.co/qMB3ZrnQ/gsv-settings-zh.webp" alt="GSV 中文设置界面" width="360">
</p>


## 2. 运行要求

- Apple 芯片（arm64）的 Mac
- 一台通过 USB 连接、已解锁并已选择“信任此电脑”的 iPhone 或 iPad。
- iOS 16 及更高版本：在“设置 → 隐私与安全性 → 开发者模式”中启用开发者模式，并按系统提示重启确认
- 可用于开发签名的 Apple Developer 团队；首次使用时需要登录 Apple ID，并可能需要完成双重认证

## 3. IPA 准备

1. 准备**已解密**的 IPA 推荐使用[decrypt.day](https://decrypt.day/home)。
2. 将 IPA 放在本项目根目录，工具只会识别小红书和哔哩哔哩的 IPA。


## 4. 如何运行

在终端进入项目目录后执行：
```zsh
./gsv
```

随后按终端提示完成：

1. 选择待处理的 IPA。
2. 选择已保存的签名证书，或登录 Apple ID 并选择开发团队。
3. 等待框架注入、IPA 重新打包，并移除 App Extension / Watch target。
4. 保持设备解锁、连接稳定，选择目标设备并等待签名安装完成。

## 5. 使用 AltStore 安装

如果没有付费 Apple Developer 开发者账号，可以使用 `inject` 命令仅注入并重新打包 IPA，无需由 `gsv` 签名或安装：

```zsh
./gsv inject
```

随后将生成的 `out/*.gsv.injected.ipa` 导入 [AltStore](https://altstore.io/) 完成安装。AltStore 会管理签名和刷新流程，后续刷新更方便。

## 6. 限制

- 功能针对特定应用版本实现；应用更新、接口或界面变化后，部分拦截能力可能失效，需等待框架更新。
- 注入过程会移除 IPA 中的 App Extension 与 Watch target，因此这些附属功能不会被安装。
- 使用免费个人开发团队签名时，Apple 的配额和配置文件通常约 7 天到期；到期后需要重新签名安装，且团队还受 App ID、设备和每台设备开发应用数量等限制。
