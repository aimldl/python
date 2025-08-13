# Pydantic

Pydantic은 주로 \*\*데이터 유효성 검사(validation)\*\*와 \*\*설정 관리(settings management)\*\*에 사용되는 파이썬 라이브러리입니다. 이를 통해 데이터를 명확하게 정의하고, 잘못된 데이터가 프로그램에 들어오는 것을 방지할 수 있습니다.

-----

### 주요 기능

#### 1\. 데이터 유효성 검사

Pydantic은 파이썬의 \*\*타입 힌트(type hints)\*\*를 활용하여 데이터 모델을 정의합니다. 예를 들어, 사용자의 이름은 문자열, 나이는 정수여야 한다고 명시하면, Pydantic은 해당 데이터가 모델에 맞는지 자동으로 확인해줍니다. 만약 타입이 맞지 않거나 필수 필드가 누락되면, 유용한 오류 메시지를 반환합니다.

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

# 올바른 데이터
user_data = {"name": "Alice", "age": 30}
user = User(**user_data)
print(user)
# 출력: name='Alice' age=30

# 잘못된 데이터 (age가 문자열)
try:
    invalid_user_data = {"name": "Bob", "age": "twenty"}
    User(**invalid_user_data)
except Exception as e:
    print(e)
# 출력: 1 validation error for User
# age
#  value is not a valid integer (type=type_error.integer)
```

#### 2\. 설정 관리

환경 변수, 파일, 또는 기타 소스로부터 프로그램 설정을 안전하게 로드하고 관리하는 데 Pydantic을 사용할 수 있습니다. `BaseSettings` 클래스를 상속받아 설정을 정의하면, Pydantic이 자동으로 환경 변수 등에서 값을 읽어와 유효성을 검사합니다.

```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    api_key: str
    database_url: str = "sqlite:///./test.db"

# 환경 변수에서 값을 읽어옴 (예: os.environ["API_KEY"] = "my_secret_key")
settings = Settings()
print(settings.api_key)
print(settings.database_url)
```

#### 3\. 데이터 직렬화 및 역직렬화

Pydantic 모델은 JSON과 같은 형식으로 쉽게 \*\*직렬화(serialization)\*\*하고, 다시 파이썬 객체로 \*\*역직렬화(deserialization)\*\*할 수 있습니다. 이는 웹 API를 구축할 때 매우 유용하며, FastAPI와 같은 프레임워크가 Pydantic을 기본적으로 사용하는 이유이기도 합니다.

  - `model_dump()`: 모델 객체를 딕셔너리로 변환
  - `model_dump_json()`: 모델 객체를 JSON 문자열로 변환

-----

### Pydantic의 장점

  - **타입 안정성**: 프로그램의 신뢰도를 높여줍니다.
  - **개발 생산성**: 반복적인 유효성 검사 코드를 줄여줍니다.
  - **자동 문서화**: 모델 정의를 통해 데이터의 구조를 쉽게 파악할 수 있습니다.
  - **뛰어난 성능**: Rust 기반의 `pydantic-core`를 사용해 매우 빠릅니다.

-----

### 사용 예시

  - **웹 API**: FastAPI와 함께 사용하여 요청 본문, 쿼리 매개변수, 응답 모델을 정의하고 유효성을 검사합니다.
  - **데이터 분석**: 데이터프레임이나 CSV 파일의 데이터를 불러올 때 스키마를 정의하여 데이터의 무결성을 보장합니다.
  - **데이터베이스 ORM**: 데이터베이스 레코드를 Pydantic 모델로 매핑하여 사용합니다.
