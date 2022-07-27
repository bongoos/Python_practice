from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())

#터미널에 pip list : pip로 가져온 리스트 표시
#터미널에 pip show beautifulsoup4 : pip에서 beautifulsoup4에 관한 자세한 정보 표시
#터미널에 pip install --upgrade beautifulsoup4 : beautifulsoup4의 업그레이드 가능
#터미널에 pip uninstall beautifulsoup4 : beautifulsoup4 삭제