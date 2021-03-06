# 接口

所有 API 默认前缀为 `/api/`.

所有 API 默认 Request 和 Response 的 Content-Type 都为 `application/json`.

## 默认状态码

- 成功: 200 OK
- 成功, 操作为创建: 201 Created
- 成功, 无响应内容: 204 No Content
- 传入的字段不符合规范或 Validation Error: 400 Bad Request
- 权限不足: 403 Forbidden
- 未找到: 404 Not Found

## 用户

### 注册

- Request

  - Url: `user/register/`

  - Method: POST

  - ```
    {
        "username": "cjc7373",
        "password": "123456",
    }
    ```
  
- Response: 几种 400 Bad Request 的情况

  - 用户名已存在: 

    ```
    {"username": "A user with that username already exists."}
    ```

  - 密码太短

    ```
    {"password": "Password too short."}
    ```

  - 密码不一致

    ```
    {"non_field_errors": "Passwords are not same."}
    ```


### 登录

- Request

  - Url: `user/login/`

  - Method: POST

  - ```
    {
        "username": "cjc7373",
        "password": "123456",
        "allow_terms": true //可选
    }
    ```

- Response

  - 若用户未同意用户条款或用户条款已更新
  
    - 403 Forbidden
  
    - ```
      {
          "detail": "请同意用户条款",
          "term": [
              {
                  "name": "xxxxx",
                  "content": "xxxx",
                  "date_created": "xxx"
              }
          ]
      }
      ```

### 登出

- Request
  - Url: `user/logout/`
  - Method: POST

### 获取个人资料

- Request

  - Url: `user/`
  - Method: GET

- Response

  ```
  {
      "username": "cjc7373",
      "email": "c@ac.com",
      "phone_number": "13012345678",
      "name": null,
      "token": "1:123123"
  }
  ```

### 修改个人资料

目前只能改 name..

- Request
  - Url: `user/`

  - Method: PUT

  - ```
    {"name": "xxx"}
    ```

### 修改密码

### 找回密码

### 更换绑定邮箱

### 更换手机号码

## 组

### 创建组

- Request

  - Url: `group/`

  - Method: POST

  - ```
    {
        "name": "某大学",
        "rules": {
            "has_phone_number": true,
            "has_email": true,
            "email_suffix": "xx.edu.cn", //可选
            "has_name": true,
            "must_be_verified_by_admin": true,
        },
        "apply_hint": "xxx", //可选
    }
    ```
  
- Response: 组的信息, 字段同上, 多了一个id

### 查看组列表

- Request

  - Url: `group/`
  - GET
  - Query String: `verified=<true>&limit=<results per page>&offset=<offset>`

- Response

  - ```json5
    {
      "count": 2, //结果计数
      "next": null, //下一页的 url
      "previous": null, //上一页的 url
      "results": [
        {},
      ]
    }
    ```

  - results 中字段同创建, 多了`id`, `verified`, `verify_message`

### 查看组信息

- Request
  - Url: `group/1[id]/`
  - GET
  
- Response

  - ```
    {
        "name": "xxx",
        "rules": {
            "has_phone_number": true,
            "email_suffix": "xx.edu.cn",
            ...
        },
        "rules_meet": {
            "has_phone_number": true,
            "email_suffix": false,
            ...
        },
        "apply_hint": "xxx",
    }
    ```

### 修改组加入条件

- Request
  - Url: `group/1[id]/`
  - Method: PATCH
  - 格式同创建, 传入要更改的字段
- Response: 返回更新后的数据

### 删除组

- Request
  - Url: `group/1[id]/`
  - Method: DELETE

### (申请)加入组

- Request

  - Url: `group/1/application/`

  - Method: POST

  - ```
    {
        "apply_message": "xxx",
    }
    ```
  
- Response:

  - ```
    {
        "status": "pending" //若无需要管理员验证这一规则则为"accepted"
    }
    ```
    
  - 重复申请:
  
    ```
    {"non_field_errors": "The fields user, group must make a unique set."}
    ```
  
    

### 查看加入申请

- Request

  - Url: `group/1/application/`
  - Method: GET

- Response

  - ```
    [
        {
          "user": {//字段和个人资料一致}, 
          "apply_message": "xxx"
        },
    ]```

### 同意或拒绝某一申请

- Request
  - Url: `group/1/application/1[id]`

  - Method: PUT

  - ```
    {
        "status": "rejected" //拒绝, accepted 为同意
    }
    ```



### 查看成员

- Request

  - Url: `group/1/member/`
  - Method: GET

- Response

  - ```
    [
        {
          "apply_message": "xxx", 
          "user": {//字段和个人资料一致}
        },
    ]
    ```

### 删除成员

- Request
  - Url: `group/1/member/10[user_id]`
  - Method: DELETE
  

## 比赛

### 查看比赛的所有阶段

- Request
    - Url: `stage/`
    - Method: GET
    
- Response
    - ```
        {
            "start_time": "",
            "end_time": "",
            "practice_start_time": "",
            "pause": [
                {"start_time": "", "end_time": ""}
            ]
        }
        ```

## 查看比赛的当前阶段
- Request
    - Url: `stage/current/`
    - Method: GET
    
- Response
    - ```
        {
            "status": "not_start"
        }
        ```


## 题目

### 查看已启用的题目
- Request
    - Url: `challenge/`
    - Method: GET
    
- Response
    - ```json5
        [
            {
                "id": 1,
                "name": "test_problem",
                "category": "test",
                "detail": "test_detail",
                "prompt": "test_prompt",
                "sub_challenge": [
                    {
                        "id": 1,
                        "name": "",
                        "score": 50
                    }
                ]
            }
        ]
        ```

### 获取做题进度

- Request
    - Url: `/challenge/clear/`
    - Method: GET
    
- Response
    - ```json5
        [
          {
            "challenge": 1,
            "clear_status": "clear", // 或 "partly" 表示部分完成
            "time": "2020-05-24T02:44:12.498Z",
            "sub_challenge_clear": [ // 表示已经完成的子题
              {
                "sub_challenge": 1,
                "time": "2020-05-24T02:44:12.498Z",
              }
            ]
          }
        ] 
        ```

## 提交

### 提交一个 flag

- Request
    - Url: `submission/`
    - Method: POST
    - ```json5
        {
            "challenge": 1,
            "flag": "flag{hello}"
        }
        ```

- Response
    - ```json5
        {
            "detail": "correct" // 或者为 wrong
        }
        ```
    - 每分钟请求限制为 10 次, 超过后将返回 429 Too Many Requests, 并在 Header 中 Retry-After 
      字段指示在多少秒后重试
      
## 榜单

### 获取分数榜单

- Request
    - Url: `borad/score/`
    - Method: GET
    - Query string: `category=<category>&group=<group id>`
      若 category 为空则为所有分类, 若 group 为空则为所有人
      
- Response
    - ```json5
        {
          "count": 2, //结果计数
          "next": null, //下一页的 url
          "previous": null, //上一页的 url
          "results": [
            {
                "user": 1, //id
                "challenge_clear": [], // 格式与获取做题进度的接口一致
                "score": 100,
                "time": "2020-05-24T02:44:12.498Z"
            }
          ]
        }
        ```
    - 榜单有 1 分钟的缓存

### 获取一血榜单

- Request
    - Url: `board/firstblood/`
    - Method: GET
    - Query string: `group=<group id>`

- Response
    - ```json5
      {
        "challenges": [
          {
            "challenge": 1,
            "user": 1,
            "time": "2020-05-24T02:44:12.498Z"
          },
        ],
        "sub_challenges": [
          {
            "user": 1,
            "challenge": 1,
            "sub_challenge": 1,
            "time": "2020-05-24T02:44:12.498Z"
          },
        ]
      }
      ```

### 获取做题历史

- Request
    - Url: `board/history/<user_id>/`
    - Method: GET
    
- Response
    - ```json5
        [
           {
              "score": 100,
              "time": "2020-05-24T02:44:12.498Z"
           } // 按时间升序排序
        ]
        ```
      
## 公告

### 获取公告

- Request
    - Url: `announcement/`
    - Method: GET
    - Query string: `challenge=<challenge id>`
    
- Response
    - ```json5
        [
          {
            "challenge": null, // 为 null 时为一般公告
            "content": "test",
            "created_time": "2020-05-24T02:44:12.498Z",
            "updated_time": "2020-05-24T02:44:12.498Z",
          },
        ]
        ```
