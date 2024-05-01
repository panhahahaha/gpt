import json

# 存储提供的 JSON 数据字符串
json_data = '''
[
    {"id":"chatcmpl-9GJJgkoKsYO32QbUwzEa5pnBLS1Mp","object":"chat.completion.chunk","created":1713674528,"model":"gpt-35-turbo","system_fingerprint":null,"choices":[{"index":0,"delta":{"role":"assistant","content":""},"logprobs":null,"finish_reason":null}]},
    {"id":"chatcmpl-9GJJgkoKsYO32QbUwzEa5pnBLS1Mp","object":"chat.completion.chunk","created":1713674528,"model":"gpt-35-turbo","system_fingerprint":null,"choices":[{"index":0,"delta":{"content":"æ"},"logprobs":null,"finish_reason":null}]},
    {"id":"chatcmpl-9GJJgkoKsYO32QbUwzEa5pnBLS1Mp","object":"chat.completion.chunk","created":1713674528,"model":"gpt-35-turbo","system_fingerprint":null,"choices":[{"index":0,"delta":{"content":"ï¼"},"logprobs":null,"finish_reason":null}]},
    {"id":"chatcmpl-9GJJgkoKsYO32QbUwzEa5pnBLS1Mp","object":"chat.completion.chunk","created":1713674528,"model":"gpt-35-turbo","system_fingerprint":null,"choices":[{"index":0,"delta":{"content":"V"},"logprobs":null,"finish_reason":null}]},
    {"id":"chatcmpl-9GJJgkoKsYO32QbUwzEa5pnBLS1Mp","object":"chat.completion.chunk","created":1713674528,"model":"gpt-35-turbo","system_fingerprint":null,"choices":[{"index":0,"delta":{"content":"ï¼"},"logprobs":null,"finish_reason":null}]},
    {"id":"chatcmpl-9GJJgkoKsYO32QbUwzEa5pnBLS1Mp","object":"chat.completion.chunk","created":1713674528,"model":"gpt-35-turbo","system_fingerprint":null,"choices":[{"index":0,"delta":{"content":"è°¨"},"logprobs":null,"finish_reason":null}]},
    {"id":"chatcmpl-9GJJgkoKsYO32QbUwzEa5pnBLS1Mp","object":"chat.completion.chunk","created":1713674528,"model":"gpt-35-turbo","system_fingerprint":null,"choices":[{"index":0,"delta":{"content":"åº"},"logprobs":null,"finish_reason":null}]},
    {"id":"chatcmpl-9GJJgkoKsYO32QbUwzEa5pnBLS1Mp","object":"chat.completion.chunk","created":1713674528,"model":"gpt-35-turbo","system_fingerprint":null,"choices":[{"index":0,"delta":{"content":"ä¸¥"},"logprobs":null,"finish_reason":null}]},
    {"id":"chatcmpl-9GJJgkoKsYO32QbUwzEa5pnBLS1Mp","object":"chat.completion.chunk","created":1713674528,"model":"gpt-35-turbo","system_fingerprint":null,"choices":[{"index":0,"delta":{"content":"å®£"},"logprobs":null,"finish_reason":null}]},
    {"id":"chatcmpl-9GJJgkoKsYO32QbUwzEa5pnBLS1Mp","object":"chat.completion.chunk","created":1713674528,"model":"gpt-35-turbo","system_fingerprint":null,"choices":[{"index":0,"delta":{"content":"èª"},"logprobs":null,"finish_reason":null}]},
    {"id":"chatcmpl-9GJJgkoKsYO32QbUwzEa5pnBLS1Mp","object":"chat.completion.chunk","created":1713674528,"model":"gpt-35-turbo","system_fingerprint":null,"choices":[{"index":0,"delta":{"content":"ã"},"logprobs":null,"finish_reason":null}]},
    {"id":"chatcmpl-9GJJgkoKsYO32QbUwzEa5pnBLS1Mp","object":"chat.completion.chunk","created":1713674528,"model":"gpt-35-turbo","system_fingerprint":null,"choices":[{"index":0,"delta":{},"logprobs":null,"finish_reason":"stop"}]}
]
'''

# 解析 JSON 数据并提取 "content" 字段的值
for data in json.loads(json_data):
    choices = data.get("choices", [])
    for choice in choices:
        delta = choice.get("delta", {})
        content = delta.get("content", None)
        if content is not None:
            print("Content:", content)
print(b"\xe5\xba\x84".decode("utf-8"))