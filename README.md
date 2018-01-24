# python-UTF8-To-EUCKR
convert utf-8 to euc-kr

삶의 고통은 인코딩 문제에서 오는 법이다.

뭔놈의 엑셀은 EUC-KR 로 저장이 되어야 하고 파싱한 데이터는 UTF8로 찾아 오는가.


```python
#사실 별 복잡한 코드는 아니다.

utfStr = '뭔가 UTF-8로 적혀있을 어느 문장'

# 보통 아래 처럼하면 \xec 얘같이 인코딩 문제가 등장한다.
eucStr = utfStr.decode('UTF-8').encode('EUC-KR')

# encode 에 내장 되어 있는 에러처리를 하면 되는데 위에 것들은 보통 무시 해줘도 된다..
eucStr = utfStr.decode('UTF-8').encode('EUC-KR','ignore')

```
