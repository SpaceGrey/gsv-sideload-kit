# Goodbye Short Video

[简体中文](README_CN.md) | English

`gsv` is a macOS command-line tool that injects `GoodbyeShortVideo.framework` into supported IPAs, then signs and installs them on a connected iPhone or iPad.

> Use this project only with IPAs you are authorized to use. Please comply with the terms of the apps, Apple Developer, and applicable local laws. This project is not affiliated with Xiaohongshu, Bilibili, or Apple.

> Use this project at your own risk. The author and contributors are not responsible for account suspension, restricted access, data loss, or any other consequences resulting from its use, to the fullest extent permitted by applicable law.

## 1. What It Does

The following apps are currently supported:

- Xiaohongshu (Bundle ID: `com.xingin.discover`; tested version: 9.43)
- Bilibili (Bundle ID: `tv.danmaku.bilianime`; tested version: 9.8)

After injection, the following features can be enabled or disabled in the app's **GSV Settings**:

- Block feed ads and splash ads
- Disable short-video looping and swiping, and hide the short-video UI
- Block vertical videos, as well as video and live-stream cards
- View and reset blocking statistics

<p align="center">
  <img src="https://i.ibb.co/pBWg8xcX/gsv-settings-en.webp" alt="GSV Settings in English" width="360">
</p>

## 2. Requirements

- An Apple Silicon (arm64) Mac
- An iPhone or iPad connected by USB, unlocked, and set to trust this Mac
- On iOS 16 or later: enable Developer Mode in **Settings → Privacy & Security → Developer Mode**, then restart and confirm when prompted
- An Apple Developer team that can be used for development signing. The first run requires Apple ID sign-in and may require two-factor authentication

## 3. Preparing an IPA

1. Prepare a **decrypted** IPA. [decrypt.day](https://decrypt.day/home) is recommended.
2. Put the IPA in the project root directory. The tool recognizes only Xiaohongshu and Bilibili IPAs.

## 4. How to Run

Open Terminal in the project directory and run:

```zsh
./gsv
```

Then follow the prompts:

1. Select the IPA to process.
2. Select a saved signing certificate, or sign in with your Apple ID and select a development team.
3. Wait for the framework to be injected, the IPA to be repackaged, and App Extension and Watch targets to be removed.

## 5. Install with AltStore

If you do not have a paid Apple Developer account, use `inject` to create a repackaged IPA without signing or installing it from `gsv`:

```zsh
./gsv inject
```

The resulting `out/*.gsv.injected.ipa` can then be imported and installed with [AltStore](https://altstore.io/). AltStore manages the signing and refresh workflow, which makes refreshing the app more convenient.

## 6. Limitations

- The features target specific app versions. App, API, or UI updates may cause some blocking features to stop working until the framework is updated.
- The injection process removes App Extension and Watch targets, so those accompanying features will not be installed.
- With a free personal development team, Apple quotas and provisioning profiles generally expire after about seven days. You will need to sign and install again after expiration, and the team is also subject to limits for App IDs, devices, and development apps per device.
