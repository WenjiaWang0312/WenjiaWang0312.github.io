# Mac 上安装 Codex 并配置 CallAI

这份教程只包含 Codex 安装和 CallAI 配置。

## 1. 打开终端

按 `Command + Space` 打开 Spotlight，输入 `Terminal`，然后按回车。

后面的命令都在 Terminal 中执行。

## 2. 安装 Codex

复制下面整行命令，粘贴到 Terminal，然后按回车：

```bash
curl -fsSL https://chatgpt.com/codex/install.sh | sh
```

安装完成后，关闭 Terminal，再重新打开。运行：

```bash
codex --version
```

如果能看到版本号，说明 Codex 已安装。

## 3. 配置 CallAI

先创建 Codex 配置目录：

```bash
mkdir -p ~/.codex
```

打开配置文件：

```bash
nano ~/.codex/config.toml
```

将下面的内容完整粘贴进去：

```toml
model_provider = "callai"
model = "gpt-5.5"
model_reasoning_effort = "max"
preferred_auth_method = "apikey"
disable_response_storage = true

[model_providers.callai]
name = "callai"
base_url = "https://sub.callai.one/v1"
wire_api = "responses"
requires_openai_auth = true
```

保存文件：

1. 按 `Control + O`。
2. 按回车确认文件名。
3. 按 `Control + X` 退出。

注意这里按的是 `Control`，不是 `Command`。

## 4. 填写 CallAI API Key

API Key 单独写在 `~/.codex/auth.json`，不要写进 `config.toml`。

打开 API Key 文件：

```bash
nano ~/.codex/auth.json
```

粘贴下面的内容：

```json
{
  "OPENAI_API_KEY": "YOUR_CALLAI_API_KEY"
}
```

把 `YOUR_CALLAI_API_KEY` 替换成拿到的完整 CallAI API Key。例如：

```json
{
  "OPENAI_API_KEY": "sk-xxxxxxxxxxxxxxxx"
}
```

只替换双引号里面的内容，保留 `OPENAI_API_KEY`、双引号和大括号。

再次保存：

1. 按 `Control + O`。
2. 按回车确认文件名。
3. 按 `Control + X` 退出。

API Key 相当于密码，不要发给其他人，不要上传到 GitHub，也不要在截图中显示。
