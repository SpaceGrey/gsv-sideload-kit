# Third-party notices

## Sideloader

`Sideloader/bin/sideloader` is a macOS arm64 build of
[SpaceGrey/Sideloader](https://github.com/SpaceGrey/Sideloader), commit
[`6429c6cc30bd7c3a65d8b0c5a4382420e87eded3`](https://github.com/SpaceGrey/Sideloader/tree/6429c6cc30bd7c3a65d8b0c5a4382420e87eded3).
Its corresponding source is available at that exact revision and is licensed
under GPL-3.0-only; a copy is included at
`ThirdParty/Sideloader-LICENSE`.
The release-specific certificate-validation changes are supplied as
`ThirdParty/Sideloader-gsv-certificate-verification.patch`.

The shipped binary was built with LDC 1.41.0 and has its build-machine home
directory paths normalized with
`ThirdParty/sanitize-sideloader-release.py` before being ad-hoc signed. Its
SHA-256 is
`2371aee82213b22afd4da49e613b4901299b542e81dd2df6651be4f36b935308`.

## Cyan

`ThirdParty/Cyan` is Cyan 1.4.4 from
[asdfzxcvbn/pyzule-rw](https://github.com/asdfzxcvbn/pyzule-rw). Its source
archive SHA-256 and Unlicense text are included in that directory.

## GoodbyeShortVideo and GSV

The framework and `gsv` executable are built from
[SpaceGrey/GoodbyeShortVideo](https://github.com/SpaceGrey/GoodbyeShortVideo),
commit
[`7963fd6c2f480660510f476fc531e757a5372f82`](https://github.com/SpaceGrey/GoodbyeShortVideo/tree/7963fd6c2f480660510f476fc531e757a5372f82).
The release-specific certificate-selection preflight is supplied as
`ThirdParty/GSV-certificate-preflight.patch`.
The framework is distributed without a personal development signature and is
signed as part of the user's own IPA installation flow.
