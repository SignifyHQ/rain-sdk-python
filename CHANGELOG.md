# Changelog

## 0.2.0 (2026-03-26)

Full Changelog: [v0.1.0...v0.2.0](https://github.com/SignifyHQ/rain-sdk-python/compare/v0.1.0...v0.2.0)

### Features

* **internal:** implement indices array format for query and form serialization ([e034171](https://github.com/SignifyHQ/rain-sdk-python/commit/e034171972d4ec0447cbee8eeeb5e606f848c1c8))


### Bug Fixes

* sanitize endpoint path params ([79d1595](https://github.com/SignifyHQ/rain-sdk-python/commit/79d159573dc2afeeb50715a02dc83e27417c7484))


### Chores

* **ci:** skip lint on metadata-only changes ([a7f10b7](https://github.com/SignifyHQ/rain-sdk-python/commit/a7f10b7b66b895e5cf0ebfe279b3bd9699b9b4e4))
* **internal:** update gitignore ([3d160ac](https://github.com/SignifyHQ/rain-sdk-python/commit/3d160acf459108d7b7bb4d3c4e851f801627716b))

## 0.1.0 (2026-03-17)

Full Changelog: [v0.0.1...v0.1.0](https://github.com/SignifyHQ/rain-sdk-python/compare/v0.0.1...v0.1.0)

### Features

* **api:** add better titles and discriminator ([1a7a8ab](https://github.com/SignifyHQ/rain-sdk-python/commit/1a7a8ab4f165a2509f1cd3efc3f659e966a8af52))
* **api:** manual updates ([7a93ab3](https://github.com/SignifyHQ/rain-sdk-python/commit/7a93ab357840e4f515296cc1201b72254bffa50b))
* **api:** manual updates ([1934919](https://github.com/SignifyHQ/rain-sdk-python/commit/193491963ce87a5d2d9ed34cac1088ff34d0cd24))
* **api:** manual updates ([903e3ee](https://github.com/SignifyHQ/rain-sdk-python/commit/903e3eee03cc4e46318f90cb9a71d5b42afe6fb2))
* **api:** manual updates ([61f970b](https://github.com/SignifyHQ/rain-sdk-python/commit/61f970ba2e8ae669215837dedaf21b04500ded92))
* **api:** manual updates ([9118967](https://github.com/SignifyHQ/rain-sdk-python/commit/911896751042a667fd2953837886d919aa556c94))
* **api:** update readme ([9917475](https://github.com/SignifyHQ/rain-sdk-python/commit/99174750751080c0d3c8659084839c9918eaef1e))
* **client:** add custom JSON encoder for extended type support ([37d534c](https://github.com/SignifyHQ/rain-sdk-python/commit/37d534cc92070ac99f80fdf8c2233247094a8b56))
* **client:** add support for binary request streaming ([38d077f](https://github.com/SignifyHQ/rain-sdk-python/commit/38d077ff3170065116e1672bada744425952d017))


### Bug Fixes

* **deps:** bump minimum typing-extensions version ([ba9c51b](https://github.com/SignifyHQ/rain-sdk-python/commit/ba9c51b81fff57ce9cdfc3a6823c3076cde5ac76))
* ensure streams are always closed ([0d0d766](https://github.com/SignifyHQ/rain-sdk-python/commit/0d0d7664bebc224a25cc7cbb840b7f2c1b2a2cda))
* **naming:** change sdk package names ([7e8977e](https://github.com/SignifyHQ/rain-sdk-python/commit/7e8977ebd22d8477e9f138cef70cbe0099f03cea))
* **pydantic:** do not pass `by_alias` unless set ([7de83e0](https://github.com/SignifyHQ/rain-sdk-python/commit/7de83e0ebabe1fe1e055b8ee270e2b4755c624d7))
* **types:** allow pyright to infer TypedDict types within SequenceNotStr ([abeb09a](https://github.com/SignifyHQ/rain-sdk-python/commit/abeb09ab75e7c8b7c2fdccdadad13cffe194775a))
* use async_to_httpx_files in patch method ([991c2e5](https://github.com/SignifyHQ/rain-sdk-python/commit/991c2e55a365e0db4843ce2d0690c8e4e8b5c4b0))


### Chores

* add missing docstrings ([0a4097c](https://github.com/SignifyHQ/rain-sdk-python/commit/0a4097cfbb6a89be5133d0b82d73c38995949b4c))
* **ci:** bump uv version ([c0f7f3d](https://github.com/SignifyHQ/rain-sdk-python/commit/c0f7f3df3fe321b5bb93d152ad97b857055a13a6))
* **ci:** skip uploading artifacts on stainless-internal branches ([3ed4186](https://github.com/SignifyHQ/rain-sdk-python/commit/3ed4186a188b56b4a9eb880375014a3ea8ca4cc1))
* **ci:** upgrade `actions/github-script` ([56d63cb](https://github.com/SignifyHQ/rain-sdk-python/commit/56d63cb7e4aa888ca373dc6551f1fba36b862d65))
* **deps:** mypy 1.18.1 has a regression, pin to 1.17 ([ea30efd](https://github.com/SignifyHQ/rain-sdk-python/commit/ea30efd01704d9e3156ddb66861ad8fc04680166))
* **docs:** use environment variables for authentication in code snippets ([a1152ee](https://github.com/SignifyHQ/rain-sdk-python/commit/a1152ee7954ba1b4e85cef2e6a1ae3fdecbf312e))
* format all `api.md` files ([a34ca35](https://github.com/SignifyHQ/rain-sdk-python/commit/a34ca351e8f40f94862cb38b2ed28fd01100c99f))
* **internal:** add `--fix` argument to lint script ([d2d0d38](https://github.com/SignifyHQ/rain-sdk-python/commit/d2d0d38b71b1cb41d76a7c2b5be974322f84bc9d))
* **internal:** add missing files argument to base client ([c6c447f](https://github.com/SignifyHQ/rain-sdk-python/commit/c6c447fff151975280c4e6496e8b6dd0203a5646))
* **internal:** add request options to SSE classes ([d186d95](https://github.com/SignifyHQ/rain-sdk-python/commit/d186d95e4d57756d83e6178f04ef8f3a4365a229))
* **internal:** bump dependencies ([90d3e36](https://github.com/SignifyHQ/rain-sdk-python/commit/90d3e367f0519a7935efbe8e0f9928f796174dd3))
* **internal:** codegen related update ([20df806](https://github.com/SignifyHQ/rain-sdk-python/commit/20df806f5705dba815197e2eddd9cbb95072a7a3))
* **internal:** fix lint error on Python 3.14 ([820afbf](https://github.com/SignifyHQ/rain-sdk-python/commit/820afbf4d450b077ad23e22292f721359cc3e518))
* **internal:** make `test_proxy_environment_variables` more resilient ([47ecc14](https://github.com/SignifyHQ/rain-sdk-python/commit/47ecc14edd42e0275a483b79880097376f9b1bd9))
* **internal:** make `test_proxy_environment_variables` more resilient to env ([8110acc](https://github.com/SignifyHQ/rain-sdk-python/commit/8110acc8b75ef0f95fe099a012eecdbff461fc9b))
* **internal:** remove mock server code ([ce4ac7d](https://github.com/SignifyHQ/rain-sdk-python/commit/ce4ac7d71c3dc8d0f57f8baf50dc947853ebcc26))
* **internal:** tweak CI branches ([ae06c84](https://github.com/SignifyHQ/rain-sdk-python/commit/ae06c84dd13a2f588a6e80c247cc03b4eb2a7ecf))
* **internal:** update `actions/checkout` version ([64ecb84](https://github.com/SignifyHQ/rain-sdk-python/commit/64ecb84cdc431b189fe4062a74fb2fdaec98c6f1))
* speedup initial import ([b3428e3](https://github.com/SignifyHQ/rain-sdk-python/commit/b3428e30a60715a82294eea58b65c5be589b7230))
* update lockfile ([35996f1](https://github.com/SignifyHQ/rain-sdk-python/commit/35996f1d463b3cf16ad7838e5c89fa92a084e4b5))
* update mock server docs ([275b72e](https://github.com/SignifyHQ/rain-sdk-python/commit/275b72e8b2f4af5741ea63932a60177b965348cd))
* update placeholder string ([521c54b](https://github.com/SignifyHQ/rain-sdk-python/commit/521c54ba406f5322b3aef595f593581009aa7297))
* update SDK settings ([2dd3853](https://github.com/SignifyHQ/rain-sdk-python/commit/2dd385365ad792c5e281ff33f56238ca16fcd1e9))
* update SDK settings ([c4508e0](https://github.com/SignifyHQ/rain-sdk-python/commit/c4508e096f7b1712c75a7e1c7f5013733a34e816))
* update SDK settings ([4799017](https://github.com/SignifyHQ/rain-sdk-python/commit/4799017e343bef49cfab9424d7a7081d33efcfe4))


### Refactors

* **internal:** switch from rye to uv ([06797a0](https://github.com/SignifyHQ/rain-sdk-python/commit/06797a005fa1827ba07d36a549ac68bc24b1cc42))
