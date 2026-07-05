# 🟢 Naver Search API: bulk multi-vertical Korean search as clean JSON

> The most efficient, reliable, and developer-friendly way to use the Naver Search API.
>
> 한국어 문서는 각 섹션의 영어 설명 바로 아래에 있습니다. (Korean documentation follows each English section below.)

**Actor page:** [apify.com/johnvc/naver-search-api](https://apify.com/johnvc/naver-search-api?fpr=9n7kx3)
**Input schema:** [apify.com/johnvc/naver-search-api/input-schema](https://apify.com/johnvc/naver-search-api/input-schema?fpr=9n7kx3)

Search Naver, South Korea's largest search engine, and get back clean structured JSON across five result types: web organic, news, images, video, and shopping. Run many queries at once, choose the vertical with the `where` input, paginate, and export. Built for Korean market research, K-content intelligence, e-commerce pricing, and AI agents.

> **한국어:** 한국 최대 검색 엔진인 네이버를 검색하고, 웹 검색, 뉴스, 이미지, 동영상, 쇼핑까지 다섯 가지 결과 유형을 깔끔한 구조화 JSON으로 받아보세요. 여러 검색어를 한 번에 실행하고, `where` 입력으로 검색 영역을 선택하고, 페이지를 넘기고, 데이터를 내보낼 수 있습니다. 한국 시장 조사, K-콘텐츠 분석, 이커머스 가격 모니터링, AI 에이전트를 위해 만들어졌습니다.

## Video Walkthrough / 동영상 안내

[![Watch the walkthrough](https://img.youtube.com/vi/jREWahDGhJM/maxresdefault.jpg)](https://www.youtube.com/watch?v=jREWahDGhJM)

> **한국어:** 위 썸네일을 클릭하면 사용 방법을 보여주는 동영상 안내를 볼 수 있습니다.

## Quick Start / 빠른 시작

### Prerequisites / 사전 준비
- Python 3.11 or higher
- An Apify account and API key ([get a free key here](https://apify.com?fpr=9n7kx3))

> **한국어:** Python 3.11 이상이 필요하며, Apify 계정과 API 키가 필요합니다 ([무료 키 받기](https://apify.com?fpr=9n7kx3)).

1. **Clone the repository / 저장소 복제**
   ```bash
   git clone https://github.com/johnisanerd/Apify-Naver-Search-API.git
   cd Apify-Naver-Search-API
   ```

2. **Install dependencies with UV / UV로 의존성 설치**
   ```bash
   # Install UV if you do not have it:
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # Install project dependencies:
   uv sync
   ```

3. **Configure your API key / API 키 설정**
   ```bash
   cp .env.example .env
   # Edit .env and add your Apify API key
   # Get your free API key at: https://apify.com?fpr=9n7kx3
   ```

4. **Run an example / 예제 실행**
   ```bash
   # Single query example:
   uv run python naver-search-api-example.py

   # Batch multi-query example (searches several terms in one run):
   uv run python naver-search-api-batch-example.py
   ```

> **한국어:** 위 단계를 따라 저장소를 복제하고, UV로 의존성을 설치하고, `.env` 파일에 API 키를 넣은 뒤 예제를 실행하세요. `naver-search-api-example.py`는 단일 검색어 예제이고, `naver-search-api-batch-example.py`는 한 번의 실행으로 여러 검색어를 처리하는 일괄(batch) 예제입니다.

### Alternative: set the API key directly / 대안: API 키 직접 설정
```bash
export APIFY_API_TOKEN="your_api_key_here"
uv run python naver-search-api-example.py
```

> **한국어:** `.env` 파일 대신 환경 변수 `APIFY_API_TOKEN`에 키를 직접 설정해서 실행할 수도 있습니다.

## Why Use This Naver Search API? / 왜 이 네이버 검색 API인가?

Naver dominates search in Korea, and its results look nothing like Google's. This API gives you that data as structured rows instead of brittle HTML.

One call, many verticals. The integrated `nexearch` view returns ads, web, shopping, and news blocks at once; the single-vertical views (`web`, `news`, `image`, `video`) drill in and paginate.

Clean, predictable JSON. Every row carries a `result_type`, the `query` it came from, the `where` vertical, and a `position`, so it loads straight into a dataframe, a database, or an AI pipeline.

Built for batch work. Pass a list of queries and the API runs each one and tags every row with its source query.

MCP-ready. AI agents can discover and call it as a tool through the hosted Apify MCP server.

> **한국어:** 네이버는 한국 검색 시장을 장악하고 있으며, 그 결과는 구글과 전혀 다릅니다. 이 API는 깨지기 쉬운 HTML 대신 구조화된 데이터 행으로 그 데이터를 제공합니다.
>
> - **한 번의 호출, 여러 영역.** 통합 `nexearch` 뷰는 광고, 웹, 쇼핑, 뉴스 블록을 한 번에 반환하고, 단일 영역 뷰(`web`, `news`, `image`, `video`)는 세부적으로 파고들며 페이지를 넘깁니다.
> - **깔끔하고 예측 가능한 JSON.** 모든 행에는 `result_type`, 원본 `query`, `where` 영역, `position`이 포함되어 데이터프레임, 데이터베이스, AI 파이프라인에 바로 적재됩니다.
> - **일괄 처리에 최적화.** 검색어 목록을 넘기면 API가 각각을 실행하고 모든 행에 원본 검색어를 태깅합니다.
> - **MCP 지원.** AI 에이전트가 호스팅된 Apify MCP 서버를 통해 이 도구를 발견하고 호출할 수 있습니다.

## Features / 주요 기능

### Core Capabilities / 핵심 기능
- Five verticals: integrated (nexearch), web, news, image, video
- Shopping results (price, rating, reviews) inline in the integrated view
- Bulk multi-query search in one run
- Pagination handled for you, up to 300 results per query

> **한국어:**
> - 다섯 가지 영역: 통합(nexearch), 웹, 뉴스, 이미지, 동영상
> - 통합 뷰에 인라인으로 표시되는 쇼핑 결과(가격, 평점, 리뷰)
> - 한 번의 실행으로 여러 검색어 일괄 검색
> - 검색어당 최대 300개 결과까지 자동 페이지네이션

### Data Quality / 데이터 품질
- Stable `result_type` tagging across all verticals
- News rows include publisher and date; video rows include channel, duration, views
- Image rows include full-size URL and dimensions
- Clean structured JSON, one row per result

> **한국어:**
> - 모든 영역에서 일관된 `result_type` 태깅
> - 뉴스 행은 언론사와 날짜를, 동영상 행은 채널, 재생 시간, 조회수를 포함
> - 이미지 행은 원본 크기 URL과 가로/세로 크기를 포함
> - 결과당 한 행으로 구성된 깔끔한 구조화 JSON

## Usage Examples / 사용 예시

### Basic Example / 기본 예시
```json
{
  "query": "서울 맛집",
  "where": "web",
  "maxResultsPerQuery": 10
}
```

### Advanced Example: batch queries / 고급 예시: 일괄 검색어
```json
{
  "queries": ["삼성전자", "LG전자", "SK하이닉스"],
  "where": "news",
  "maxResultsPerQuery": 50
}
```

> **한국어:** 기본 예시는 단일 `query`로 검색합니다. 고급 예시는 `queries` 목록으로 여러 검색어를 한 번에 검색하며, 각 결과 행에는 원본 검색어가 태깅됩니다. 실행 가능한 일괄 검색 스크립트는 `naver-search-api-batch-example.py`를 참고하세요.

## Input Parameters / 입력 파라미터

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `query` | `str` | one of query/queries | - | A single search query, in Korean or any language, e.g. `서울 맛집`. |
| `queries` | `list[str]` | one of query/queries | - | A batch of queries. Merged with `query` and de-duplicated. |
| `where` | `str` | no | `"nexearch"` | Vertical: `nexearch`, `web`, `news`, `image`, or `video`. |
| `maxResultsPerQuery` | `int` | no | `30` | Result rows per query (maximum 300). |

> **한국어 (입력 파라미터):**
>
> | 파라미터 | 타입 | 필수 여부 | 기본값 | 설명 |
> |-----------|------|----------|---------|-------------|
> | `query` | `str` | query/queries 중 하나 | - | 단일 검색어. 한국어 또는 모든 언어 가능, 예: `서울 맛집`. |
> | `queries` | `list[str]` | query/queries 중 하나 | - | 검색어 묶음. `query`와 병합되고 중복 제거됩니다. |
> | `where` | `str` | 아니오 | `"nexearch"` | 검색 영역: `nexearch`, `web`, `news`, `image`, `video`. |
> | `maxResultsPerQuery` | `int` | 아니오 | `30` | 검색어당 결과 행 수 (최대 300). |

## Output Format / 출력 형식

Each item in the dataset is a single result row:

```json
{
  "result_type": "web_organic",
  "query": "서울 맛집",
  "where": "web",
  "position": 1,
  "title": "서울 맛집 베스트 30",
  "link": "https://example.co.kr/seoul-restaurants",
  "snippet": "서울에서 꼭 가봐야 할 맛집을 정리했습니다 ...",
  "source": "example.co.kr",
  "displayed_link": "example.co.kr"
}
```

A shopping row adds `price`, `rating`, `reviews`, and `stores`; a video row adds `channel`, `duration`, and `views`; an image row adds `original`, `width`, and `height`.

> **한국어:** 데이터셋의 각 항목은 하나의 결과 행입니다. 쇼핑 행에는 `price`, `rating`, `reviews`, `stores`가 추가되고, 동영상 행에는 `channel`, `duration`, `views`가, 이미지 행에는 `original`, `width`, `height`가 추가됩니다.

---

<!-- The five install sections below are the canonical MCP install copy. -->

## Install in Claude Cowork Desktop / Claude Cowork 데스크톱에 설치

![Install in Claude Cowork Desktop](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_desktop.png)

Cowork is the desktop app's automation mode. To give it the Naver Search API as a tool, add the Apify MCP server as a connector.

1. Open the Claude desktop app and go to **Settings → Connectors** (or **Settings → Developer → Edit Config** to edit `claude_desktop_config.json` directly).
   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`
2. Add the Apify MCP server, preloaded with only this Actor:

```json
{
  "mcpServers": {
    "apify": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://mcp.apify.com/?tools=actors,docs,johnvc/naver-search-api"
      ]
    }
  }
}
```

3. Restart the app. When Cowork first calls the tool, complete the OAuth prompt in your browser, or add your Apify API token in the connector settings to skip OAuth.
4. In a Cowork chat, confirm the tool is available and ask it to run the Naver Search API.

Download the desktop app and start a free trial: https://claude.ai/referral/uIlpa7nPLg
More help: https://docs.apify.com/platform/integrations/claude-desktop

> **한국어:** Cowork는 데스크톱 앱의 자동화 모드입니다. 네이버 검색 API를 도구로 사용하려면 Apify MCP 서버를 커넥터로 추가하세요.
> 1. Claude 데스크톱 앱을 열고 **Settings → Connectors**로 이동합니다 (또는 **Settings → Developer → Edit Config**에서 `claude_desktop_config.json`을 직접 편집).
> 2. 위 JSON처럼 이 Actor만 미리 로드한 Apify MCP 서버를 추가합니다.
> 3. 앱을 재시작합니다. Cowork가 도구를 처음 호출할 때 브라우저에서 OAuth를 완료하거나, 커넥터 설정에 Apify API 토큰을 추가해 OAuth를 건너뛸 수 있습니다.
> 4. Cowork 채팅에서 도구가 사용 가능한지 확인하고 네이버 검색 API 실행을 요청하세요.
>
> 데스크톱 앱을 내려받고 무료 체험을 시작하세요: https://claude.ai/referral/uIlpa7nPLg

---

## Install in Claude Code / Claude Code에 설치

![Install in Claude Code](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_code.png)

Claude Code is the command-line tool. Add the Actor's MCP server with one command:

```bash
claude mcp add --transport http apify \
  "https://mcp.apify.com/?tools=actors,docs,johnvc/naver-search-api"
```

To use a token instead of browser OAuth:

```bash
claude mcp add --transport http apify \
  "https://mcp.apify.com/?tools=actors,docs,johnvc/naver-search-api" \
  --header "Authorization: Bearer YOUR_APIFY_TOKEN"
```

Then verify with `claude mcp list`, or run `/mcp` inside a session. Ask Claude Code to call the Naver Search API.

Try Claude Code free: https://claude.ai/referral/uIlpa7nPLg
Claude Code MCP docs: https://code.claude.com/docs/en/mcp

> **한국어:** Claude Code는 명령줄 도구입니다. 위 명령 한 줄로 Actor의 MCP 서버를 추가하세요. 브라우저 OAuth 대신 토큰을 쓰려면 `--header`로 `Authorization: Bearer YOUR_APIFY_TOKEN`을 추가합니다. 이후 `claude mcp list`로 확인하거나 세션 안에서 `/mcp`를 실행한 뒤, Claude Code에 네이버 검색 API 호출을 요청하세요.
>
> Claude Code를 무료로 사용해 보세요: https://claude.ai/referral/uIlpa7nPLg

---

## Install in Claude (website) / Claude (웹사이트)에 설치

![Install in Claude (website)](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_ai.png)

On claude.ai you add Apify as a connector, then enable just this Actor's tool.

1. Go to **Settings → Connectors → Browse connectors** and search for **Apify MCP server**. Install it (enable or update if prompted).
2. When connecting, authenticate with your Apify API token, and enable the tool `johnvc/naver-search-api`.
3. In any chat, open **+ → Connectors** and turn on **Apify**.
4. Alternatively, choose **Add custom connector** and paste the full MCP URL `https://mcp.apify.com/?tools=actors,docs,johnvc/naver-search-api`, using OAuth when prompted.
5. Ask Claude to run the Naver Search API.

Open Claude on the web: https://claude.ai

> **한국어:** claude.ai에서는 Apify를 커넥터로 추가한 뒤 이 Actor의 도구만 활성화합니다.
> 1. **Settings → Connectors → Browse connectors**로 이동해 **Apify MCP server**를 검색하고 설치합니다.
> 2. 연결할 때 Apify API 토큰으로 인증하고 `johnvc/naver-search-api` 도구를 활성화합니다.
> 3. 아무 채팅에서 **+ → Connectors**를 열고 **Apify**를 켭니다.
> 4. 또는 **Add custom connector**를 선택해 전체 MCP URL `https://mcp.apify.com/?tools=actors,docs,johnvc/naver-search-api`를 붙여넣고 OAuth로 인증합니다.
> 5. Claude에 네이버 검색 API 실행을 요청하세요.
>
> 웹에서 Claude 열기: https://claude.ai

---

## Install in Cursor / Cursor에 설치

![Install in Cursor](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_cursor.png)

Cursor reads MCP servers from a project file at `.cursor/mcp.json`.

1. In your project, create `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "apify": {
      "url": "https://mcp.apify.com/?tools=actors,docs,johnvc/naver-search-api"
    }
  }
}
```

2. If you prefer token auth over browser OAuth, add a header:

```json
{
  "mcpServers": {
    "apify": {
      "url": "https://mcp.apify.com/?tools=actors,docs,johnvc/naver-search-api",
      "headers": { "Authorization": "Bearer YOUR_APIFY_TOKEN" }
    }
  }
}
```

3. Open **Cursor → Settings → MCP** and confirm the **apify** server is connected (green dot).
4. In Composer or Chat, ask Cursor to call the Naver Search API.

New to Cursor? Get it here: https://cursor.com/referral?code=XQP4VBLI3NNX

> **한국어:** Cursor는 프로젝트 파일 `.cursor/mcp.json`에서 MCP 서버를 읽습니다.
> 1. 프로젝트에 위 JSON 내용으로 `.cursor/mcp.json`을 생성합니다.
> 2. 브라우저 OAuth 대신 토큰 인증을 원하면 `headers`에 `Authorization: Bearer YOUR_APIFY_TOKEN`을 추가합니다.
> 3. **Cursor → Settings → MCP**를 열고 **apify** 서버가 연결되었는지(초록 점) 확인합니다.
> 4. Composer 또는 Chat에서 Cursor에 네이버 검색 API 호출을 요청하세요.
>
> Cursor가 처음이신가요? 여기에서 받으세요: https://cursor.com/referral?code=XQP4VBLI3NNX

---

## Install in ChatGPT / ChatGPT에 설치

![Install in ChatGPT](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_ChatGPT.png)

ChatGPT connects to the Apify MCP server through Developer mode (available on ChatGPT Pro, Plus, Business, Enterprise, and Education plans).

1. Click your profile icon, then go to **Settings > Apps**. If you do not see a **Create app** button, open **Advanced settings** and enable **Developer mode**.
2. Click **Create app** and fill out the form:
   - **Name:** Apify
   - **MCP Server URL:** `https://mcp.apify.com/?tools=actors,docs,johnvc/naver-search-api`
   - **Authentication:** OAuth
3. Click **Create** and authorize the connection with Apify.
4. To use the app in a conversation, click **+** in the chat, choose **Developer mode**, and select **Apify**.

More help: https://docs.apify.com/platform/integrations/mcp

> **한국어:** ChatGPT는 개발자 모드(ChatGPT Pro, Plus, Business, Enterprise, Education 플랜에서 사용 가능)를 통해 Apify MCP 서버에 연결합니다.
> 1. 프로필 아이콘을 클릭한 뒤 **Settings > Apps**로 이동합니다. **Create app** 버튼이 보이지 않으면 **Advanced settings**에서 **Developer mode**를 켭니다.
> 2. **Create app**을 클릭하고 양식을 작성합니다. 이름은 Apify, MCP 서버 URL은 `https://mcp.apify.com/?tools=actors,docs,johnvc/naver-search-api`, 인증은 OAuth로 설정합니다.
> 3. **Create**를 클릭하고 Apify 연결을 승인합니다.
> 4. 대화에서 사용하려면 채팅의 **+**를 클릭하고 **Developer mode**를 선택한 뒤 **Apify**를 고릅니다.

---

[**Made with care**](https://apify.com/johnvc?fpr=9n7kx3)

*Use the Naver Search API to power your Korean-market data workflows with reliable, structured results.*

*네이버 검색 API로 신뢰할 수 있는 구조화된 결과를 활용해 한국 시장 데이터 워크플로를 구축하세요.*

## Featured Tasks

Ready-to-run examples on the Apify Store.

- [Export Naver Search Results to CSV](https://apify.com/johnvc/naver-search-api/examples/export-naver-search-results-to-csv?fpr=9n7kx3)

Last Updated: 2026.07.05
