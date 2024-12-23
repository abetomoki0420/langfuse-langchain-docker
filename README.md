# FastAPI Chat Application with LangChain and Langfuse

このプロジェクトは、OpenAI APIを使用したチャットアプリケーションで、FastAPI、LangChain、Langfuseを統合しています。

## 必要条件

- Python 3.11以上
- Poetry
- OpenAI API Key
- Docker と Docker Compose
- Langfuse アカウント（Self-hostedの場合は不要）

## セットアップ

1. リポジトリをクローンします：
```bash
git clone <repository-url>
cd <repository-name>
```

2. Poetryで依存関係をインストールします：
```bash
poetry install
```

3. 環境変数を設定します。`.env`ファイルを作成し、以下の内容を追加します：
```bash
OPENAI_API_KEY=your_openai_api_key_here
LANGFUSE_PUBLIC_KEY=your_langfuse_public_key_here
LANGFUSE_SECRET_KEY=your_langfuse_secret_key_here
LANGFUSE_HOST=http://localhost:3000
```

### Langfuseのセットアップ（Self-hosted）

1. Langfuseを起動します：
```bash
docker compose up -d
```

2. Langfuseの管理画面（http://localhost:3000）にアクセスし、初期設定を行います。
   - 最初のユーザーを作成
   - プロジェクトを作成
   - API Keysから必要なキーを取得

### Langfuseキーの取得方法

1. [Langfuse](https://langfuse.com)にアクセスしてアカウントを作成します
2. 新しいプロジェクトを作成します
3. プロジェクトの設定画面から、以下のキーを取得します：
   - Public Key (`pk-lf-` で始まる)
   - Secret Key (`sk-lf-` で始まる)

## アプリケーションの起動

1. FastAPIサーバーを起動します：
```bash
poetry run uvicorn src.main:app --reload
```

2. ブラウザで http://localhost:8000/docs にアクセスしてSwagger UIを確認できます

## APIの使用方法

チャットエンドポイントにPOSTリクエストを送信します：

```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{
    "chat_history": [],
    "user_input": "こんにちは！"
  }'
```

レスポンス例：
```json
{
  "response": "こんにちは！お手伝いできることがありましたら、お申し付けください。"
}
```

## 機能

- OpenAI GPTモデルを使用したチャット機能
- チャット履歴の管理
- Langfuseによる監視と分析
- FastAPIによる高速なAPIレスポンス 