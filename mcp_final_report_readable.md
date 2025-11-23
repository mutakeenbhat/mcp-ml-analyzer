# MCP Repository Analyzer — Final Report

## Transport Inference

- **Type:** websocket
- **Confidence:** 0.85

## Tools Overview (325 tools)

### 🛠️ Tool: **cli**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\clients\simple-auth-client\mcp_simple_auth_client\main.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: ['webbrowser.open']
- Network: []
- Subprocess: []
- Env: ['os.getenv']
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "cli",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **main**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\clients\simple-chatbot\mcp_simple_chatbot\main.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "title": "None"
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "title": "None"
  }
}
```

#### Syscalls
- Filesystem: ['open']
- Network: ['httpx.Client', 'client.post']
- Subprocess: []
- Env: ['os.getenv']
- Severity: **medium-high**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "main",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **name_shrimp**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\fastmcp\complex_inputs.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "tank": {
      "type": "object",
      "properties": {
        "shrimp": {
          "type": "array",
          "items": {
            "type": "object",
            "title": "Shrimp"
          }
        }
      },
      "required": [
        "shrimp"
      ]
    },
    "extra_names": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "max_length": 10
    }
  },
  "required": [
    "extra_names",
    "tank"
  ]
}
```

#### Output Schema
```json
{
  "type": "array",
  "items": {
    "type": "string"
  }
}
```

#### Payload Shape
```json
{
  "request": {
    "tank": {
      "type": "object",
      "properties": {
        "shrimp": {
          "type": "array",
          "items": {
            "type": "object",
            "title": "Shrimp"
          }
        }
      },
      "required": [
        "shrimp"
      ]
    },
    "extra_names": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "max_length": 10
    }
  },
  "response": {
    "type": "array",
    "items": {
      "type": "string"
    }
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "name_shrimp",
    "arguments": {
      "tank": {},
      "extra_names": []
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **desktop**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\fastmcp\desktop.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "array",
  "items": {
    "type": "string"
  }
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "array",
    "items": {
      "type": "string"
    }
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "desktop",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **sum**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\fastmcp\desktop.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "a": {
      "type": "integer"
    },
    "b": {
      "type": "integer"
    }
  },
  "required": [
    "a",
    "b"
  ]
}
```

#### Output Schema
```json
{
  "type": "integer"
}
```

#### Payload Shape
```json
{
  "request": {
    "a": {
      "type": "integer"
    },
    "b": {
      "type": "integer"
    }
  },
  "response": {
    "type": "integer"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "sum",
    "arguments": {
      "a": 0,
      "b": 0
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **echo**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\fastmcp\direct_call_tool_result_return.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "text": {
      "type": "string"
    }
  },
  "required": [
    "text"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "title": "Annotated[CallToolResult, EchoResponse]"
}
```

#### Payload Shape
```json
{
  "request": {
    "text": {
      "type": "string"
    }
  },
  "response": {
    "type": "object",
    "title": "Annotated[CallToolResult, EchoResponse]"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "echo",
    "arguments": {
      "text": "<text_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **echo_tool**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\fastmcp\echo.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "text": {
      "type": "string"
    }
  },
  "required": [
    "text"
  ]
}
```

#### Output Schema
```json
{
  "type": "string"
}
```

#### Payload Shape
```json
{
  "request": {
    "text": {
      "type": "string"
    }
  },
  "response": {
    "type": "string"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "echo_tool",
    "arguments": {
      "text": "<text_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **echo_resource**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\fastmcp\echo.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "string"
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "string"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "echo_resource",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **echo_template**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\fastmcp\echo.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "text": {
      "type": "string"
    }
  },
  "required": [
    "text"
  ]
}
```

#### Output Schema
```json
{
  "type": "string"
}
```

#### Payload Shape
```json
{
  "request": {
    "text": {
      "type": "string"
    }
  },
  "response": {
    "type": "string"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "echo_template",
    "arguments": {
      "text": "<text_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **echo_prompt**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\fastmcp\echo.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "text": {
      "type": "string"
    }
  },
  "required": [
    "text"
  ]
}
```

#### Output Schema
```json
{
  "type": "string"
}
```

#### Payload Shape
```json
{
  "request": {
    "text": {
      "type": "string"
    }
  },
  "response": {
    "type": "string"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "echo_prompt",
    "arguments": {
      "text": "<text_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **demo_tool**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\fastmcp\icons_demo.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "message": {
      "type": "string"
    }
  },
  "required": [
    "message"
  ]
}
```

#### Output Schema
```json
{
  "type": "string"
}
```

#### Payload Shape
```json
{
  "request": {
    "message": {
      "type": "string"
    }
  },
  "response": {
    "type": "string"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "demo_tool",
    "arguments": {
      "message": "<message_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **readme_resource**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\fastmcp\icons_demo.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "string"
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "string"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "readme_resource",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **prompt_with_icon**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\fastmcp\icons_demo.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "text": {
      "type": "string"
    }
  },
  "required": [
    "text"
  ]
}
```

#### Output Schema
```json
{
  "type": "string"
}
```

#### Payload Shape
```json
{
  "request": {
    "text": {
      "type": "string"
    }
  },
  "response": {
    "type": "string"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "prompt_with_icon",
    "arguments": {
      "text": "<text_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **multi_icon_tool**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\fastmcp\icons_demo.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "action": {
      "type": "string"
    }
  },
  "required": [
    "action"
  ]
}
```

#### Output Schema
```json
{
  "type": "string"
}
```

#### Payload Shape
```json
{
  "request": {
    "action": {
      "type": "string"
    }
  },
  "response": {
    "type": "string"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "multi_icon_tool",
    "arguments": {
      "action": "<action_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **cosine_similarity**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\fastmcp\memory.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "a": {
      "type": "array",
      "items": {
        "type": "number"
      }
    },
    "b": {
      "type": "array",
      "items": {
        "type": "number"
      }
    }
  },
  "required": [
    "a",
    "b"
  ]
}
```

#### Output Schema
```json
{
  "type": "number"
}
```

#### Payload Shape
```json
{
  "request": {
    "a": {
      "type": "array",
      "items": {
        "type": "number"
      }
    },
    "b": {
      "type": "array",
      "items": {
        "type": "number"
      }
    }
  },
  "response": {
    "type": "number"
  }
}
```

#### Syscalls
- Filesystem: ['PROFILE_DIR.mkdir']
- Network: []
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "cosine_similarity",
    "arguments": {
      "a": [],
      "b": []
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **greet_user**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\fastmcp\parameter_descriptions.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "name": {
      "type": "string"
    },
    "title": {
      "type": "string"
    },
    "times": {
      "type": "integer"
    }
  }
}
```

#### Output Schema
```json
{
  "type": "string"
}
```

#### Payload Shape
```json
{
  "request": {
    "name": {
      "type": "string"
    },
    "title": {
      "type": "string"
    },
    "times": {
      "type": "integer"
    }
  },
  "response": {
    "type": "string"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "greet_user",
    "arguments": {
      "name": "<name_str>",
      "title": "<title_str>",
      "times": 0
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **sum**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\fastmcp\readme-quickstart.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "a": {
      "type": "integer"
    },
    "b": {
      "type": "integer"
    }
  },
  "required": [
    "a",
    "b"
  ]
}
```

#### Output Schema
```json
{
  "type": "integer"
}
```

#### Payload Shape
```json
{
  "request": {
    "a": {
      "type": "integer"
    },
    "b": {
      "type": "integer"
    }
  },
  "response": {
    "type": "integer"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "sum",
    "arguments": {
      "a": 0,
      "b": 0
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **get_greeting**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\fastmcp\readme-quickstart.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "name": {
      "type": "string"
    }
  },
  "required": [
    "name"
  ]
}
```

#### Output Schema
```json
{
  "type": "string"
}
```

#### Payload Shape
```json
{
  "request": {
    "name": {
      "type": "string"
    }
  },
  "response": {
    "type": "string"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "get_greeting",
    "arguments": {
      "name": "<name_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **take_screenshot**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\fastmcp\screenshot.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "properties": {}
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "take_screenshot",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **echo**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\fastmcp\simple_echo.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "text": {
      "type": "string"
    }
  },
  "required": [
    "text"
  ]
}
```

#### Output Schema
```json
{
  "type": "string"
}
```

#### Payload Shape
```json
{
  "request": {
    "text": {
      "type": "string"
    }
  },
  "response": {
    "type": "string"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "echo",
    "arguments": {
      "text": "<text_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **text_me**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\fastmcp\text_me.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "text_content": {
      "type": "string"
    }
  },
  "required": [
    "text_content"
  ]
}
```

#### Output Schema
```json
{
  "type": "string"
}
```

#### Payload Shape
```json
{
  "request": {
    "text_content": {
      "type": "string"
    }
  },
  "response": {
    "type": "string"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['httpx.Client', 'client.post']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "text_me",
    "arguments": {
      "text_content": "<text_content_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **hello_unicode**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\fastmcp\unicode_example.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "name": {
      "type": "string"
    },
    "greeting": {
      "type": "string"
    }
  }
}
```

#### Output Schema
```json
{
  "type": "string"
}
```

#### Payload Shape
```json
{
  "request": {
    "name": {
      "type": "string"
    },
    "greeting": {
      "type": "string"
    }
  },
  "response": {
    "type": "string"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "hello_unicode",
    "arguments": {
      "name": "<name_str>",
      "greeting": "<greeting_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **list_emoji_categories**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\fastmcp\unicode_example.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "array",
  "items": {
    "type": "string"
  }
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "array",
    "items": {
      "type": "string"
    }
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "list_emoji_categories",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **multilingual_hello**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\fastmcp\unicode_example.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "string"
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "string"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "multilingual_hello",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **get_weather**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\fastmcp\weather_structured.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "city": {
      "type": "string"
    }
  },
  "required": [
    "city"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "properties": {
    "temperature": {
      "type": "number"
    },
    "humidity": {
      "type": "number"
    },
    "condition": {
      "type": "string"
    },
    "wind_speed": {
      "type": "number"
    },
    "location": {
      "type": "string"
    },
    "timestamp": {
      "type": "object",
      "title": "datetime"
    }
  },
  "required": [
    "temperature",
    "humidity",
    "condition",
    "wind_speed",
    "location",
    "timestamp"
  ]
}
```

#### Payload Shape
```json
{
  "request": {
    "city": {
      "type": "string"
    }
  },
  "response": {
    "type": "object",
    "properties": {
      "temperature": {
        "type": "number"
      },
      "humidity": {
        "type": "number"
      },
      "condition": {
        "type": "string"
      },
      "wind_speed": {
        "type": "number"
      },
      "location": {
        "type": "string"
      },
      "timestamp": {
        "type": "object",
        "title": "datetime"
      }
    },
    "required": [
      "temperature",
      "humidity",
      "condition",
      "wind_speed",
      "location",
      "timestamp"
    ]
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "get_weather",
    "arguments": {
      "city": "<city_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **get_weather_summary**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\fastmcp\weather_structured.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "city": {
      "type": "string"
    }
  },
  "required": [
    "city"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "properties": {
    "city": {
      "type": "string"
    },
    "temp_c": {
      "type": "number"
    },
    "description": {
      "type": "string"
    }
  },
  "required": [
    "city",
    "temp_c",
    "description"
  ]
}
```

#### Payload Shape
```json
{
  "request": {
    "city": {
      "type": "string"
    }
  },
  "response": {
    "type": "object",
    "properties": {
      "city": {
        "type": "string"
      },
      "temp_c": {
        "type": "number"
      },
      "description": {
        "type": "string"
      }
    },
    "required": [
      "city",
      "temp_c",
      "description"
    ]
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "get_weather_summary",
    "arguments": {
      "city": "<city_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **get_weather_metrics**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\fastmcp\weather_structured.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "cities": {
      "type": "array",
      "items": {
        "type": "string"
      }
    }
  },
  "required": [
    "cities"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "additionalProperties": {
    "type": "string",
    "guessed": true
  }
}
```

#### Payload Shape
```json
{
  "request": {
    "cities": {
      "type": "array",
      "items": {
        "type": "string"
      }
    }
  },
  "response": {
    "type": "object",
    "additionalProperties": {
      "type": "string",
      "guessed": true
    }
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "get_weather_metrics",
    "arguments": {
      "cities": []
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **get_weather_alerts**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\fastmcp\weather_structured.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "region": {
      "type": "string"
    }
  },
  "required": [
    "region"
  ]
}
```

#### Output Schema
```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "severity": {
        "type": "string"
      },
      "title": {
        "type": "string"
      },
      "description": {
        "type": "string"
      },
      "affected_areas": {
        "type": "array",
        "items": {
          "type": "string"
        }
      },
      "valid_until": {
        "type": "object",
        "title": "datetime"
      }
    },
    "required": [
      "severity",
      "title",
      "description",
      "affected_areas",
      "valid_until"
    ]
  }
}
```

#### Payload Shape
```json
{
  "request": {
    "region": {
      "type": "string"
    }
  },
  "response": {
    "type": "array",
    "items": {
      "type": "object",
      "properties": {
        "severity": {
          "type": "string"
        },
        "title": {
          "type": "string"
        },
        "description": {
          "type": "string"
        },
        "affected_areas": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "valid_until": {
          "type": "object",
          "title": "datetime"
        }
      },
      "required": [
        "severity",
        "title",
        "description",
        "affected_areas",
        "valid_until"
      ]
    }
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "get_weather_alerts",
    "arguments": {
      "region": "<region_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **get_temperature**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\fastmcp\weather_structured.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "city": {
      "type": "string"
    },
    "unit": {
      "type": "string"
    }
  },
  "required": [
    "city"
  ]
}
```

#### Output Schema
```json
{
  "type": "number"
}
```

#### Payload Shape
```json
{
  "request": {
    "city": {
      "type": "string"
    },
    "unit": {
      "type": "string"
    }
  },
  "response": {
    "type": "number"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "get_temperature",
    "arguments": {
      "city": "<city_str>",
      "unit": "<unit_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **get_weather_stats**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\fastmcp\weather_structured.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "city": {
      "type": "string"
    },
    "days": {
      "type": "integer"
    }
  },
  "required": [
    "city"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "properties": {
    "location": {
      "type": "string"
    },
    "period_days": {
      "type": "integer"
    },
    "temperature": {
      "type": "object",
      "properties": {
        "high": {
          "type": "number"
        },
        "low": {
          "type": "number"
        },
        "mean": {
          "type": "number"
        }
      },
      "required": [
        "high",
        "low",
        "mean"
      ]
    },
    "humidity": {
      "type": "object",
      "properties": {
        "high": {
          "type": "number"
        },
        "low": {
          "type": "number"
        },
        "mean": {
          "type": "number"
        }
      },
      "required": [
        "high",
        "low",
        "mean"
      ]
    },
    "precipitation_mm": {
      "type": "number"
    }
  },
  "required": [
    "location",
    "period_days",
    "temperature",
    "humidity",
    "precipitation_mm"
  ]
}
```

#### Payload Shape
```json
{
  "request": {
    "city": {
      "type": "string"
    },
    "days": {
      "type": "integer"
    }
  },
  "response": {
    "type": "object",
    "properties": {
      "location": {
        "type": "string"
      },
      "period_days": {
        "type": "integer"
      },
      "temperature": {
        "type": "object",
        "properties": {
          "high": {
            "type": "number"
          },
          "low": {
            "type": "number"
          },
          "mean": {
            "type": "number"
          }
        },
        "required": [
          "high",
          "low",
          "mean"
        ]
      },
      "humidity": {
        "type": "object",
        "properties": {
          "high": {
            "type": "number"
          },
          "low": {
            "type": "number"
          },
          "mean": {
            "type": "number"
          }
        },
        "required": [
          "high",
          "low",
          "mean"
        ]
      },
      "precipitation_mm": {
        "type": "number"
      }
    },
    "required": [
      "location",
      "period_days",
      "temperature",
      "humidity",
      "precipitation_mm"
    ]
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "get_weather_stats",
    "arguments": {
      "city": "<city_str>",
      "days": 0
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **test_simple_text**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\servers\everything-server\mcp_everything_server\server.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "string"
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "string"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['client.get']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "test_simple_text",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **test_image_content**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\servers\everything-server\mcp_everything_server\server.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "type": {
        "type": "string",
        "enum": [
          "image"
        ]
      },
      "data": {
        "type": "string"
      },
      "mimeType": {
        "type": "string"
      },
      "annotations": {
        "oneOf": [
          {
            "type": "object",
            "properties": {
              "audience": {
                "type": "array",
                "items": {
                  "type": "object",
                  "title": "Role"
                }
              },
              "priority": {
                "type": "object",
                "title": "Annotated[float, Field(ge=0.0, le=1.0)] | None"
              }
            }
          }
        ]
      },
      "meta": {
        "type": "object",
        "additionalProperties": {
          "type": "string",
          "guessed": true
        }
      }
    },
    "required": [
      "type",
      "data",
      "mimeType",
      "annotations",
      "meta"
    ]
  }
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "array",
    "items": {
      "type": "object",
      "properties": {
        "type": {
          "type": "string",
          "enum": [
            "image"
          ]
        },
        "data": {
          "type": "string"
        },
        "mimeType": {
          "type": "string"
        },
        "annotations": {
          "oneOf": [
            {
              "type": "object",
              "properties": {
                "audience": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "title": "Role"
                  }
                },
                "priority": {
                  "type": "object",
                  "title": "Annotated[float, Field(ge=0.0, le=1.0)] | None"
                }
              }
            }
          ]
        },
        "meta": {
          "type": "object",
          "additionalProperties": {
            "type": "string",
            "guessed": true
          }
        }
      },
      "required": [
        "type",
        "data",
        "mimeType",
        "annotations",
        "meta"
      ]
    }
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['client.get']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "test_image_content",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **test_audio_content**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\servers\everything-server\mcp_everything_server\server.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "type": {
        "type": "string",
        "enum": [
          "audio"
        ]
      },
      "data": {
        "type": "string"
      },
      "mimeType": {
        "type": "string"
      },
      "annotations": {
        "oneOf": [
          {
            "type": "object",
            "properties": {
              "audience": {
                "type": "array",
                "items": {
                  "type": "object",
                  "title": "Role"
                }
              },
              "priority": {
                "type": "object",
                "title": "Annotated[float, Field(ge=0.0, le=1.0)] | None"
              }
            }
          }
        ]
      },
      "meta": {
        "type": "object",
        "additionalProperties": {
          "type": "string",
          "guessed": true
        }
      }
    },
    "required": [
      "type",
      "data",
      "mimeType",
      "annotations",
      "meta"
    ]
  }
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "array",
    "items": {
      "type": "object",
      "properties": {
        "type": {
          "type": "string",
          "enum": [
            "audio"
          ]
        },
        "data": {
          "type": "string"
        },
        "mimeType": {
          "type": "string"
        },
        "annotations": {
          "oneOf": [
            {
              "type": "object",
              "properties": {
                "audience": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "title": "Role"
                  }
                },
                "priority": {
                  "type": "object",
                  "title": "Annotated[float, Field(ge=0.0, le=1.0)] | None"
                }
              }
            }
          ]
        },
        "meta": {
          "type": "object",
          "additionalProperties": {
            "type": "string",
            "guessed": true
          }
        }
      },
      "required": [
        "type",
        "data",
        "mimeType",
        "annotations",
        "meta"
      ]
    }
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['client.get']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "test_audio_content",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **test_embedded_resource**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\servers\everything-server\mcp_everything_server\server.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "type": {
        "type": "string",
        "enum": [
          "resource"
        ]
      },
      "resource": {
        "oneOf": [
          {
            "type": "object",
            "properties": {
              "text": {
                "type": "string"
              }
            },
            "required": [
              "text"
            ]
          },
          {
            "type": "object",
            "properties": {
              "blob": {
                "type": "string"
              }
            },
            "required": [
              "blob"
            ]
          }
        ]
      },
      "annotations": {
        "oneOf": [
          {
            "type": "object",
            "properties": {
              "audience": {
                "type": "array",
                "items": {
                  "type": "object",
                  "title": "Role"
                }
              },
              "priority": {
                "type": "object",
                "title": "Annotated[float, Field(ge=0.0, le=1.0)] | None"
              }
            }
          }
        ]
      },
      "meta": {
        "type": "object",
        "additionalProperties": {
          "type": "string",
          "guessed": true
        }
      }
    },
    "required": [
      "type",
      "resource",
      "annotations",
      "meta"
    ]
  }
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "array",
    "items": {
      "type": "object",
      "properties": {
        "type": {
          "type": "string",
          "enum": [
            "resource"
          ]
        },
        "resource": {
          "oneOf": [
            {
              "type": "object",
              "properties": {
                "text": {
                  "type": "string"
                }
              },
              "required": [
                "text"
              ]
            },
            {
              "type": "object",
              "properties": {
                "blob": {
                  "type": "string"
                }
              },
              "required": [
                "blob"
              ]
            }
          ]
        },
        "annotations": {
          "oneOf": [
            {
              "type": "object",
              "properties": {
                "audience": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "title": "Role"
                  }
                },
                "priority": {
                  "type": "object",
                  "title": "Annotated[float, Field(ge=0.0, le=1.0)] | None"
                }
              }
            }
          ]
        },
        "meta": {
          "type": "object",
          "additionalProperties": {
            "type": "string",
            "guessed": true
          }
        }
      },
      "required": [
        "type",
        "resource",
        "annotations",
        "meta"
      ]
    }
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['client.get']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "test_embedded_resource",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **test_multiple_content_types**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\servers\everything-server\mcp_everything_server\server.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "array",
  "items": {
    "oneOf": [
      {
        "type": "object",
        "properties": {
          "type": {
            "type": "object",
            "title": "Literal['text']"
          },
          "text": {
            "type": "string"
          },
          "annotations": {
            "type": "object",
            "title": "Annotations | None"
          },
          "meta": {
            "type": "object",
            "additionalProperties": {
              "type": "string",
              "guessed": true
            }
          }
        },
        "required": [
          "type",
          "text"
        ]
      },
      {
        "type": "object",
        "properties": {
          "type": {
            "type": "object",
            "title": "Literal['image']"
          },
          "data": {
            "type": "string"
          },
          "mimeType": {
            "type": "string"
          },
          "annotations": {
            "type": "object",
            "title": "Annotations | None"
          },
          "meta": {
            "type": "object",
            "additionalProperties": {
              "type": "string",
              "guessed": true
            }
          }
        },
        "required": [
          "type",
          "data",
          "mimeType"
        ]
      },
      {
        "type": "object",
        "properties": {
          "type": {
            "type": "object",
            "title": "Literal['resource']"
          },
          "resource": {
            "type": "object",
            "title": "TextResourceContents | BlobResourceContents"
          },
          "annotations": {
            "type": "object",
            "title": "Annotations | None"
          },
          "meta": {
            "type": "object",
            "additionalProperties": {
              "type": "string",
              "guessed": true
            }
          }
        },
        "required": [
          "type",
          "resource"
        ]
      }
    ]
  }
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "array",
    "items": {
      "oneOf": [
        {
          "type": "object",
          "properties": {
            "type": {
              "type": "object",
              "title": "Literal['text']"
            },
            "text": {
              "type": "string"
            },
            "annotations": {
              "type": "object",
              "title": "Annotations | None"
            },
            "meta": {
              "type": "object",
              "additionalProperties": {
                "type": "string",
                "guessed": true
              }
            }
          },
          "required": [
            "type",
            "text"
          ]
        },
        {
          "type": "object",
          "properties": {
            "type": {
              "type": "object",
              "title": "Literal['image']"
            },
            "data": {
              "type": "string"
            },
            "mimeType": {
              "type": "string"
            },
            "annotations": {
              "type": "object",
              "title": "Annotations | None"
            },
            "meta": {
              "type": "object",
              "additionalProperties": {
                "type": "string",
                "guessed": true
              }
            }
          },
          "required": [
            "type",
            "data",
            "mimeType"
          ]
        },
        {
          "type": "object",
          "properties": {
            "type": {
              "type": "object",
              "title": "Literal['resource']"
            },
            "resource": {
              "type": "object",
              "title": "TextResourceContents | BlobResourceContents"
            },
            "annotations": {
              "type": "object",
              "title": "Annotations | None"
            },
            "meta": {
              "type": "object",
              "additionalProperties": {
                "type": "string",
                "guessed": true
              }
            }
          },
          "required": [
            "type",
            "resource"
          ]
        }
      ]
    }
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['client.get']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "test_multiple_content_types",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **test_error_handling**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\servers\everything-server\mcp_everything_server\server.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "string"
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "string"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['client.get']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "test_error_handling",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **static_text_resource**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\servers\everything-server\mcp_everything_server\server.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "string"
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "string"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['client.get']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "static_text_resource",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **static_binary_resource**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\servers\everything-server\mcp_everything_server\server.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "title": "bytes"
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "title": "bytes"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['client.get']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "static_binary_resource",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **template_resource**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\servers\everything-server\mcp_everything_server\server.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "id": {
      "type": "string"
    }
  },
  "required": [
    "id"
  ]
}
```

#### Output Schema
```json
{
  "type": "string"
}
```

#### Payload Shape
```json
{
  "request": {
    "id": {
      "type": "string"
    }
  },
  "response": {
    "type": "string"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['client.get']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "template_resource",
    "arguments": {
      "id": "<id_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **watched_resource**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\servers\everything-server\mcp_everything_server\server.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "string"
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "string"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['client.get']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "watched_resource",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **test_simple_prompt**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\servers\everything-server\mcp_everything_server\server.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "role": {
        "type": "string",
        "enum": [
          "user",
          "assistant"
        ]
      }
    },
    "required": [
      "role"
    ]
  }
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "array",
    "items": {
      "type": "object",
      "properties": {
        "role": {
          "type": "string",
          "enum": [
            "user",
            "assistant"
          ]
        }
      },
      "required": [
        "role"
      ]
    }
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['client.get']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "test_simple_prompt",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **test_prompt_with_arguments**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\servers\everything-server\mcp_everything_server\server.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "arg1": {
      "type": "string"
    },
    "arg2": {
      "type": "string"
    }
  },
  "required": [
    "arg1",
    "arg2"
  ]
}
```

#### Output Schema
```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "role": {
        "type": "string",
        "enum": [
          "user",
          "assistant"
        ]
      }
    },
    "required": [
      "role"
    ]
  }
}
```

#### Payload Shape
```json
{
  "request": {
    "arg1": {
      "type": "string"
    },
    "arg2": {
      "type": "string"
    }
  },
  "response": {
    "type": "array",
    "items": {
      "type": "object",
      "properties": {
        "role": {
          "type": "string",
          "enum": [
            "user",
            "assistant"
          ]
        }
      },
      "required": [
        "role"
      ]
    }
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['client.get']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "test_prompt_with_arguments",
    "arguments": {
      "arg1": "<arg1_str>",
      "arg2": "<arg2_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **test_prompt_with_embedded_resource**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\servers\everything-server\mcp_everything_server\server.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "resourceUri": {
      "type": "string"
    }
  },
  "required": [
    "resourceUri"
  ]
}
```

#### Output Schema
```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "role": {
        "type": "string",
        "enum": [
          "user",
          "assistant"
        ]
      }
    },
    "required": [
      "role"
    ]
  }
}
```

#### Payload Shape
```json
{
  "request": {
    "resourceUri": {
      "type": "string"
    }
  },
  "response": {
    "type": "array",
    "items": {
      "type": "object",
      "properties": {
        "role": {
          "type": "string",
          "enum": [
            "user",
            "assistant"
          ]
        }
      },
      "required": [
        "role"
      ]
    }
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['client.get']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "test_prompt_with_embedded_resource",
    "arguments": {
      "resourceUri": "<resourceUri_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **test_prompt_with_image**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\servers\everything-server\mcp_everything_server\server.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "role": {
        "type": "string",
        "enum": [
          "user",
          "assistant"
        ]
      }
    },
    "required": [
      "role"
    ]
  }
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "array",
    "items": {
      "type": "object",
      "properties": {
        "role": {
          "type": "string",
          "enum": [
            "user",
            "assistant"
          ]
        }
      },
      "required": [
        "role"
      ]
    }
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['client.get']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "test_prompt_with_image",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **main**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\servers\everything-server\mcp_everything_server\server.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "port": {
      "type": "integer"
    },
    "log_level": {
      "type": "string"
    }
  },
  "required": [
    "log_level",
    "port"
  ]
}
```

#### Output Schema
```json
{
  "type": "integer"
}
```

#### Payload Shape
```json
{
  "request": {
    "port": {
      "type": "integer"
    },
    "log_level": {
      "type": "string"
    }
  },
  "response": {
    "type": "integer"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['client.get']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "main",
    "arguments": {
      "port": 0,
      "log_level": "<log_level_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **create_authorization_server**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\servers\simple-auth\mcp_simple_auth\auth_server.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "server_settings": {
      "type": "object",
      "properties": {
        "host": {
          "type": "string"
        },
        "port": {
          "type": "integer"
        },
        "server_url": {
          "type": "object",
          "title": "AnyHttpUrl"
        },
        "auth_callback_path": {
          "type": "string"
        }
      },
      "required": [
        "host",
        "port",
        "server_url",
        "auth_callback_path"
      ]
    },
    "auth_settings": {
      "type": "object",
      "properties": {
        "demo_username": {
          "type": "string"
        },
        "demo_password": {
          "type": "string"
        },
        "mcp_scope": {
          "type": "string"
        }
      },
      "required": [
        "demo_username",
        "demo_password",
        "mcp_scope"
      ]
    }
  },
  "required": [
    "auth_settings",
    "server_settings"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "title": "Starlette"
}
```

#### Payload Shape
```json
{
  "request": {
    "server_settings": {
      "type": "object",
      "properties": {
        "host": {
          "type": "string"
        },
        "port": {
          "type": "integer"
        },
        "server_url": {
          "type": "object",
          "title": "AnyHttpUrl"
        },
        "auth_callback_path": {
          "type": "string"
        }
      },
      "required": [
        "host",
        "port",
        "server_url",
        "auth_callback_path"
      ]
    },
    "auth_settings": {
      "type": "object",
      "properties": {
        "demo_username": {
          "type": "string"
        },
        "demo_password": {
          "type": "string"
        },
        "mcp_scope": {
          "type": "string"
        }
      },
      "required": [
        "demo_username",
        "demo_password",
        "mcp_scope"
      ]
    }
  },
  "response": {
    "type": "object",
    "title": "Starlette"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "create_authorization_server",
    "arguments": {
      "server_settings": {},
      "auth_settings": {}
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **main**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\servers\simple-auth\mcp_simple_auth\auth_server.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "port": {
      "type": "integer"
    }
  },
  "required": [
    "port"
  ]
}
```

#### Output Schema
```json
{
  "type": "integer"
}
```

#### Payload Shape
```json
{
  "request": {
    "port": {
      "type": "integer"
    }
  },
  "response": {
    "type": "integer"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "main",
    "arguments": {
      "port": 0
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **create_simple_mcp_server**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\servers\simple-auth\mcp_simple_auth\legacy_as_server.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "server_settings": {
      "type": "object",
      "properties": {
        "host": {
          "type": "string"
        },
        "port": {
          "type": "integer"
        },
        "server_url": {
          "type": "object",
          "title": "AnyHttpUrl"
        },
        "auth_callback_path": {
          "type": "string"
        }
      },
      "required": [
        "host",
        "port",
        "server_url",
        "auth_callback_path"
      ]
    },
    "auth_settings": {
      "type": "object",
      "properties": {
        "demo_username": {
          "type": "string"
        },
        "demo_password": {
          "type": "string"
        },
        "mcp_scope": {
          "type": "string"
        }
      },
      "required": [
        "demo_username",
        "demo_password",
        "mcp_scope"
      ]
    }
  },
  "required": [
    "auth_settings",
    "server_settings"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Payload Shape
```json
{
  "request": {
    "server_settings": {
      "type": "object",
      "properties": {
        "host": {
          "type": "string"
        },
        "port": {
          "type": "integer"
        },
        "server_url": {
          "type": "object",
          "title": "AnyHttpUrl"
        },
        "auth_callback_path": {
          "type": "string"
        }
      },
      "required": [
        "host",
        "port",
        "server_url",
        "auth_callback_path"
      ]
    },
    "auth_settings": {
      "type": "object",
      "properties": {
        "demo_username": {
          "type": "string"
        },
        "demo_password": {
          "type": "string"
        },
        "mcp_scope": {
          "type": "string"
        }
      },
      "required": [
        "demo_username",
        "demo_password",
        "mcp_scope"
      ]
    }
  },
  "response": {
    "type": "object",
    "properties": {}
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "create_simple_mcp_server",
    "arguments": {
      "server_settings": {},
      "auth_settings": {}
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **main**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\servers\simple-auth\mcp_simple_auth\legacy_as_server.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "port": {
      "type": "integer"
    },
    "transport": {
      "type": "string",
      "enum": [
        "sse",
        "streamable-http"
      ]
    }
  },
  "required": [
    "port",
    "transport"
  ]
}
```

#### Output Schema
```json
{
  "type": "integer"
}
```

#### Payload Shape
```json
{
  "request": {
    "port": {
      "type": "integer"
    },
    "transport": {
      "type": "string",
      "enum": [
        "sse",
        "streamable-http"
      ]
    }
  },
  "response": {
    "type": "integer"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "main",
    "arguments": {
      "port": 0,
      "transport": "<transport_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **create_resource_server**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\servers\simple-auth\mcp_simple_auth\server.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "settings": {
      "type": "object",
      "properties": {
        "host": {
          "type": "string"
        },
        "port": {
          "type": "integer"
        },
        "server_url": {
          "type": "object",
          "title": "AnyHttpUrl"
        },
        "auth_server_url": {
          "type": "object",
          "title": "AnyHttpUrl"
        },
        "auth_server_introspection_endpoint": {
          "type": "string"
        },
        "mcp_scope": {
          "type": "string"
        },
        "oauth_strict": {
          "type": "boolean"
        }
      },
      "required": [
        "host",
        "port",
        "server_url",
        "auth_server_url",
        "auth_server_introspection_endpoint",
        "mcp_scope",
        "oauth_strict"
      ]
    }
  },
  "required": [
    "settings"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Payload Shape
```json
{
  "request": {
    "settings": {
      "type": "object",
      "properties": {
        "host": {
          "type": "string"
        },
        "port": {
          "type": "integer"
        },
        "server_url": {
          "type": "object",
          "title": "AnyHttpUrl"
        },
        "auth_server_url": {
          "type": "object",
          "title": "AnyHttpUrl"
        },
        "auth_server_introspection_endpoint": {
          "type": "string"
        },
        "mcp_scope": {
          "type": "string"
        },
        "oauth_strict": {
          "type": "boolean"
        }
      },
      "required": [
        "host",
        "port",
        "server_url",
        "auth_server_url",
        "auth_server_introspection_endpoint",
        "mcp_scope",
        "oauth_strict"
      ]
    }
  },
  "response": {
    "type": "object",
    "properties": {}
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['client.get']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "create_resource_server",
    "arguments": {
      "settings": {}
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **main**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\servers\simple-auth\mcp_simple_auth\server.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "port": {
      "type": "integer"
    },
    "auth_server": {
      "type": "string"
    },
    "transport": {
      "type": "string",
      "enum": [
        "sse",
        "streamable-http"
      ]
    },
    "oauth_strict": {
      "type": "boolean"
    }
  },
  "required": [
    "auth_server",
    "oauth_strict",
    "port",
    "transport"
  ]
}
```

#### Output Schema
```json
{
  "type": "integer"
}
```

#### Payload Shape
```json
{
  "request": {
    "port": {
      "type": "integer"
    },
    "auth_server": {
      "type": "string"
    },
    "transport": {
      "type": "string",
      "enum": [
        "sse",
        "streamable-http"
      ]
    },
    "oauth_strict": {
      "type": "boolean"
    }
  },
  "response": {
    "type": "integer"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['client.get']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "main",
    "arguments": {
      "port": 0,
      "auth_server": "<auth_server_str>",
      "transport": "<transport_str>",
      "oauth_strict": false
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **main**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\servers\simple-pagination\mcp_simple_pagination\server.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "port": {
      "type": "integer"
    },
    "transport": {
      "type": "string"
    }
  },
  "required": [
    "port",
    "transport"
  ]
}
```

#### Output Schema
```json
{
  "type": "integer"
}
```

#### Payload Shape
```json
{
  "request": {
    "port": {
      "type": "integer"
    },
    "transport": {
      "type": "string"
    }
  },
  "response": {
    "type": "integer"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['client.get']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "main",
    "arguments": {
      "port": 0,
      "transport": "<transport_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **create_messages**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\servers\simple-prompt\mcp_simple_prompt\server.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "context": {
      "type": "object",
      "title": "str | None"
    },
    "topic": {
      "type": "object",
      "title": "str | None"
    }
  }
}
```

#### Output Schema
```json
{
  "type": "array",
  "items": {
    "type": "object",
    "title": "types.PromptMessage"
  }
}
```

#### Payload Shape
```json
{
  "request": {
    "context": {
      "type": "object",
      "title": "str | None"
    },
    "topic": {
      "type": "object",
      "title": "str | None"
    }
  },
  "response": {
    "type": "array",
    "items": {
      "type": "object",
      "title": "types.PromptMessage"
    }
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['client.get']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "create_messages",
    "arguments": {
      "context": {},
      "topic": {}
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **main**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\servers\simple-prompt\mcp_simple_prompt\server.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "port": {
      "type": "integer"
    },
    "transport": {
      "type": "string"
    }
  },
  "required": [
    "port",
    "transport"
  ]
}
```

#### Output Schema
```json
{
  "type": "integer"
}
```

#### Payload Shape
```json
{
  "request": {
    "port": {
      "type": "integer"
    },
    "transport": {
      "type": "string"
    }
  },
  "response": {
    "type": "integer"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['client.get']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "main",
    "arguments": {
      "port": 0,
      "transport": "<transport_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **main**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\servers\simple-resource\mcp_simple_resource\server.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "port": {
      "type": "integer"
    },
    "transport": {
      "type": "string"
    }
  },
  "required": [
    "port",
    "transport"
  ]
}
```

#### Output Schema
```json
{
  "type": "integer"
}
```

#### Payload Shape
```json
{
  "request": {
    "port": {
      "type": "integer"
    },
    "transport": {
      "type": "string"
    }
  },
  "response": {
    "type": "integer"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['client.get']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "main",
    "arguments": {
      "port": 0,
      "transport": "<transport_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **main**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\servers\simple-streamablehttp\mcp_simple_streamablehttp\server.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "port": {
      "type": "integer"
    },
    "log_level": {
      "type": "string"
    },
    "json_response": {
      "type": "boolean"
    }
  },
  "required": [
    "json_response",
    "log_level",
    "port"
  ]
}
```

#### Output Schema
```json
{
  "type": "integer"
}
```

#### Payload Shape
```json
{
  "request": {
    "port": {
      "type": "integer"
    },
    "log_level": {
      "type": "string"
    },
    "json_response": {
      "type": "boolean"
    }
  },
  "response": {
    "type": "integer"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['client.get']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "main",
    "arguments": {
      "port": 0,
      "log_level": "<log_level_str>",
      "json_response": false
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **main**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\servers\simple-streamablehttp-stateless\mcp_simple_streamablehttp_stateless\server.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "port": {
      "type": "integer"
    },
    "log_level": {
      "type": "string"
    },
    "json_response": {
      "type": "boolean"
    }
  },
  "required": [
    "json_response",
    "log_level",
    "port"
  ]
}
```

#### Output Schema
```json
{
  "type": "integer"
}
```

#### Payload Shape
```json
{
  "request": {
    "port": {
      "type": "integer"
    },
    "log_level": {
      "type": "string"
    },
    "json_response": {
      "type": "boolean"
    }
  },
  "response": {
    "type": "integer"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['client.get']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "main",
    "arguments": {
      "port": 0,
      "log_level": "<log_level_str>",
      "json_response": false
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **main**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\servers\simple-tool\mcp_simple_tool\server.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "port": {
      "type": "integer"
    },
    "transport": {
      "type": "string"
    }
  },
  "required": [
    "port",
    "transport"
  ]
}
```

#### Output Schema
```json
{
  "type": "integer"
}
```

#### Payload Shape
```json
{
  "request": {
    "port": {
      "type": "integer"
    },
    "transport": {
      "type": "string"
    }
  },
  "response": {
    "type": "integer"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['client.get']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "main",
    "arguments": {
      "port": 0,
      "transport": "<transport_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **main**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\snippets\clients\completion_client.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "main",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **main**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\snippets\clients\display_utilities.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "main",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **run**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\snippets\clients\oauth_client.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "run",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **main**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\snippets\clients\stdio_client.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "main",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **review_code**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\snippets\servers\basic_prompt.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "code": {
      "type": "string"
    }
  },
  "required": [
    "code"
  ]
}
```

#### Output Schema
```json
{
  "type": "string"
}
```

#### Payload Shape
```json
{
  "request": {
    "code": {
      "type": "string"
    }
  },
  "response": {
    "type": "string"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "review_code",
    "arguments": {
      "code": "<code_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **debug_error**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\snippets\servers\basic_prompt.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "error": {
      "type": "string"
    }
  },
  "required": [
    "error"
  ]
}
```

#### Output Schema
```json
{
  "type": "array",
  "items": {
    "type": "object",
    "title": "base.Message"
  }
}
```

#### Payload Shape
```json
{
  "request": {
    "error": {
      "type": "string"
    }
  },
  "response": {
    "type": "array",
    "items": {
      "type": "object",
      "title": "base.Message"
    }
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "debug_error",
    "arguments": {
      "error": "<error_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **read_document**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\snippets\servers\basic_resource.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "name": {
      "type": "string"
    }
  },
  "required": [
    "name"
  ]
}
```

#### Output Schema
```json
{
  "type": "string"
}
```

#### Payload Shape
```json
{
  "request": {
    "name": {
      "type": "string"
    }
  },
  "response": {
    "type": "string"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "read_document",
    "arguments": {
      "name": "<name_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **get_settings**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\snippets\servers\basic_resource.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "string"
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "string"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "get_settings",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **sum**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\snippets\servers\basic_tool.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "a": {
      "type": "integer"
    },
    "b": {
      "type": "integer"
    }
  },
  "required": [
    "a",
    "b"
  ]
}
```

#### Output Schema
```json
{
  "type": "integer"
}
```

#### Payload Shape
```json
{
  "request": {
    "a": {
      "type": "integer"
    },
    "b": {
      "type": "integer"
    }
  },
  "response": {
    "type": "integer"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "sum",
    "arguments": {
      "a": 0,
      "b": 0
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **get_weather**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\snippets\servers\basic_tool.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "city": {
      "type": "string"
    },
    "unit": {
      "type": "string"
    }
  },
  "required": [
    "city"
  ]
}
```

#### Output Schema
```json
{
  "type": "string"
}
```

#### Payload Shape
```json
{
  "request": {
    "city": {
      "type": "string"
    },
    "unit": {
      "type": "string"
    }
  },
  "response": {
    "type": "string"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "get_weather",
    "arguments": {
      "city": "<city_str>",
      "unit": "<unit_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **github_repo**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\snippets\servers\completion.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "owner": {
      "type": "string"
    },
    "repo": {
      "type": "string"
    }
  },
  "required": [
    "owner",
    "repo"
  ]
}
```

#### Output Schema
```json
{
  "type": "string"
}
```

#### Payload Shape
```json
{
  "request": {
    "owner": {
      "type": "string"
    },
    "repo": {
      "type": "string"
    }
  },
  "response": {
    "type": "string"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "github_repo",
    "arguments": {
      "owner": "<owner_str>",
      "repo": "<repo_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **review_code**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\snippets\servers\completion.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "language": {
      "type": "string"
    },
    "code": {
      "type": "string"
    }
  },
  "required": [
    "code",
    "language"
  ]
}
```

#### Output Schema
```json
{
  "type": "string"
}
```

#### Payload Shape
```json
{
  "request": {
    "language": {
      "type": "string"
    },
    "code": {
      "type": "string"
    }
  },
  "response": {
    "type": "string"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "review_code",
    "arguments": {
      "language": "<language_str>",
      "code": "<code_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **advanced_tool**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\snippets\servers\direct_call_tool_result.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "properties": {
    "content": {
      "type": "array",
      "items": {
        "type": "object",
        "title": "ContentBlock"
      }
    },
    "structuredContent": {
      "type": "object",
      "additionalProperties": {
        "type": "string",
        "guessed": true
      }
    },
    "isError": {
      "type": "boolean"
    }
  },
  "required": [
    "content",
    "structuredContent",
    "isError"
  ]
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "properties": {
      "content": {
        "type": "array",
        "items": {
          "type": "object",
          "title": "ContentBlock"
        }
      },
      "structuredContent": {
        "type": "object",
        "additionalProperties": {
          "type": "string",
          "guessed": true
        }
      },
      "isError": {
        "type": "boolean"
      }
    },
    "required": [
      "content",
      "structuredContent",
      "isError"
    ]
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "advanced_tool",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **validated_tool**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\snippets\servers\direct_call_tool_result.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "title": "Annotated[CallToolResult, ValidationModel]"
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "title": "Annotated[CallToolResult, ValidationModel]"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "validated_tool",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **empty_result_tool**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\snippets\servers\direct_call_tool_result.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "properties": {
    "content": {
      "type": "array",
      "items": {
        "type": "object",
        "title": "ContentBlock"
      }
    },
    "structuredContent": {
      "type": "object",
      "additionalProperties": {
        "type": "string",
        "guessed": true
      }
    },
    "isError": {
      "type": "boolean"
    }
  },
  "required": [
    "content",
    "structuredContent",
    "isError"
  ]
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "properties": {
      "content": {
        "type": "array",
        "items": {
          "type": "object",
          "title": "ContentBlock"
        }
      },
      "structuredContent": {
        "type": "object",
        "additionalProperties": {
          "type": "string",
          "guessed": true
        }
      },
      "isError": {
        "type": "boolean"
      }
    },
    "required": [
      "content",
      "structuredContent",
      "isError"
    ]
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "empty_result_tool",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **hello**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\snippets\servers\direct_execution.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "name": {
      "type": "string"
    }
  }
}
```

#### Output Schema
```json
{
  "type": "string"
}
```

#### Payload Shape
```json
{
  "request": {
    "name": {
      "type": "string"
    }
  },
  "response": {
    "type": "string"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "hello",
    "arguments": {
      "name": "<name_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **main**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\snippets\servers\direct_execution.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "main",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **add**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\snippets\servers\fastmcp_quickstart.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "a": {
      "type": "integer"
    },
    "b": {
      "type": "integer"
    }
  },
  "required": [
    "a",
    "b"
  ]
}
```

#### Output Schema
```json
{
  "type": "integer"
}
```

#### Payload Shape
```json
{
  "request": {
    "a": {
      "type": "integer"
    },
    "b": {
      "type": "integer"
    }
  },
  "response": {
    "type": "integer"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "add",
    "arguments": {
      "a": 0,
      "b": 0
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **get_greeting**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\snippets\servers\fastmcp_quickstart.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "name": {
      "type": "string"
    }
  },
  "required": [
    "name"
  ]
}
```

#### Output Schema
```json
{
  "type": "string"
}
```

#### Payload Shape
```json
{
  "request": {
    "name": {
      "type": "string"
    }
  },
  "response": {
    "type": "string"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "get_greeting",
    "arguments": {
      "name": "<name_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **greet_user**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\snippets\servers\fastmcp_quickstart.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "name": {
      "type": "string"
    },
    "style": {
      "type": "string"
    }
  },
  "required": [
    "name"
  ]
}
```

#### Output Schema
```json
{
  "type": "string"
}
```

#### Payload Shape
```json
{
  "request": {
    "name": {
      "type": "string"
    },
    "style": {
      "type": "string"
    }
  },
  "response": {
    "type": "string"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "greet_user",
    "arguments": {
      "name": "<name_str>",
      "style": "<style_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **create_thumbnail**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\snippets\servers\images.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "image_path": {
      "type": "string"
    }
  },
  "required": [
    "image_path"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Payload Shape
```json
{
  "request": {
    "image_path": {
      "type": "string"
    }
  },
  "response": {
    "type": "object",
    "properties": {}
  }
}
```

#### Syscalls
- Filesystem: ['PILImage.open']
- Network: []
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "create_thumbnail",
    "arguments": {
      "image_path": "<image_path_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **query_db**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\snippets\servers\lifespan_example.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "ctx": {
      "type": "object",
      "title": "Context[ServerSession, AppContext]"
    }
  },
  "required": [
    "ctx"
  ]
}
```

#### Output Schema
```json
{
  "type": "string"
}
```

#### Payload Shape
```json
{
  "request": {
    "ctx": {
      "type": "object",
      "title": "Context[ServerSession, AppContext]"
    }
  },
  "response": {
    "type": "string"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "query_db",
    "arguments": {
      "ctx": {}
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **greet**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\snippets\servers\streamable_config.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "name": {
      "type": "string"
    }
  }
}
```

#### Output Schema
```json
{
  "type": "string"
}
```

#### Payload Shape
```json
{
  "request": {
    "name": {
      "type": "string"
    }
  },
  "response": {
    "type": "string"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "greet",
    "arguments": {
      "name": "<name_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **hello**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\snippets\servers\streamable_http_basic_mounting.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "string"
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "string"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "hello",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **domain_info**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\snippets\servers\streamable_http_host_mounting.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "string"
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "string"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "domain_info",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **api_status**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\snippets\servers\streamable_http_multiple_servers.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "string"
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "string"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "api_status",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **send_message**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\snippets\servers\streamable_http_multiple_servers.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "message": {
      "type": "string"
    }
  },
  "required": [
    "message"
  ]
}
```

#### Output Schema
```json
{
  "type": "string"
}
```

#### Payload Shape
```json
{
  "request": {
    "message": {
      "type": "string"
    }
  },
  "response": {
    "type": "string"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "send_message",
    "arguments": {
      "message": "<message_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **process_data**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\snippets\servers\streamable_http_path_config.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "data": {
      "type": "string"
    }
  },
  "required": [
    "data"
  ]
}
```

#### Output Schema
```json
{
  "type": "string"
}
```

#### Payload Shape
```json
{
  "request": {
    "data": {
      "type": "string"
    }
  },
  "response": {
    "type": "string"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "process_data",
    "arguments": {
      "data": "<data_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **echo**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\snippets\servers\streamable_starlette_mount.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "message": {
      "type": "string"
    }
  },
  "required": [
    "message"
  ]
}
```

#### Output Schema
```json
{
  "type": "string"
}
```

#### Payload Shape
```json
{
  "request": {
    "message": {
      "type": "string"
    }
  },
  "response": {
    "type": "string"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "echo",
    "arguments": {
      "message": "<message_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **add_two**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\snippets\servers\streamable_starlette_mount.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "n": {
      "type": "integer"
    }
  },
  "required": [
    "n"
  ]
}
```

#### Output Schema
```json
{
  "type": "integer"
}
```

#### Payload Shape
```json
{
  "request": {
    "n": {
      "type": "integer"
    }
  },
  "response": {
    "type": "integer"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "add_two",
    "arguments": {
      "n": 0
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **get_weather**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\snippets\servers\structured_output.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "city": {
      "type": "string"
    }
  },
  "required": [
    "city"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "properties": {
    "temperature": {
      "type": "number"
    },
    "humidity": {
      "type": "number"
    },
    "condition": {
      "type": "string"
    },
    "wind_speed": {
      "type": "number"
    },
    "location": {
      "type": "string"
    },
    "timestamp": {
      "type": "object",
      "title": "datetime"
    }
  },
  "required": [
    "temperature",
    "humidity",
    "condition",
    "wind_speed",
    "location",
    "timestamp"
  ]
}
```

#### Payload Shape
```json
{
  "request": {
    "city": {
      "type": "string"
    }
  },
  "response": {
    "type": "object",
    "properties": {
      "temperature": {
        "type": "number"
      },
      "humidity": {
        "type": "number"
      },
      "condition": {
        "type": "string"
      },
      "wind_speed": {
        "type": "number"
      },
      "location": {
        "type": "string"
      },
      "timestamp": {
        "type": "object",
        "title": "datetime"
      }
    },
    "required": [
      "temperature",
      "humidity",
      "condition",
      "wind_speed",
      "location",
      "timestamp"
    ]
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "get_weather",
    "arguments": {
      "city": "<city_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **get_location**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\snippets\servers\structured_output.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "address": {
      "type": "string"
    }
  },
  "required": [
    "address"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "properties": {
    "latitude": {
      "type": "number"
    },
    "longitude": {
      "type": "number"
    },
    "name": {
      "type": "string"
    }
  },
  "required": [
    "latitude",
    "longitude",
    "name"
  ]
}
```

#### Payload Shape
```json
{
  "request": {
    "address": {
      "type": "string"
    }
  },
  "response": {
    "type": "object",
    "properties": {
      "latitude": {
        "type": "number"
      },
      "longitude": {
        "type": "number"
      },
      "name": {
        "type": "string"
      }
    },
    "required": [
      "latitude",
      "longitude",
      "name"
    ]
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "get_location",
    "arguments": {
      "address": "<address_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **get_statistics**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\snippets\servers\structured_output.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "data_type": {
      "type": "string"
    }
  },
  "required": [
    "data_type"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "additionalProperties": {
    "type": "string",
    "guessed": true
  }
}
```

#### Payload Shape
```json
{
  "request": {
    "data_type": {
      "type": "string"
    }
  },
  "response": {
    "type": "object",
    "additionalProperties": {
      "type": "string",
      "guessed": true
    }
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "get_statistics",
    "arguments": {
      "data_type": "<data_type_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **get_user**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\snippets\servers\structured_output.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "user_id": {
      "type": "string"
    }
  },
  "required": [
    "user_id"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "properties": {
    "name": {
      "type": "string"
    },
    "age": {
      "type": "integer"
    },
    "email": {
      "type": "object",
      "title": "str | None"
    }
  },
  "required": [
    "name",
    "age",
    "email"
  ]
}
```

#### Payload Shape
```json
{
  "request": {
    "user_id": {
      "type": "string"
    }
  },
  "response": {
    "type": "object",
    "properties": {
      "name": {
        "type": "string"
      },
      "age": {
        "type": "integer"
      },
      "email": {
        "type": "object",
        "title": "str | None"
      }
    },
    "required": [
      "name",
      "age",
      "email"
    ]
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "get_user",
    "arguments": {
      "user_id": "<user_id_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **get_config**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\snippets\servers\structured_output.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "properties": {}
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "get_config",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **list_cities**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\snippets\servers\structured_output.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "array",
  "items": {
    "type": "string"
  }
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "array",
    "items": {
      "type": "string"
    }
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "list_cities",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **get_temperature**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\snippets\servers\structured_output.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "city": {
      "type": "string"
    }
  },
  "required": [
    "city"
  ]
}
```

#### Output Schema
```json
{
  "type": "number"
}
```

#### Payload Shape
```json
{
  "request": {
    "city": {
      "type": "string"
    }
  },
  "response": {
    "type": "number"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "get_temperature",
    "arguments": {
      "city": "<city_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **run_server**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\examples\snippets\servers\__init__.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "run_server",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **get_github_url**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\scripts\update_readme_snippets.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "file_path": {
      "type": "string"
    }
  },
  "required": [
    "file_path"
  ]
}
```

#### Output Schema
```json
{
  "type": "string"
}
```

#### Payload Shape
```json
{
  "request": {
    "file_path": {
      "type": "string"
    }
  },
  "response": {
    "type": "string"
  }
}
```

#### Syscalls
- Filesystem: ['file.read_text', 'readme_path.read_text', 'readme_path.write_text']
- Network: []
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "get_github_url",
    "arguments": {
      "file_path": "<file_path_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **process_snippet_block**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\scripts\update_readme_snippets.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "match": {
      "type": "object",
      "title": "re.Match[str]"
    },
    "check_mode": {
      "type": "boolean"
    }
  },
  "required": [
    "match"
  ]
}
```

#### Output Schema
```json
{
  "type": "string"
}
```

#### Payload Shape
```json
{
  "request": {
    "match": {
      "type": "object",
      "title": "re.Match[str]"
    },
    "check_mode": {
      "type": "boolean"
    }
  },
  "response": {
    "type": "string"
  }
}
```

#### Syscalls
- Filesystem: ['file.read_text', 'readme_path.read_text', 'readme_path.write_text']
- Network: []
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "process_snippet_block",
    "arguments": {
      "match": {},
      "check_mode": false
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **update_readme_snippets**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\scripts\update_readme_snippets.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "readme_path": {
      "type": "object",
      "title": "Path"
    },
    "check_mode": {
      "type": "boolean"
    }
  }
}
```

#### Output Schema
```json
{
  "type": "boolean"
}
```

#### Payload Shape
```json
{
  "request": {
    "readme_path": {
      "type": "object",
      "title": "Path"
    },
    "check_mode": {
      "type": "boolean"
    }
  },
  "response": {
    "type": "boolean"
  }
}
```

#### Syscalls
- Filesystem: ['file.read_text', 'readme_path.read_text', 'readme_path.write_text']
- Network: []
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "update_readme_snippets",
    "arguments": {
      "readme_path": {},
      "check_mode": false
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **main**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\scripts\update_readme_snippets.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: ['file.read_text', 'readme_path.read_text', 'readme_path.write_text']
- Network: []
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "main",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **get_claude_config_path**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\src\mcp\cli\claude.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "title": "Path | None"
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "title": "Path | None"
  }
}
```

#### Syscalls
- Filesystem: ['config_file.write_text', 'config_file.read_text']
- Network: []
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "get_claude_config_path",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **get_uv_path**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\src\mcp\cli\claude.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "string"
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "string"
  }
}
```

#### Syscalls
- Filesystem: ['config_file.write_text', 'config_file.read_text']
- Network: []
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "get_uv_path",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **update_claude_config**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\src\mcp\cli\claude.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "file_spec": {
      "type": "string"
    },
    "server_name": {
      "type": "string"
    }
  },
  "required": [
    "file_spec",
    "server_name"
  ]
}
```

#### Output Schema
```json
{
  "type": "boolean"
}
```

#### Payload Shape
```json
{
  "request": {
    "file_spec": {
      "type": "string"
    },
    "server_name": {
      "type": "string"
    }
  },
  "response": {
    "type": "boolean"
  }
}
```

#### Syscalls
- Filesystem: ['config_file.write_text', 'config_file.read_text']
- Network: []
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "update_claude_config",
    "arguments": {
      "file_spec": "<file_spec_str>",
      "server_name": "<server_name_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **_get_npx_command**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\src\mcp\cli\cli.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: ['subprocess.run']
- Env: []
- Severity: **high**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "_get_npx_command",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **_parse_env_var**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\src\mcp\cli\cli.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "env_var": {
      "type": "string"
    }
  },
  "required": [
    "env_var"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "title": "tuple[str, str]"
}
```

#### Payload Shape
```json
{
  "request": {
    "env_var": {
      "type": "string"
    }
  },
  "response": {
    "type": "object",
    "title": "tuple[str, str]"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: ['subprocess.run']
- Env: []
- Severity: **high**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "_parse_env_var",
    "arguments": {
      "env_var": "<env_var_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **_build_uv_command**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\src\mcp\cli\cli.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "file_spec": {
      "type": "string"
    },
    "with_editable": {
      "type": "object",
      "title": "Path | None"
    },
    "with_packages": {
      "type": "array",
      "items": {
        "type": "string"
      }
    }
  },
  "required": [
    "file_spec"
  ]
}
```

#### Output Schema
```json
{
  "type": "array",
  "items": {
    "type": "string"
  }
}
```

#### Payload Shape
```json
{
  "request": {
    "file_spec": {
      "type": "string"
    },
    "with_editable": {
      "type": "object",
      "title": "Path | None"
    },
    "with_packages": {
      "type": "array",
      "items": {
        "type": "string"
      }
    }
  },
  "response": {
    "type": "array",
    "items": {
      "type": "string"
    }
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: ['subprocess.run']
- Env: []
- Severity: **high**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "_build_uv_command",
    "arguments": {
      "file_spec": "<file_spec_str>",
      "with_editable": {},
      "with_packages": []
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **_parse_file_path**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\src\mcp\cli\cli.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "file_spec": {
      "type": "string"
    }
  },
  "required": [
    "file_spec"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "title": "tuple[Path, str | None]"
}
```

#### Payload Shape
```json
{
  "request": {
    "file_spec": {
      "type": "string"
    }
  },
  "response": {
    "type": "object",
    "title": "tuple[Path, str | None]"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: ['subprocess.run']
- Env: []
- Severity: **high**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "_parse_file_path",
    "arguments": {
      "file_spec": "<file_spec_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **_import_server**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\src\mcp\cli\cli.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "file": {
      "type": "object",
      "title": "Path"
    },
    "server_object": {
      "type": "object",
      "title": "str | None"
    }
  },
  "required": [
    "file"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {
    "file": {
      "type": "object",
      "title": "Path"
    },
    "server_object": {
      "type": "object",
      "title": "str | None"
    }
  },
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: ['subprocess.run']
- Env: []
- Severity: **high**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "_import_server",
    "arguments": {
      "file": {},
      "server_object": {}
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **version**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\src\mcp\cli\cli.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "title": "None"
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "title": "None"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: ['subprocess.run']
- Env: []
- Severity: **high**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "version",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **dev**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\src\mcp\cli\cli.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "file_spec": {
      "type": "string"
    },
    "with_editable": {
      "type": "object",
      "title": "Annotated[Path | None, typer.Option('--with-editable', '-e', help='Directory containing pyproject.toml to install in editable mode', exists=True, file_okay=False, resolve_path=True)]"
    },
    "with_packages": {
      "type": "object",
      "title": "Annotated[list[str], typer.Option('--with', help='Additional packages to install')]"
    }
  }
}
```

#### Output Schema
```json
{
  "type": "object",
  "title": "None"
}
```

#### Payload Shape
```json
{
  "request": {
    "file_spec": {
      "type": "string"
    },
    "with_editable": {
      "type": "object",
      "title": "Annotated[Path | None, typer.Option('--with-editable', '-e', help='Directory containing pyproject.toml to install in editable mode', exists=True, file_okay=False, resolve_path=True)]"
    },
    "with_packages": {
      "type": "object",
      "title": "Annotated[list[str], typer.Option('--with', help='Additional packages to install')]"
    }
  },
  "response": {
    "type": "object",
    "title": "None"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: ['subprocess.run']
- Env: []
- Severity: **high**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "dev",
    "arguments": {
      "file_spec": "<file_spec_str>",
      "with_editable": {},
      "with_packages": {}
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **run**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\src\mcp\cli\cli.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "file_spec": {
      "type": "string"
    },
    "transport": {
      "type": "object",
      "title": "Annotated[str | None, typer.Option('--transport', '-t', help='Transport protocol to use (stdio or sse)')]"
    }
  }
}
```

#### Output Schema
```json
{
  "type": "object",
  "title": "None"
}
```

#### Payload Shape
```json
{
  "request": {
    "file_spec": {
      "type": "string"
    },
    "transport": {
      "type": "object",
      "title": "Annotated[str | None, typer.Option('--transport', '-t', help='Transport protocol to use (stdio or sse)')]"
    }
  },
  "response": {
    "type": "object",
    "title": "None"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: ['subprocess.run']
- Env: []
- Severity: **high**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "run",
    "arguments": {
      "file_spec": "<file_spec_str>",
      "transport": {}
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **install**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\src\mcp\cli\cli.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "file_spec": {
      "type": "string"
    },
    "server_name": {
      "type": "object",
      "title": "Annotated[str | None, typer.Option('--name', '-n', help=\"Custom name for the server (defaults to server's name attribute or file name)\")]"
    },
    "with_editable": {
      "type": "object",
      "title": "Annotated[Path | None, typer.Option('--with-editable', '-e', help='Directory containing pyproject.toml to install in editable mode', exists=True, file_okay=False, resolve_path=True)]"
    },
    "with_packages": {
      "type": "object",
      "title": "Annotated[list[str], typer.Option('--with', help='Additional packages to install')]"
    },
    "env_vars": {
      "type": "object",
      "title": "Annotated[list[str], typer.Option('--env-var', '-v', help='Environment variables in KEY=VALUE format')]"
    },
    "env_file": {
      "type": "object",
      "title": "Annotated[Path | None, typer.Option('--env-file', '-f', help='Load environment variables from a .env file', exists=True, file_okay=True, dir_okay=False, resolve_path=True)]"
    }
  }
}
```

#### Output Schema
```json
{
  "type": "object",
  "title": "None"
}
```

#### Payload Shape
```json
{
  "request": {
    "file_spec": {
      "type": "string"
    },
    "server_name": {
      "type": "object",
      "title": "Annotated[str | None, typer.Option('--name', '-n', help=\"Custom name for the server (defaults to server's name attribute or file name)\")]"
    },
    "with_editable": {
      "type": "object",
      "title": "Annotated[Path | None, typer.Option('--with-editable', '-e', help='Directory containing pyproject.toml to install in editable mode', exists=True, file_okay=False, resolve_path=True)]"
    },
    "with_packages": {
      "type": "object",
      "title": "Annotated[list[str], typer.Option('--with', help='Additional packages to install')]"
    },
    "env_vars": {
      "type": "object",
      "title": "Annotated[list[str], typer.Option('--env-var', '-v', help='Environment variables in KEY=VALUE format')]"
    },
    "env_file": {
      "type": "object",
      "title": "Annotated[Path | None, typer.Option('--env-file', '-f', help='Load environment variables from a .env file', exists=True, file_okay=True, dir_okay=False, resolve_path=True)]"
    }
  },
  "response": {
    "type": "object",
    "title": "None"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: ['subprocess.run']
- Env: []
- Severity: **high**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "install",
    "arguments": {
      "file_spec": "<file_spec_str>",
      "server_name": {},
      "with_editable": {},
      "with_packages": {},
      "env_vars": {},
      "env_file": {}
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **remove_request_params**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\src\mcp\client\sse.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "url": {
      "type": "string"
    }
  },
  "required": [
    "url"
  ]
}
```

#### Output Schema
```json
{
  "type": "string"
}
```

#### Payload Shape
```json
{
  "request": {
    "url": {
      "type": "string"
    }
  },
  "response": {
    "type": "string"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['httpx.Timeout', 'client.post']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "remove_request_params",
    "arguments": {
      "url": "<url_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **cli**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\src\mcp\client\__main__.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "cli",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **extract_field_from_www_auth**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\src\mcp\client\auth\utils.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "response": {
      "type": "object",
      "title": "Response"
    },
    "field_name": {
      "type": "string"
    }
  },
  "required": [
    "field_name",
    "response"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "title": "str | None"
}
```

#### Payload Shape
```json
{
  "request": {
    "response": {
      "type": "object",
      "title": "Response"
    },
    "field_name": {
      "type": "string"
    }
  },
  "response": {
    "type": "object",
    "title": "str | None"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "extract_field_from_www_auth",
    "arguments": {
      "response": {},
      "field_name": "<field_name_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **extract_scope_from_www_auth**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\src\mcp\client\auth\utils.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "response": {
      "type": "object",
      "title": "Response"
    }
  },
  "required": [
    "response"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "title": "str | None"
}
```

#### Payload Shape
```json
{
  "request": {
    "response": {
      "type": "object",
      "title": "Response"
    }
  },
  "response": {
    "type": "object",
    "title": "str | None"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "extract_scope_from_www_auth",
    "arguments": {
      "response": {}
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **extract_resource_metadata_from_www_auth**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\src\mcp\client\auth\utils.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "response": {
      "type": "object",
      "title": "Response"
    }
  },
  "required": [
    "response"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "title": "str | None"
}
```

#### Payload Shape
```json
{
  "request": {
    "response": {
      "type": "object",
      "title": "Response"
    }
  },
  "response": {
    "type": "object",
    "title": "str | None"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "extract_resource_metadata_from_www_auth",
    "arguments": {
      "response": {}
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **build_protected_resource_metadata_discovery_urls**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\src\mcp\client\auth\utils.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "www_auth_url": {
      "type": "object",
      "title": "str | None"
    },
    "server_url": {
      "type": "string"
    }
  },
  "required": [
    "server_url",
    "www_auth_url"
  ]
}
```

#### Output Schema
```json
{
  "type": "array",
  "items": {
    "type": "string"
  }
}
```

#### Payload Shape
```json
{
  "request": {
    "www_auth_url": {
      "type": "object",
      "title": "str | None"
    },
    "server_url": {
      "type": "string"
    }
  },
  "response": {
    "type": "array",
    "items": {
      "type": "string"
    }
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "build_protected_resource_metadata_discovery_urls",
    "arguments": {
      "www_auth_url": {},
      "server_url": "<server_url_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **get_client_metadata_scopes**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\src\mcp\client\auth\utils.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "www_authenticate_scope": {
      "type": "object",
      "title": "str | None"
    },
    "protected_resource_metadata": {
      "oneOf": [
        {
          "type": "object",
          "properties": {
            "resource": {
              "type": "object",
              "title": "AnyHttpUrl"
            },
            "authorization_servers": {
              "type": "array",
              "items": {
                "type": "object",
                "title": "AnyHttpUrl"
              }
            },
            "jwks_uri": {
              "type": "object",
              "title": "AnyHttpUrl | None"
            },
            "scopes_supported": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "bearer_methods_supported": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "resource_signing_alg_values_supported": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "resource_name": {
              "type": "object",
              "title": "str | None"
            },
            "resource_documentation": {
              "type": "object",
              "title": "AnyHttpUrl | None"
            },
            "resource_policy_uri": {
              "type": "object",
              "title": "AnyHttpUrl | None"
            },
            "resource_tos_uri": {
              "type": "object",
              "title": "AnyHttpUrl | None"
            },
            "tls_client_certificate_bound_access_tokens": {
              "type": "object",
              "title": "bool | None"
            },
            "authorization_details_types_supported": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "dpop_signing_alg_values_supported": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "dpop_bound_access_tokens_required": {
              "type": "object",
              "title": "bool | None"
            }
          },
          "required": [
            "resource"
          ]
        }
      ]
    },
    "authorization_server_metadata": {
      "oneOf": [
        {
          "type": "object",
          "properties": {
            "issuer": {
              "type": "object",
              "title": "AnyHttpUrl"
            },
            "authorization_endpoint": {
              "type": "object",
              "title": "AnyHttpUrl"
            },
            "token_endpoint": {
              "type": "object",
              "title": "AnyHttpUrl"
            },
            "registration_endpoint": {
              "type": "object",
              "title": "AnyHttpUrl | None"
            },
            "scopes_supported": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "response_types_supported": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "response_modes_supported": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "grant_types_supported": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "token_endpoint_auth_methods_supported": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "token_endpoint_auth_signing_alg_values_supported": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "service_documentation": {
              "type": "object",
              "title": "AnyHttpUrl | None"
            },
            "ui_locales_supported": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "op_policy_uri": {
              "type": "object",
              "title": "AnyHttpUrl | None"
            },
            "op_tos_uri": {
              "type": "object",
              "title": "AnyHttpUrl | None"
            },
            "revocation_endpoint": {
              "type": "object",
              "title": "AnyHttpUrl | None"
            },
            "revocation_endpoint_auth_methods_supported": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "revocation_endpoint_auth_signing_alg_values_supported": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "introspection_endpoint": {
              "type": "object",
              "title": "AnyHttpUrl | None"
            },
            "introspection_endpoint_auth_methods_supported": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "introspection_endpoint_auth_signing_alg_values_supported": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "code_challenge_methods_supported": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "client_id_metadata_document_supported": {
              "type": "object",
              "title": "bool | None"
            }
          },
          "required": [
            "issuer",
            "authorization_endpoint",
            "token_endpoint"
          ]
        }
      ]
    }
  },
  "required": [
    "protected_resource_metadata",
    "www_authenticate_scope"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "title": "str | None"
}
```

#### Payload Shape
```json
{
  "request": {
    "www_authenticate_scope": {
      "type": "object",
      "title": "str | None"
    },
    "protected_resource_metadata": {
      "oneOf": [
        {
          "type": "object",
          "properties": {
            "resource": {
              "type": "object",
              "title": "AnyHttpUrl"
            },
            "authorization_servers": {
              "type": "array",
              "items": {
                "type": "object",
                "title": "AnyHttpUrl"
              }
            },
            "jwks_uri": {
              "type": "object",
              "title": "AnyHttpUrl | None"
            },
            "scopes_supported": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "bearer_methods_supported": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "resource_signing_alg_values_supported": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "resource_name": {
              "type": "object",
              "title": "str | None"
            },
            "resource_documentation": {
              "type": "object",
              "title": "AnyHttpUrl | None"
            },
            "resource_policy_uri": {
              "type": "object",
              "title": "AnyHttpUrl | None"
            },
            "resource_tos_uri": {
              "type": "object",
              "title": "AnyHttpUrl | None"
            },
            "tls_client_certificate_bound_access_tokens": {
              "type": "object",
              "title": "bool | None"
            },
            "authorization_details_types_supported": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "dpop_signing_alg_values_supported": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "dpop_bound_access_tokens_required": {
              "type": "object",
              "title": "bool | None"
            }
          },
          "required": [
            "resource"
          ]
        }
      ]
    },
    "authorization_server_metadata": {
      "oneOf": [
        {
          "type": "object",
          "properties": {
            "issuer": {
              "type": "object",
              "title": "AnyHttpUrl"
            },
            "authorization_endpoint": {
              "type": "object",
              "title": "AnyHttpUrl"
            },
            "token_endpoint": {
              "type": "object",
              "title": "AnyHttpUrl"
            },
            "registration_endpoint": {
              "type": "object",
              "title": "AnyHttpUrl | None"
            },
            "scopes_supported": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "response_types_supported": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "response_modes_supported": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "grant_types_supported": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "token_endpoint_auth_methods_supported": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "token_endpoint_auth_signing_alg_values_supported": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "service_documentation": {
              "type": "object",
              "title": "AnyHttpUrl | None"
            },
            "ui_locales_supported": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "op_policy_uri": {
              "type": "object",
              "title": "AnyHttpUrl | None"
            },
            "op_tos_uri": {
              "type": "object",
              "title": "AnyHttpUrl | None"
            },
            "revocation_endpoint": {
              "type": "object",
              "title": "AnyHttpUrl | None"
            },
            "revocation_endpoint_auth_methods_supported": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "revocation_endpoint_auth_signing_alg_values_supported": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "introspection_endpoint": {
              "type": "object",
              "title": "AnyHttpUrl | None"
            },
            "introspection_endpoint_auth_methods_supported": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "introspection_endpoint_auth_signing_alg_values_supported": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "code_challenge_methods_supported": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "client_id_metadata_document_supported": {
              "type": "object",
              "title": "bool | None"
            }
          },
          "required": [
            "issuer",
            "authorization_endpoint",
            "token_endpoint"
          ]
        }
      ]
    }
  },
  "response": {
    "type": "object",
    "title": "str | None"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "get_client_metadata_scopes",
    "arguments": {
      "www_authenticate_scope": {},
      "protected_resource_metadata": "<protected_resource_metadata_str>",
      "authorization_server_metadata": "<authorization_server_metadata_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **build_oauth_authorization_server_metadata_discovery_urls**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\src\mcp\client\auth\utils.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "auth_server_url": {
      "type": "object",
      "title": "str | None"
    },
    "server_url": {
      "type": "string"
    }
  },
  "required": [
    "auth_server_url",
    "server_url"
  ]
}
```

#### Output Schema
```json
{
  "type": "array",
  "items": {
    "type": "string"
  }
}
```

#### Payload Shape
```json
{
  "request": {
    "auth_server_url": {
      "type": "object",
      "title": "str | None"
    },
    "server_url": {
      "type": "string"
    }
  },
  "response": {
    "type": "array",
    "items": {
      "type": "string"
    }
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "build_oauth_authorization_server_metadata_discovery_urls",
    "arguments": {
      "auth_server_url": {},
      "server_url": "<server_url_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **create_oauth_metadata_request**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\src\mcp\client\auth\utils.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "url": {
      "type": "string"
    }
  },
  "required": [
    "url"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "properties": {
    "method": {
      "type": "object",
      "title": "MethodT"
    },
    "params": {
      "type": "object",
      "title": "RequestParamsT"
    }
  },
  "required": [
    "method",
    "params"
  ]
}
```

#### Payload Shape
```json
{
  "request": {
    "url": {
      "type": "string"
    }
  },
  "response": {
    "type": "object",
    "properties": {
      "method": {
        "type": "object",
        "title": "MethodT"
      },
      "params": {
        "type": "object",
        "title": "RequestParamsT"
      }
    },
    "required": [
      "method",
      "params"
    ]
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "create_oauth_metadata_request",
    "arguments": {
      "url": "<url_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **create_client_registration_request**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\src\mcp\client\auth\utils.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "auth_server_metadata": {
      "oneOf": [
        {
          "type": "object",
          "properties": {
            "issuer": {
              "type": "object",
              "title": "AnyHttpUrl"
            },
            "authorization_endpoint": {
              "type": "object",
              "title": "AnyHttpUrl"
            },
            "token_endpoint": {
              "type": "object",
              "title": "AnyHttpUrl"
            },
            "registration_endpoint": {
              "type": "object",
              "title": "AnyHttpUrl | None"
            },
            "scopes_supported": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "response_types_supported": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "response_modes_supported": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "grant_types_supported": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "token_endpoint_auth_methods_supported": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "token_endpoint_auth_signing_alg_values_supported": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "service_documentation": {
              "type": "object",
              "title": "AnyHttpUrl | None"
            },
            "ui_locales_supported": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "op_policy_uri": {
              "type": "object",
              "title": "AnyHttpUrl | None"
            },
            "op_tos_uri": {
              "type": "object",
              "title": "AnyHttpUrl | None"
            },
            "revocation_endpoint": {
              "type": "object",
              "title": "AnyHttpUrl | None"
            },
            "revocation_endpoint_auth_methods_supported": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "revocation_endpoint_auth_signing_alg_values_supported": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "introspection_endpoint": {
              "type": "object",
              "title": "AnyHttpUrl | None"
            },
            "introspection_endpoint_auth_methods_supported": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "introspection_endpoint_auth_signing_alg_values_supported": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "code_challenge_methods_supported": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "client_id_metadata_document_supported": {
              "type": "object",
              "title": "bool | None"
            }
          },
          "required": [
            "issuer",
            "authorization_endpoint",
            "token_endpoint"
          ]
        }
      ]
    },
    "client_metadata": {
      "type": "object",
      "properties": {
        "redirect_uris": {
          "type": "array",
          "items": {
            "type": "object",
            "title": "AnyUrl"
          }
        },
        "token_endpoint_auth_method": {
          "type": "string",
          "enum": [
            "none",
            "client_secret_post",
            "client_secret_basic",
            "private_key_jwt"
          ]
        },
        "grant_types": {
          "type": "array",
          "items": {
            "type": "string",
            "enum": [
              "authorization_code",
              "refresh_token",
              "urn:ietf:params:oauth:grant-type:jwt-bearer"
            ]
          }
        },
        "response_types": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "scope": {
          "type": "object",
          "title": "str | None"
        },
        "client_name": {
          "type": "object",
          "title": "str | None"
        },
        "client_uri": {
          "type": "object",
          "title": "AnyHttpUrl | None"
        },
        "logo_uri": {
          "type": "object",
          "title": "AnyHttpUrl | None"
        },
        "contacts": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "tos_uri": {
          "type": "object",
          "title": "AnyHttpUrl | None"
        },
        "policy_uri": {
          "type": "object",
          "title": "AnyHttpUrl | None"
        },
        "jwks_uri": {
          "type": "object",
          "title": "AnyHttpUrl | None"
        },
        "jwks": {
          "type": "object",
          "title": "Any | None"
        },
        "software_id": {
          "type": "object",
          "title": "str | None"
        },
        "software_version": {
          "type": "object",
          "title": "str | None"
        }
      },
      "required": [
        "redirect_uris",
        "token_endpoint_auth_method",
        "grant_types",
        "response_types",
        "scope",
        "client_name",
        "client_uri",
        "logo_uri",
        "contacts",
        "tos_uri",
        "policy_uri",
        "jwks_uri",
        "jwks",
        "software_id",
        "software_version"
      ]
    },
    "auth_base_url": {
      "type": "string"
    }
  },
  "required": [
    "auth_base_url",
    "auth_server_metadata",
    "client_metadata"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "properties": {
    "method": {
      "type": "object",
      "title": "MethodT"
    },
    "params": {
      "type": "object",
      "title": "RequestParamsT"
    }
  },
  "required": [
    "method",
    "params"
  ]
}
```

#### Payload Shape
```json
{
  "request": {
    "auth_server_metadata": {
      "oneOf": [
        {
          "type": "object",
          "properties": {
            "issuer": {
              "type": "object",
              "title": "AnyHttpUrl"
            },
            "authorization_endpoint": {
              "type": "object",
              "title": "AnyHttpUrl"
            },
            "token_endpoint": {
              "type": "object",
              "title": "AnyHttpUrl"
            },
            "registration_endpoint": {
              "type": "object",
              "title": "AnyHttpUrl | None"
            },
            "scopes_supported": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "response_types_supported": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "response_modes_supported": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "grant_types_supported": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "token_endpoint_auth_methods_supported": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "token_endpoint_auth_signing_alg_values_supported": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "service_documentation": {
              "type": "object",
              "title": "AnyHttpUrl | None"
            },
            "ui_locales_supported": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "op_policy_uri": {
              "type": "object",
              "title": "AnyHttpUrl | None"
            },
            "op_tos_uri": {
              "type": "object",
              "title": "AnyHttpUrl | None"
            },
            "revocation_endpoint": {
              "type": "object",
              "title": "AnyHttpUrl | None"
            },
            "revocation_endpoint_auth_methods_supported": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "revocation_endpoint_auth_signing_alg_values_supported": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "introspection_endpoint": {
              "type": "object",
              "title": "AnyHttpUrl | None"
            },
            "introspection_endpoint_auth_methods_supported": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "introspection_endpoint_auth_signing_alg_values_supported": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "code_challenge_methods_supported": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "client_id_metadata_document_supported": {
              "type": "object",
              "title": "bool | None"
            }
          },
          "required": [
            "issuer",
            "authorization_endpoint",
            "token_endpoint"
          ]
        }
      ]
    },
    "client_metadata": {
      "type": "object",
      "properties": {
        "redirect_uris": {
          "type": "array",
          "items": {
            "type": "object",
            "title": "AnyUrl"
          }
        },
        "token_endpoint_auth_method": {
          "type": "string",
          "enum": [
            "none",
            "client_secret_post",
            "client_secret_basic",
            "private_key_jwt"
          ]
        },
        "grant_types": {
          "type": "array",
          "items": {
            "type": "string",
            "enum": [
              "authorization_code",
              "refresh_token",
              "urn:ietf:params:oauth:grant-type:jwt-bearer"
            ]
          }
        },
        "response_types": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "scope": {
          "type": "object",
          "title": "str | None"
        },
        "client_name": {
          "type": "object",
          "title": "str | None"
        },
        "client_uri": {
          "type": "object",
          "title": "AnyHttpUrl | None"
        },
        "logo_uri": {
          "type": "object",
          "title": "AnyHttpUrl | None"
        },
        "contacts": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "tos_uri": {
          "type": "object",
          "title": "AnyHttpUrl | None"
        },
        "policy_uri": {
          "type": "object",
          "title": "AnyHttpUrl | None"
        },
        "jwks_uri": {
          "type": "object",
          "title": "AnyHttpUrl | None"
        },
        "jwks": {
          "type": "object",
          "title": "Any | None"
        },
        "software_id": {
          "type": "object",
          "title": "str | None"
        },
        "software_version": {
          "type": "object",
          "title": "str | None"
        }
      },
      "required": [
        "redirect_uris",
        "token_endpoint_auth_method",
        "grant_types",
        "response_types",
        "scope",
        "client_name",
        "client_uri",
        "logo_uri",
        "contacts",
        "tos_uri",
        "policy_uri",
        "jwks_uri",
        "jwks",
        "software_id",
        "software_version"
      ]
    },
    "auth_base_url": {
      "type": "string"
    }
  },
  "response": {
    "type": "object",
    "properties": {
      "method": {
        "type": "object",
        "title": "MethodT"
      },
      "params": {
        "type": "object",
        "title": "RequestParamsT"
      }
    },
    "required": [
      "method",
      "params"
    ]
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "create_client_registration_request",
    "arguments": {
      "auth_server_metadata": "<auth_server_metadata_str>",
      "client_metadata": {},
      "auth_base_url": "<auth_base_url_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **get_default_environment**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\src\mcp\client\stdio\__init__.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "additionalProperties": {
    "type": "string",
    "guessed": true
  }
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "additionalProperties": {
      "type": "string",
      "guessed": true
    }
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "get_default_environment",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **_get_executable_command**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\src\mcp\client\stdio\__init__.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "command": {
      "type": "string"
    }
  },
  "required": [
    "command"
  ]
}
```

#### Output Schema
```json
{
  "type": "string"
}
```

#### Payload Shape
```json
{
  "request": {
    "command": {
      "type": "string"
    }
  },
  "response": {
    "type": "string"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "_get_executable_command",
    "arguments": {
      "command": "<command_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **get_windows_executable_command**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\src\mcp\os\win32\utilities.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "command": {
      "type": "string"
    }
  },
  "required": [
    "command"
  ]
}
```

#### Output Schema
```json
{
  "type": "string"
}
```

#### Payload Shape
```json
{
  "request": {
    "command": {
      "type": "string"
    }
  },
  "response": {
    "type": "string"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: ['subprocess.Popen']
- Env: []
- Severity: **high**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "get_windows_executable_command",
    "arguments": {
      "command": "<command_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **_create_job_object**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\src\mcp\os\win32\utilities.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "title": "int | None"
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "title": "int | None"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: ['subprocess.Popen']
- Env: []
- Severity: **high**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "_create_job_object",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **_maybe_assign_process_to_job**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\src\mcp\os\win32\utilities.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "process": {
      "type": "object",
      "title": "Process | FallbackProcess"
    },
    "job": {
      "type": "object",
      "title": "JobHandle | None"
    }
  },
  "required": [
    "job",
    "process"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "title": "None"
}
```

#### Payload Shape
```json
{
  "request": {
    "process": {
      "type": "object",
      "title": "Process | FallbackProcess"
    },
    "job": {
      "type": "object",
      "title": "JobHandle | None"
    }
  },
  "response": {
    "type": "object",
    "title": "None"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: ['subprocess.Popen']
- Env: []
- Severity: **high**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "_maybe_assign_process_to_job",
    "arguments": {
      "process": {},
      "job": {}
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **_validate_elicitation_schema**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\src\mcp\server\elicitation.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "schema": {
      "type": "object",
      "title": "type[BaseModel]"
    }
  },
  "required": [
    "schema"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "title": "None"
}
```

#### Payload Shape
```json
{
  "request": {
    "schema": {
      "type": "object",
      "title": "type[BaseModel]"
    }
  },
  "response": {
    "type": "object",
    "title": "None"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "_validate_elicitation_schema",
    "arguments": {
      "schema": {}
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **_is_primitive_field**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\src\mcp\server\elicitation.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "field_info": {
      "type": "object",
      "title": "FieldInfo"
    }
  },
  "required": [
    "field_info"
  ]
}
```

#### Output Schema
```json
{
  "type": "boolean"
}
```

#### Payload Shape
```json
{
  "request": {
    "field_info": {
      "type": "object",
      "title": "FieldInfo"
    }
  },
  "response": {
    "type": "boolean"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "_is_primitive_field",
    "arguments": {
      "field_info": {}
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **stringify_pydantic_error**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\src\mcp\server\auth\errors.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "validation_error": {
      "type": "object",
      "properties": {}
    }
  },
  "required": [
    "validation_error"
  ]
}
```

#### Output Schema
```json
{
  "type": "string"
}
```

#### Payload Shape
```json
{
  "request": {
    "validation_error": {
      "type": "object",
      "properties": {}
    }
  },
  "response": {
    "type": "string"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "stringify_pydantic_error",
    "arguments": {
      "validation_error": {}
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **construct_redirect_uri**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\src\mcp\server\auth\provider.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "redirect_uri_base": {
      "type": "string"
    }
  },
  "required": [
    "redirect_uri_base"
  ]
}
```

#### Output Schema
```json
{
  "type": "string"
}
```

#### Payload Shape
```json
{
  "request": {
    "redirect_uri_base": {
      "type": "string"
    }
  },
  "response": {
    "type": "string"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "construct_redirect_uri",
    "arguments": {
      "redirect_uri_base": "<redirect_uri_base_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **validate_issuer_url**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\src\mcp\server\auth\routes.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "url": {
      "type": "object",
      "title": "AnyHttpUrl"
    }
  },
  "required": [
    "url"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {
    "url": {
      "type": "object",
      "title": "AnyHttpUrl"
    }
  },
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "validate_issuer_url",
    "arguments": {
      "url": {}
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **cors_middleware**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\src\mcp\server\auth\routes.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "handler": {
      "type": "object",
      "title": "Callable[[Request], Response | Awaitable[Response]]"
    },
    "allow_methods": {
      "type": "array",
      "items": {
        "type": "string"
      }
    }
  },
  "required": [
    "allow_methods",
    "handler"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "title": "ASGIApp"
}
```

#### Payload Shape
```json
{
  "request": {
    "handler": {
      "type": "object",
      "title": "Callable[[Request], Response | Awaitable[Response]]"
    },
    "allow_methods": {
      "type": "array",
      "items": {
        "type": "string"
      }
    }
  },
  "response": {
    "type": "object",
    "title": "ASGIApp"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "cors_middleware",
    "arguments": {
      "handler": {},
      "allow_methods": []
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **create_auth_routes**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\src\mcp\server\auth\routes.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "provider": {
      "type": "object",
      "title": "OAuthAuthorizationServerProvider[Any, Any, Any]"
    },
    "issuer_url": {
      "type": "object",
      "title": "AnyHttpUrl"
    },
    "service_documentation_url": {
      "type": "object",
      "title": "AnyHttpUrl | None"
    },
    "client_registration_options": {
      "oneOf": [
        {
          "type": "object",
          "properties": {
            "enabled": {
              "type": "boolean"
            },
            "client_secret_expiry_seconds": {
              "type": "object",
              "title": "int | None"
            },
            "valid_scopes": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "default_scopes": {
              "type": "array",
              "items": {
                "type": "string"
              }
            }
          }
        }
      ]
    },
    "revocation_options": {
      "oneOf": [
        {
          "type": "object",
          "properties": {
            "enabled": {
              "type": "boolean"
            }
          }
        }
      ]
    }
  },
  "required": [
    "issuer_url",
    "provider"
  ]
}
```

#### Output Schema
```json
{
  "type": "array",
  "items": {
    "type": "object",
    "title": "Route"
  }
}
```

#### Payload Shape
```json
{
  "request": {
    "provider": {
      "type": "object",
      "title": "OAuthAuthorizationServerProvider[Any, Any, Any]"
    },
    "issuer_url": {
      "type": "object",
      "title": "AnyHttpUrl"
    },
    "service_documentation_url": {
      "type": "object",
      "title": "AnyHttpUrl | None"
    },
    "client_registration_options": {
      "oneOf": [
        {
          "type": "object",
          "properties": {
            "enabled": {
              "type": "boolean"
            },
            "client_secret_expiry_seconds": {
              "type": "object",
              "title": "int | None"
            },
            "valid_scopes": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "default_scopes": {
              "type": "array",
              "items": {
                "type": "string"
              }
            }
          }
        }
      ]
    },
    "revocation_options": {
      "oneOf": [
        {
          "type": "object",
          "properties": {
            "enabled": {
              "type": "boolean"
            }
          }
        }
      ]
    }
  },
  "response": {
    "type": "array",
    "items": {
      "type": "object",
      "title": "Route"
    }
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "create_auth_routes",
    "arguments": {
      "provider": {},
      "issuer_url": {},
      "service_documentation_url": {},
      "client_registration_options": "<client_registration_options_str>",
      "revocation_options": "<revocation_options_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **build_metadata**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\src\mcp\server\auth\routes.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "issuer_url": {
      "type": "object",
      "title": "AnyHttpUrl"
    },
    "service_documentation_url": {
      "type": "object",
      "title": "AnyHttpUrl | None"
    },
    "client_registration_options": {
      "type": "object",
      "properties": {
        "enabled": {
          "type": "boolean"
        },
        "client_secret_expiry_seconds": {
          "type": "object",
          "title": "int | None"
        },
        "valid_scopes": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "default_scopes": {
          "type": "array",
          "items": {
            "type": "string"
          }
        }
      },
      "required": [
        "enabled",
        "client_secret_expiry_seconds",
        "valid_scopes",
        "default_scopes"
      ]
    },
    "revocation_options": {
      "type": "object",
      "properties": {
        "enabled": {
          "type": "boolean"
        }
      },
      "required": [
        "enabled"
      ]
    }
  },
  "required": [
    "client_registration_options",
    "issuer_url",
    "revocation_options",
    "service_documentation_url"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "properties": {
    "issuer": {
      "type": "object",
      "title": "AnyHttpUrl"
    },
    "authorization_endpoint": {
      "type": "object",
      "title": "AnyHttpUrl"
    },
    "token_endpoint": {
      "type": "object",
      "title": "AnyHttpUrl"
    },
    "registration_endpoint": {
      "type": "object",
      "title": "AnyHttpUrl | None"
    },
    "scopes_supported": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "response_types_supported": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "response_modes_supported": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "grant_types_supported": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "token_endpoint_auth_methods_supported": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "token_endpoint_auth_signing_alg_values_supported": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "service_documentation": {
      "type": "object",
      "title": "AnyHttpUrl | None"
    },
    "ui_locales_supported": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "op_policy_uri": {
      "type": "object",
      "title": "AnyHttpUrl | None"
    },
    "op_tos_uri": {
      "type": "object",
      "title": "AnyHttpUrl | None"
    },
    "revocation_endpoint": {
      "type": "object",
      "title": "AnyHttpUrl | None"
    },
    "revocation_endpoint_auth_methods_supported": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "revocation_endpoint_auth_signing_alg_values_supported": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "introspection_endpoint": {
      "type": "object",
      "title": "AnyHttpUrl | None"
    },
    "introspection_endpoint_auth_methods_supported": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "introspection_endpoint_auth_signing_alg_values_supported": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "code_challenge_methods_supported": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "client_id_metadata_document_supported": {
      "type": "object",
      "title": "bool | None"
    }
  },
  "required": [
    "issuer",
    "authorization_endpoint",
    "token_endpoint",
    "registration_endpoint",
    "scopes_supported",
    "response_types_supported",
    "response_modes_supported",
    "grant_types_supported",
    "token_endpoint_auth_methods_supported",
    "token_endpoint_auth_signing_alg_values_supported",
    "service_documentation",
    "ui_locales_supported",
    "op_policy_uri",
    "op_tos_uri",
    "revocation_endpoint",
    "revocation_endpoint_auth_methods_supported",
    "revocation_endpoint_auth_signing_alg_values_supported",
    "introspection_endpoint",
    "introspection_endpoint_auth_methods_supported",
    "introspection_endpoint_auth_signing_alg_values_supported",
    "code_challenge_methods_supported",
    "client_id_metadata_document_supported"
  ]
}
```

#### Payload Shape
```json
{
  "request": {
    "issuer_url": {
      "type": "object",
      "title": "AnyHttpUrl"
    },
    "service_documentation_url": {
      "type": "object",
      "title": "AnyHttpUrl | None"
    },
    "client_registration_options": {
      "type": "object",
      "properties": {
        "enabled": {
          "type": "boolean"
        },
        "client_secret_expiry_seconds": {
          "type": "object",
          "title": "int | None"
        },
        "valid_scopes": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "default_scopes": {
          "type": "array",
          "items": {
            "type": "string"
          }
        }
      },
      "required": [
        "enabled",
        "client_secret_expiry_seconds",
        "valid_scopes",
        "default_scopes"
      ]
    },
    "revocation_options": {
      "type": "object",
      "properties": {
        "enabled": {
          "type": "boolean"
        }
      },
      "required": [
        "enabled"
      ]
    }
  },
  "response": {
    "type": "object",
    "properties": {
      "issuer": {
        "type": "object",
        "title": "AnyHttpUrl"
      },
      "authorization_endpoint": {
        "type": "object",
        "title": "AnyHttpUrl"
      },
      "token_endpoint": {
        "type": "object",
        "title": "AnyHttpUrl"
      },
      "registration_endpoint": {
        "type": "object",
        "title": "AnyHttpUrl | None"
      },
      "scopes_supported": {
        "type": "array",
        "items": {
          "type": "string"
        }
      },
      "response_types_supported": {
        "type": "array",
        "items": {
          "type": "string"
        }
      },
      "response_modes_supported": {
        "type": "array",
        "items": {
          "type": "string"
        }
      },
      "grant_types_supported": {
        "type": "array",
        "items": {
          "type": "string"
        }
      },
      "token_endpoint_auth_methods_supported": {
        "type": "array",
        "items": {
          "type": "string"
        }
      },
      "token_endpoint_auth_signing_alg_values_supported": {
        "type": "array",
        "items": {
          "type": "string"
        }
      },
      "service_documentation": {
        "type": "object",
        "title": "AnyHttpUrl | None"
      },
      "ui_locales_supported": {
        "type": "array",
        "items": {
          "type": "string"
        }
      },
      "op_policy_uri": {
        "type": "object",
        "title": "AnyHttpUrl | None"
      },
      "op_tos_uri": {
        "type": "object",
        "title": "AnyHttpUrl | None"
      },
      "revocation_endpoint": {
        "type": "object",
        "title": "AnyHttpUrl | None"
      },
      "revocation_endpoint_auth_methods_supported": {
        "type": "array",
        "items": {
          "type": "string"
        }
      },
      "revocation_endpoint_auth_signing_alg_values_supported": {
        "type": "array",
        "items": {
          "type": "string"
        }
      },
      "introspection_endpoint": {
        "type": "object",
        "title": "AnyHttpUrl | None"
      },
      "introspection_endpoint_auth_methods_supported": {
        "type": "array",
        "items": {
          "type": "string"
        }
      },
      "introspection_endpoint_auth_signing_alg_values_supported": {
        "type": "array",
        "items": {
          "type": "string"
        }
      },
      "code_challenge_methods_supported": {
        "type": "array",
        "items": {
          "type": "string"
        }
      },
      "client_id_metadata_document_supported": {
        "type": "object",
        "title": "bool | None"
      }
    },
    "required": [
      "issuer",
      "authorization_endpoint",
      "token_endpoint",
      "registration_endpoint",
      "scopes_supported",
      "response_types_supported",
      "response_modes_supported",
      "grant_types_supported",
      "token_endpoint_auth_methods_supported",
      "token_endpoint_auth_signing_alg_values_supported",
      "service_documentation",
      "ui_locales_supported",
      "op_policy_uri",
      "op_tos_uri",
      "revocation_endpoint",
      "revocation_endpoint_auth_methods_supported",
      "revocation_endpoint_auth_signing_alg_values_supported",
      "introspection_endpoint",
      "introspection_endpoint_auth_methods_supported",
      "introspection_endpoint_auth_signing_alg_values_supported",
      "code_challenge_methods_supported",
      "client_id_metadata_document_supported"
    ]
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "build_metadata",
    "arguments": {
      "issuer_url": {},
      "service_documentation_url": {},
      "client_registration_options": {},
      "revocation_options": {}
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **build_resource_metadata_url**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\src\mcp\server\auth\routes.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "resource_server_url": {
      "type": "object",
      "title": "AnyHttpUrl"
    }
  },
  "required": [
    "resource_server_url"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "title": "AnyHttpUrl"
}
```

#### Payload Shape
```json
{
  "request": {
    "resource_server_url": {
      "type": "object",
      "title": "AnyHttpUrl"
    }
  },
  "response": {
    "type": "object",
    "title": "AnyHttpUrl"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "build_resource_metadata_url",
    "arguments": {
      "resource_server_url": {}
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **create_protected_resource_routes**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\src\mcp\server\auth\routes.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "resource_url": {
      "type": "object",
      "title": "AnyHttpUrl"
    },
    "authorization_servers": {
      "type": "array",
      "items": {
        "type": "object",
        "title": "AnyHttpUrl"
      }
    },
    "scopes_supported": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "resource_name": {
      "type": "object",
      "title": "str | None"
    },
    "resource_documentation": {
      "type": "object",
      "title": "AnyHttpUrl | None"
    }
  },
  "required": [
    "authorization_servers",
    "resource_url"
  ]
}
```

#### Output Schema
```json
{
  "type": "array",
  "items": {
    "type": "object",
    "title": "Route"
  }
}
```

#### Payload Shape
```json
{
  "request": {
    "resource_url": {
      "type": "object",
      "title": "AnyHttpUrl"
    },
    "authorization_servers": {
      "type": "array",
      "items": {
        "type": "object",
        "title": "AnyHttpUrl"
      }
    },
    "scopes_supported": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "resource_name": {
      "type": "object",
      "title": "str | None"
    },
    "resource_documentation": {
      "type": "object",
      "title": "AnyHttpUrl | None"
    }
  },
  "response": {
    "type": "array",
    "items": {
      "type": "object",
      "title": "Route"
    }
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "create_protected_resource_routes",
    "arguments": {
      "resource_url": {},
      "authorization_servers": [],
      "scopes_supported": [],
      "resource_name": {},
      "resource_documentation": {}
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **best_effort_extract_string**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\src\mcp\server\auth\handlers\authorize.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "key": {
      "type": "string"
    },
    "params": {
      "type": "object",
      "title": "None | FormData | QueryParams"
    }
  },
  "required": [
    "key",
    "params"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "title": "str | None"
}
```

#### Payload Shape
```json
{
  "request": {
    "key": {
      "type": "string"
    },
    "params": {
      "type": "object",
      "title": "None | FormData | QueryParams"
    }
  },
  "response": {
    "type": "object",
    "title": "str | None"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "best_effort_extract_string",
    "arguments": {
      "key": "<key_str>",
      "params": {}
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **get_access_token**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\src\mcp\server\auth\middleware\auth_context.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "oneOf": [
    {
      "type": "object",
      "properties": {
        "token": {
          "type": "string"
        },
        "client_id": {
          "type": "string"
        },
        "scopes": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "expires_at": {
          "type": "object",
          "title": "int | None"
        },
        "resource": {
          "type": "object",
          "title": "str | None"
        }
      },
      "required": [
        "token",
        "client_id",
        "scopes"
      ]
    }
  ]
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "oneOf": [
      {
        "type": "object",
        "properties": {
          "token": {
            "type": "string"
          },
          "client_id": {
            "type": "string"
          },
          "scopes": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "expires_at": {
            "type": "object",
            "title": "int | None"
          },
          "resource": {
            "type": "object",
            "title": "str | None"
          }
        },
        "required": [
          "token",
          "client_id",
          "scopes"
        ]
      }
    ]
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "get_access_token",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **lifespan_wrapper**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\src\mcp\server\fastmcp\server.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "app": {
      "type": "object",
      "title": "FastMCP[LifespanResultT]"
    },
    "lifespan": {
      "type": "object",
      "title": "Callable[[FastMCP[LifespanResultT]], AbstractAsyncContextManager[LifespanResultT]]"
    }
  },
  "required": [
    "app",
    "lifespan"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "title": "Callable[[MCPServer[LifespanResultT, Request]], AbstractAsyncContextManager[LifespanResultT]]"
}
```

#### Payload Shape
```json
{
  "request": {
    "app": {
      "type": "object",
      "title": "FastMCP[LifespanResultT]"
    },
    "lifespan": {
      "type": "object",
      "title": "Callable[[FastMCP[LifespanResultT]], AbstractAsyncContextManager[LifespanResultT]]"
    }
  },
  "response": {
    "type": "object",
    "title": "Callable[[MCPServer[LifespanResultT, Request]], AbstractAsyncContextManager[LifespanResultT]]"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['client.get']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "lifespan_wrapper",
    "arguments": {
      "app": {},
      "lifespan": {}
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **_is_async_callable**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\src\mcp\server\fastmcp\tools\base.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "obj": {
      "type": "object",
      "title": "Any"
    }
  },
  "required": [
    "obj"
  ]
}
```

#### Output Schema
```json
{
  "type": "boolean"
}
```

#### Payload Shape
```json
{
  "request": {
    "obj": {
      "type": "object",
      "title": "Any"
    }
  },
  "response": {
    "type": "boolean"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "_is_async_callable",
    "arguments": {
      "obj": {}
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **find_context_parameter**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\src\mcp\server\fastmcp\utilities\context_injection.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "fn": {
      "type": "object",
      "title": "Callable[..., Any]"
    }
  },
  "required": [
    "fn"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "title": "str | None"
}
```

#### Payload Shape
```json
{
  "request": {
    "fn": {
      "type": "object",
      "title": "Callable[..., Any]"
    }
  },
  "response": {
    "type": "object",
    "title": "str | None"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "find_context_parameter",
    "arguments": {
      "fn": {}
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **inject_context**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\src\mcp\server\fastmcp\utilities\context_injection.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "fn": {
      "type": "object",
      "title": "Callable[..., Any]"
    },
    "kwargs": {
      "type": "object",
      "additionalProperties": {
        "type": "string",
        "guessed": true
      }
    },
    "context": {
      "type": "object",
      "title": "Any | None"
    },
    "context_kwarg": {
      "type": "object",
      "title": "str | None"
    }
  },
  "required": [
    "context",
    "context_kwarg",
    "fn",
    "kwargs"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "additionalProperties": {
    "type": "string",
    "guessed": true
  }
}
```

#### Payload Shape
```json
{
  "request": {
    "fn": {
      "type": "object",
      "title": "Callable[..., Any]"
    },
    "kwargs": {
      "type": "object",
      "additionalProperties": {
        "type": "string",
        "guessed": true
      }
    },
    "context": {
      "type": "object",
      "title": "Any | None"
    },
    "context_kwarg": {
      "type": "object",
      "title": "str | None"
    }
  },
  "response": {
    "type": "object",
    "additionalProperties": {
      "type": "string",
      "guessed": true
    }
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "inject_context",
    "arguments": {
      "fn": {},
      "kwargs": {},
      "context": {},
      "context_kwarg": {}
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **func_metadata**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\src\mcp\server\fastmcp\utilities\func_metadata.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "func": {
      "type": "object",
      "title": "Callable[..., Any]"
    },
    "skip_names": {
      "type": "object",
      "title": "Sequence[str]"
    },
    "structured_output": {
      "type": "object",
      "title": "bool | None"
    }
  },
  "required": [
    "func"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "properties": {
    "arg_model": {
      "type": "object",
      "title": "Annotated[type[ArgModelBase], WithJsonSchema(None)]"
    },
    "output_schema": {
      "type": "object",
      "additionalProperties": {
        "type": "string",
        "guessed": true
      }
    },
    "output_model": {
      "type": "object",
      "title": "Annotated[type[BaseModel], WithJsonSchema(None)] | None"
    },
    "wrap_output": {
      "type": "boolean"
    }
  },
  "required": [
    "arg_model",
    "output_schema",
    "output_model",
    "wrap_output"
  ]
}
```

#### Payload Shape
```json
{
  "request": {
    "func": {
      "type": "object",
      "title": "Callable[..., Any]"
    },
    "skip_names": {
      "type": "object",
      "title": "Sequence[str]"
    },
    "structured_output": {
      "type": "object",
      "title": "bool | None"
    }
  },
  "response": {
    "type": "object",
    "properties": {
      "arg_model": {
        "type": "object",
        "title": "Annotated[type[ArgModelBase], WithJsonSchema(None)]"
      },
      "output_schema": {
        "type": "object",
        "additionalProperties": {
          "type": "string",
          "guessed": true
        }
      },
      "output_model": {
        "type": "object",
        "title": "Annotated[type[BaseModel], WithJsonSchema(None)] | None"
      },
      "wrap_output": {
        "type": "boolean"
      }
    },
    "required": [
      "arg_model",
      "output_schema",
      "output_model",
      "wrap_output"
    ]
  }
}
```

#### Syscalls
- Filesystem: ['data.copy']
- Network: []
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "func_metadata",
    "arguments": {
      "func": {},
      "skip_names": {},
      "structured_output": {}
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **_try_create_model_and_schema**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\src\mcp\server\fastmcp\utilities\func_metadata.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "original_annotation": {
      "type": "object",
      "title": "Any"
    },
    "type_expr": {
      "type": "object",
      "title": "Any"
    },
    "func_name": {
      "type": "string"
    }
  },
  "required": [
    "func_name",
    "original_annotation",
    "type_expr"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "title": "tuple[type[BaseModel] | None, dict[str, Any] | None, bool]"
}
```

#### Payload Shape
```json
{
  "request": {
    "original_annotation": {
      "type": "object",
      "title": "Any"
    },
    "type_expr": {
      "type": "object",
      "title": "Any"
    },
    "func_name": {
      "type": "string"
    }
  },
  "response": {
    "type": "object",
    "title": "tuple[type[BaseModel] | None, dict[str, Any] | None, bool]"
  }
}
```

#### Syscalls
- Filesystem: ['data.copy']
- Network: []
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "_try_create_model_and_schema",
    "arguments": {
      "original_annotation": {},
      "type_expr": {},
      "func_name": "<func_name_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **_create_model_from_class**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\src\mcp\server\fastmcp\utilities\func_metadata.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "type_hints": {
      "type": "object",
      "additionalProperties": {
        "type": "string",
        "guessed": true
      }
    }
  },
  "required": [
    "type_hints"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "title": "type[BaseModel]"
}
```

#### Payload Shape
```json
{
  "request": {
    "type_hints": {
      "type": "object",
      "additionalProperties": {
        "type": "string",
        "guessed": true
      }
    }
  },
  "response": {
    "type": "object",
    "title": "type[BaseModel]"
  }
}
```

#### Syscalls
- Filesystem: ['data.copy']
- Network: []
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "_create_model_from_class",
    "arguments": {
      "type_hints": {}
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **_create_model_from_typeddict**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\src\mcp\server\fastmcp\utilities\func_metadata.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "td_type": {
      "type": "object",
      "title": "type[Any]"
    }
  },
  "required": [
    "td_type"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "title": "type[BaseModel]"
}
```

#### Payload Shape
```json
{
  "request": {
    "td_type": {
      "type": "object",
      "title": "type[Any]"
    }
  },
  "response": {
    "type": "object",
    "title": "type[BaseModel]"
  }
}
```

#### Syscalls
- Filesystem: ['data.copy']
- Network: []
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "_create_model_from_typeddict",
    "arguments": {
      "td_type": {}
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **_create_wrapped_model**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\src\mcp\server\fastmcp\utilities\func_metadata.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "func_name": {
      "type": "string"
    },
    "annotation": {
      "type": "object",
      "title": "Any"
    }
  },
  "required": [
    "annotation",
    "func_name"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "title": "type[BaseModel]"
}
```

#### Payload Shape
```json
{
  "request": {
    "func_name": {
      "type": "string"
    },
    "annotation": {
      "type": "object",
      "title": "Any"
    }
  },
  "response": {
    "type": "object",
    "title": "type[BaseModel]"
  }
}
```

#### Syscalls
- Filesystem: ['data.copy']
- Network: []
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "_create_wrapped_model",
    "arguments": {
      "func_name": "<func_name_str>",
      "annotation": {}
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **_create_dict_model**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\src\mcp\server\fastmcp\utilities\func_metadata.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "func_name": {
      "type": "string"
    },
    "dict_annotation": {
      "type": "object",
      "title": "Any"
    }
  },
  "required": [
    "dict_annotation",
    "func_name"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "title": "type[BaseModel]"
}
```

#### Payload Shape
```json
{
  "request": {
    "func_name": {
      "type": "string"
    },
    "dict_annotation": {
      "type": "object",
      "title": "Any"
    }
  },
  "response": {
    "type": "object",
    "title": "type[BaseModel]"
  }
}
```

#### Syscalls
- Filesystem: ['data.copy']
- Network: []
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "_create_dict_model",
    "arguments": {
      "func_name": "<func_name_str>",
      "dict_annotation": {}
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **_convert_to_content**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\src\mcp\server\fastmcp\utilities\func_metadata.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "result": {
      "type": "object",
      "title": "Any"
    }
  },
  "required": [
    "result"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "title": "Sequence[ContentBlock]"
}
```

#### Payload Shape
```json
{
  "request": {
    "result": {
      "type": "object",
      "title": "Any"
    }
  },
  "response": {
    "type": "object",
    "title": "Sequence[ContentBlock]"
  }
}
```

#### Syscalls
- Filesystem: ['data.copy']
- Network: []
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "_convert_to_content",
    "arguments": {
      "result": {}
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **get_logger**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\src\mcp\server\fastmcp\utilities\logging.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "name": {
      "type": "string"
    }
  },
  "required": [
    "name"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "title": "logging.Logger"
}
```

#### Payload Shape
```json
{
  "request": {
    "name": {
      "type": "string"
    }
  },
  "response": {
    "type": "object",
    "title": "logging.Logger"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "get_logger",
    "arguments": {
      "name": "<name_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **configure_logging**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\src\mcp\server\fastmcp\utilities\logging.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "level": {
      "type": "string",
      "enum": [
        "DEBUG",
        "INFO",
        "WARNING",
        "ERROR",
        "CRITICAL"
      ]
    }
  }
}
```

#### Output Schema
```json
{
  "type": "object",
  "title": "None"
}
```

#### Payload Shape
```json
{
  "request": {
    "level": {
      "type": "string",
      "enum": [
        "DEBUG",
        "INFO",
        "WARNING",
        "ERROR",
        "CRITICAL"
      ]
    }
  },
  "response": {
    "type": "object",
    "title": "None"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "configure_logging",
    "arguments": {
      "level": "<level_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **create_call_wrapper**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\src\mcp\server\lowlevel\func_inspection.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "func": {
      "type": "object",
      "title": "Callable[..., R]"
    },
    "request_type": {
      "type": "object",
      "title": "type[T]"
    }
  },
  "required": [
    "func",
    "request_type"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "title": "Callable[[T], R]"
}
```

#### Payload Shape
```json
{
  "request": {
    "func": {
      "type": "object",
      "title": "Callable[..., R]"
    },
    "request_type": {
      "type": "object",
      "title": "type[T]"
    }
  },
  "response": {
    "type": "object",
    "title": "Callable[[T], R]"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "create_call_wrapper",
    "arguments": {
      "func": {},
      "request_type": {}
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **resource_url_from_server_url**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\src\mcp\shared\auth_utils.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "url": {
      "type": "object",
      "title": "str | HttpUrl | AnyUrl"
    }
  },
  "required": [
    "url"
  ]
}
```

#### Output Schema
```json
{
  "type": "string"
}
```

#### Payload Shape
```json
{
  "request": {
    "url": {
      "type": "object",
      "title": "str | HttpUrl | AnyUrl"
    }
  },
  "response": {
    "type": "string"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "resource_url_from_server_url",
    "arguments": {
      "url": {}
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **check_resource_allowed**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\src\mcp\shared\auth_utils.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "requested_resource": {
      "type": "string"
    },
    "configured_resource": {
      "type": "string"
    }
  },
  "required": [
    "configured_resource",
    "requested_resource"
  ]
}
```

#### Output Schema
```json
{
  "type": "boolean"
}
```

#### Payload Shape
```json
{
  "request": {
    "requested_resource": {
      "type": "string"
    },
    "configured_resource": {
      "type": "string"
    }
  },
  "response": {
    "type": "boolean"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "check_resource_allowed",
    "arguments": {
      "requested_resource": "<requested_resource_str>",
      "configured_resource": "<configured_resource_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **calculate_token_expiry**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\src\mcp\shared\auth_utils.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "expires_in": {
      "type": "object",
      "title": "int | str | None"
    }
  },
  "required": [
    "expires_in"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "title": "float | None"
}
```

#### Payload Shape
```json
{
  "request": {
    "expires_in": {
      "type": "object",
      "title": "int | str | None"
    }
  },
  "response": {
    "type": "object",
    "title": "float | None"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "calculate_token_expiry",
    "arguments": {
      "expires_in": {}
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **get_display_name**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\src\mcp\shared\metadata_utils.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "obj": {
      "oneOf": [
        {
          "type": "object",
          "properties": {
            "description": {
              "type": "object",
              "title": "str | None"
            },
            "inputSchema": {
              "type": "object",
              "additionalProperties": {
                "type": "string",
                "guessed": true
              }
            },
            "outputSchema": {
              "type": "object",
              "additionalProperties": {
                "type": "string",
                "guessed": true
              }
            },
            "icons": {
              "type": "array",
              "items": {
                "type": "object",
                "title": "Icon"
              }
            },
            "annotations": {
              "type": "object",
              "title": "ToolAnnotations | None"
            },
            "meta": {
              "type": "object",
              "additionalProperties": {
                "type": "string",
                "guessed": true
              }
            }
          },
          "required": [
            "inputSchema"
          ]
        },
        {
          "type": "object",
          "properties": {
            "uri": {
              "type": "object",
              "title": "Annotated[AnyUrl, UrlConstraints(host_required=False)]"
            },
            "description": {
              "type": "object",
              "title": "str | None"
            },
            "mimeType": {
              "type": "object",
              "title": "str | None"
            },
            "size": {
              "type": "object",
              "title": "int | None"
            },
            "icons": {
              "type": "array",
              "items": {
                "type": "object",
                "title": "Icon"
              }
            },
            "annotations": {
              "type": "object",
              "title": "Annotations | None"
            },
            "meta": {
              "type": "object",
              "additionalProperties": {
                "type": "string",
                "guessed": true
              }
            }
          },
          "required": [
            "uri"
          ]
        },
        {
          "type": "object",
          "properties": {
            "description": {
              "type": "object",
              "title": "str | None"
            },
            "arguments": {
              "type": "array",
              "items": {
                "type": "object",
                "title": "PromptArgument"
              }
            },
            "icons": {
              "type": "array",
              "items": {
                "type": "object",
                "title": "Icon"
              }
            },
            "meta": {
              "type": "object",
              "additionalProperties": {
                "type": "string",
                "guessed": true
              }
            }
          }
        },
        {
          "type": "object",
          "properties": {
            "uriTemplate": {
              "type": "string"
            },
            "description": {
              "type": "object",
              "title": "str | None"
            },
            "mimeType": {
              "type": "object",
              "title": "str | None"
            },
            "icons": {
              "type": "array",
              "items": {
                "type": "object",
                "title": "Icon"
              }
            },
            "annotations": {
              "type": "object",
              "title": "Annotations | None"
            },
            "meta": {
              "type": "object",
              "additionalProperties": {
                "type": "string",
                "guessed": true
              }
            }
          },
          "required": [
            "uriTemplate"
          ]
        },
        {
          "type": "object",
          "properties": {
            "version": {
              "type": "string"
            },
            "websiteUrl": {
              "type": "object",
              "title": "str | None"
            },
            "icons": {
              "type": "array",
              "items": {
                "type": "object",
                "title": "Icon"
              }
            }
          },
          "required": [
            "version"
          ]
        }
      ]
    }
  },
  "required": [
    "obj"
  ]
}
```

#### Output Schema
```json
{
  "type": "string"
}
```

#### Payload Shape
```json
{
  "request": {
    "obj": {
      "oneOf": [
        {
          "type": "object",
          "properties": {
            "description": {
              "type": "object",
              "title": "str | None"
            },
            "inputSchema": {
              "type": "object",
              "additionalProperties": {
                "type": "string",
                "guessed": true
              }
            },
            "outputSchema": {
              "type": "object",
              "additionalProperties": {
                "type": "string",
                "guessed": true
              }
            },
            "icons": {
              "type": "array",
              "items": {
                "type": "object",
                "title": "Icon"
              }
            },
            "annotations": {
              "type": "object",
              "title": "ToolAnnotations | None"
            },
            "meta": {
              "type": "object",
              "additionalProperties": {
                "type": "string",
                "guessed": true
              }
            }
          },
          "required": [
            "inputSchema"
          ]
        },
        {
          "type": "object",
          "properties": {
            "uri": {
              "type": "object",
              "title": "Annotated[AnyUrl, UrlConstraints(host_required=False)]"
            },
            "description": {
              "type": "object",
              "title": "str | None"
            },
            "mimeType": {
              "type": "object",
              "title": "str | None"
            },
            "size": {
              "type": "object",
              "title": "int | None"
            },
            "icons": {
              "type": "array",
              "items": {
                "type": "object",
                "title": "Icon"
              }
            },
            "annotations": {
              "type": "object",
              "title": "Annotations | None"
            },
            "meta": {
              "type": "object",
              "additionalProperties": {
                "type": "string",
                "guessed": true
              }
            }
          },
          "required": [
            "uri"
          ]
        },
        {
          "type": "object",
          "properties": {
            "description": {
              "type": "object",
              "title": "str | None"
            },
            "arguments": {
              "type": "array",
              "items": {
                "type": "object",
                "title": "PromptArgument"
              }
            },
            "icons": {
              "type": "array",
              "items": {
                "type": "object",
                "title": "Icon"
              }
            },
            "meta": {
              "type": "object",
              "additionalProperties": {
                "type": "string",
                "guessed": true
              }
            }
          }
        },
        {
          "type": "object",
          "properties": {
            "uriTemplate": {
              "type": "string"
            },
            "description": {
              "type": "object",
              "title": "str | None"
            },
            "mimeType": {
              "type": "object",
              "title": "str | None"
            },
            "icons": {
              "type": "array",
              "items": {
                "type": "object",
                "title": "Icon"
              }
            },
            "annotations": {
              "type": "object",
              "title": "Annotations | None"
            },
            "meta": {
              "type": "object",
              "additionalProperties": {
                "type": "string",
                "guessed": true
              }
            }
          },
          "required": [
            "uriTemplate"
          ]
        },
        {
          "type": "object",
          "properties": {
            "version": {
              "type": "string"
            },
            "websiteUrl": {
              "type": "object",
              "title": "str | None"
            },
            "icons": {
              "type": "array",
              "items": {
                "type": "object",
                "title": "Icon"
              }
            }
          },
          "required": [
            "version"
          ]
        }
      ]
    }
  },
  "response": {
    "type": "string"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "get_display_name",
    "arguments": {
      "obj": "<obj_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **progress**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\src\mcp\shared\progress.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "ctx": {
      "type": "object",
      "title": "RequestContext[BaseSession[SendRequestT, SendNotificationT, SendResultT, ReceiveRequestT, ReceiveNotificationT], LifespanContextT]"
    },
    "total": {
      "type": "object",
      "title": "float | None"
    }
  },
  "required": [
    "ctx"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "title": "Generator[ProgressContext[SendRequestT, SendNotificationT, SendResultT, ReceiveRequestT, ReceiveNotificationT], None]"
}
```

#### Payload Shape
```json
{
  "request": {
    "ctx": {
      "type": "object",
      "title": "RequestContext[BaseSession[SendRequestT, SendNotificationT, SendResultT, ReceiveRequestT, ReceiveNotificationT], LifespanContextT]"
    },
    "total": {
      "type": "object",
      "title": "float | None"
    }
  },
  "response": {
    "type": "object",
    "title": "Generator[ProgressContext[SendRequestT, SendNotificationT, SendResultT, ReceiveRequestT, ReceiveNotificationT], None]"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "progress",
    "arguments": {
      "ctx": {},
      "total": {}
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **create_mcp_http_client**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\src\mcp\shared\_httpx_utils.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "headers": {
      "type": "object",
      "additionalProperties": {
        "type": "string",
        "guessed": true
      }
    },
    "timeout": {
      "type": "object",
      "title": "httpx.Timeout | None"
    },
    "auth": {
      "type": "object",
      "title": "httpx.Auth | None"
    }
  }
}
```

#### Output Schema
```json
{
  "type": "object",
  "title": "httpx.AsyncClient"
}
```

#### Payload Shape
```json
{
  "request": {
    "headers": {
      "type": "object",
      "additionalProperties": {
        "type": "string",
        "guessed": true
      }
    },
    "timeout": {
      "type": "object",
      "title": "httpx.Timeout | None"
    },
    "auth": {
      "type": "object",
      "title": "httpx.Auth | None"
    }
  },
  "response": {
    "type": "object",
    "title": "httpx.AsyncClient"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['httpx.Timeout', 'httpx.AsyncClient']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "create_mcp_http_client",
    "arguments": {
      "headers": {},
      "timeout": {},
      "auth": {}
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **anyio_backend**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\conftest.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "anyio_backend",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **test_docs_examples**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\test_examples.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "example": {
      "type": "object",
      "title": "CodeExample"
    },
    "eval_example": {
      "type": "object",
      "title": "EvalExample"
    }
  },
  "required": [
    "eval_example",
    "example"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {
    "example": {
      "type": "object",
      "title": "CodeExample"
    },
    "eval_example": {
      "type": "object",
      "title": "EvalExample"
    }
  },
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "test_docs_examples",
    "arguments": {
      "example": {},
      "eval_example": {}
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **wait_for_server**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\test_helpers.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "port": {
      "type": "integer"
    },
    "timeout": {
      "type": "number"
    }
  },
  "required": [
    "port"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "title": "None"
}
```

#### Payload Shape
```json
{
  "request": {
    "port": {
      "type": "integer"
    },
    "timeout": {
      "type": "number"
    }
  },
  "response": {
    "type": "object",
    "title": "None"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['socket.socket']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "wait_for_server",
    "arguments": {
      "port": 0,
      "timeout": 0
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **test_tool_preserves_json_schema_2020_12_fields**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\test_types.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "test_tool_preserves_json_schema_2020_12_fields",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **test_list_tools_result_preserves_json_schema_2020_12_fields**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\test_types.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "test_list_tools_result_preserves_json_schema_2020_12_fields",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **test_parse_file_path_accepts_valid_specs**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\cli\test_utils.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "tmp_path": {
      "type": "object",
      "title": "Path"
    },
    "spec": {
      "type": "string"
    },
    "expected_obj": {
      "type": "object",
      "title": "str | None"
    }
  },
  "required": [
    "expected_obj",
    "spec",
    "tmp_path"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {
    "tmp_path": {
      "type": "object",
      "title": "Path"
    },
    "spec": {
      "type": "string"
    },
    "expected_obj": {
      "type": "object",
      "title": "str | None"
    }
  },
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: ['file.write_text', 'dir_path.mkdir']
- Network: []
- Subprocess: ['subprocess.CompletedProcess', 'subprocess.CalledProcessError']
- Env: []
- Severity: **high**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "test_parse_file_path_accepts_valid_specs",
    "arguments": {
      "tmp_path": {},
      "spec": "<spec_str>",
      "expected_obj": {}
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **test_parse_file_path_missing**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\cli\test_utils.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "tmp_path": {
      "type": "object",
      "title": "Path"
    }
  },
  "required": [
    "tmp_path"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {
    "tmp_path": {
      "type": "object",
      "title": "Path"
    }
  },
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: ['file.write_text', 'dir_path.mkdir']
- Network: []
- Subprocess: ['subprocess.CompletedProcess', 'subprocess.CalledProcessError']
- Env: []
- Severity: **high**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "test_parse_file_path_missing",
    "arguments": {
      "tmp_path": {}
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **test_parse_file_exit_on_dir**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\cli\test_utils.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "tmp_path": {
      "type": "object",
      "title": "Path"
    }
  },
  "required": [
    "tmp_path"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {
    "tmp_path": {
      "type": "object",
      "title": "Path"
    }
  },
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: ['file.write_text', 'dir_path.mkdir']
- Network: []
- Subprocess: ['subprocess.CompletedProcess', 'subprocess.CalledProcessError']
- Env: []
- Severity: **high**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "test_parse_file_exit_on_dir",
    "arguments": {
      "tmp_path": {}
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **test_build_uv_command_minimal**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\cli\test_utils.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: ['file.write_text', 'dir_path.mkdir']
- Network: []
- Subprocess: ['subprocess.CompletedProcess', 'subprocess.CalledProcessError']
- Env: []
- Severity: **high**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "test_build_uv_command_minimal",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **test_build_uv_command_adds_editable_and_packages**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\cli\test_utils.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: ['file.write_text', 'dir_path.mkdir']
- Network: []
- Subprocess: ['subprocess.CompletedProcess', 'subprocess.CalledProcessError']
- Env: []
- Severity: **high**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "test_build_uv_command_adds_editable_and_packages",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **test_get_npx_unix_like**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\cli\test_utils.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "monkeypatch": {
      "type": "object",
      "title": "pytest.MonkeyPatch"
    }
  },
  "required": [
    "monkeypatch"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {
    "monkeypatch": {
      "type": "object",
      "title": "pytest.MonkeyPatch"
    }
  },
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: ['file.write_text', 'dir_path.mkdir']
- Network: []
- Subprocess: ['subprocess.CompletedProcess', 'subprocess.CalledProcessError']
- Env: []
- Severity: **high**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "test_get_npx_unix_like",
    "arguments": {
      "monkeypatch": {}
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **test_get_npx_windows**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\cli\test_utils.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "monkeypatch": {
      "type": "object",
      "title": "pytest.MonkeyPatch"
    }
  },
  "required": [
    "monkeypatch"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {
    "monkeypatch": {
      "type": "object",
      "title": "pytest.MonkeyPatch"
    }
  },
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: ['file.write_text', 'dir_path.mkdir']
- Network: []
- Subprocess: ['subprocess.CompletedProcess', 'subprocess.CalledProcessError']
- Env: []
- Severity: **high**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "test_get_npx_windows",
    "arguments": {
      "monkeypatch": {}
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **test_get_npx_returns_none_when_npx_missing**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\cli\test_utils.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "monkeypatch": {
      "type": "object",
      "title": "pytest.MonkeyPatch"
    }
  },
  "required": [
    "monkeypatch"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {
    "monkeypatch": {
      "type": "object",
      "title": "pytest.MonkeyPatch"
    }
  },
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: ['file.write_text', 'dir_path.mkdir']
- Network: []
- Subprocess: ['subprocess.CompletedProcess', 'subprocess.CalledProcessError']
- Env: []
- Severity: **high**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "test_get_npx_returns_none_when_npx_missing",
    "arguments": {
      "monkeypatch": {}
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **stream_spy**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\client\conftest.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "title": "Generator[Callable[[], StreamSpyCollection], None, None]"
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "title": "Generator[Callable[[], StreamSpyCollection], None, None]"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "stream_spy",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **mock_storage**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\client\test_auth.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['httpx.Response', 'httpx.Request']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "mock_storage",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **client_metadata**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\client\test_auth.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['httpx.Response', 'httpx.Request']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "client_metadata",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **valid_tokens**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\client\test_auth.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['httpx.Response', 'httpx.Request']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "valid_tokens",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **oauth_provider**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\client\test_auth.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "client_metadata": {
      "type": "object",
      "properties": {
        "redirect_uris": {
          "type": "array",
          "items": {
            "type": "object",
            "title": "AnyUrl"
          }
        },
        "token_endpoint_auth_method": {
          "type": "string",
          "enum": [
            "none",
            "client_secret_post",
            "client_secret_basic",
            "private_key_jwt"
          ]
        },
        "grant_types": {
          "type": "array",
          "items": {
            "type": "string",
            "enum": [
              "authorization_code",
              "refresh_token",
              "urn:ietf:params:oauth:grant-type:jwt-bearer"
            ]
          }
        },
        "response_types": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "scope": {
          "type": "object",
          "title": "str | None"
        },
        "client_name": {
          "type": "object",
          "title": "str | None"
        },
        "client_uri": {
          "type": "object",
          "title": "AnyHttpUrl | None"
        },
        "logo_uri": {
          "type": "object",
          "title": "AnyHttpUrl | None"
        },
        "contacts": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "tos_uri": {
          "type": "object",
          "title": "AnyHttpUrl | None"
        },
        "policy_uri": {
          "type": "object",
          "title": "AnyHttpUrl | None"
        },
        "jwks_uri": {
          "type": "object",
          "title": "AnyHttpUrl | None"
        },
        "jwks": {
          "type": "object",
          "title": "Any | None"
        },
        "software_id": {
          "type": "object",
          "title": "str | None"
        },
        "software_version": {
          "type": "object",
          "title": "str | None"
        }
      },
      "required": [
        "redirect_uris",
        "token_endpoint_auth_method",
        "grant_types",
        "response_types",
        "scope",
        "client_name",
        "client_uri",
        "logo_uri",
        "contacts",
        "tos_uri",
        "policy_uri",
        "jwks_uri",
        "jwks",
        "software_id",
        "software_version"
      ]
    },
    "mock_storage": {
      "type": "object",
      "properties": {}
    }
  },
  "required": [
    "client_metadata",
    "mock_storage"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {
    "client_metadata": {
      "type": "object",
      "properties": {
        "redirect_uris": {
          "type": "array",
          "items": {
            "type": "object",
            "title": "AnyUrl"
          }
        },
        "token_endpoint_auth_method": {
          "type": "string",
          "enum": [
            "none",
            "client_secret_post",
            "client_secret_basic",
            "private_key_jwt"
          ]
        },
        "grant_types": {
          "type": "array",
          "items": {
            "type": "string",
            "enum": [
              "authorization_code",
              "refresh_token",
              "urn:ietf:params:oauth:grant-type:jwt-bearer"
            ]
          }
        },
        "response_types": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "scope": {
          "type": "object",
          "title": "str | None"
        },
        "client_name": {
          "type": "object",
          "title": "str | None"
        },
        "client_uri": {
          "type": "object",
          "title": "AnyHttpUrl | None"
        },
        "logo_uri": {
          "type": "object",
          "title": "AnyHttpUrl | None"
        },
        "contacts": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "tos_uri": {
          "type": "object",
          "title": "AnyHttpUrl | None"
        },
        "policy_uri": {
          "type": "object",
          "title": "AnyHttpUrl | None"
        },
        "jwks_uri": {
          "type": "object",
          "title": "AnyHttpUrl | None"
        },
        "jwks": {
          "type": "object",
          "title": "Any | None"
        },
        "software_id": {
          "type": "object",
          "title": "str | None"
        },
        "software_version": {
          "type": "object",
          "title": "str | None"
        }
      },
      "required": [
        "redirect_uris",
        "token_endpoint_auth_method",
        "grant_types",
        "response_types",
        "scope",
        "client_name",
        "client_uri",
        "logo_uri",
        "contacts",
        "tos_uri",
        "policy_uri",
        "jwks_uri",
        "jwks",
        "software_id",
        "software_version"
      ]
    },
    "mock_storage": {
      "type": "object",
      "properties": {}
    }
  },
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['httpx.Response', 'httpx.Request']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "oauth_provider",
    "arguments": {
      "client_metadata": {},
      "mock_storage": {}
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **prm_metadata_response**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\client\test_auth.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['httpx.Response', 'httpx.Request']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "prm_metadata_response",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **prm_metadata_without_scopes_response**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\client\test_auth.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['httpx.Response', 'httpx.Request']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "prm_metadata_without_scopes_response",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **init_response_with_www_auth_scope**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\client\test_auth.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['httpx.Response', 'httpx.Request']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "init_response_with_www_auth_scope",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **init_response_without_www_auth_scope**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\client\test_auth.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['httpx.Response', 'httpx.Request']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "init_response_without_www_auth_scope",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **test_build_metadata**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\client\test_auth.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "issuer_url": {
      "type": "string"
    },
    "service_documentation_url": {
      "type": "string"
    },
    "authorization_endpoint": {
      "type": "string"
    },
    "token_endpoint": {
      "type": "string"
    },
    "registration_endpoint": {
      "type": "string"
    },
    "revocation_endpoint": {
      "type": "string"
    }
  },
  "required": [
    "authorization_endpoint",
    "issuer_url",
    "registration_endpoint",
    "revocation_endpoint",
    "service_documentation_url",
    "token_endpoint"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {
    "issuer_url": {
      "type": "string"
    },
    "service_documentation_url": {
      "type": "string"
    },
    "authorization_endpoint": {
      "type": "string"
    },
    "token_endpoint": {
      "type": "string"
    },
    "registration_endpoint": {
      "type": "string"
    },
    "revocation_endpoint": {
      "type": "string"
    }
  },
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['httpx.Response', 'httpx.Request']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "test_build_metadata",
    "arguments": {
      "issuer_url": "<issuer_url_str>",
      "service_documentation_url": "<service_documentation_url_str>",
      "authorization_endpoint": "<authorization_endpoint_str>",
      "token_endpoint": "<token_endpoint_str>",
      "registration_endpoint": "<registration_endpoint_str>",
      "revocation_endpoint": "<revocation_endpoint_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **temp_config_dir**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\client\test_config.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "tmp_path": {
      "type": "object",
      "title": "Path"
    }
  },
  "required": [
    "tmp_path"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {
    "tmp_path": {
      "type": "object",
      "title": "Path"
    }
  },
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: ['config_dir.mkdir', 'config_file.read_text']
- Network: []
- Subprocess: ['subprocess.run']
- Env: []
- Severity: **high**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "temp_config_dir",
    "arguments": {
      "tmp_path": {}
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **mock_config_path**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\client\test_config.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "temp_config_dir": {
      "type": "object",
      "title": "Path"
    }
  },
  "required": [
    "temp_config_dir"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {
    "temp_config_dir": {
      "type": "object",
      "title": "Path"
    }
  },
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: ['config_dir.mkdir', 'config_file.read_text']
- Network: []
- Subprocess: ['subprocess.run']
- Env: []
- Severity: **high**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "mock_config_path",
    "arguments": {
      "temp_config_dir": {}
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **test_command_execution**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\client\test_config.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "mock_config_path": {
      "type": "object",
      "title": "Path"
    }
  },
  "required": [
    "mock_config_path"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {
    "mock_config_path": {
      "type": "object",
      "title": "Path"
    }
  },
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: ['config_dir.mkdir', 'config_file.read_text']
- Network: []
- Subprocess: ['subprocess.run']
- Env: []
- Severity: **high**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "test_command_execution",
    "arguments": {
      "mock_config_path": {}
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **test_absolute_uv_path**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\client\test_config.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "mock_config_path": {
      "type": "object",
      "title": "Path"
    }
  },
  "required": [
    "mock_config_path"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {
    "mock_config_path": {
      "type": "object",
      "title": "Path"
    }
  },
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: ['config_dir.mkdir', 'config_file.read_text']
- Network: []
- Subprocess: ['subprocess.run']
- Env: []
- Severity: **high**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "test_absolute_uv_path",
    "arguments": {
      "mock_config_path": {}
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **run_unicode_server**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\client\test_http_unicode.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "port": {
      "type": "integer"
    }
  },
  "required": [
    "port"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "title": "None"
}
```

#### Payload Shape
```json
{
  "request": {
    "port": {
      "type": "integer"
    }
  },
  "response": {
    "type": "object",
    "title": "None"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['socket.socket']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "run_unicode_server",
    "arguments": {
      "port": 0
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **unicode_server_port**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\client\test_http_unicode.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "integer"
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "integer"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['socket.socket']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "unicode_server_port",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **running_unicode_server**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\client\test_http_unicode.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "unicode_server_port": {
      "type": "integer"
    }
  },
  "required": [
    "unicode_server_port"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "title": "Generator[str, None, None]"
}
```

#### Payload Shape
```json
{
  "request": {
    "unicode_server_port": {
      "type": "integer"
    }
  },
  "response": {
    "type": "object",
    "title": "Generator[str, None, None]"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['socket.socket']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "running_unicode_server",
    "arguments": {
      "unicode_server_port": 0
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **create_non_sdk_server_app**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\client\test_notification_response.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "title": "Starlette"
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "title": "Starlette"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['socket.socket']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "create_non_sdk_server_app",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **run_non_sdk_server**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\client\test_notification_response.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "port": {
      "type": "integer"
    }
  },
  "required": [
    "port"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "title": "None"
}
```

#### Payload Shape
```json
{
  "request": {
    "port": {
      "type": "integer"
    }
  },
  "response": {
    "type": "object",
    "title": "None"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['socket.socket']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "run_non_sdk_server",
    "arguments": {
      "port": 0
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **non_sdk_server_port**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\client\test_notification_response.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "integer"
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "integer"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['socket.socket']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "non_sdk_server_port",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **non_sdk_server**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\client\test_notification_response.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "non_sdk_server_port": {
      "type": "integer"
    }
  },
  "required": [
    "non_sdk_server_port"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "title": "Generator[None, None, None]"
}
```

#### Payload Shape
```json
{
  "request": {
    "non_sdk_server_port": {
      "type": "integer"
    }
  },
  "response": {
    "type": "object",
    "title": "Generator[None, None, None]"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['socket.socket']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "non_sdk_server",
    "arguments": {
      "non_sdk_server_port": 0
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **bypass_server_output_validation**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\client\test_output_schema_validation.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "bypass_server_output_validation",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **mock_exit_stack**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\client\test_session_group.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "mock_exit_stack",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **mock_storage**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\client\auth\extensions\test_client_credentials.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['urllib.parse.unquote_plus']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "mock_storage",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **client_metadata**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\client\auth\extensions\test_client_credentials.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['urllib.parse.unquote_plus']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "client_metadata",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **rfc7523_oauth_provider**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\client\auth\extensions\test_client_credentials.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "client_metadata": {
      "type": "object",
      "properties": {
        "redirect_uris": {
          "type": "array",
          "items": {
            "type": "object",
            "title": "AnyUrl"
          }
        },
        "token_endpoint_auth_method": {
          "type": "string",
          "enum": [
            "none",
            "client_secret_post",
            "client_secret_basic",
            "private_key_jwt"
          ]
        },
        "grant_types": {
          "type": "array",
          "items": {
            "type": "string",
            "enum": [
              "authorization_code",
              "refresh_token",
              "urn:ietf:params:oauth:grant-type:jwt-bearer"
            ]
          }
        },
        "response_types": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "scope": {
          "type": "object",
          "title": "str | None"
        },
        "client_name": {
          "type": "object",
          "title": "str | None"
        },
        "client_uri": {
          "type": "object",
          "title": "AnyHttpUrl | None"
        },
        "logo_uri": {
          "type": "object",
          "title": "AnyHttpUrl | None"
        },
        "contacts": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "tos_uri": {
          "type": "object",
          "title": "AnyHttpUrl | None"
        },
        "policy_uri": {
          "type": "object",
          "title": "AnyHttpUrl | None"
        },
        "jwks_uri": {
          "type": "object",
          "title": "AnyHttpUrl | None"
        },
        "jwks": {
          "type": "object",
          "title": "Any | None"
        },
        "software_id": {
          "type": "object",
          "title": "str | None"
        },
        "software_version": {
          "type": "object",
          "title": "str | None"
        }
      },
      "required": [
        "redirect_uris",
        "token_endpoint_auth_method",
        "grant_types",
        "response_types",
        "scope",
        "client_name",
        "client_uri",
        "logo_uri",
        "contacts",
        "tos_uri",
        "policy_uri",
        "jwks_uri",
        "jwks",
        "software_id",
        "software_version"
      ]
    },
    "mock_storage": {
      "type": "object",
      "properties": {}
    }
  },
  "required": [
    "client_metadata",
    "mock_storage"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {
    "client_metadata": {
      "type": "object",
      "properties": {
        "redirect_uris": {
          "type": "array",
          "items": {
            "type": "object",
            "title": "AnyUrl"
          }
        },
        "token_endpoint_auth_method": {
          "type": "string",
          "enum": [
            "none",
            "client_secret_post",
            "client_secret_basic",
            "private_key_jwt"
          ]
        },
        "grant_types": {
          "type": "array",
          "items": {
            "type": "string",
            "enum": [
              "authorization_code",
              "refresh_token",
              "urn:ietf:params:oauth:grant-type:jwt-bearer"
            ]
          }
        },
        "response_types": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "scope": {
          "type": "object",
          "title": "str | None"
        },
        "client_name": {
          "type": "object",
          "title": "str | None"
        },
        "client_uri": {
          "type": "object",
          "title": "AnyHttpUrl | None"
        },
        "logo_uri": {
          "type": "object",
          "title": "AnyHttpUrl | None"
        },
        "contacts": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "tos_uri": {
          "type": "object",
          "title": "AnyHttpUrl | None"
        },
        "policy_uri": {
          "type": "object",
          "title": "AnyHttpUrl | None"
        },
        "jwks_uri": {
          "type": "object",
          "title": "AnyHttpUrl | None"
        },
        "jwks": {
          "type": "object",
          "title": "Any | None"
        },
        "software_id": {
          "type": "object",
          "title": "str | None"
        },
        "software_version": {
          "type": "object",
          "title": "str | None"
        }
      },
      "required": [
        "redirect_uris",
        "token_endpoint_auth_method",
        "grant_types",
        "response_types",
        "scope",
        "client_name",
        "client_uri",
        "logo_uri",
        "contacts",
        "tos_uri",
        "policy_uri",
        "jwks_uri",
        "jwks",
        "software_id",
        "software_version"
      ]
    },
    "mock_storage": {
      "type": "object",
      "properties": {}
    }
  },
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['urllib.parse.unquote_plus']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "rfc7523_oauth_provider",
    "arguments": {
      "client_metadata": {},
      "mock_storage": {}
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **query_db**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\issues\test_355_type_error.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "ctx": {
      "type": "object",
      "title": "Context[ServerSession, AppContext]"
    }
  },
  "required": [
    "ctx"
  ]
}
```

#### Output Schema
```json
{
  "type": "string"
}
```

#### Payload Shape
```json
{
  "request": {
    "ctx": {
      "type": "object",
      "title": "Context[ServerSession, AppContext]"
    }
  },
  "response": {
    "type": "string"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "query_db",
    "arguments": {
      "ctx": {}
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **create_add_tool**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\server\test_lowlevel_input_validation.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "properties": {}
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "create_add_tool",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **temp_file**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\server\test_read_resource.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: ['path.unlink']
- Network: []
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "temp_file",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **server_port**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\server\test_sse_security.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "integer"
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "integer"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['socket.socket', 'httpx.AsyncClient', 'client.get', 'client.post']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "server_port",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **server_url**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\server\test_sse_security.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "server_port": {
      "type": "integer"
    }
  },
  "required": [
    "server_port"
  ]
}
```

#### Output Schema
```json
{
  "type": "string"
}
```

#### Payload Shape
```json
{
  "request": {
    "server_port": {
      "type": "integer"
    }
  },
  "response": {
    "type": "string"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['socket.socket', 'httpx.AsyncClient', 'client.get', 'client.post']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "server_url",
    "arguments": {
      "server_port": 0
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **run_server_with_settings**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\server\test_sse_security.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "port": {
      "type": "integer"
    },
    "security_settings": {
      "oneOf": [
        {
          "type": "object",
          "properties": {
            "enable_dns_rebinding_protection": {
              "type": "boolean"
            },
            "allowed_hosts": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "allowed_origins": {
              "type": "array",
              "items": {
                "type": "string"
              }
            }
          }
        }
      ]
    }
  },
  "required": [
    "port"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {
    "port": {
      "type": "integer"
    },
    "security_settings": {
      "oneOf": [
        {
          "type": "object",
          "properties": {
            "enable_dns_rebinding_protection": {
              "type": "boolean"
            },
            "allowed_hosts": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "allowed_origins": {
              "type": "array",
              "items": {
                "type": "string"
              }
            }
          }
        }
      ]
    }
  },
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['socket.socket', 'httpx.AsyncClient', 'client.get', 'client.post']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "run_server_with_settings",
    "arguments": {
      "port": 0,
      "security_settings": "<security_settings_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **start_server_process**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\server\test_sse_security.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "port": {
      "type": "integer"
    },
    "security_settings": {
      "oneOf": [
        {
          "type": "object",
          "properties": {
            "enable_dns_rebinding_protection": {
              "type": "boolean"
            },
            "allowed_hosts": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "allowed_origins": {
              "type": "array",
              "items": {
                "type": "string"
              }
            }
          }
        }
      ]
    }
  },
  "required": [
    "port"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {
    "port": {
      "type": "integer"
    },
    "security_settings": {
      "oneOf": [
        {
          "type": "object",
          "properties": {
            "enable_dns_rebinding_protection": {
              "type": "boolean"
            },
            "allowed_hosts": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "allowed_origins": {
              "type": "array",
              "items": {
                "type": "string"
              }
            }
          }
        }
      ]
    }
  },
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['socket.socket', 'httpx.AsyncClient', 'client.get', 'client.post']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "start_server_process",
    "arguments": {
      "port": 0,
      "security_settings": "<security_settings_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **server_port**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\server\test_streamable_http_security.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "integer"
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "integer"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['socket.socket', 'httpx.AsyncClient', 'client.post', 'client.get']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "server_port",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **server_url**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\server\test_streamable_http_security.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "server_port": {
      "type": "integer"
    }
  },
  "required": [
    "server_port"
  ]
}
```

#### Output Schema
```json
{
  "type": "string"
}
```

#### Payload Shape
```json
{
  "request": {
    "server_port": {
      "type": "integer"
    }
  },
  "response": {
    "type": "string"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['socket.socket', 'httpx.AsyncClient', 'client.post', 'client.get']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "server_url",
    "arguments": {
      "server_port": 0
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **run_server_with_settings**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\server\test_streamable_http_security.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "port": {
      "type": "integer"
    },
    "security_settings": {
      "oneOf": [
        {
          "type": "object",
          "properties": {
            "enable_dns_rebinding_protection": {
              "type": "boolean"
            },
            "allowed_hosts": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "allowed_origins": {
              "type": "array",
              "items": {
                "type": "string"
              }
            }
          }
        }
      ]
    }
  },
  "required": [
    "port"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {
    "port": {
      "type": "integer"
    },
    "security_settings": {
      "oneOf": [
        {
          "type": "object",
          "properties": {
            "enable_dns_rebinding_protection": {
              "type": "boolean"
            },
            "allowed_hosts": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "allowed_origins": {
              "type": "array",
              "items": {
                "type": "string"
              }
            }
          }
        }
      ]
    }
  },
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['socket.socket', 'httpx.AsyncClient', 'client.post', 'client.get']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "run_server_with_settings",
    "arguments": {
      "port": 0,
      "security_settings": "<security_settings_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **start_server_process**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\server\test_streamable_http_security.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "port": {
      "type": "integer"
    },
    "security_settings": {
      "oneOf": [
        {
          "type": "object",
          "properties": {
            "enable_dns_rebinding_protection": {
              "type": "boolean"
            },
            "allowed_hosts": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "allowed_origins": {
              "type": "array",
              "items": {
                "type": "string"
              }
            }
          }
        }
      ]
    }
  },
  "required": [
    "port"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {
    "port": {
      "type": "integer"
    },
    "security_settings": {
      "oneOf": [
        {
          "type": "object",
          "properties": {
            "enable_dns_rebinding_protection": {
              "type": "boolean"
            },
            "allowed_hosts": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "allowed_origins": {
              "type": "array",
              "items": {
                "type": "string"
              }
            }
          }
        }
      ]
    }
  },
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['socket.socket', 'httpx.AsyncClient', 'client.post', 'client.get']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "start_server_process",
    "arguments": {
      "port": 0,
      "security_settings": "<security_settings_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **oauth_provider**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\server\auth\test_error_handling.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['httpx.AsyncClient', 'client.post', 'client.get']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "oauth_provider",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **app**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\server\auth\test_error_handling.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "oauth_provider": {
      "type": "object",
      "properties": {}
    }
  },
  "required": [
    "oauth_provider"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {
    "oauth_provider": {
      "type": "object",
      "properties": {}
    }
  },
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['httpx.AsyncClient', 'client.post', 'client.get']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "app",
    "arguments": {
      "oauth_provider": {}
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **client**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\server\auth\test_error_handling.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "app": {
      "type": "object",
      "title": "Starlette"
    }
  },
  "required": [
    "app"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {
    "app": {
      "type": "object",
      "title": "Starlette"
    }
  },
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['httpx.AsyncClient', 'client.post', 'client.get']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "client",
    "arguments": {
      "app": {}
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **pkce_challenge**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\server\auth\test_error_handling.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['httpx.AsyncClient', 'client.post', 'client.get']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "pkce_challenge",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **test_app**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\server\auth\test_protected_resource.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['httpx.AsyncClient', 'httpx.ASGITransport']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "test_app",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **root_resource_app**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\server\auth\test_protected_resource.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['httpx.AsyncClient', 'httpx.ASGITransport']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "root_resource_app",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **valid_access_token**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\server\auth\middleware\test_auth_context.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "properties": {
    "token": {
      "type": "string"
    },
    "client_id": {
      "type": "string"
    },
    "scopes": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "expires_at": {
      "type": "object",
      "title": "int | None"
    },
    "resource": {
      "type": "object",
      "title": "str | None"
    }
  },
  "required": [
    "token",
    "client_id",
    "scopes",
    "expires_at",
    "resource"
  ]
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "properties": {
      "token": {
        "type": "string"
      },
      "client_id": {
        "type": "string"
      },
      "scopes": {
        "type": "array",
        "items": {
          "type": "string"
        }
      },
      "expires_at": {
        "type": "object",
        "title": "int | None"
      },
      "resource": {
        "type": "object",
        "title": "str | None"
      }
    },
    "required": [
      "token",
      "client_id",
      "scopes",
      "expires_at",
      "resource"
    ]
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "valid_access_token",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **add_token_to_provider**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\server\auth\middleware\test_bearer_auth.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "provider": {
      "type": "object",
      "title": "OAuthAuthorizationServerProvider[Any, Any, Any]"
    },
    "token": {
      "type": "string"
    },
    "access_token": {
      "type": "object",
      "properties": {
        "token": {
          "type": "string"
        },
        "client_id": {
          "type": "string"
        },
        "scopes": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "expires_at": {
          "type": "object",
          "title": "int | None"
        },
        "resource": {
          "type": "object",
          "title": "str | None"
        }
      },
      "required": [
        "token",
        "client_id",
        "scopes",
        "expires_at",
        "resource"
      ]
    }
  },
  "required": [
    "access_token",
    "provider",
    "token"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "title": "None"
}
```

#### Payload Shape
```json
{
  "request": {
    "provider": {
      "type": "object",
      "title": "OAuthAuthorizationServerProvider[Any, Any, Any]"
    },
    "token": {
      "type": "string"
    },
    "access_token": {
      "type": "object",
      "properties": {
        "token": {
          "type": "string"
        },
        "client_id": {
          "type": "string"
        },
        "scopes": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "expires_at": {
          "type": "object",
          "title": "int | None"
        },
        "resource": {
          "type": "object",
          "title": "str | None"
        }
      },
      "required": [
        "token",
        "client_id",
        "scopes",
        "expires_at",
        "resource"
      ]
    }
  },
  "response": {
    "type": "object",
    "title": "None"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "add_token_to_provider",
    "arguments": {
      "provider": {},
      "token": "<token_str>",
      "access_token": {}
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **mock_oauth_provider**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\server\auth\middleware\test_bearer_auth.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "title": "OAuthAuthorizationServerProvider[Any, Any, Any]"
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "title": "OAuthAuthorizationServerProvider[Any, Any, Any]"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "mock_oauth_provider",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **valid_access_token**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\server\auth\middleware\test_bearer_auth.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "properties": {
    "token": {
      "type": "string"
    },
    "client_id": {
      "type": "string"
    },
    "scopes": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "expires_at": {
      "type": "object",
      "title": "int | None"
    },
    "resource": {
      "type": "object",
      "title": "str | None"
    }
  },
  "required": [
    "token",
    "client_id",
    "scopes",
    "expires_at",
    "resource"
  ]
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "properties": {
      "token": {
        "type": "string"
      },
      "client_id": {
        "type": "string"
      },
      "scopes": {
        "type": "array",
        "items": {
          "type": "string"
        }
      },
      "expires_at": {
        "type": "object",
        "title": "int | None"
      },
      "resource": {
        "type": "object",
        "title": "str | None"
      }
    },
    "required": [
      "token",
      "client_id",
      "scopes",
      "expires_at",
      "resource"
    ]
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "valid_access_token",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **expired_access_token**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\server\auth\middleware\test_bearer_auth.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "properties": {
    "token": {
      "type": "string"
    },
    "client_id": {
      "type": "string"
    },
    "scopes": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "expires_at": {
      "type": "object",
      "title": "int | None"
    },
    "resource": {
      "type": "object",
      "title": "str | None"
    }
  },
  "required": [
    "token",
    "client_id",
    "scopes",
    "expires_at",
    "resource"
  ]
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "properties": {
      "token": {
        "type": "string"
      },
      "client_id": {
        "type": "string"
      },
      "scopes": {
        "type": "array",
        "items": {
          "type": "string"
        }
      },
      "expires_at": {
        "type": "object",
        "title": "int | None"
      },
      "resource": {
        "type": "object",
        "title": "str | None"
      }
    },
    "required": [
      "token",
      "client_id",
      "scopes",
      "expires_at",
      "resource"
    ]
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "expired_access_token",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **no_expiry_access_token**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\server\auth\middleware\test_bearer_auth.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "properties": {
    "token": {
      "type": "string"
    },
    "client_id": {
      "type": "string"
    },
    "scopes": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "expires_at": {
      "type": "object",
      "title": "int | None"
    },
    "resource": {
      "type": "object",
      "title": "str | None"
    }
  },
  "required": [
    "token",
    "client_id",
    "scopes",
    "expires_at",
    "resource"
  ]
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "properties": {
      "token": {
        "type": "string"
      },
      "client_id": {
        "type": "string"
      },
      "scopes": {
        "type": "array",
        "items": {
          "type": "string"
        }
      },
      "expires_at": {
        "type": "object",
        "title": "int | None"
      },
      "resource": {
        "type": "object",
        "title": "str | None"
      }
    },
    "required": [
      "token",
      "client_id",
      "scopes",
      "expires_at",
      "resource"
    ]
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "no_expiry_access_token",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **create_ask_user_tool**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\server\fastmcp\test_elicitation.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "mcp": {
      "type": "object",
      "properties": {}
    }
  },
  "required": [
    "mcp"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {
    "mcp": {
      "type": "object",
      "properties": {}
    }
  },
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "create_ask_user_tool",
    "arguments": {
      "mcp": {}
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **complex_arguments_fn**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\server\fastmcp\test_func_metadata.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "an_int": {
      "type": "integer"
    },
    "must_be_none": {
      "type": "object",
      "title": "None"
    },
    "must_be_none_dumb_annotation": {
      "type": "object",
      "title": "Annotated[None, 'blah']"
    },
    "list_of_ints": {
      "type": "array",
      "items": {
        "type": "integer"
      }
    },
    "list_str_or_str": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "an_int_annotated_with_field": {
      "type": "integer"
    },
    "an_int_annotated_with_field_and_others": {
      "type": "object",
      "title": "int, str"
    },
    "an_int_annotated_with_junk": {
      "type": "object",
      "title": "Annotated[int, '123', 456]"
    },
    "field_with_default_via_field_annotation_before_nondefault_arg": {
      "type": "integer"
    },
    "unannotated": {
      "type": "string",
      "guessed": true
    },
    "my_model_a": {
      "type": "object",
      "properties": {}
    },
    "my_model_a_forward_ref": {
      "type": "object",
      "title": "'SomeInputModelA'"
    },
    "my_model_b": {
      "type": "object",
      "properties": {
        "how_many_shrimp": {
          "type": "object",
          "title": "Annotated[int, Field(description='How many shrimp in the tank???')]"
        },
        "ok": {
          "type": "object",
          "title": "InnerModel"
        },
        "y": {
          "type": "object",
          "title": "None"
        }
      },
      "required": [
        "how_many_shrimp",
        "ok",
        "y"
      ]
    },
    "an_int_annotated_with_field_default": {
      "type": "integer"
    },
    "unannotated_with_default": {
      "type": "string",
      "guessed": true
    },
    "my_model_a_with_default": {
      "type": "object",
      "properties": {}
    },
    "an_int_with_default": {
      "type": "integer"
    },
    "must_be_none_with_default": {
      "type": "object",
      "title": "None"
    },
    "an_int_with_equals_field": {
      "type": "integer"
    },
    "int_annotated_with_default": {
      "type": "integer"
    }
  },
  "required": [
    "an_int",
    "an_int_annotated_with_field",
    "an_int_annotated_with_field_and_others",
    "an_int_annotated_with_field_default",
    "an_int_annotated_with_junk",
    "field_with_default_via_field_annotation_before_nondefault_arg",
    "list_of_ints",
    "list_str_or_str",
    "must_be_none",
    "must_be_none_dumb_annotation",
    "my_model_a",
    "my_model_a_forward_ref",
    "my_model_b",
    "unannotated"
  ]
}
```

#### Output Schema
```json
{
  "type": "string"
}
```

#### Payload Shape
```json
{
  "request": {
    "an_int": {
      "type": "integer"
    },
    "must_be_none": {
      "type": "object",
      "title": "None"
    },
    "must_be_none_dumb_annotation": {
      "type": "object",
      "title": "Annotated[None, 'blah']"
    },
    "list_of_ints": {
      "type": "array",
      "items": {
        "type": "integer"
      }
    },
    "list_str_or_str": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "an_int_annotated_with_field": {
      "type": "integer"
    },
    "an_int_annotated_with_field_and_others": {
      "type": "object",
      "title": "int, str"
    },
    "an_int_annotated_with_junk": {
      "type": "object",
      "title": "Annotated[int, '123', 456]"
    },
    "field_with_default_via_field_annotation_before_nondefault_arg": {
      "type": "integer"
    },
    "unannotated": {
      "type": "string",
      "guessed": true
    },
    "my_model_a": {
      "type": "object",
      "properties": {}
    },
    "my_model_a_forward_ref": {
      "type": "object",
      "title": "'SomeInputModelA'"
    },
    "my_model_b": {
      "type": "object",
      "properties": {
        "how_many_shrimp": {
          "type": "object",
          "title": "Annotated[int, Field(description='How many shrimp in the tank???')]"
        },
        "ok": {
          "type": "object",
          "title": "InnerModel"
        },
        "y": {
          "type": "object",
          "title": "None"
        }
      },
      "required": [
        "how_many_shrimp",
        "ok",
        "y"
      ]
    },
    "an_int_annotated_with_field_default": {
      "type": "integer"
    },
    "unannotated_with_default": {
      "type": "string",
      "guessed": true
    },
    "my_model_a_with_default": {
      "type": "object",
      "properties": {}
    },
    "an_int_with_default": {
      "type": "integer"
    },
    "must_be_none_with_default": {
      "type": "object",
      "title": "None"
    },
    "an_int_with_equals_field": {
      "type": "integer"
    },
    "int_annotated_with_default": {
      "type": "integer"
    }
  },
  "response": {
    "type": "string"
  }
}
```

#### Syscalls
- Filesystem: ['actual_schema.copy']
- Network: []
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "complex_arguments_fn",
    "arguments": {
      "an_int": 0,
      "must_be_none": {},
      "must_be_none_dumb_annotation": {},
      "list_of_ints": [],
      "list_str_or_str": [],
      "an_int_annotated_with_field": 0,
      "an_int_annotated_with_field_and_others": {},
      "an_int_annotated_with_junk": {},
      "field_with_default_via_field_annotation_before_nondefault_arg": 0,
      "unannotated": "<unannotated_str>",
      "my_model_a": {},
      "my_model_a_forward_ref": {},
      "my_model_b": {},
      "an_int_annotated_with_field_default": 0,
      "unannotated_with_default": "<unannotated_with_default_str>",
      "my_model_a_with_default": {},
      "an_int_with_default": 0,
      "must_be_none_with_default": {},
      "an_int_with_equals_field": 0,
      "int_annotated_with_default": 0
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **test_str_vs_list_str**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\server\fastmcp\test_func_metadata.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: ['actual_schema.copy']
- Network: []
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "test_str_vs_list_str",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **test_skip_names**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\server\fastmcp\test_func_metadata.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: ['actual_schema.copy']
- Network: []
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "test_skip_names",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **test_structured_output_dict_str_types**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\server\fastmcp\test_func_metadata.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: ['actual_schema.copy']
- Network: []
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "test_structured_output_dict_str_types",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **test_complex_function_json_schema**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\server\fastmcp\test_func_metadata.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: ['actual_schema.copy']
- Network: []
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "test_complex_function_json_schema",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **test_str_vs_int**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\server\fastmcp\test_func_metadata.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: ['actual_schema.copy']
- Network: []
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "test_str_vs_int",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **test_str_annotation_preserves_json_string**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\server\fastmcp\test_func_metadata.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: ['actual_schema.copy']
- Network: []
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "test_str_annotation_preserves_json_string",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **test_structured_output_requires_return_annotation**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\server\fastmcp\test_func_metadata.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: ['actual_schema.copy']
- Network: []
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "test_structured_output_requires_return_annotation",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **test_structured_output_basemodel**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\server\fastmcp\test_func_metadata.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: ['actual_schema.copy']
- Network: []
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "test_structured_output_basemodel",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **test_structured_output_primitives**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\server\fastmcp\test_func_metadata.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: ['actual_schema.copy']
- Network: []
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "test_structured_output_primitives",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **test_structured_output_generic_types**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\server\fastmcp\test_func_metadata.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: ['actual_schema.copy']
- Network: []
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "test_structured_output_generic_types",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **test_structured_output_dataclass**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\server\fastmcp\test_func_metadata.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: ['actual_schema.copy']
- Network: []
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "test_structured_output_dataclass",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **test_structured_output_typeddict**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\server\fastmcp\test_func_metadata.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: ['actual_schema.copy']
- Network: []
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "test_structured_output_typeddict",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **test_structured_output_ordinary_class**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\server\fastmcp\test_func_metadata.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: ['actual_schema.copy']
- Network: []
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "test_structured_output_ordinary_class",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **test_unstructured_output_unannotated_class**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\server\fastmcp\test_func_metadata.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: ['actual_schema.copy']
- Network: []
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "test_unstructured_output_unannotated_class",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **test_tool_call_result_is_unstructured_and_not_converted**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\server\fastmcp\test_func_metadata.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: ['actual_schema.copy']
- Network: []
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "test_tool_call_result_is_unstructured_and_not_converted",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **test_tool_call_result_annotated_is_structured_and_converted**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\server\fastmcp\test_func_metadata.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: ['actual_schema.copy']
- Network: []
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "test_tool_call_result_annotated_is_structured_and_converted",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **test_tool_call_result_annotated_is_structured_and_invalid**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\server\fastmcp\test_func_metadata.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: ['actual_schema.copy']
- Network: []
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "test_tool_call_result_annotated_is_structured_and_invalid",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **test_tool_call_result_in_optional_is_rejected**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\server\fastmcp\test_func_metadata.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: ['actual_schema.copy']
- Network: []
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "test_tool_call_result_in_optional_is_rejected",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **test_tool_call_result_in_union_is_rejected**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\server\fastmcp\test_func_metadata.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: ['actual_schema.copy']
- Network: []
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "test_tool_call_result_in_union_is_rejected",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **test_tool_call_result_in_pipe_union_is_rejected**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\server\fastmcp\test_func_metadata.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: ['actual_schema.copy']
- Network: []
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "test_tool_call_result_in_pipe_union_is_rejected",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **test_structured_output_with_field_descriptions**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\server\fastmcp\test_func_metadata.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: ['actual_schema.copy']
- Network: []
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "test_structured_output_with_field_descriptions",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **test_structured_output_nested_models**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\server\fastmcp\test_func_metadata.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: ['actual_schema.copy']
- Network: []
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "test_structured_output_nested_models",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **test_structured_output_unserializable_type_error**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\server\fastmcp\test_func_metadata.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: ['actual_schema.copy']
- Network: []
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "test_structured_output_unserializable_type_error",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **test_structured_output_aliases**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\server\fastmcp\test_func_metadata.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: ['actual_schema.copy']
- Network: []
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "test_structured_output_aliases",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **test_basemodel_reserved_names**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\server\fastmcp\test_func_metadata.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: ['actual_schema.copy']
- Network: []
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "test_basemodel_reserved_names",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **test_basemodel_reserved_names_with_json_preparsing**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\server\fastmcp\test_func_metadata.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: ['actual_schema.copy']
- Network: []
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "test_basemodel_reserved_names_with_json_preparsing",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **test_disallowed_type_qualifier**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\server\fastmcp\test_func_metadata.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: ['actual_schema.copy']
- Network: []
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "test_disallowed_type_qualifier",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **test_preserves_pydantic_metadata**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\server\fastmcp\test_func_metadata.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: ['actual_schema.copy']
- Network: []
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "test_preserves_pydantic_metadata",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **server_port**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\server\fastmcp\test_integration.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "integer"
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "integer"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['socket.socket']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "server_port",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **server_url**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\server\fastmcp\test_integration.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "server_port": {
      "type": "integer"
    }
  },
  "required": [
    "server_port"
  ]
}
```

#### Output Schema
```json
{
  "type": "string"
}
```

#### Payload Shape
```json
{
  "request": {
    "server_port": {
      "type": "integer"
    }
  },
  "response": {
    "type": "string"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['socket.socket']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "server_url",
    "arguments": {
      "server_port": 0
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **run_server_with_transport**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\server\fastmcp\test_integration.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "module_name": {
      "type": "string"
    },
    "port": {
      "type": "integer"
    },
    "transport": {
      "type": "string"
    }
  },
  "required": [
    "module_name",
    "port",
    "transport"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "title": "None"
}
```

#### Payload Shape
```json
{
  "request": {
    "module_name": {
      "type": "string"
    },
    "port": {
      "type": "integer"
    },
    "transport": {
      "type": "string"
    }
  },
  "response": {
    "type": "object",
    "title": "None"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['socket.socket']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "run_server_with_transport",
    "arguments": {
      "module_name": "<module_name_str>",
      "port": 0,
      "transport": "<transport_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **server_transport**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\server\fastmcp\test_integration.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "request": {
      "type": "object",
      "title": "pytest.FixtureRequest"
    },
    "server_port": {
      "type": "integer"
    }
  },
  "required": [
    "request",
    "server_port"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "title": "Generator[str, None, None]"
}
```

#### Payload Shape
```json
{
  "request": {
    "request": {
      "type": "object",
      "title": "pytest.FixtureRequest"
    },
    "server_port": {
      "type": "integer"
    }
  },
  "response": {
    "type": "object",
    "title": "Generator[str, None, None]"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['socket.socket']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "server_transport",
    "arguments": {
      "request": {},
      "server_port": 0
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **create_client_for_transport**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\server\fastmcp\test_integration.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "transport": {
      "type": "string"
    },
    "server_url": {
      "type": "string"
    }
  },
  "required": [
    "server_url",
    "transport"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {
    "transport": {
      "type": "string"
    },
    "server_url": {
      "type": "string"
    }
  },
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['socket.socket']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "create_client_for_transport",
    "arguments": {
      "transport": "<transport_str>",
      "server_url": "<server_url_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **unpack_streams**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\server\fastmcp\test_integration.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "client_streams": {
      "type": "object",
      "title": "tuple[MemoryObjectReceiveStream[SessionMessage | Exception], MemoryObjectSendStream[SessionMessage]] | tuple[MemoryObjectReceiveStream[SessionMessage | Exception], MemoryObjectSendStream[SessionMessage], GetSessionIdCallback]"
    }
  },
  "required": [
    "client_streams"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {
    "client_streams": {
      "type": "object",
      "title": "tuple[MemoryObjectReceiveStream[SessionMessage | Exception], MemoryObjectSendStream[SessionMessage]] | tuple[MemoryObjectReceiveStream[SessionMessage | Exception], MemoryObjectSendStream[SessionMessage], GetSessionIdCallback]"
    }
  },
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['socket.socket']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "unpack_streams",
    "arguments": {
      "client_streams": {}
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **tool_fn**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\server\fastmcp\test_server.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "x": {
      "type": "integer"
    },
    "y": {
      "type": "integer"
    }
  },
  "required": [
    "x",
    "y"
  ]
}
```

#### Output Schema
```json
{
  "type": "integer"
}
```

#### Payload Shape
```json
{
  "request": {
    "x": {
      "type": "integer"
    },
    "y": {
      "type": "integer"
    }
  },
  "response": {
    "type": "integer"
  }
}
```

#### Syscalls
- Filesystem: ['text_file.write_text']
- Network: []
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "tool_fn",
    "arguments": {
      "x": 0,
      "y": 0
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **error_tool_fn**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\server\fastmcp\test_server.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "title": "None"
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "title": "None"
  }
}
```

#### Syscalls
- Filesystem: ['text_file.write_text']
- Network: []
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "error_tool_fn",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **image_tool_fn**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\server\fastmcp\test_server.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "path": {
      "type": "string"
    }
  },
  "required": [
    "path"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Payload Shape
```json
{
  "request": {
    "path": {
      "type": "string"
    }
  },
  "response": {
    "type": "object",
    "properties": {}
  }
}
```

#### Syscalls
- Filesystem: ['text_file.write_text']
- Network: []
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "image_tool_fn",
    "arguments": {
      "path": "<path_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **audio_tool_fn**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\server\fastmcp\test_server.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "path": {
      "type": "string"
    }
  },
  "required": [
    "path"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Payload Shape
```json
{
  "request": {
    "path": {
      "type": "string"
    }
  },
  "response": {
    "type": "object",
    "properties": {}
  }
}
```

#### Syscalls
- Filesystem: ['text_file.write_text']
- Network: []
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "audio_tool_fn",
    "arguments": {
      "path": "<path_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **mixed_content_tool_fn**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\server\fastmcp\test_server.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "array",
  "items": {
    "type": "object",
    "title": "ContentBlock"
  }
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "array",
    "items": {
      "type": "object",
      "title": "ContentBlock"
    }
  }
}
```

#### Syscalls
- Filesystem: ['text_file.write_text']
- Network: []
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "mixed_content_tool_fn",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **test_streamable_http_no_redirect**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\server\fastmcp\test_server.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "title": "None"
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "title": "None"
  }
}
```

#### Syscalls
- Filesystem: ['text_file.write_text']
- Network: []
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "test_streamable_http_no_redirect",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **mock_oauth_provider**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\server\fastmcp\auth\test_auth_integration.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['httpx.AsyncClient', 'httpx.ASGITransport']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "mock_oauth_provider",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **auth_app**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\server\fastmcp\auth\test_auth_integration.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "mock_oauth_provider": {
      "type": "object",
      "properties": {}
    }
  },
  "required": [
    "mock_oauth_provider"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {
    "mock_oauth_provider": {
      "type": "object",
      "properties": {}
    }
  },
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['httpx.AsyncClient', 'httpx.ASGITransport']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "auth_app",
    "arguments": {
      "mock_oauth_provider": {}
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **pkce_challenge**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\server\fastmcp\auth\test_auth_integration.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['httpx.AsyncClient', 'httpx.ASGITransport']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "pkce_challenge",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **temp_file**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\server\fastmcp\resources\test_file_resources.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: ['path.unlink']
- Network: []
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "temp_file",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **temp_file**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\server\fastmcp\resources\test_resource_manager.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: ['path.unlink']
- Network: []
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "temp_file",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **test_dir**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\server\fastmcp\servers\test_file_server.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "tmp_path_factory": {
      "type": "object",
      "title": "pytest.TempPathFactory"
    }
  },
  "required": [
    "tmp_path_factory"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "title": "Path"
}
```

#### Payload Shape
```json
{
  "request": {
    "tmp_path_factory": {
      "type": "object",
      "title": "pytest.TempPathFactory"
    }
  },
  "response": {
    "type": "object",
    "title": "Path"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "test_dir",
    "arguments": {
      "tmp_path_factory": {}
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **mcp**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\server\fastmcp\servers\test_file_server.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "properties": {}
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "mcp",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **resources**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\server\fastmcp\servers\test_file_server.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "mcp": {
      "type": "object",
      "properties": {}
    },
    "test_dir": {
      "type": "object",
      "title": "Path"
    }
  },
  "required": [
    "mcp",
    "test_dir"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Payload Shape
```json
{
  "request": {
    "mcp": {
      "type": "object",
      "properties": {}
    },
    "test_dir": {
      "type": "object",
      "title": "Path"
    }
  },
  "response": {
    "type": "object",
    "properties": {}
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "resources",
    "arguments": {
      "mcp": {},
      "test_dir": {}
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **tools**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\server\fastmcp\servers\test_file_server.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "mcp": {
      "type": "object",
      "properties": {}
    },
    "test_dir": {
      "type": "object",
      "title": "Path"
    }
  },
  "required": [
    "mcp",
    "test_dir"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Payload Shape
```json
{
  "request": {
    "mcp": {
      "type": "object",
      "properties": {}
    },
    "test_dir": {
      "type": "object",
      "title": "Path"
    }
  },
  "response": {
    "type": "object",
    "properties": {}
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "tools",
    "arguments": {
      "mcp": {},
      "test_dir": {}
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **test_default_settings**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\shared\test_httpx_utils.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['httpx.Timeout']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "test_default_settings",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **test_custom_parameters**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\shared\test_httpx_utils.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['httpx.Timeout']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "test_custom_parameters",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **mcp_server**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\shared\test_memory.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "properties": {}
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "mcp_server",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **mcp_server**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\shared\test_session.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "properties": {}
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "mcp_server",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **server_port**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\shared\test_sse.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "integer"
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "integer"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['socket.socket', 'httpx.AsyncClient']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "server_port",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **server_url**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\shared\test_sse.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "server_port": {
      "type": "integer"
    }
  },
  "required": [
    "server_port"
  ]
}
```

#### Output Schema
```json
{
  "type": "string"
}
```

#### Payload Shape
```json
{
  "request": {
    "server_port": {
      "type": "integer"
    }
  },
  "response": {
    "type": "string"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['socket.socket', 'httpx.AsyncClient']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "server_url",
    "arguments": {
      "server_port": 0
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **make_server_app**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\shared\test_sse.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "title": "Starlette"
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "title": "Starlette"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['socket.socket', 'httpx.AsyncClient']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "make_server_app",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **run_server**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\shared\test_sse.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "server_port": {
      "type": "integer"
    }
  },
  "required": [
    "server_port"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "title": "None"
}
```

#### Payload Shape
```json
{
  "request": {
    "server_port": {
      "type": "integer"
    }
  },
  "response": {
    "type": "object",
    "title": "None"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['socket.socket', 'httpx.AsyncClient']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "run_server",
    "arguments": {
      "server_port": 0
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **server**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\shared\test_sse.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "server_port": {
      "type": "integer"
    }
  },
  "required": [
    "server_port"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "title": "Generator[None, None, None]"
}
```

#### Payload Shape
```json
{
  "request": {
    "server_port": {
      "type": "integer"
    }
  },
  "response": {
    "type": "object",
    "title": "Generator[None, None, None]"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['socket.socket', 'httpx.AsyncClient']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "server",
    "arguments": {
      "server_port": 0
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **run_mounted_server**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\shared\test_sse.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "server_port": {
      "type": "integer"
    }
  },
  "required": [
    "server_port"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "title": "None"
}
```

#### Payload Shape
```json
{
  "request": {
    "server_port": {
      "type": "integer"
    }
  },
  "response": {
    "type": "object",
    "title": "None"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['socket.socket', 'httpx.AsyncClient']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "run_mounted_server",
    "arguments": {
      "server_port": 0
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **mounted_server**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\shared\test_sse.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "server_port": {
      "type": "integer"
    }
  },
  "required": [
    "server_port"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "title": "Generator[None, None, None]"
}
```

#### Payload Shape
```json
{
  "request": {
    "server_port": {
      "type": "integer"
    }
  },
  "response": {
    "type": "object",
    "title": "Generator[None, None, None]"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['socket.socket', 'httpx.AsyncClient']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "mounted_server",
    "arguments": {
      "server_port": 0
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **run_context_server**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\shared\test_sse.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "server_port": {
      "type": "integer"
    }
  },
  "required": [
    "server_port"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "title": "None"
}
```

#### Payload Shape
```json
{
  "request": {
    "server_port": {
      "type": "integer"
    }
  },
  "response": {
    "type": "object",
    "title": "None"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['socket.socket', 'httpx.AsyncClient']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "run_context_server",
    "arguments": {
      "server_port": 0
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **context_server**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\shared\test_sse.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "server_port": {
      "type": "integer"
    }
  },
  "required": [
    "server_port"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "title": "Generator[None, None, None]"
}
```

#### Payload Shape
```json
{
  "request": {
    "server_port": {
      "type": "integer"
    }
  },
  "response": {
    "type": "object",
    "title": "Generator[None, None, None]"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['socket.socket', 'httpx.AsyncClient']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "context_server",
    "arguments": {
      "server_port": 0
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **test_sse_message_id_coercion**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\shared\test_sse.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['socket.socket', 'httpx.AsyncClient']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "test_sse_message_id_coercion",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **test_sse_server_transport_endpoint_validation**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\shared\test_sse.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "endpoint": {
      "type": "string"
    },
    "expected_result": {
      "type": "object",
      "title": "str | type[Exception]"
    }
  },
  "required": [
    "endpoint",
    "expected_result"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {
    "endpoint": {
      "type": "string"
    },
    "expected_result": {
      "type": "object",
      "title": "str | type[Exception]"
    }
  },
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['socket.socket', 'httpx.AsyncClient']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "test_sse_server_transport_endpoint_validation",
    "arguments": {
      "endpoint": "<endpoint_str>",
      "expected_result": {}
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **extract_protocol_version_from_sse**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\shared\test_streamable_http.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "response": {
      "type": "object",
      "title": "requests.Response"
    }
  },
  "required": [
    "response"
  ]
}
```

#### Output Schema
```json
{
  "type": "string"
}
```

#### Payload Shape
```json
{
  "request": {
    "response": {
      "type": "object",
      "title": "requests.Response"
    }
  },
  "response": {
    "type": "string"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['socket.socket', 'requests.post', 'requests.put', 'requests.delete', 'requests.get', 'httpx.AsyncClient', 'httpx.Response']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "extract_protocol_version_from_sse",
    "arguments": {
      "response": {}
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **create_app**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\shared\test_streamable_http.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "is_json_response_enabled": {
      "type": "boolean"
    },
    "event_store": {
      "type": "object",
      "title": "EventStore | None"
    }
  }
}
```

#### Output Schema
```json
{
  "type": "object",
  "title": "Starlette"
}
```

#### Payload Shape
```json
{
  "request": {
    "is_json_response_enabled": {
      "type": "boolean"
    },
    "event_store": {
      "type": "object",
      "title": "EventStore | None"
    }
  },
  "response": {
    "type": "object",
    "title": "Starlette"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['socket.socket', 'requests.post', 'requests.put', 'requests.delete', 'requests.get', 'httpx.AsyncClient', 'httpx.Response']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "create_app",
    "arguments": {
      "is_json_response_enabled": false,
      "event_store": {}
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **run_server**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\shared\test_streamable_http.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "port": {
      "type": "integer"
    },
    "is_json_response_enabled": {
      "type": "boolean"
    },
    "event_store": {
      "type": "object",
      "title": "EventStore | None"
    }
  },
  "required": [
    "port"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "title": "None"
}
```

#### Payload Shape
```json
{
  "request": {
    "port": {
      "type": "integer"
    },
    "is_json_response_enabled": {
      "type": "boolean"
    },
    "event_store": {
      "type": "object",
      "title": "EventStore | None"
    }
  },
  "response": {
    "type": "object",
    "title": "None"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['socket.socket', 'requests.post', 'requests.put', 'requests.delete', 'requests.get', 'httpx.AsyncClient', 'httpx.Response']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "run_server",
    "arguments": {
      "port": 0,
      "is_json_response_enabled": false,
      "event_store": {}
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **basic_server_port**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\shared\test_streamable_http.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "integer"
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "integer"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['socket.socket', 'requests.post', 'requests.put', 'requests.delete', 'requests.get', 'httpx.AsyncClient', 'httpx.Response']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "basic_server_port",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **json_server_port**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\shared\test_streamable_http.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "integer"
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "integer"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['socket.socket', 'requests.post', 'requests.put', 'requests.delete', 'requests.get', 'httpx.AsyncClient', 'httpx.Response']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "json_server_port",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **basic_server**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\shared\test_streamable_http.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "basic_server_port": {
      "type": "integer"
    }
  },
  "required": [
    "basic_server_port"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "title": "Generator[None, None, None]"
}
```

#### Payload Shape
```json
{
  "request": {
    "basic_server_port": {
      "type": "integer"
    }
  },
  "response": {
    "type": "object",
    "title": "Generator[None, None, None]"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['socket.socket', 'requests.post', 'requests.put', 'requests.delete', 'requests.get', 'httpx.AsyncClient', 'httpx.Response']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "basic_server",
    "arguments": {
      "basic_server_port": 0
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **event_store**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\shared\test_streamable_http.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "properties": {}
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['socket.socket', 'requests.post', 'requests.put', 'requests.delete', 'requests.get', 'httpx.AsyncClient', 'httpx.Response']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "event_store",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **event_server_port**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\shared\test_streamable_http.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "integer"
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "integer"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['socket.socket', 'requests.post', 'requests.put', 'requests.delete', 'requests.get', 'httpx.AsyncClient', 'httpx.Response']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "event_server_port",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **event_server**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\shared\test_streamable_http.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "event_server_port": {
      "type": "integer"
    },
    "event_store": {
      "type": "object",
      "properties": {}
    }
  },
  "required": [
    "event_server_port",
    "event_store"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "title": "Generator[tuple[SimpleEventStore, str], None, None]"
}
```

#### Payload Shape
```json
{
  "request": {
    "event_server_port": {
      "type": "integer"
    },
    "event_store": {
      "type": "object",
      "properties": {}
    }
  },
  "response": {
    "type": "object",
    "title": "Generator[tuple[SimpleEventStore, str], None, None]"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['socket.socket', 'requests.post', 'requests.put', 'requests.delete', 'requests.get', 'httpx.AsyncClient', 'httpx.Response']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "event_server",
    "arguments": {
      "event_server_port": 0,
      "event_store": {}
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **json_response_server**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\shared\test_streamable_http.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "json_server_port": {
      "type": "integer"
    }
  },
  "required": [
    "json_server_port"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "title": "Generator[None, None, None]"
}
```

#### Payload Shape
```json
{
  "request": {
    "json_server_port": {
      "type": "integer"
    }
  },
  "response": {
    "type": "object",
    "title": "Generator[None, None, None]"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['socket.socket', 'requests.post', 'requests.put', 'requests.delete', 'requests.get', 'httpx.AsyncClient', 'httpx.Response']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "json_response_server",
    "arguments": {
      "json_server_port": 0
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **basic_server_url**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\shared\test_streamable_http.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "basic_server_port": {
      "type": "integer"
    }
  },
  "required": [
    "basic_server_port"
  ]
}
```

#### Output Schema
```json
{
  "type": "string"
}
```

#### Payload Shape
```json
{
  "request": {
    "basic_server_port": {
      "type": "integer"
    }
  },
  "response": {
    "type": "string"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['socket.socket', 'requests.post', 'requests.put', 'requests.delete', 'requests.get', 'httpx.AsyncClient', 'httpx.Response']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "basic_server_url",
    "arguments": {
      "basic_server_port": 0
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **json_server_url**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\shared\test_streamable_http.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "json_server_port": {
      "type": "integer"
    }
  },
  "required": [
    "json_server_port"
  ]
}
```

#### Output Schema
```json
{
  "type": "string"
}
```

#### Payload Shape
```json
{
  "request": {
    "json_server_port": {
      "type": "integer"
    }
  },
  "response": {
    "type": "string"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['socket.socket', 'requests.post', 'requests.put', 'requests.delete', 'requests.get', 'httpx.AsyncClient', 'httpx.Response']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "json_server_url",
    "arguments": {
      "json_server_port": 0
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **test_accept_header_validation**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\shared\test_streamable_http.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "basic_server": {
      "type": "object",
      "title": "None"
    },
    "basic_server_url": {
      "type": "string"
    }
  },
  "required": [
    "basic_server",
    "basic_server_url"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {
    "basic_server": {
      "type": "object",
      "title": "None"
    },
    "basic_server_url": {
      "type": "string"
    }
  },
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['socket.socket', 'requests.post', 'requests.put', 'requests.delete', 'requests.get', 'httpx.AsyncClient', 'httpx.Response']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "test_accept_header_validation",
    "arguments": {
      "basic_server": {},
      "basic_server_url": "<basic_server_url_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **test_content_type_validation**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\shared\test_streamable_http.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "basic_server": {
      "type": "object",
      "title": "None"
    },
    "basic_server_url": {
      "type": "string"
    }
  },
  "required": [
    "basic_server",
    "basic_server_url"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {
    "basic_server": {
      "type": "object",
      "title": "None"
    },
    "basic_server_url": {
      "type": "string"
    }
  },
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['socket.socket', 'requests.post', 'requests.put', 'requests.delete', 'requests.get', 'httpx.AsyncClient', 'httpx.Response']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "test_content_type_validation",
    "arguments": {
      "basic_server": {},
      "basic_server_url": "<basic_server_url_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **test_json_validation**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\shared\test_streamable_http.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "basic_server": {
      "type": "object",
      "title": "None"
    },
    "basic_server_url": {
      "type": "string"
    }
  },
  "required": [
    "basic_server",
    "basic_server_url"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {
    "basic_server": {
      "type": "object",
      "title": "None"
    },
    "basic_server_url": {
      "type": "string"
    }
  },
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['socket.socket', 'requests.post', 'requests.put', 'requests.delete', 'requests.get', 'httpx.AsyncClient', 'httpx.Response']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "test_json_validation",
    "arguments": {
      "basic_server": {},
      "basic_server_url": "<basic_server_url_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **test_json_parsing**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\shared\test_streamable_http.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "basic_server": {
      "type": "object",
      "title": "None"
    },
    "basic_server_url": {
      "type": "string"
    }
  },
  "required": [
    "basic_server",
    "basic_server_url"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {
    "basic_server": {
      "type": "object",
      "title": "None"
    },
    "basic_server_url": {
      "type": "string"
    }
  },
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['socket.socket', 'requests.post', 'requests.put', 'requests.delete', 'requests.get', 'httpx.AsyncClient', 'httpx.Response']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "test_json_parsing",
    "arguments": {
      "basic_server": {},
      "basic_server_url": "<basic_server_url_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **test_method_not_allowed**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\shared\test_streamable_http.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "basic_server": {
      "type": "object",
      "title": "None"
    },
    "basic_server_url": {
      "type": "string"
    }
  },
  "required": [
    "basic_server",
    "basic_server_url"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {
    "basic_server": {
      "type": "object",
      "title": "None"
    },
    "basic_server_url": {
      "type": "string"
    }
  },
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['socket.socket', 'requests.post', 'requests.put', 'requests.delete', 'requests.get', 'httpx.AsyncClient', 'httpx.Response']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "test_method_not_allowed",
    "arguments": {
      "basic_server": {},
      "basic_server_url": "<basic_server_url_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **test_session_validation**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\shared\test_streamable_http.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "basic_server": {
      "type": "object",
      "title": "None"
    },
    "basic_server_url": {
      "type": "string"
    }
  },
  "required": [
    "basic_server",
    "basic_server_url"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {
    "basic_server": {
      "type": "object",
      "title": "None"
    },
    "basic_server_url": {
      "type": "string"
    }
  },
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['socket.socket', 'requests.post', 'requests.put', 'requests.delete', 'requests.get', 'httpx.AsyncClient', 'httpx.Response']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "test_session_validation",
    "arguments": {
      "basic_server": {},
      "basic_server_url": "<basic_server_url_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **test_session_id_pattern**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\shared\test_streamable_http.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['socket.socket', 'requests.post', 'requests.put', 'requests.delete', 'requests.get', 'httpx.AsyncClient', 'httpx.Response']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "test_session_id_pattern",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **test_streamable_http_transport_init_validation**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\shared\test_streamable_http.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['socket.socket', 'requests.post', 'requests.put', 'requests.delete', 'requests.get', 'httpx.AsyncClient', 'httpx.Response']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "test_streamable_http_transport_init_validation",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **test_session_termination**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\shared\test_streamable_http.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "basic_server": {
      "type": "object",
      "title": "None"
    },
    "basic_server_url": {
      "type": "string"
    }
  },
  "required": [
    "basic_server",
    "basic_server_url"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {
    "basic_server": {
      "type": "object",
      "title": "None"
    },
    "basic_server_url": {
      "type": "string"
    }
  },
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['socket.socket', 'requests.post', 'requests.put', 'requests.delete', 'requests.get', 'httpx.AsyncClient', 'httpx.Response']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "test_session_termination",
    "arguments": {
      "basic_server": {},
      "basic_server_url": "<basic_server_url_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **test_response**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\shared\test_streamable_http.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "basic_server": {
      "type": "object",
      "title": "None"
    },
    "basic_server_url": {
      "type": "string"
    }
  },
  "required": [
    "basic_server",
    "basic_server_url"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {
    "basic_server": {
      "type": "object",
      "title": "None"
    },
    "basic_server_url": {
      "type": "string"
    }
  },
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['socket.socket', 'requests.post', 'requests.put', 'requests.delete', 'requests.get', 'httpx.AsyncClient', 'httpx.Response']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "test_response",
    "arguments": {
      "basic_server": {},
      "basic_server_url": "<basic_server_url_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **test_json_response**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\shared\test_streamable_http.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "json_response_server": {
      "type": "object",
      "title": "None"
    },
    "json_server_url": {
      "type": "string"
    }
  },
  "required": [
    "json_response_server",
    "json_server_url"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {
    "json_response_server": {
      "type": "object",
      "title": "None"
    },
    "json_server_url": {
      "type": "string"
    }
  },
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['socket.socket', 'requests.post', 'requests.put', 'requests.delete', 'requests.get', 'httpx.AsyncClient', 'httpx.Response']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "test_json_response",
    "arguments": {
      "json_response_server": {},
      "json_server_url": "<json_server_url_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **test_json_response_accept_json_only**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\shared\test_streamable_http.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "json_response_server": {
      "type": "object",
      "title": "None"
    },
    "json_server_url": {
      "type": "string"
    }
  },
  "required": [
    "json_response_server",
    "json_server_url"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {
    "json_response_server": {
      "type": "object",
      "title": "None"
    },
    "json_server_url": {
      "type": "string"
    }
  },
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['socket.socket', 'requests.post', 'requests.put', 'requests.delete', 'requests.get', 'httpx.AsyncClient', 'httpx.Response']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "test_json_response_accept_json_only",
    "arguments": {
      "json_response_server": {},
      "json_server_url": "<json_server_url_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **test_json_response_missing_accept_header**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\shared\test_streamable_http.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "json_response_server": {
      "type": "object",
      "title": "None"
    },
    "json_server_url": {
      "type": "string"
    }
  },
  "required": [
    "json_response_server",
    "json_server_url"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {
    "json_response_server": {
      "type": "object",
      "title": "None"
    },
    "json_server_url": {
      "type": "string"
    }
  },
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['socket.socket', 'requests.post', 'requests.put', 'requests.delete', 'requests.get', 'httpx.AsyncClient', 'httpx.Response']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "test_json_response_missing_accept_header",
    "arguments": {
      "json_response_server": {},
      "json_server_url": "<json_server_url_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **test_json_response_incorrect_accept_header**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\shared\test_streamable_http.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "json_response_server": {
      "type": "object",
      "title": "None"
    },
    "json_server_url": {
      "type": "string"
    }
  },
  "required": [
    "json_response_server",
    "json_server_url"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {
    "json_response_server": {
      "type": "object",
      "title": "None"
    },
    "json_server_url": {
      "type": "string"
    }
  },
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['socket.socket', 'requests.post', 'requests.put', 'requests.delete', 'requests.get', 'httpx.AsyncClient', 'httpx.Response']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "test_json_response_incorrect_accept_header",
    "arguments": {
      "json_response_server": {},
      "json_server_url": "<json_server_url_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **test_get_sse_stream**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\shared\test_streamable_http.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "basic_server": {
      "type": "object",
      "title": "None"
    },
    "basic_server_url": {
      "type": "string"
    }
  },
  "required": [
    "basic_server",
    "basic_server_url"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {
    "basic_server": {
      "type": "object",
      "title": "None"
    },
    "basic_server_url": {
      "type": "string"
    }
  },
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['socket.socket', 'requests.post', 'requests.put', 'requests.delete', 'requests.get', 'httpx.AsyncClient', 'httpx.Response']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "test_get_sse_stream",
    "arguments": {
      "basic_server": {},
      "basic_server_url": "<basic_server_url_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **test_get_validation**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\shared\test_streamable_http.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "basic_server": {
      "type": "object",
      "title": "None"
    },
    "basic_server_url": {
      "type": "string"
    }
  },
  "required": [
    "basic_server",
    "basic_server_url"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {
    "basic_server": {
      "type": "object",
      "title": "None"
    },
    "basic_server_url": {
      "type": "string"
    }
  },
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['socket.socket', 'requests.post', 'requests.put', 'requests.delete', 'requests.get', 'httpx.AsyncClient', 'httpx.Response']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "test_get_validation",
    "arguments": {
      "basic_server": {},
      "basic_server_url": "<basic_server_url_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **run_context_aware_server**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\shared\test_streamable_http.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "port": {
      "type": "integer"
    }
  },
  "required": [
    "port"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {
    "port": {
      "type": "integer"
    }
  },
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['socket.socket', 'requests.post', 'requests.put', 'requests.delete', 'requests.get', 'httpx.AsyncClient', 'httpx.Response']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "run_context_aware_server",
    "arguments": {
      "port": 0
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **context_aware_server**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\shared\test_streamable_http.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "basic_server_port": {
      "type": "integer"
    }
  },
  "required": [
    "basic_server_port"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "title": "Generator[None, None, None]"
}
```

#### Payload Shape
```json
{
  "request": {
    "basic_server_port": {
      "type": "integer"
    }
  },
  "response": {
    "type": "object",
    "title": "Generator[None, None, None]"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['socket.socket', 'requests.post', 'requests.put', 'requests.delete', 'requests.get', 'httpx.AsyncClient', 'httpx.Response']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "context_aware_server",
    "arguments": {
      "basic_server_port": 0
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **test_server_validates_protocol_version_header**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\shared\test_streamable_http.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "basic_server": {
      "type": "object",
      "title": "None"
    },
    "basic_server_url": {
      "type": "string"
    }
  },
  "required": [
    "basic_server",
    "basic_server_url"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {
    "basic_server": {
      "type": "object",
      "title": "None"
    },
    "basic_server_url": {
      "type": "string"
    }
  },
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['socket.socket', 'requests.post', 'requests.put', 'requests.delete', 'requests.get', 'httpx.AsyncClient', 'httpx.Response']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "test_server_validates_protocol_version_header",
    "arguments": {
      "basic_server": {},
      "basic_server_url": "<basic_server_url_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **test_server_backwards_compatibility_no_protocol_version**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\shared\test_streamable_http.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "basic_server": {
      "type": "object",
      "title": "None"
    },
    "basic_server_url": {
      "type": "string"
    }
  },
  "required": [
    "basic_server",
    "basic_server_url"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "guessed": true
}
```

#### Payload Shape
```json
{
  "request": {
    "basic_server": {
      "type": "object",
      "title": "None"
    },
    "basic_server_url": {
      "type": "string"
    }
  },
  "response": {
    "type": "object",
    "guessed": true
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['socket.socket', 'requests.post', 'requests.put', 'requests.delete', 'requests.get', 'httpx.AsyncClient', 'httpx.Response']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "test_server_backwards_compatibility_no_protocol_version",
    "arguments": {
      "basic_server": {},
      "basic_server_url": "<basic_server_url_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **escape_path_for_python**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\shared\test_win32_utils.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "path": {
      "type": "string"
    }
  },
  "required": [
    "path"
  ]
}
```

#### Output Schema
```json
{
  "type": "string"
}
```

#### Payload Shape
```json
{
  "request": {
    "path": {
      "type": "string"
    }
  },
  "response": {
    "type": "string"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: []
- Subprocess: []
- Env: []
- Severity: **low**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "escape_path_for_python",
    "arguments": {
      "path": "<path_str>"
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **server_port**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\shared\test_ws.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "integer"
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "integer"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['socket.socket']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "server_port",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **server_url**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\shared\test_ws.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "server_port": {
      "type": "integer"
    }
  },
  "required": [
    "server_port"
  ]
}
```

#### Output Schema
```json
{
  "type": "string"
}
```

#### Payload Shape
```json
{
  "request": {
    "server_port": {
      "type": "integer"
    }
  },
  "response": {
    "type": "string"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['socket.socket']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "server_url",
    "arguments": {
      "server_port": 0
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **make_server_app**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\shared\test_ws.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {}
}
```

#### Output Schema
```json
{
  "type": "object",
  "title": "Starlette"
}
```

#### Payload Shape
```json
{
  "request": {},
  "response": {
    "type": "object",
    "title": "Starlette"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['socket.socket']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "make_server_app",
    "arguments": {}
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **run_server**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\shared\test_ws.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "server_port": {
      "type": "integer"
    }
  },
  "required": [
    "server_port"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "title": "None"
}
```

#### Payload Shape
```json
{
  "request": {
    "server_port": {
      "type": "integer"
    }
  },
  "response": {
    "type": "object",
    "title": "None"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['socket.socket']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "run_server",
    "arguments": {
      "server_port": 0
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

### 🛠️ Tool: **server**
- **File:** `C:\Users\MUTAKEEN\OneDrive\Desktop\nogap-aimcp\repos\python-sdk\python-sdk\tests\shared\test_ws.py`
- **Confidence:** 0.89

#### Input Schema
```json
{
  "type": "object",
  "properties": {
    "server_port": {
      "type": "integer"
    }
  },
  "required": [
    "server_port"
  ]
}
```

#### Output Schema
```json
{
  "type": "object",
  "title": "Generator[None, None, None]"
}
```

#### Payload Shape
```json
{
  "request": {
    "server_port": {
      "type": "integer"
    }
  },
  "response": {
    "type": "object",
    "title": "Generator[None, None, None]"
  }
}
```

#### Syscalls
- Filesystem: []
- Network: ['socket.socket']
- Subprocess: []
- Env: []
- Severity: **medium**

#### Run Template
```json
{
  "jsonrpc": "2.0",
  "method": "tools.call",
  "params": {
    "name": "server",
    "arguments": {
      "server_port": 0
    }
  }
}
```

#### Evidence Summary (Short)
- missing_file — ``
- syscall_summary — ``

---

## Evidence Pack (Metadata)

```json
{
  "generated_by": "schema_extractor_v4 (evidence adder)",
  "notes": "Each tool includes 'evidence' list with function snippet, syscall lines, and imports when available.",
  "repo_scanned": "/mnt/data/python-sdk_extracted",
  "tool_count": 325
}
```

