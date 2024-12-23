# FastAPI Chat Application with LangChain and Langfuse

このプロジェクトは、OpenAI APIを使用したチャットアプリケーションで、FastAPI、LangChain、Langfuseを統合しています。

## 必要条件

- Python 3.11以上
- Poetry
- OpenAI API Key
- Langfuse アカウント

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

### Langfuseキーの取得方法

1. [Langfuse](https://langfuse.com)にアクセスしてアカウントを作成します
1. 新しいプロジェクトを作成します
1. プロジェクトを新規作成します
1. プロジェクトの設定画面から、以下のキーを取得します：
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