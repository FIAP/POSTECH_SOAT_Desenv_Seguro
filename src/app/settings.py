import os

DEVEX_WEBHOOK_SECRET = os.getenv("DEVEX_WEBHOOK_SECRET")
DEVEX_WEBHOOK_HOST = os.getenv("DEVEX_WEBHOOK_HOST", "https://moonlight-pipeline-webhook.tekton.ppay.me/microservices")
DEVEX_REQUEST_TIMEOUT_DEFAULT = int(os.getenv("DEVEX_REQUEST_TIMEOUT_DEFAULT", 20))
DEVEX_INSTALLATION_ID = os.getenv("DEVEX_INSTALLATION_ID", "26158850")
DEVEX_GITHUB_HOST = os.getenv("DEVEX_GITHUB_HOST", "https://api.github.com")
