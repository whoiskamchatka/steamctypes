# steamctypes

Auto-generated, pure-Python Steamworks bindings, built on `ctypes`: no compiled extension and no
runtime dependencies.

> **Status: early development.** Nothing is implemented yet. The repository contains only the
> project setup, and the package is not published on PyPI.

## Requirements

- 64-bit CPython 3.11 or newer
- Windows, Linux or macOS
- The Steamworks SDK, downloaded from Valve

## The Steamworks SDK is not included

The SDK is proprietary. This repository and its packages contain no SDK headers, metadata or
native libraries. Download the SDK from the
[Steamworks partner site](https://partner.steamgames.com/downloads/list) and use it under Valve's
terms; your game ships the SDK's redistributable library itself.

## License

steamctypes's own source code is released under the [Apache License 2.0](LICENSE). The
Steamworks SDK is licensed separately by Valve.

steamctypes is an independent project, not affiliated with, endorsed by or sponsored by Valve
Corporation. Steam and Steamworks are trademarks and/or registered trademarks of Valve Corporation
in the U.S. and/or other countries.