# 运行命令

- 项目：silero-vad（Voice Activity Detector）
- 生成时间：2026-09-08
- 运行方式：直接运行（`uv` + 本地 editable 安装）
- 硬件评估：**满足** — 官方要求约 1G+ RAM、现代 CPU（AVX）；本机 RTX 4080 16GB（剩余约 15GB）、内存 31.8GB（空闲约 13GB）。模型约 2MB，CPU 即可，无 GPU 硬门槛。

## 环境准备

```powershell
# 使用本机全局 ffmpeg（torchaudio 音频 I/O）
$env:Path = "E:\Programs\ffmpeg-master-latest-win64-gpl\bin;$env:Path"

# 官方 pypi.org 探测超时，使用清华镜像
$env:UV_INDEX_URL = 'https://pypi.tuna.tsinghua.edu.cn/simple'

Set-Location E:\AI\local-voice\silero-vad
uv venv --python 3.10.11
uv pip install -e ".[onnx-cpu,test]" --index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

## 启动

- 推荐：`pwsh -NoProfile -File .\start.ps1`
- 说明：单服务（官方样例音频 VAD 演示），无菜单，直接跑完并打印语音时间戳
- 等价手动命令：

```powershell
$env:Path = "E:\Programs\ffmpeg-master-latest-win64-gpl\bin;$env:Path"
Set-Location E:\AI\local-voice\silero-vad
uv run python scripts\run_vad_demo.py
```

## 验证

- 退出码 0
- 打印非空的 `speech_timestamps` 列表（若干段 `start`/`end` 秒）
- 可选：`uv run pytest tests/test_basic.py -q`

## 备注

- 镜像源：PyPI → `https://pypi.tuna.tsinghua.edu.cn/simple`（官方 5s 超时）
- ffmpeg：`E:\Programs\ffmpeg-master-latest-win64-gpl\bin`
- 默认走 JIT（torch）；ONNX 可用 `load_silero_vad(onnx=True)`（已装 `onnxruntime`）
- 非长期服务，无端口；属库 + CLI 演示
- 本机交付物：`RUN.md`、`start.ps1`（默认不提交）
