# Bundled Cyan

This directory contains the Cyan 1.4.4 runtime used by `gsv` to inject
`GoodbyeShortVideo.framework` into an IPA. It is included so users do not need
to install Cyan, pipx, or Python packages.

Only the macOS Apple-silicon tools are included because GSV supports Apple
silicon Macs. Cyan runs with the macOS-provided `/usr/bin/python3` (Python 3.9
or later); it has no additional Python package dependencies for this workflow.

Source: https://github.com/asdfzxcvbn/pyzule-rw/archive/main.zip

Source archive SHA-256:
`f30fdf42a8500d8f0b2c745dce43a3273f9c084f4b4a76ce032c29bb7b2bdcbf`

The original Cyan license is in [LICENSE](LICENSE). Cyan's bundled injection
tools retain their upstream attribution; see the upstream README for details.
